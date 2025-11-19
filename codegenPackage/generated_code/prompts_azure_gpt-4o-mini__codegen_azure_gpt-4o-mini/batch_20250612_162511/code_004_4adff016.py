"""
Generated Code Metadata:
========================
Original URL: https://etherealize.fi
Prompt: Provide an example of how to leverage Ethereum for asset tokenization, incorporating insights from Etherealize's research.
Generated: DETERMINISTIC_4adff016a6732982
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's ERC721 implementation for non-fungible tokens (NFTs)
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// AssetToken is a contract for tokenizing assets as NFTs
contract AssetToken is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to asset details
    mapping(uint256 => string) private _assetDetails;

    // Event emitted when a new asset is tokenized
    event AssetTokenized(uint256 indexed tokenId, string assetDetail);

    // Constructor to set the name and symbol of the NFT
    constructor() ERC721("AssetToken", "ATK") {}

    // Function to tokenize a new asset
    // @param assetDetail: A string containing details about the asset
    function tokenizeAsset(string memory assetDetail) public onlyOwner {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the owner
        _mint(msg.sender, tokenId);

        // Store the asset details
        _assetDetails[tokenId] = assetDetail;

        // Emit the asset tokenized event
        emit AssetTokenized(tokenId, assetDetail);
    }

    // Function to retrieve asset details by token ID
    // @param tokenId: The ID of the token to query
    // @return The details of the asset associated with the token ID
    function getAssetDetails(uint256 tokenId) public view returns (string memory) {
        // Ensure the token exists
        require(_exists(tokenId), "Token does not exist");
        return _assetDetails[tokenId];
    }

    // Function to transfer ownership of an asset
    // @param to: The address to transfer the asset to
    // @param tokenId: The ID of the token to transfer
    function transferAsset(address to, uint256 tokenId) public {
        // Ensure the caller is the owner of the token
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner");
        // Transfer the token
        _transfer(msg.sender, to, tokenId);
    }
}
```
