# my-1st-pipeline

A small project where I learn to set up CI with GitHub Actions for Python data-processing code.

## What's inside

- `transform.py`: the function `avg_revenue_per_customer`, which calculates average revenue per customer (pandas).
- `test_transform.py`: a pytest unit test using a small DataFrame with three orders.
- `.github/workflows/ci.yml`: the CI workflow. On every Pull Request into `main`, it installs dependencies and runs the tests.

## Run the tests locally

```bash
pip install -r requirements.txt
pytest
```

## What's next

- Add dbt models and their tests.
- Connect Snowflake.
- Extend CI to check the dbt project.