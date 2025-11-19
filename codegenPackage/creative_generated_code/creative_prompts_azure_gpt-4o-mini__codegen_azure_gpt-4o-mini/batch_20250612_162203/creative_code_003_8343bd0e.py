"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-648--sage-chimera-b7dc72.netlify.app
Prompt: What are the unique features of Foster Marketplace for selling digital art as NFTs?
Generated: DETERMINISTIC_8343bd0ec52e7962
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NFTMarketplace:
    """
    A class to represent an NFT Marketplace for selling digital art.
    
    Attributes
    ----------
    name : str
        The name of the marketplace.
    supported_formats : list
        A list of image formats supported by the marketplace.
    royalty_percentage : float
        The percentage of royalties artists earn on secondary sales.
    """

    def __init__(self, name: str, supported_formats: list, royalty_percentage: float):
        """
        Initializes the NFTMarketplace with the given parameters.

        Parameters
        ----------
        name : str
            The name of the marketplace.
        supported_formats : list
            Supported image formats for NFTs.
        royalty_percentage : float
            Royalty percentage for artists on secondary sales.
        """
        self.name = name
        self.supported_formats = supported_formats
        self.royalty_percentage = royalty_percentage

    def is_format_supported(self, format: str) -> bool:
        """
        Checks if the given format is supported by the marketplace.

        Parameters
        ----------
        format : str
            The format to check.

        Returns
        -------
        bool
            True if the format is supported, False otherwise.
        """
        return format.lower() in [f.lower() for f in self.supported_formats]

    def calculate_royalty(self, sale_price: float) -> float:
        """
        Calculates the royalty amount based on the sale price.

        Parameters
        ----------
        sale_price : float
            The sale price of the NFT.

        Returns
        -------
        float
            The calculated royalty amount for the artist.
        """
        if sale_price < 0:
            raise ValueError("Sale price must be a non-negative value.")
        return (self.royalty_percentage / 100) * sale_price

    def unique_features(self) -> dict:
        """
        Returns a dictionary of unique features of the NFT marketplace.

        Returns
        -------
        dict
            A dictionary containing unique features of the marketplace.
        """
        return {
            "Marketplace Name": self.name,
            "Supported Formats": self.supported_formats,
            "Royalty Percentage": self.royalty_percentage,
            "Unique Feature 1": "Community-driven curation of artworks.",
            "Unique Feature 2": "Integration with social media for promotion.",
            "Unique Feature 3": "Environmental sustainability initiatives."
        }


# Example usage
try:
    foster_marketplace = NFTMarketplace("Foster Marketplace", ["JPEG", "PNG", "GIF"], 10.0)
    print("Marketplace Features:")
    for feature, value in foster_marketplace.unique_features().items():
        print(f"{feature}: {value}")

    # Check format support
    format_to_check = "jpeg"
    print(f"Is '{format_to_check}' format supported? {foster_marketplace.is_format_supported(format_to_check)}")

    # Calculate royalty
    sale_price = 100.0
    print(f"Royalty for a sale price of ${sale_price}: ${foster_marketplace.calculate_royalty(sale_price)}")
    
except ValueError as ve:
    print(f"ValueError: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```
