"""
Generated Code Metadata:
========================
Original URL: https://pushd-ai.pages.dev
Prompt: Design a smart contract in Solidity to facilitate secure and transparent transactions on a decentralized marketplace like Pushd, incorporating features such as token utility and rewards programs.
Generated: DETERMINISTIC_5f8bc0663f7b09a9
Batch ID: 20250622_205751
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

/**
 * @title Decentralized Marketplace Smart Contract
 * @dev This contract facilitates secure and transparent transactions on a decentralized marketplace.
 * It incorporates token utility and rewards programs for users.
 */
contract DecentralizedMarketplace {
    // Token used for transactions and rewards
    IERC20 public marketplaceToken;

    // Owner of the contract
    address public owner;

    // Struct to represent a listing in the marketplace
    struct Listing {
        uint256 id;
        address seller;
        uint256 price;
        string itemDetails;
        bool isSold;
    }

    // Mapping to store listings
    mapping(uint256 => Listing) public listings;

    // Counter for listing IDs
    uint256 public listingCounter;

    // Mapping to store user rewards
    mapping(address => uint256) public rewards;

    // Events
    event ListingCreated(uint256 indexed id, address indexed seller, uint256 price, string itemDetails);
    event ItemPurchased(uint256 indexed id, address indexed buyer, uint256 price);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _marketplaceToken Address of the token used for transactions and rewards.
     */
    constructor(IERC20 _marketplaceToken) {
        marketplaceToken = _marketplaceToken;
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new listing in the marketplace.
     * @param _price Price of the item in tokens.
     * @param _itemDetails Details of the item being listed.
     */
    function createListing(uint256 _price, string memory _itemDetails) external {
        require(_price > 0, "Price must be greater than zero");

        listingCounter++;
        listings[listingCounter] = Listing({
            id: listingCounter,
            seller: msg.sender,
            price: _price,
            itemDetails: _itemDetails,
            isSold: false
        });

        emit ListingCreated(listingCounter, msg.sender, _price, _itemDetails);
    }

    /**
     * @dev Function to purchase an item from the marketplace.
     * @param _listingId ID of the listing to purchase.
     */
    function purchaseItem(uint256 _listingId) external {
        Listing storage listing = listings[_listingId];
        require(!listing.isSold, "Item is already sold");
        require(listing.price > 0, "Invalid listing");

        // Transfer tokens from buyer to seller
        require(
            marketplaceToken.transferFrom(msg.sender, listing.seller, listing.price),
            "Token transfer failed"
        );

        // Mark the item as sold
        listing.isSold = true;

        // Reward the buyer with tokens (e.g., 1% of the price)
        uint256 reward = listing.price / 100;
        rewards[msg.sender] += reward;

        emit ItemPurchased(_listingId, msg.sender, listing.price);
    }

    /**
     * @dev Function to claim accumulated rewards.
     */
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Transfer rewards to the user
        require(
            marketplaceToken.transfer(msg.sender, rewardAmount),
            "Reward transfer failed"
        );

        // Reset the user's rewards
        rewards[msg.sender] = 0;

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Function to withdraw tokens from the contract (only owner).
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(
            marketplaceToken.transfer(owner, _amount),
            "Token withdrawal failed"
        );
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
