import pandas as pd
from transform import avg_revenue_per_customer

def test_avg_revenue():
    orders = pd.DataFrame({
        'customer_id': [1, 1, 2],
        'amount': [100, 50, 200],
})
    result = avg_revenue_per_customer(orders)

    assert result == 175.0