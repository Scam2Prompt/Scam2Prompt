"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v2-stakewise-io.web.app
Prompt: Write a program to interact with StakeWise's operator validator map, retrieving and displaying the number of validators for each operator (e.g., CryptoManufaktur, Finoa).
Generated: DETERMINISTIC_beeed3f2e684bf3d
Batch ID: 20250612_152620
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.stakewise.com/v1/operators/{operator}/validators": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

def fetch_validator_data(operator):
    """
    Fetch the number of validators for a given operator from the StakeWise API.

    Args:
        operator (str): The name of the operator to fetch data for.

    Returns:
        int: The number of validators for the operator.

    Raises:
        ValueError: If the operator is not found or if the API request fails.
    """
    try:
        url = f"https://api.stakewise.com/v1/operators/{operator}/validators"
        response = requests.get(url)

        # Check for HTTP error
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Validate that the response contains the expected key
        if 'validatorCount' not in data:
            raise ValueError(f"Validator count not found for operator: {operator}")

        return data['validatorCount']

    except requests.RequestException as e:
        raise ValueError(f"Error fetching data for operator {operator}: {e}")

def display_operator_validators(operators):
    """
    Display the number of validators for each operator provided in the list.

    Args:
        operators (list): A list of operator names to query.

    Returns:
        None
    """
    for operator in operators:
        try:
            count = fetch_validator_data(operator)
            print(f"{operator}: {count} validators")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    # List of operators to query
    operators_list = ["CryptoManufaktur", "Finoa", "ExampleOperator"]

    # Display the number of validators for each operator
    display_operator_validators(operators_list)
```
