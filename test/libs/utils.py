import requests

from .fixtures import *  # noqa: F401, F403

from lib.utils import (
    customer_with_max_spending,
    get_customer,
    get_max_spend_with_pandas,
    get_remote_data
)


# Test for a successful request with valid JSON data
def test_get_remote_data_success(
    mock_data,
    mock_requests,
    mocked_url
):

    mock_requests.get(
        mocked_url,
        json=mock_data,
        status_code=200
    )

    result = get_remote_data(mocked_url)

    # Assertions
    assert result == mock_data
    assert len(result) == 2
    assert result[0]["name"] == "Alice"


# Test for a 404 response
def test_get_remote_data_404(
    mock_requests,
    mocked_url
):
    mock_requests.get(
        mocked_url,
        status_code=404
    )

    result = get_remote_data(mocked_url)

    # Expecting an empty list if the response code is not 200
    assert result == []


# Test for an exception (like connection error)º
def test_get_remote_data_exception(
    mock_requests,
    mocked_url
):
    mock_requests.get(
        mocked_url,
        exc=requests.exceptions.ConnectionError
    )

    result = get_remote_data(mocked_url)

    # Expecting an empty list if an exception occurs
    assert result == []


def test_customer_with_max_spending_sucess(
    get_invoices_payload
):
    max_customer, max_spent = customer_with_max_spending(
        invoices=get_invoices_payload
    )

    assert max_customer == 1
    assert max_spent == 276.55


def test_customer_with_max_spending_exception():
    max_customer, max_spent = customer_with_max_spending(
        invoices={}
    )

    assert max_customer is None
    assert max_spent is None


def test_get_customer_sucess(
    get_customers_payload
):
    customer = get_customer(
        customer_id=0,
        customers=get_customers_payload
    )

    assert customer["ID"] == 0
    assert customer["name"] == "Alice"
    assert customer["surname"] == "Klark"


def test_get_customer_exception():
    customer = get_customer(
        customer_id=0,
        customers={}
    )

    assert customer == {}


def test_get_max_spend_with_pandas(
    get_customers_payload,
    get_invoices_payload
):
    # Expected values
    expected_name = get_customers_payload["customers"][1]["name"]
    expected_surname = get_customers_payload["customers"][1]["surname"]
    expected_max_amount = 276.55

    result = get_max_spend_with_pandas(
        invoices=get_invoices_payload,
        customers=get_customers_payload
    )

    assert result.iloc[0]['name'] == expected_name
    assert result.iloc[0]['surname'] == expected_surname
    assert result.iloc[0]['max_amount'] == expected_max_amount


def test_get_max_spend_with_pandas_exception(
    get_customers_payload
):
    result = get_max_spend_with_pandas(
        invoices={},
        customers=get_customers_payload
    )

    assert result is None

