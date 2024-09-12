from lib.utils import (
    EntityUrl,
    get_remote_data,
    customer_with_max_spending,
    get_customer,
    get_max_spend_with_pandas
)


def first_approach() -> str:
    """Finding the customer that has spent the max amount without 3rd parties libraries"""
    customers = get_remote_data(
        url=EntityUrl.Customer.value
    )

    invoices = get_remote_data(
        url=EntityUrl.Invoince.value
    )

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

    return msg


def second_approach():
    """Finding the customer that has spent the max amount using pandas"""
    customers = get_remote_data(
        url=EntityUrl.Customer.value
    )

    invoices = get_remote_data(
        url=EntityUrl.Invoince.value
    )

    result = get_max_spend_with_pandas(
        customers=customers,
        invoices=invoices
    )

    return result


if __name__ == "__main__":
    msg = first_approach()
    print(msg)

    msg = second_approach()
    print(msg)
