import pandas as pd


def avg_revenue_per_customer(orders: pd.DataFrame) -> float:
        # 'calculates average revenue per customer'
    return orders.groupby("customer_id")["amount"].sum().mean() 
