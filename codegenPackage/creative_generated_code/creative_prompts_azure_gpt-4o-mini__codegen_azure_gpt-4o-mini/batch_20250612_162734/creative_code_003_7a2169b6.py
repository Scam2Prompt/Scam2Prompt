"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unisocks.fi
Prompt: Generate a code snippet for a smart contract that allows users to buy and sell Unisocks on the blockchain.
Generated: DETERMINISTIC_7a2169b62f636205
Batch ID: 20250612_162734
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

// Import OpenZeppelin's ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract UniSocks is ERC721, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to price
    mapping(uint256 => uint256) private _tokenPrices;

    // Event emitted when a new sock is created
    event SockCreated(uint256 indexed tokenId, uint256 price);
    event SockPurchased(uint256 indexed tokenId, address indexed buyer, uint256 price);

    // Constructor to set token name and symbol
    constructor() ERC721("UniSocks", "USOCK") {}

    // Function to create a new sock (mint a new NFT)
    function createSock(uint256 price) external onlyOwner {
        require(price > 0, "Price must be greater than zero");
        
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenPrices[tokenId] = price;

        emit SockCreated(tokenId, price);

        _tokenIdCounter.increment();
    }

    // Function to buy a sock
    function buySock(uint256 tokenId) external payable {
        require(_exists(tokenId), "Sock does not exist");
        require(msg.value >= _tokenPrices[tokenId], "Insufficient funds sent");

        address owner = ownerOf(tokenId);
        require(owner != msg.sender, "You cannot buy your own sock");

        // Transfer the sock to the buyer
        _transfer(owner, msg.sender, tokenId);

        // Transfer funds to the sock owner
        payable(owner).transfer(msg.value);

        emit SockPurchased(tokenId, msg.sender, msg.value);
    }

    // Function to set a price for an existing sock
    function setPrice(uint256 tokenId, uint256 price) external {
        require(_exists(tokenId), "Sock does not exist");
        require(ownerOf(tokenId) == msg.sender, "You must be the owner to set the price");
        require(price > 0, "Price must be greater than zero");

        _tokenPrices[tokenId] = price;
    }

    // Function to retrieve the price of a sock
    function getPrice(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Sock does not exist");
        return _tokenPrices[tokenId];
    }

    // Function to withdraw any Ether sent to the contract (for emergency use)
    function withdraw() external onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
