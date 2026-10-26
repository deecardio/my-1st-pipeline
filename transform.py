import pandas as pd


def avg_revenue_per_customer(orders: pd.DataFrame) -> float:
    """Считает среднюю выручку на одного клиента."""
    return orders.groupby("customer_id")["amount"].sum().mean()