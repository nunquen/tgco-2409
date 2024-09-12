import time
from unittest.mock import patch

from .fixtures import *  # noqa: F401, F403

from main import (
    first_approach,
    second_approach
)


def test_first_approach_success(
    get_customer_and_max_spending,
    get_customers_payload,
    get_invoices_payload
):
    with patch(
        "lib.utils.customer_with_max_spending"  # noqa: E501
    ) as mocked_customer_with_max_spending, patch(
        "lib.utils.get_customer"
    ) as mocked_get_customer:
        mocked_customer_with_max_spending.return_value = get_customer_and_max_spending
        mocked_get_customer.return_value = get_customers_payload["customers"][1]

        result = first_approach(
            customers=get_customers_payload,
            invoices=get_invoices_payload
        )

        expected_msg = "User {} {} has spent {}".format(
            get_customers_payload["customers"][1]["name"],
            get_customers_payload["customers"][1]["surname"],
            get_customer_and_max_spending[1]
        )

        assert result == expected_msg


def test_second_approach_success(
    get_customers_payload,
    get_invoices_payload,
    get_dataframe
):
    with patch(
        "lib.utils.get_max_spend_with_pandas"
    ) as mocked_get_max_spend_with_pandas:
        mocked_get_max_spend_with_pandas.return_value = get_dataframe

        # Expected values
        expected_name = get_customers_payload["customers"][1]["name"]
        expected_surname = get_customers_payload["customers"][1]["surname"]
        expected_max_amount = 276.55

        result = second_approach(
            customers=get_customers_payload,
            invoices=get_invoices_payload
        )

        assert result.iloc[0]['name'] == expected_name
        assert result.iloc[0]['surname'] == expected_surname
        assert result.iloc[0]['max_amount'] == expected_max_amount


def test_approaches_speed(
    get_customers_payload,
    get_invoices_payload
):
    """Using pandas is easy but slower than conventional python scripting"""
    start_time = time.time()
    first_approach(
        invoices=get_invoices_payload,
        customers=get_customers_payload
    )
    end_time = time.time()
    elapsed_time_without_pandas = end_time - start_time

    start_time = time.time()
    second_approach(
        invoices=get_invoices_payload,
        customers=get_customers_payload
    )
    end_time = time.time()
    elapsed_time_pandas = end_time - start_time

    assert elapsed_time_without_pandas < elapsed_time_pandas
