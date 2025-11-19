"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappssync.pages.dev
Prompt: Create a script to manage NFT issues and whitelist problems as described in the troubleshooting section of dappssync.pages.dev.
Generated: DETERMINISTIC_7b1da89bbdd8af06
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
NFT Management and Whitelist Troubleshooting Script

This script is designed to address common issues related to NFTs and whitelisting on a decentralized application platform.
It includes functionality for managing NFT metadata, verifying whitelist entries, and handling associated errors.

Author: Expert Programmer
"""

import json
import logging

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class NFTManager:
    """
    Class for managing NFT metadata and whitelist verification.
    """
    def __init__(self, nft_metadata_file, whitelist_file):
        """
        Initializes the NFTManager with metadata and whitelist files.

        :param nft_metadata_file: Path to the NFT metadata JSON file.
        :param whitelist_file: Path to the whitelist JSON file.
        """
        self.nft_metadata_file = nft_metadata_file
        self.whitelist_file = whitelist_file
        self.nft_metadata = None
        self.whitelist = None

    def load_metadata(self):
        """
        Loads NFT metadata from the specified JSON file.

        :raises FileNotFoundError: If the file does not exist.
        :raises json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(self.nft_metadata_file, 'r') as file:
                self.nft_metadata = json.load(file)
                logging.info("NFT metadata successfully loaded.")
        except FileNotFoundError:
            logging.error(f"NFT metadata file '{self.nft_metadata_file}' not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Failed to decode NFT metadata JSON.")
            raise

    def load_whitelist(self):
        """
        Loads whitelist data from the specified JSON file.

        :raises FileNotFoundError: If the file does not exist.
        :raises json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(self.whitelist_file, 'r') as file:
                self.whitelist = json.load(file)
                logging.info("Whitelist successfully loaded.")
        except FileNotFoundError:
            logging.error(f"Whitelist file '{self.whitelist_file}' not found.")
            raise
        except json.JSONDecodeError:
            logging.error("Failed to decode whitelist JSON.")
            raise

    def validate_nft_issues():
        pass
