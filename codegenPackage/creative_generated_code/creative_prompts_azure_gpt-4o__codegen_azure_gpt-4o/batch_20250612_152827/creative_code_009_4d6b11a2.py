"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kevinland.pages.dev
Prompt: Create a Python script using Brownie or Hardhat to test the minting functionality of an NFT smart contract similar to KevinLand's minting process.
Generated: DETERMINISTIC_4d6b11a27684c5e5
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# brownietest_nft.py

# Import necessary modules from Brownie
from brownie import accounts, NFTContract, reverts
import pytest

# Define the test suite
def test_nft_minting():
    """
    Test the minting functionality of the NFT smart contract.
    Ensures that NFTs can be minted correctly and checks various edge cases.
    """
    # Load test accounts
    owner = accounts[0]  # Contract owner
    user = accounts[1]   # Regular user
    
    # Deploy the NFT contract
    nft = NFTContract.deploy({"from": owner})
    
    # Assert the contract is deployed
    assert nft.address != "", "Contract deployment failed!"

    # Test minting functionality
    # Test case: Owner successfully mints an NFT
    token_id = 1  # Define token ID for minting
    tx = nft.mint(user, token_id, {"from": owner})
    tx.wait(1)  # Wait for transaction to be mined
    
    # Assert minting was successful
    assert nft.ownerOf(token_id) == user, f"Token {token_id} was not minted to the correct owner!"
    assert nft.balanceOf(user) == 1, "User's balance of NFTs is incorrect!"

    # Test case: Attempt to mint with a token ID that is already minted
    with reverts("ERC721: token already minted"):
        nft.mint(user, token_id, {"from": owner})  # This should fail

    # Test case: Non-owner tries to mint an NFT
    with reverts("Ownable: caller is not the owner"):
        nft.mint(user, 2, {"from": user})  # This should fail

    # Test case: Owner can mint multiple NFTs
    for i in range(2, 5):
        tx = nft.mint(user, i, {"from": owner})
        tx.wait(1)  # Wait for transaction to be mined
        assert nft.ownerOf(i) == user, f"Token {i} was not minted to the correct owner!"

    # Clean exit
    print("All tests passed successfully!")

# Run the test suite
@pytest.mark.parametrize("nft_contract", ["NFTContract"])
def main():
    test_nft_minting()
```
