from lib.utils import (
    EntityUrl,
    get_remote_data,
    customer_with_max_spending,
    get_customer,
    get_max_spend_with_pandas
)
import time


def first_approach(
    customers=dict,
    invoices=dict
) -> str:
    """Finding the customer that has spent the max amount without 3rd parties libraries"""
    start_time = time.time()

    customer_id, max_spent = customer_with_max_spending(
        invoices=invoices
    )

    customer = get_customer(
        customer_id=customer_id,
        customers=customers
    )

    msg = "User {} {} has spent {}".format(
        customer["name"],
        customer["surname"],
        max_spent
    )

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"first_approach function took {elapsed_time:.4f} seconds to run.")

    return msg


def second_approach(
    customers=dict,
    invoices=dict
) -> any:
    """Finding the customer that has spent the max amount using pandas"""
    start_time = time.time()

    result = get_max_spend_with_pandas(
        customers=customers,
        invoices=invoices
    )

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"second_approach function took {elapsed_time:.4f} seconds to run.")

    return result


if __name__ == "__main__":
    customers = get_remote_data(
        url=EntityUrl.Customer.value
    )

    invoices = get_remote_data(
        url=EntityUrl.Invoice.value
    )

    msg = second_approach(
        customers=customers,
        invoices=invoices
    )
    print(msg)

    msg = first_approach(
        customers=customers,
        invoices=invoices
    )
    print(msg)
