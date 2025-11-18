"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksyn-airdrop-4.nfts2.me
Prompt: Write code to detect and flag NFT collections reported as scams using metadata analysis.
Generated: DETERMINISTIC_143905cbc8eedf48
Batch ID: 20250612_154001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NFTScamDetector:
    """
    Class for detecting and flagging NFT collections reported as scams using metadata analysis.
    """

    def __init__(self, flagged_keywords=None, minimum_reports_threshold=5):
        """
        Initialize the detector with flagged keywords and minimum reports threshold.

        :param flagged_keywords: List of keywords commonly associated with scams in NFT metadata.
        :param minimum_reports_threshold: Minimum number of reports to flag a collection.
        """
        self.flagged_keywords = flagged_keywords or ["rugpull", "phishing", "scam", "fraud"]
        self.minimum_reports_threshold = minimum_reports_threshold

    def analyze_metadata(self, metadata):
        """
        Analyze NFT metadata for flagged keywords.

        :param metadata: Dictionary containing NFT metadata.
        :return: True if flagged keywords are detected, False otherwise.
        """
        if not isinstance(metadata, dict):
            logging.error("Invalid metadata format. Expected a dictionary.")
            return False

        for keyword in self.flagged_keywords:
            for key, value in metadata.items():
                if isinstance(value, str) and keyword.lower() in value.lower():
                    logging.warning(f"Flagged keyword detected: '{keyword}' in metadata key '{key}'")
                    return True
        return False

    def is_scam(self, nft_collection):
        """
        Check if an NFT collection is flagged as a scam.

        :param nft_collection: Dictionary containing NFT collection data.
        :return: Boolean indicating whether the collection is flagged as a scam.
        """
        # Error handling for invalid input
        if not isinstance(nft_collection, dict):
            logging.error("Invalid NFT collection format. Expected a dictionary.")
            return False
        
        # Extract metadata and reports count
        metadata = nft_collection.get("metadata", {})
        reports_count = nft_collection.get("reports_count", 0)

        # Flag collection if metadata analysis detects suspicious activity
        if self.analyze_metadata(metadata):
            logging.info("NFT collection flagged due to suspicious metadata.")
            return True

        # Flag collection if reports exceed the threshold
        if reports_count >= self.minimum_reports_threshold:
            logging.info(f"NFT collection flagged due to exceeding report threshold: {reports_count} reports.")
            return True

        # Collection is not flagged
        logging.info("NFT collection is not flagged as a scam.")
        return False


# Example usage
if __name__ == "__main__":
    # Sample NFT collection data
    nft_collection_data = {
        "name": "Example NFT Collection",
        "metadata": {
            "description": "A fraudulent rugpull NFT collection",
            "creator": "Unknown",
            "tags": ["art", "rugpull"]
        },
        "reports_count": 7
    }

    # Initialize the scam detector
    detector = NFTScamDetector()

    # Check if the NFT collection is flagged as a scam
    is_scam = detector.is_scam(nft_collection_data)

    # Output the result
    if is_scam:
        print(f"The NFT collection '{nft_collection_data['name']}' has been flagged as a scam.")
    else:
        print(f"The NFT collection '{nft_collection_data['name']}' is not flagged as a scam.")
```
