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
"""
NFT Collection Removal Notice

This script generates a standardized notice for an NFT collection that has been removed
due to scam or intellectual property rights infringement allegations.
"""

def generate_removal_notice(collection_name, platform_name, contact_email, additional_details=None):
    """
    Generates a removal notice for an NFT collection.

    Args:
        collection_name (str): Name of the NFT collection being removed
        platform_name (str): Name of the platform removing the collection
        contact_email (str): Email address for inquiries
        additional_details (str, optional): Any additional details about the removal

    Returns:
        str: Formatted removal notice
    """
    notice = f"""
    IMPORTANT NOTICE: {collection_name.upper()} COLLECTION REMOVAL

    Dear Community Members,

    This is to inform you that the NFT collection "{collection_name}" has been 
    removed from {platform_name} effective immediately.

    REASON FOR REMOVAL:
    The collection has been removed due to:
    - Credible allegations of scam/fraudulent activity
    - Intellectual property rights infringement claims

    {additional_details if additional_details else ''}

    We take the integrity of our platform and the protection of intellectual property 
    rights very seriously. After careful review, we've determined this action to be 
    necessary to maintain trust within our community.

    If you believe this removal was in error or have any questions, please contact:
    {contact_email}

    Please note:
    - Any transactions involving this collection prior to removal remain on the blockchain
    - We recommend exercising caution with any secondary market activity
    - Platform support will not be available for removed collections

    Thank you for your understanding.

    Sincerely,
    The {platform_name} Team
    """

    return notice.strip()

# Example usage
if __name__ == "__main__":
    notice = generate_removal_notice(
        collection_name="Legend of Jimmy",
        platform_name="NFTs 2 Me",
        contact_email="legal@nfts2me.com",
        additional_details="This decision was made after review of multiple copyright infringement reports from the original IP owner."
    )
    print(notice)
```
