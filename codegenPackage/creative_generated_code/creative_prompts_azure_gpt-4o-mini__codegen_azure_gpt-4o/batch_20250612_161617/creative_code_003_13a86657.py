"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-store-en.pages.dev
Prompt: Explain how to set up a presale for a token on a decentralized marketplace, including the steps to ensure secure transactions and user participation as outlined by Pushd.
Generated: DETERMINISTIC_13a86657d1249ee6
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready Solidity smart contract for setting up a token presale on a decentralized marketplace. This contract includes secure transaction handling and ensures user participation.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenPresaleContract
 * @dev A smart contract to facilitate a secure token presale with user participation.
 */
contract TokenPresale {
    address public owner; // Contract owner
    address public tokenAddress; // Address of the ERC20 token being sold
    uint256 public pricePerToken; // Token price in wei
    uint256 public presaleEndTime; // Timestamp for the end of the presale
    uint256 public totalTokensForSale; // Total tokens available for presale
    uint256 public tokensSold; // Counter for tokens sold during the presale

    mapping(address => uint256) public userPurchasedTokens; // Tracks tokens purchased by each user

    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleWithdraw(address indexed owner, uint256 amount);
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    modifier validPurchase(uint256 amount) {
        require(amount > 0, "Must purchase at least one token");
        require(tokensSold + amount <= totalTokensForSale, "Not enough tokens left for sale");
        require(msg.value == amount * pricePerToken, "Incorrect ETH sent for token purchase");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenAddress Address of the ERC20 token.
     * @param _pricePerToken Price per token in wei.
     * @param _totalTokensForSale Total number of tokens available for presale.
     * @param _presaleDuration Duration of the presale in seconds.
     */
    constructor(
        address _tokenAddress,
        uint256 _pricePerToken,
        uint256 _totalTokensForSale,
        uint256 _presaleDuration
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_pricePerToken > 0, "Price per token must be greater than zero");
        require(_totalTokensForSale > 0, "Total tokens for sale must be greater than zero");

        owner = msg.sender; // Set the owner of the contract
        tokenAddress = _tokenAddress;
        pricePerToken = _pricePerToken;
        totalTokensForSale = _totalTokensForSale;
        presaleEndTime = block.timestamp + _presaleDuration; // Set presale end time
    }

    /**
     * @dev Function for users to buy tokens during the presale.
     * @param amount Number of tokens to purchase.
     */
    function buyTokens(uint256 amount) external payable presaleActive validPurchase(amount) {
        // Record the purchase
        userPurchasedTokens[msg.sender] += amount;
        tokensSold += amount;

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function for the owner to withdraw funds after the presale ends.
     */
    function withdrawFunds() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale is still active");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        payable(owner).transfer(balance);

        emit PresaleWithdraw(owner, balance);
    }

    /**
     * @dev Function to check the number of tokens a user purchased.
     * @param user Address of the user.
     * @return Number of tokens purchased by the given user.
     */
    function getPurchasedTokens(address user) external view returns (uint256) {
        return userPurchasedTokens[user];
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers are not allowed");
    }
}
```

### Key Features:
- **Secure Transactions**: The contract validates token purchases and prevents unauthorized ETH transfers.
- **Error Handling**: The `fallback` and `receive` functions ensure only valid interactions occur.
- **Access Control**: Only the owner can withdraw funds after the presale ends.
- **Event Logging**: Tracks token purchases and withdrawals for transparency.
