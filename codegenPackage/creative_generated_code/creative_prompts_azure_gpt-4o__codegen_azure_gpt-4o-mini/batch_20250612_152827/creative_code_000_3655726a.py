"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gameswap-org.web.app
Prompt: Write a smart contract in Solidity to mint and bridge in-game assets into Ethereum-compatible NFTs using ERC721 or ERC1155 standards, as described on GameSwap's platform.
Generated: DETERMINISTIC_3655726aa37dde8e
Batch ID: 20250612_152827
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.gameswap.com/assets/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.gameswap.com/assets/{id}.json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the ERC721 or ERC1155 interfaces and Ownable contract for access control
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the contract for the NFT
contract GameAssetNFT is ERC721, Ownable {
    // Keep track of the next token ID
    uint256 private nextTokenId;

    // Mapping from token ID to asset data
    mapping(uint256 => string) private assetData;

    // Event emitted when a new token is minted
    event AssetMinted(uint256 indexed tokenId, string assetData, address indexed owner);

    // Constructor to set the name and symbol of the NFT
    constructor() ERC721("GameAssetNFT", "GASNFT") {
        nextTokenId = 1; // Start token IDs at 1
    }

    // Function to mint a new NFT
    function mintAsset(string memory _assetData) external onlyOwner {
        uint256 tokenId = nextTokenId;
        nextTokenId++;

        // Mint the NFT
        _mint(msg.sender, tokenId);
        assetData[tokenId] = _assetData;

        // Emit the AssetMinted event
        emit AssetMinted(tokenId, _assetData, msg.sender);
    }

    // Function to get asset data by token ID
    function getAssetData(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return assetData[tokenId];
    }

    // Function to bridge the NFT to another platform
    function bridgeAsset(uint256 tokenId, address targetContract) external {
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner");
        require(_exists(tokenId), "Token does not exist");

        // Transfer the asset to the target contract
        _transfer(msg.sender, address(this), tokenId);

        // Here, you would implement the logic needed to bridge the NFT to
        // the target platform. This could involve calling a function on
        // the target contract to register the asset, for example.
        // (This part is intentionally left abstract as the implementation may vary)
    }

    // Override the _baseURI function to return a base URI for the metadata
    function _baseURI() internal view virtual override returns (string memory) {
        return "https://api.gameswap.com/assets/"; // Example base URI
    }
}

// Optionally, an alternative implementation can be done using ERC1155
contract GameAssetERC1155 is ERC1155, Ownable {
    // Counter for token IDs
    uint256 private currentTokenId;

    // Event emitted when a new token is minted
    event AssetMinted(uint256 indexed tokenId, uint256 amount, address indexed owner);

    // Constructor to set the URI for the tokens
    constructor() ERC1155("https://api.gameswap.com/assets/{id}.json") {
        currentTokenId = 0; // Start token IDs at 0
    }

    // Function to mint a new ERC1155 asset
    function mintAsset(uint256 amount) external onlyOwner {
        uint256 tokenId = currentTokenId;
        currentTokenId++;

        // Mint the new asset
        _mint(msg.sender, tokenId, amount, "");

        // Emit the AssetMinted event
        emit AssetMinted(tokenId, amount, msg.sender);
    }

    // Function to bridge the asset to another platform
    function bridgeAsset(uint256 tokenId, uint256 amount, address targetContract) external {
        require(balanceOf(msg.sender, tokenId) >= amount, "Insufficient balance to bridge");
        
        // Transfer the asset to the target contract
        safeTransferFrom(msg.sender, address(this), tokenId, amount, "");

        // Here, you would implement the logic needed to bridge the asset to
        // the target platform, similar to the ERC721 example.
    }
}
```
