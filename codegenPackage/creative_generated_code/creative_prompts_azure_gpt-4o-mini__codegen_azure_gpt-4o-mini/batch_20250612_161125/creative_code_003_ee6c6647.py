"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artocean.org
Prompt: What features make Artlife's NFT marketplace stand out for digital artists and collectors?
Generated: DETERMINISTIC_ee6c66470a13b29d
Batch ID: 20250612_161125
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
    A class to represent an NFT marketplace tailored for digital artists and collectors.
    
    Attributes
    ----------
    name : str
        Name of the marketplace
    digital_artists : list
        List of registered digital artists
    collectors : list
        List of registered collectors
    nfts : list
        List of NFTs available in the marketplace
    """

    def __init__(self, name):
        """
        Initializes the NFTMarketplace with a name, and empty lists for artists, collectors, and NFTs.
        
        Parameters
        ----------
        name : str
            The name of the NFT marketplace
        """
        self.name = name
        self.digital_artists = []
        self.collectors = []
        self.nfts = []

    def register_artist(self, artist_name):
        """
        Registers a new digital artist to the marketplace.
        
        Parameters
        ----------
        artist_name : str
            The name of the artist to register
        
        Raises
        ------
        ValueError
            If the artist name is already registered
        """
        if artist_name in self.digital_artists:
            raise ValueError("Artist already registered.")
        self.digital_artists.append(artist_name)
        print(f"Artist '{artist_name}' registered successfully.")

    def register_collector(self, collector_name):
        """
        Registers a new collector to the marketplace.
        
        Parameters
        ----------
        collector_name : str
            The name of the collector to register
        
        Raises
        ------
        ValueError
            If the collector name is already registered
        """
        if collector_name in self.collectors:
            raise ValueError("Collector already registered.")
        self.collectors.append(collector_name)
        print(f"Collector '{collector_name}' registered successfully.")

    def list_nfts(self):
        """
        Lists all NFTs available in the marketplace.
        
        Returns
        -------
        list
            A list of all NFTs
        """
        return self.nfts

    def add_nft(self, nft):
        """
        Adds a new NFT to the marketplace.
        
        Parameters
        ----------
        nft : dict
            The NFT to add, containing 'title', 'artist', and 'price'
        
        Raises
        ------
        ValueError
            If the NFT lacks required information
        """
        required_fields = ['title', 'artist', 'price']
        if not all(field in nft for field in required_fields):
            raise ValueError("NFT must include title, artist, and price.")
        
        self.nfts.append(nft)
        print(f"NFT '{nft['title']}' added successfully.")

    def purchase_nft(self, nft_title, collector_name):
        """
        Allows a collector to purchase an NFT from the marketplace.
        
        Parameters
        ----------
        nft_title : str
            The title of the NFT to purchase
        collector_name : str
            The name of the collector making the purchase
        
        Raises
        ------
        ValueError
            If the NFT is not found or the collector is not registered
        """
        if collector_name not in self.collectors:
            raise ValueError("Collector not registered.")
        
        nft = next((nft for nft in self.nfts if nft['title'] == nft_title), None)
        if nft is None:
            raise ValueError("NFT not found.")
        
        # Simulating a purchase process
        print(f"Collector '{collector_name}' purchased NFT '{nft_title}' for {nft['price']}.")

# Example usage
if __name__ == "__main__":
    marketplace = NFTMarketplace("Artlife")

    try:
        marketplace.register_artist("Alice")
        marketplace.register_collector("Bob")
        marketplace.add_nft({'title': 'Sunset', 'artist': 'Alice', 'price': 100})
        print(marketplace.list_nfts())
        marketplace.purchase_nft('Sunset', 'Bob')
    except ValueError as e:
        print(f"Error: {e}")
```
