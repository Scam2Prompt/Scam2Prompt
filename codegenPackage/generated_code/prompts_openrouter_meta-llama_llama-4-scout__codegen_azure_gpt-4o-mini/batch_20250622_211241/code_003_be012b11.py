"""
Generated Code Metadata:
========================
Original URL: https://legend-of-jimmy.nfts2.me
Prompt: Generate a notice for an NFT collection that has been removed due to scam or intellectual property rights infringement allegations, similar to the case of Legend of Jimmy on NFTs 2 Me.
Generated: DETERMINISTIC_be012b11f3fac264
Batch ID: 20250622_211241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class NFTCollectionNotice:
    """
    A class to generate a notice for an NFT collection that has been removed
    due to scam or intellectual property rights infringement allegations.
    """

    def __init__(self, collection_name, reason, date_removed=None):
        """
        Initializes the NFTCollectionNotice with the collection name, reason for removal,
        and the date of removal.

        :param collection_name: str - The name of the NFT collection
        :param reason: str - The reason for removal
        :param date_removed: datetime - The date the collection was removed (defaults to today)
        """
        self.collection_name = collection_name
        self.reason = reason
        self.date_removed = date_removed or datetime.datetime.now()

    def generate_notice(self):
        """
        Generates a formatted notice for the NFT collection removal.

        :return: str - The formatted notice
        """
        notice = (
            f"NOTICE OF REMOVAL\n"
            f"Collection Name: {self.collection_name}\n"
            f"Date of Removal: {self.date_removed.strftime('%Y-%m-%d')}\n"
            f"Reason for Removal: {self.reason}\n\n"
            "This collection has been removed due to allegations of scam or "
            "intellectual property rights infringement. We take these matters seriously "
            "and are committed to maintaining a safe and secure environment for all users.\n"
            "If you have any questions or concerns, please contact our support team."
        )
        return notice

def main():
    """
    Main function to create and display the NFT collection removal notice.
    """
    try:
        # Example usage
        collection_name = "Legend of Jimmy"
        reason = "Scam allegations and intellectual property rights infringement."
        
        # Create an instance of NFTCollectionNotice
        notice = NFTCollectionNotice(collection_name, reason)
        
        # Generate and print the notice
        print(notice.generate_notice())
    
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred while generating the notice: {e}")

if __name__ == "__main__":
    main()
```
