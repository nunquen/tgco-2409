import pytest
import pandas as pd


@pytest.fixture
def get_dataframe():
    data = {'name': ['Bob'],
            'surname': ['McAdoo'],
            'max_amount': [276.55]}

    df = pd.DataFrame(data)

    yield df


@pytest.fixture
def get_customer_and_max_spending():
    customer_id = 1
    max_amount = 276.55

    yield customer_id, max_amount


@pytest.fixture
def get_customers_payload():
    request_body = {
        'customers':
            [
                {
                    'ID': 0,
                    'name': 'Alice',
                    'surname': 'Klark'
                },
                {
                    'ID': 1,
                    'name': 'Bob',
                    'surname': 'McAdoo'
                },
                {
                    'ID': 2,
                    'name': 'Cindy',
                    'surname': 'Law'},
                {
                    'ID': 3,
                    'name': 'David',
                    'surname': 'Nap'
                },
                {
                    'ID': 4,
                    'name': 'Elvis',
                    'surname': 'Blue'
                }
            ]
        }

    yield request_body


@pytest.fixture
def get_invoices_payload():
    request_body = {
        "invoices": [
            {
                "ID": 0,
                "customerId": 0,
                "amount": 12.0
            },
            {
                "ID": 1,
                "customerId": 0,
                "amount": 235.78
            },
            {
                "ID": 2,
                "customerId": 1,
                "amount": 5.06
            },
            {
                "ID": 3,
                "customerId": 2,
                "amount": 12.6
            },
            {
                "ID": 4,
                "customerId": 3,
                "amount": 0.99
            },
            {
                "ID": 5,
                "customerId": 1,
                "amount": 12.0
            },
            {
                "ID": 6,
                "customerId": 1,
                "amount": 235.78
            },
            {
                "ID": 7,
                "customerId": 1,
                "amount": 5.06
            },
            {
                "ID": 8,
                "customerId": 1,
                "amount": 12.6
            },
            {
                "ID": 9,
                "customerId": 1,
                "amount": 0.99
            },
            {
                "ID": 10,
                "customerId": 3,
                "amount": 12.0
            },
            {
                "ID": 11,
                "customerId": 2,
                "amount": 235.78
            },
            {
                "ID": 12,
                "customerId": 1,
                "amount": 5.06
            },
            {
                "ID": 13,
                "customerId": 0,
                "amount": 12.6
            },
            {
                "ID": 15,
                "customerId": 3,
                "amount": 0.99
            }
        ]
        }

    yield request_body
