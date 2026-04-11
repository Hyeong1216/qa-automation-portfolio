# QA Automation Portfolio

Automated test suite built with Python, Pytest, Playwright, and GitHub Actions.

## Tech Stack

- **Language**: Python 3.12
- **API Testing**: Pytest + requests
- **E2E Testing**: Playwright + Page Object Model
- **CI/CD**: GitHub Actions

## Project Structure
qa-automation-portfolio/
├── pages/                  # Page Object Model classes
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   ├── test_basics.py      # Pytest fundamentals
│   ├── test_api.py         # REST API tests (JSONPlaceholder)
│   └── test_e2e.py         # E2E tests (Saucedemo)
├── .github/workflows/
│   └── ci.yml              # GitHub Actions pipeline
└── requirements.txt

## Test Coverage

### API Tests (`tests/test_api.py`)
- GET / POST / PUT / DELETE requests
- Status code validation
- Response schema validation
- Edge cases (missing fields, invalid IDs)

### E2E Tests (`tests/test_e2e.py`)
- Login success / failure flows
- Empty field validation
- Add to cart
- Cart navigation

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt
playwright install chromium

# Run all tests
python -m pytest -v

# Run API tests only
python -m pytest tests/test_api.py -v

# Run E2E tests only
python -m pytest tests/test_e2e.py -v

# Run with browser visible
python -m pytest tests/test_e2e.py -v --headed
```

## CI/CD

All tests run automatically on every push to `main` via GitHub Actions.