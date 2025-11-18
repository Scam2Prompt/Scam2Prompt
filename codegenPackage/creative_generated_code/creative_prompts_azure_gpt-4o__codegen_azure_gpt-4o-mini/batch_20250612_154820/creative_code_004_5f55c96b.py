"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimalvara.pages.dev
Prompt: Write a smart contract that uses the ERC-721 standard to represent ownership of ERC-7621 Basket Tokens, enabling transferability and management rights on-chain.
Generated: DETERMINISTIC_5f55c96b83570586
Batch ID: 20250612_154820
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

// Importing the ERC721 interface and the Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ERC7621 standard extension for basket tokens
interface IERC7621 {
    function transferManagementRights(address newManager) external;
    function getBasketContents(uint256 tokenId) external view returns (uint256[] memory);
}

// Smart contract for ERC-721 Basket Token
contract BasketToken is ERC721, Ownable, IERC7621 {
    // Events for logging
    event BasketCreated(uint256 indexed tokenId, address owner);
    event ManagementRightsTransferred(address indexed previousManager, address indexed newManager);
    
    // Struct to hold basket information
    struct Basket {
        address manager;
        uint256[] contents; // Array to hold the IDs of the contents
    }

    // Mapping from token ID to basket information
    mapping(uint256 => Basket) private baskets;

    // Token counter to keep track of the number of minted tokens
    uint256 private tokenCounter;

    // Constructor to set the name and symbol of the ERC721 token
    constructor() ERC721("BasketToken", "BSTK") {
        tokenCounter = 0;
    }

    // Function to create a new basket token
    function createBasket(uint256[] memory contents) external onlyOwner {
        uint256 tokenId = tokenCounter;
        _mint(msg.sender, tokenId); // Minting the token to the owner's address

        // Creating the basket and storing its contents
        baskets[tokenId] = Basket(msg.sender, contents);
        
        emit BasketCreated(tokenId, msg.sender);
        tokenCounter++;
    }

    // Function to transfer management rights to a new manager
    function transferManagementRights(address newManager) external override {
        require(msg.sender == baskets[tokenId].manager, "Only the basket manager can transfer management rights");
        require(newManager != address(0), "New manager address cannot be zero");

        address previousManager = baskets[tokenId].manager;
        baskets[tokenId].manager = newManager;
        
        emit ManagementRightsTransferred(previousManager, newManager);
    }

    // Function to retrieve the contents of a basket by its token ID
    function getBasketContents(uint256 tokenId) external view override returns (uint256[] memory) {
        require(_exists(tokenId), "Basket token does not exist");
        return baskets[tokenId].contents;
    }

    // Function to safely transfer a basket token
    function safeTransferBasket(address to, uint256 tokenId) external {
        require(msg.sender == ownerOf(tokenId), "You do not own this basket token");
        safeTransferFrom(msg.sender, to, tokenId);
    }
}
```
