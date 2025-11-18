"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmfinance-claim.pages.dev
Prompt: Develop a program to utilize MMF NFTs for boosting yields in farms and vaults. Include logic to calculate the yield boost percentage based on NFT ownership.
Generated: DETERMINISTIC_6a292757e2aa0288
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NFT:
    """
    Represents a Non-Fungible Token (NFT) that can boost yields.
    """
    def __init__(self, id: str, boost_percentage: float):
        """
        Initializes the NFT with an ID and a boost percentage.

        :param id: Unique identifier for the NFT
        :param boost_percentage: The percentage by which it boosts yields
        """
        self.id = id
        self.boost_percentage = boost_percentage


class User:
    """
    Represents a user who can own NFTs and participate in yield farming.
    """
    def __init__(self, username: str):
        """
        Initializes the user with a username and an empty list of NFTs.

        :param username: The username of the user
        """
        self.username = username
        self.owned_nfts = []

    def add_nft(self, nft: NFT):
        """
        Adds an NFT to the user's collection.

        :param nft: The NFT to be added
        """
        self.owned_nfts.append(nft)

    def calculate_yield_boost(self) -> float:
        """
        Calculates the total yield boost from all owned NFTs.

        :return: Total yield boost percentage
        """
        total_boost = sum(nft.boost_percentage for nft in self.owned_nfts)
        return total_boost


class Farm:
    """
    Represents a yield farm that can utilize NFTs for boosting yields.
    """
    def __init__(self, base_yield: float):
        """
        Initializes the farm with a base yield.

        :param base_yield: The base yield of the farm without any boosts
        """
        self.base_yield = base_yield

    def calculate_final_yield(self, user: User) -> float:
        """
        Calculates the final yield of the farm, factoring in the user's NFT yield boosts.

        :param user: The user participating in the farm
        :return: The final yield after applying NFT boosts
        """
        try:
            yield_boost = user.calculate_yield_boost()
            final_yield = self.base_yield * (1 + yield_boost / 100)
            return final_yield
        except Exception as e:
            print(f"Error calculating final yield: {e}")
            return self.base_yield  # Return base yield in case of error


# Example Usage:
if __name__ == "__main__":
    # Create some NFTs
    nft1 = NFT("NFT_1", 10.0)  # 10% boost
    nft2 = NFT("NFT_2", 15.0)  # 15% boost

    # Create a user and assign NFTs
    user = User("farmer123")
    user.add_nft(nft1)
    user.add_nft(nft2)

    # Create a farm with a base yield
    farm = Farm(base_yield=100.0)  # Base yield of 100

    # Calculate the final yield for the user
    final_yield = farm.calculate_final_yield(user)
    print(f"Final yield for {user.username}: {final_yield:.2f}")
```
