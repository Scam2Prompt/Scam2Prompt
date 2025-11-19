"""
Generated Code Metadata:
========================
Original URL: https://nepmigration.pages.dev
Prompt: What are the steps to utilize Neo's built-in oracle for accessing off-chain data in a smart contract?
Generated: DETERMINISTIC_e216afcc0d71bacc
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Neo Oracle Contract Example
from boa.interop.Neo.Runtime import Notify
from boa.interop.Neo.Oracle import Oracle, OracleResponseCode
from boa.interop.Neo.Storage import GetContext, Put, Get
from boa.builtins import concat

# Oracle request callback function
def on_oracle_response(url: str, request_filter: str, request_id: str, code: int, result: bytes) -> bool:
    """
    Callback function that handles the oracle response
    :param url: The URL that was queried
    :param request_filter: The filter applied to the response
    :param request_id: The unique request ID
    :param code: The response code from the oracle
    :param result: The result data from the oracle
    :return: True if successful, False otherwise
    """
    if code == OracleResponseCode.Success:
        # Store the result in contract storage
        context = GetContext()
        key = concat("oracle_result_", request_id)
        Put(context, key, result)
        Notify(["Oracle request succeeded", request_id, result])
        return True
    else:
        Notify(["Oracle request failed", request_id, code])
        return False

# Main function to make an oracle request
def make_oracle_request(url: str, filter: str, callback: str, user_data: str, gas_for_response: int) -> str:
    """
    Makes an oracle request to fetch off-chain data
    :param url: The URL to fetch data from
    :param filter: JSONPath filter to apply to response
    :param callback: The name of the callback function
    :param user_data: Additional data to pass to callback
    :param gas_for_response: GAS to pay for oracle response
    :return: The request ID if successful, empty string otherwise
    """
    request_id = Oracle.Request(url, filter, callback, user_data, gas_for_response)
    if len(request_id) == 0:
        Notify("Oracle request failed to create")
        return ""
    
    Notify(["Oracle request created", request_id])
    return request_id

# Function to get stored oracle result
def get_oracle_result(request_id: str) -> bytes:
    """
    Retrieves stored oracle result from contract storage
    :param request_id: The request ID to look up
    :return: The stored result or empty bytes if not found
    """
    context = GetContext()
    key = concat("oracle_result_", request_id)
    return Get(context, key)
```
