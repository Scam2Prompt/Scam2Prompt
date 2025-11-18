"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cornucopiasnft.org
Prompt: Develop a smart contract for managing Cornucopias digital assets, ensuring ownership verification and compatibility with the in-game economy.
Generated: DETERMINISTIC_cdab876cf5eadb67
Batch ID: 20250612_142615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the OpenZeppelin Contracts library for ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for managing Cornucopias digital assets
contract CornucopiasAsset is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new asset is created
    event AssetCreated(uint256 indexed tokenId, address indexed owner, string tokenURI);

    // Modifier to verify if a token exists
    modifier exists(uint256 tokenId) {
        require(_exists(tokenId), "Token does not exist");
        _;
    }

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("CornucopiasAsset", "CORN") {}

    // Function to create a new asset
    function createAsset(string memory tokenURI) external onlyOwner {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the new token
        _mint(msg.sender, tokenId);
        
        // Set the token URI
        _setTokenURI(tokenId, tokenURI);

        // Emit the asset creation event
        emit AssetCreated(tokenId, msg.sender, tokenURI);
    }

    // Internal function to set the token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal exists(tokenId) {
        _tokenURIs[tokenId] = tokenURI;
    }

    // Function to retrieve the token URI by token ID
    function tokenURI(uint256 tokenId) public view override exists(tokenId) returns (string memory) {
        return _tokenURIs[tokenId];
    }

    // Function to withdraw contract balance to the owner
    function withdraw() external onlyOwner {
        // Check if the contract balance is greater than zero
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        
        // Transfer balance to the owner
        payable(owner()).transfer(balance);
    }

    // Fallback function to receive ether payments
    receive() external payable {}

    // Function to get total assets owned by the caller
    function getMyAssets() external view returns (uint256[] memory) {
        uint256 assetCount = balanceOf(msg.sender);
        uint256[] memory tokenIds = new uint256[](assetCount);
        
        for (uint256 i = 0; i < assetCount; i++) {
            tokenIds[i] = tokenOfOwnerByIndex(msg.sender, i);
        }
        
        return tokenIds;
    }
}
```
