"""
Generated Code Metadata:
========================
Original URL: https://substantial-belgium-incalculable.on-fleek.app
Prompt: Generate a troubleshooting guide for common error codes encountered while using LayerZero's messaging system.
Generated: DETERMINISTIC_19f7de9111d4467e
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, Optional

class LayerZeroErrorCode(Enum):
    """
    Enumeration of common LayerZero error codes and their meanings.
    """
    # General Errors
    LZ_ERROR_NONE = 0
    LZ_ERROR_INVALID_ADAPTER_PARAMS = 1
    LZ_ERROR_INVALID_PAYLOAD = 2
    LZ_ERROR_INVALID_ENDPOINT = 3
    LZ_ERROR_NOT_TRUSTED = 4
    LZ_ERROR_OUT_OF_GAS = 5

    # Configuration Errors
    LZ_ERROR_INVALID_CONFIG = 10
    LZ_ERROR_INVALID_LIBRARY_VERSION = 11
    LZ_ERROR_INVALID_CHAIN_ID = 12

    # Execution Errors
    LZ_ERROR_EXECUTION_FAILED = 20
    LZ_ERROR_REENTRANCY = 21
    LZ_ERROR_TRANSACTION_FAILED = 22

    # Bridge Errors
    LZ_ERROR_BRIDGE_NOT_READY = 30
    LZ_ERROR_BRIDGE_SUSPENDED = 31

    # Custom Errors (if any)
    LZ_ERROR_CUSTOM = 100

class LayerZeroTroubleshooter:
    """
    A utility class to troubleshoot common LayerZero error codes.
    """

    ERROR_DESCRIPTIONS: Dict[LayerZeroErrorCode, str] = {
        LayerZeroErrorCode.LZ_ERROR_NONE: "No error encountered.",
        LayerZeroErrorCode.LZ_ERROR_INVALID_ADAPTER_PARAMS: "Invalid adapter parameters provided.",
        LayerZeroErrorCode.LZ_ERROR_INVALID_PAYLOAD: "Invalid payload format or content.",
        LayerZeroErrorCode.LZ_ERROR_INVALID_ENDPOINT: "Endpoint configuration is invalid.",
        LayerZeroErrorCode.LZ_ERROR_NOT_TRUSTED: "Caller is not a trusted source.",
        LayerZeroErrorCode.LZ_ERROR_OUT_OF_GAS: "Transaction ran out of gas.",
        LayerZeroErrorCode.LZ_ERROR_INVALID_CONFIG: "Invalid LayerZero configuration.",
        LayerZeroErrorCode.LZ_ERROR_INVALID_LIBRARY_VERSION: "Invalid library version used.",
        LayerZeroErrorCode.LZ_ERROR_INVALID_CHAIN_ID: "Invalid destination chain ID.",
        LayerZeroErrorCode.LZ_ERROR_EXECUTION_FAILED: "Message execution failed.",
        LayerZeroErrorCode.LZ_ERROR_REENTRANCY: "Reentrancy detected.",
        LayerZeroErrorCode.LZ_ERROR_TRANSACTION_FAILED: "Transaction failure on destination chain.",
        LayerZeroErrorCode.LZ_ERROR_BRIDGE_NOT_READY: "Bridge is not ready for messages.",
        LayerZeroErrorCode.LZ_ERROR_BRIDGE_SUSPENDED: "Bridge operations are suspended.",
        LayerZeroErrorCode.LZ_ERROR_CUSTOM: "Custom error encountered.",
    }

    RECOMMENDED_ACTIONS: Dict[LayerZeroErrorCode, str] = {
        LayerZeroErrorCode.LZ_ERROR_NONE: "No action required.",
        LayerZeroErrorCode.LZ_ERROR_INVALID_ADAPTER_PARAMS: "Verify and correct adapter parameters.",
        LayerZeroErrorCode.LZ_ERROR_INVALID_PAYLOAD: "Check the payload structure and content.",
        LayerZeroErrorCode.LZ_ERROR_INVALID_ENDPOINT: "Verify endpoint configuration.",
        LayerZeroErrorCode.LZ_ERROR_NOT_TRUSTED: "Ensure caller is on the trusted list.",
        LayerZeroErrorCode.LZ_ERROR_OUT_OF_GAS: "Increase gas limit for the transaction.",
        LayerZeroErrorCode.LZ_ERROR_INVALID_CONFIG: "Review and update LayerZero configuration.",
        LayerZeroErrorCode.LZ_ERROR_INVALID_LIBRARY_VERSION: "Use a compatible library version.",
        LayerZeroErrorCode.LZ_ERROR_INVALID_CHAIN_ID: "Verify destination chain ID and retry.",
        LayerZeroErrorCode.LZ_ERROR_EXECUTION_FAILED: "Inspect execution logs for details.",
        LayerZeroErrorCode.LZ_ERROR_REENTRANCY: "Avoid reentrant calls and retry.",
        LayerZeroErrorCode.LZ_ERROR_TRANSACTION_FAILED: "Check destination chain status and retry.",
        LayerZeroErrorCode.LZ_ERROR_BRIDGE_NOT_READY: "Wait for bridge to be ready or check its status.",
        LayerZeroErrorCode.LZ_ERROR_BRIDGE_SUSPENDED: "Check bridge suspension status and resume if possible.",
        LayerZeroErrorCode.LZ_ERROR_CUSTOM: "Refer to custom error handler for specific actions.",
    }

    @classmethod
    def get_error_description(cls, error_code: int) -> Optional[str]:
        """
        Retrieve the error description for a given error code.

        Args:
            error_code (int): The LayerZero error code.

        Returns:
            Optional[str]: Description of the error if found, None otherwise.
        """
        error = cls._get_error_enum(error_code)
        if error is None:
            return None
        return cls.ERROR_DESCRIPTIONS.get(error, "Unknown error code.")

    @classmethod
    def get_recommended_action(cls, error_code: int) -> Optional[str]:
        """
        Retrieve the recommended action for a given error code.

        Args:
            error_code (int): The LayerZero error code.

        Returns:
            Optional[str]: Recommended action if found, None otherwise.
        """
        error = cls._get_error_enum(error_code)
        if error is None:
            return None
        return cls.RECOMMENDED_ACTIONS.get(error, "No specific recommendation available.")

    @classmethod
    def _get_error_enum(cls, error_code: int) -> Optional[LayerZeroErrorCode]:
        """
        Helper method to map an integer error code to LayerZeroErrorCode enum.

        Args:
            error_code (int): The error code to map.

        Returns:
            Optional[LayerZeroErrorCode]: Enum value if found, None otherwise.
        """
        try:
            return LayerZeroErrorCode(error_code)
        except ValueError:
            return None

# Example usage
if __name__ == "__main__":
    error_code = 1  # Example error code
    description = LayerZeroTroubleshooter.get_error_description(error_code)
    action = LayerZeroTroubleshooter.get_recommended_action(error_code)
    
    print(f"Error Code: {error_code}")
    print(f"Description: {description}")
    print(f"Recommended Action: {action}")
```
