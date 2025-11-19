"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://genesis-bfc.pages.dev
Prompt: Create a function to handle NFT minting issues based on the guidelines from the Genesis BFC platform.
Generated: DETERMINISTIC_6057e6544af7d88e
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import Dict, Any

# Set up logging for monitoring and debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NFTMintingError(Exception):
    """Custom exception for NFT minting issues."""
    pass

def handle_nft_minting_issue(issue_details: Dict[str, Any]) -> str:
    """
    Handles NFT minting issues as per Genesis BFC platform guidelines.

    Args:
        issue_details (Dict[str, Any]): A dictionary containing details about the minting issue.
            Expected keys:
            - 'error_code' (str): The unique error code for the issue.
            - 'error_message' (str): A description of the issue.
            - 'user_id' (str): The ID of the user experiencing the issue.
            - 'nft_id' (str, optional): The ID of the NFT involved, if applicable.

    Returns:
        str: A human-readable resolution message.

    Raises:
        NFTMintingError: If the issue cannot be resolved automatically.
    """
    try:
        # Validate input
        required_keys = ['error_code', 'error_message', 'user_id']
        for key in required_keys:
            if key not in issue_details:
                raise ValueError(f"Missing required key: {key}")

        error_code = issue_details['error_code']
        error_message = issue_details['error_message']
        user_id = issue_details['user_id']
        nft_id = issue_details.get('nft_id', None)

        logger.info(f"Processing minting issue for user_id={user_id}, error_code={error_code}")

        # Handle known error codes as per Genesis BFC guidelines
        resolution_map = {
            "GENESIS001": "Network instability detected. Please retry minting later.",
            "GENESIS002": "Insufficient wallet balance. Advise user to fund their wallet.",
            "GENESIS003": "Invalid NFT metadata. Request user to review and resubmit.",
            "GENESIS004": f"NFT ID {nft_id} already exists. Duplicate minting attempt detected."
        }

        if error_code in resolution_map:
            resolution_message = resolution_map[error_code]
            logger.info(f"Issue resolved: {resolution_message}")
            return resolution_message
        else:
            # If the error code is not recognized, log and raise an exception
            logger.error(f"Unrecognized error code: {error_code}, message: {error_message}")
            raise NFTMintingError(f"Unable to resolve issue with code {error_code}: {error_message}")

    except ValueError as ve:
        logger.exception("Validation error occurred while processing minting issue.")
        raise ve
    except NFTMintingError as nme:
        logger.exception("Unhandled NFT minting issue.")
        raise nme
    except Exception as e:
        logger.exception("An unexpected error occurred.")
        raise NFTMintingError("A critical error occurred during issue handling.") from e
```
