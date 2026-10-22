# Automated Test Results

- **Run date:** 2026-10-22
- **Source:** `main` at `3346263c9774af0d762634c415d8fcddcaf7ad5f`
- **Runtime:** Python 3.12.0, pytest 8.3.5
- **Command:** `PYTHONPATH=src .venv/bin/python -m pytest -q`
- **Result:** **3 passed**, 0 failed (0.84 seconds)

Coverage in this small demo suite:

- Health endpoint returns `200` and `{"status": "ok"}`.
- Synthetic KYC endpoint returns the fixed `review_required` result.
- Invalid application ID input is rejected with `422`.

Pytest reported one dependency deprecation warning from Starlette's test client (`anyio.abc.BlockingPortal`); it did not affect the test result.

The complete `requirements-dev.txt` installation was not used for this run: pip's dependency resolver could not resolve the pinned `pip-audit==2.8.0` dependency chain in this environment. The app dependencies and the pinned pytest/httpx test dependencies installed successfully in an isolated virtual environment. Lint, static analysis, dependency auditing, and container scanning are not included in this local test result; the GitHub Actions workflow remains configured to run those checks.

> This result verifies only the synthetic demo tests. It does not certify the project for banking, production KYC, regulatory compliance, or real customer data.
