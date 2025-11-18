"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test.fulviomenegozzo.com
Prompt: Create a smart contract in Solidity that limits NFT purchases to a maximum of 5 per wallet and includes functionality for setting a total price in ETH, based on the features of the Memeland pre-sale.
Generated: DETERMINISTIC_72f691b0efb09ad1
Batch ID: 20250612_151624
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
 * @title NFTLimitedPurchaseContract
 * @dev A contract that limits NFT purchases to a maximum of 5 per wallet.
 * Includes functionality for setting a total price in ETH.
 */
contract NFTLimitedPurchaseContract {
    // Maximum NFTs allowed per wallet
    uint256 public constant MAX_NFTS_PER_WALLET = 5;

    // Price per NFT in wei
    uint256 public nftPrice;

    // Mapping to track the number of NFTs purchased by a wallet
    mapping(address => uint256) private walletPurchases;

    // Owner of the contract
    address public owner;

    // Events
    event NFTPurchased(address indexed buyer, uint256 quantity);
    event NFTPriceUpdated(uint256 newPrice);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Constructor to set the initial price and assign ownership
    constructor(uint256 _initialPrice) {
        require(_initialPrice > 0, "Initial price must be greater than zero");
        nftPrice = _initialPrice;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase NFTs.
     * @param quantity The number of NFTs to purchase.
     */
    function purchaseNFT(uint256 quantity) external payable {
        require(quantity > 0, "Quantity must be greater than zero");
        require(walletPurchases[msg.sender] + quantity <= MAX_NFTS_PER_WALLET, "Max NFT limit exceeded");
        require(msg.value == nftPrice * quantity, "Incorrect ETH amount sent");

        // Update wallet purchases
        walletPurchases[msg.sender] += quantity;

        // Emit event
        emit NFTPurchased(msg.sender, quantity);
    }

    /**
     * @dev Function to get the number of NFTs purchased by a wallet.
     * @param wallet The wallet address to query.
     * @return The number of NFTs purchased by the wallet.
     */
    function getWalletPurchases(address wallet) external view returns (uint256) {
        return walletPurchases[wallet];
    }

    /**
     * @dev Function to update the price per NFT (owner-only).
     * @param newPrice The new price per NFT in wei.
     */
    function updateNFTPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be greater than zero");
        nftPrice = newPrice;

        // Emit event
        emit NFTPriceUpdated(newPrice);
    }

    /**
     * @dev Function to withdraw contract balance (owner-only).
     */
    function withdrawBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }
}
```
