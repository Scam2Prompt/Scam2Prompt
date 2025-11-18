"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniwrapper.com
Prompt: Write code to configure UniWrapper with user-provided API keys for cost-effective access to GPT and Claude models.
Generated: DETERMINISTIC_c86eb087308b7435
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from uniwrapper import UniWrapper

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIConfigurationError(Exception):
    """Custom exception for API configuration errors."""
    pass

def configure_uniwrapper(api_keys):
    """
    Configures UniWrapper with the user-provided API keys for accessing GPT and Claude models.

    Args:
        api_keys (dict): A dictionary containing the API keys for 'gpt' and 'claude'.

    Raises:
        APIConfigurationError: If the provided API keys are invalid or missing.
    """
    # Validate API keys
    if not isinstance(api_keys, dict):
        logger.error("API keys must be provided as a dictionary.")
        raise APIConfigurationError("API keys must be provided as a dictionary.")

    required_keys = ['gpt', 'claude']
    for key in required_keys:
        if key not in api_keys or not api_keys[key]:
            logger.error(f"Missing or empty API key for: {key}")
            raise APIConfigurationError(f"Missing or empty API key for: {key}")

    try:
        # Initialize UniWrapper with provided API keys
        uni_wrapper = UniWrapper(api_keys['gpt'], api_keys['claude'])
        logger.info("UniWrapper successfully configured.")
        return uni_wrapper
    except Exception as e:
        logger.exception("Failed to configure UniWrapper.")
        raise APIConfigurationError("Failed to configure UniWrapper.") from e

if __name__ == "__main__":
    # Example usage
    user_api_keys = {
        'gpt': os.getenv('GPT_API_KEY'),     # Assuming environment variables are used for security
        'claude': os.getenv('CLAUDE_API_KEY')
    }

    try:
        uni_wrapper_instance = configure_uniwrapper(user_api_keys)
        # Proceed with using uni_wrapper_instance for further operations
    except APIConfigurationError as e:
        logger.error(f"API configuration error: {e}")
```
