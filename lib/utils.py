from enum import Enum
from typing import (
    List,
    Union
)

import json
import pandas as pd
import requests


class EntityUrl(Enum):
    Customer = "http://localhost:9090"
    Invoince = "http://localhost:9092"


def get_remote_data(
    url: str
) -> List[dict]:

    response = []

    try:
        r = requests.get(
            url=url
        )

        if r.status_code == 200:
            response = json.loads(r.content)

    except Exception as e:
        print(e)

    return response


def customer_with_max_spending(
    invoices: dict
) -> Union[str, int]:
    # Dictionary to store the total amount spent by each customer
    customer_spending = {}
    max_customer = None
    max_spent = None

    try:
        # Iterate through each invoice
        for invoice in invoices["invoices"]:
            customer_id = invoice['customerId']
            amount = invoice['amount']

            # Sum the amount for each customer
            if customer_id in customer_spending:
                customer_spending[customer_id] += amount
            else:
                customer_spending[customer_id] = amount

        # Find the customer who spent the most
        max_customer = max(customer_spending, key=customer_spending.get)
        max_spent = customer_spending[max_customer]

    except Exception as e:
        print("Exception while getting max spent: {}".format(e))

    return max_customer, max_spent


def get_customer(
    customer_id: int,
    customers: dict
  ) -> dict:
    response = {}

    try:
        customer = list(
            filter(
                lambda x: x["ID"] == customer_id, customers["customers"]
            )
        )

        response = customer[0]

    except Exception as e:
        print("Couldn't get customer with id {}. Exception found: {}".format(
            customer_id,
            e
        ))

    return response


def get_max_spend_with_pandas(
    invoices: dict,
    customers: dict
):
    result = None

    try:
        # Convert to DataFrames
        df_customers = pd.DataFrame(customers['customers'])
        df_invoices = pd.DataFrame(invoices['invoices'])

        # Group by customerId and sum the amounts
        grouped_invoices = df_invoices.groupby('customerId')['amount'].sum().reset_index()

        # Get the row with the max amount
        max_invoice = grouped_invoices.loc[grouped_invoices['amount'].idxmax()]

        # Merge the max customerId with the customers dataframe to get customer details
        max_customer = df_customers[df_customers['ID'] == max_invoice['customerId']]

        # Extract the name, surname, and max amount
        result = max_customer[['name', 'surname']].copy()
        result['max_amount'] = max_invoice['amount']

    except Exception as e:
        print("exception found: {}".format(e))

    return result
