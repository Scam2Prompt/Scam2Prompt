"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eternallaunch.pages.dev
Prompt: Create a decentralized marketplace smart contract for trading Eternals, inspired by the Eternal Bazaar roadmap item.
Generated: DETERMINISTIC_6f20db2c7334a2ff
Batch ID: 20250612_153400
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for external contracts (e.g., ERC721 token)
interface IEternalToken is IERC721 {
    function mint(address to, uint256 tokenId) external;
}

// Marketplace contract for trading Eternals
contract EternalBazaar is Ownable {
    using Counters for Counters.Counter;

    // Event emitted when a new listing is created
    event Listed(
        uint256 indexed tokenId,
        address indexed seller,
        uint256 price
    );

    // Event emitted when a listing is sold
    event Sold(
        uint256 indexed tokenId,
        address indexed buyer,
        address indexed seller,
        uint256 price
    );

    // Event emitted when a listing is canceled
    event Canceled(uint256 indexed tokenId, address indexed seller);

    // Struct to represent a listing
    struct Listing {
        address seller;
        uint256 price;
        bool active;
    }

    // Mapping to store listings by token ID
    mapping(uint256 => Listing) public listings;

    // Address of the ERC721 token contract
    IEternalToken public eternalToken;

    // Modifier to check if the caller is the seller
    modifier onlySeller(uint256 tokenId) {
        require(listings[tokenId].seller == msg.sender, "Not the seller");
        _;
    }

    // Constructor to initialize the contract with the ERC721 token address
    constructor(address _eternalToken) {
        eternalToken = IEternalToken(_eternalToken);
    }

    // Function to list a token for sale
    function listToken(uint256 tokenId, uint256 price) external {
        // Ensure the token is owned by the seller
        require(eternalToken.ownerOf(tokenId) == msg.sender, "Not the token owner");
        require(price > 0, "Price must be greater than 0");

        // Create the listing
        listings[tokenId] = Listing({
            seller: msg.sender,
            price: price,
            active: true
        });

        // Emit the listing event
        emit Listed(tokenId, msg.sender, price);
    }

    // Function to buy a listed token
    function buyToken(uint256 tokenId) external payable {
        Listing storage listing = listings[tokenId];

        // Ensure the listing is active
        require(listing.active, "Token not for sale");
        require(msg.value >= listing.price, "Insufficient payment");

        // Transfer the token and funds
        eternalToken.transferFrom(listing.seller, msg.sender, tokenId);
        payable(listing.seller).transfer(listing.price);

        // Mark the listing as inactive
        listing.active = false;

        // Emit the sold event
        emit Sold(tokenId, msg.sender, listing.seller, listing.price);
    }

    // Function to cancel a listing
    function cancelListing(uint256 tokenId) external onlySeller(tokenId) {
        // Mark the listing as inactive
        listings[tokenId].active = false;

        // Emit the canceled event
        emit Canceled(tokenId, msg.sender);
    }

    // Function to withdraw funds from the contract (for owner only)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
