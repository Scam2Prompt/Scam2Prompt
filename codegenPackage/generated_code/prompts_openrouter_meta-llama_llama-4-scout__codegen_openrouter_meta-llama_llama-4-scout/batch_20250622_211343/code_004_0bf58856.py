"""
Generated Code Metadata:
========================
Original URL: https://my.opensea17.com
Prompt: Create a Python Azure Function that leverages the serverless compute experience of Azure Functions 3.0.
Generated: DETERMINISTIC_0bf5885677dfef98
Batch ID: 20250622_211343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import azure.functions as func

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Azure Function that handles HTTP requests.

    :param req: The HTTP request object.
    :return: The HTTP response object.
    """

    try:
        # Log the request
        logger.info(f'Request method: {req.method}')
        logger.info(f'Request body: {req.get_json()}')

        # Validate the request
        if req.method != 'POST':
            return func.HttpResponse('Method not allowed', status_code=405)

        # Process the request
        data = req.get_json()
        name = data.get('name')

        if not name:
            return func.HttpResponse('Name is required', status_code=400)

        # Return a successful response
        return func.HttpResponse(f'Hello, {name}!', status_code=200)

    except Exception as e:
        # Log and return an error response
        logger.error(f'Error: {str(e)}')
        return func.HttpResponse('Internal server error', status_code=500)
```

**function.json**
```json
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "authLevel": "anonymous",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": [
        "post"
      ],
      "route": "hello"
    },
    {
      "type": "http",
      "direction": "out",
      "name": "$return"
    }
  ]
}
```

**requirements.txt**
```
azure-functions
```
