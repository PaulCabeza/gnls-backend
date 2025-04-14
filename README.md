# Genlogs test exercise API

A FastAPI application that provides a search functionality for transport carriers between cities.

## Features

- Search for transport carriers based on the origin and destination cities.
- Returns a list of carriers with their names and the number of trucks they operate per day.
- Default carriers are returned if the route is unknown.

## Requirements

Make sure you have the following requirements installed:

- Python 3.x
- FastAPI
- Uvicorn
- HTTPX
- Pytest

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/paulcabeza/gnls-backend.git
   ```
2. Navigate to the project directory:
   ```bash
   cd your_repository
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the FastAPI application, use the following command:

```bash
uvicorn main:app --reload
```

You can then access the API at `http://127.0.0.1:8000/search` and use query parameters `from_city` and `to_city` to search for carriers.

## Testing

Instructions on how to run the tests:

```bash
pytest test_main.py
```
