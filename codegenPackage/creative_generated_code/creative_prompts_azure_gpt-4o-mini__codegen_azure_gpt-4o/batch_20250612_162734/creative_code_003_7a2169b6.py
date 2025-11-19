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

/**
 * @title UniSocksMarket
 * @dev A smart contract that facilitates buying and selling of Unisocks (ERC20 tokens).
 */
contract UniSocksMarket {
    // Address of the UniSocks ERC20 token contract
    address public unisocksTokenAddress;

    // Owner of the contract
    address public owner;

    // Mapping to track listed Unisocks for sale
    mapping(uint256 => Listing) public listings;

    // Struct to represent a listing
    struct Listing {
        address seller; // Seller's address
        uint256 price;  // Price in wei
        bool exists;    // Whether the listing exists
    }

    // Event emitted when a listing is created
    event ListingCreated(uint256 tokenId, address indexed seller, uint256 price);

    // Event emitted when a listing is removed
    event ListingRemoved(uint256 tokenId, address indexed seller);

    // Event emitted when a Unisock is bought
    event UnisockSold(uint256 tokenId, address indexed buyer, uint256 price);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _unisocksTokenAddress Address of the UniSocks ERC20 token contract.
     */
    constructor(address _unisocksTokenAddress) {
        require(_unisocksTokenAddress != address(0), "Invalid token address");
        unisocksTokenAddress = _unisocksTokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Creates a new listing for a specific Unisock token.
     * @param tokenId The ID of the Unisock token to list.
     * @param price The price in wei for the token.
     */
    function createListing(uint256 tokenId, uint256 price) external {
        require(price > 0, "Price must be greater than zero");
        require(listings[tokenId].exists == false, "Listing already exists");
        
        // Transfer the token from the seller to the contract for escrow
        IERC20(unisocksTokenAddress).transferFrom(msg.sender, address(this), 1);
        
        listings[tokenId] = Listing({
            seller: msg.sender,
            price: price,
            exists: true
        });

        emit ListingCreated(tokenId, msg.sender, price);
    }

    /**
     * @dev Removes a listing for a specific Unisock token.
     * @param tokenId The ID of the Unisock token to remove.
     */
    function removeListing(uint256 tokenId) external {
        Listing memory listing = listings[tokenId];
        require(listing.exists, "Listing does not exist");
        require(listing.seller == msg.sender, "Only the seller can remove the listing");

        // Transfer the token back to the seller
        IERC20(unisocksTokenAddress).transfer(msg.sender, 1);

        delete listings[tokenId];
        emit ListingRemoved(tokenId, msg.sender);
    }

    /**
     * @dev Buys a listed Unisock token.
     * @param tokenId The ID of the Unisock token to buy.
     */
    function buyUnisock(uint256 tokenId) external payable {
        Listing memory listing = listings[tokenId];
        require(listing.exists, "Listing does not exist");
        require(msg.value == listing.price, "Incorrect payment amount");

        // Transfer payment to the seller
        payable(listing.seller).transfer(msg.value);

        // Transfer the token to the buyer
        IERC20(unisocksTokenAddress).transfer(msg.sender, 1);

        delete listings[tokenId];
        emit UnisockSold(tokenId, msg.sender, listing.price);
    }

    /**
     * @dev Withdraws any Ether balance in the contract (owner only).
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Fallback function to reject direct Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }

    /**
     * @dev Interface for ERC20 token contract.
     */
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
    }
}
```
