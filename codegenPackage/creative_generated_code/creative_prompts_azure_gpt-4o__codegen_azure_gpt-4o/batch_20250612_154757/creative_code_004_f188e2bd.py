"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone.cx
Prompt: Develop a smart contract on the ERC20 or BSC20 blockchain to handle the distribution of $INIT tokens during the pre-sale and airdrop phases, ensuring compliance with the first-come-first-served model.
Generated: DETERMINISTIC_f188e2bd2ec49873
Batch ID: 20250612_154757
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
 * @title INITTokenDistribution
 * @dev A contract to handle the distribution of $INIT tokens during pre-sale and airdrop phases.
 *      Follows a first-come-first-served model for token distribution.
 */
contract INITTokenDistribution {
    // Token details
    address public immutable tokenAddress;
    uint256 public immutable tokenDecimals;

    // Pre-sale and airdrop details
    uint256 public preSalePrice; // Price per token in wei
    uint256 public maxPreSaleTokens; // Maximum tokens available for pre-sale
    uint256 public maxAirdropTokens; // Maximum tokens available for airdrop
    uint256 public distributedPreSaleTokens; // Tokens distributed in pre-sale
    uint256 public distributedAirdropTokens; // Tokens distributed in airdrop

    // Address of contract owner
    address public owner;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event TokensAirdropped(address indexed recipient, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this");
        _;
    }

    modifier validAddress(address addr) {
        require(addr != address(0), "Invalid address");
        _;
    }

    modifier sufficientTokensLeft(uint256 amount, uint256 maxTokens, uint256 distributedTokens) {
        require(distributedTokens + amount <= maxTokens, "Not enough tokens available");
        _;
    }

    /**
     * @dev Constructor initializes the contract with token details and distribution limits.
     * @param _tokenAddress Address of the ERC20/BSC20 token contract.
     * @param _tokenDecimals Number of decimals the token uses.
     * @param _preSalePrice Price per token during pre-sale in wei.
     * @param _maxPreSaleTokens Maximum tokens allocated for pre-sale.
     * @param _maxAirdropTokens Maximum tokens allocated for airdrop.
     */
    constructor(
        address _tokenAddress,
        uint256 _tokenDecimals,
        uint256 _preSalePrice,
        uint256 _maxPreSaleTokens,
        uint256 _maxAirdropTokens
    ) validAddress(_tokenAddress) {
        tokenAddress = _tokenAddress;
        tokenDecimals = _tokenDecimals;
        preSalePrice = _preSalePrice;
        maxPreSaleTokens = _maxPreSaleTokens;
        maxAirdropTokens = _maxAirdropTokens;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to purchase tokens during the pre-sale.
     * @param amount The number of tokens to purchase (in whole units, not adjusted for decimals).
     */
    function buyPreSaleTokens(uint256 amount)
        external
        payable
        sufficientTokensLeft(amount, maxPreSaleTokens, distributedPreSaleTokens)
    {
        require(amount > 0, "Amount must be greater than zero");
        uint256 cost = amount * preSalePrice;
        require(msg.value >= cost, "Insufficient ETH sent");

        // Update state
        distributedPreSaleTokens += amount;

        // Transfer tokens to buyer
        bool success = IERC20(tokenAddress).transfer(msg.sender, amount * (10**tokenDecimals));
        require(success, "Token transfer failed");

        // Refund excess ETH if overpaid
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }

        emit TokensPurchased(msg.sender, amount, cost);
    }

    /**
     * @dev Allows the owner to airdrop tokens to a recipient.
     * @param recipient The recipient of the airdropped tokens.
     * @param amount The number of tokens to airdrop (in whole units, not adjusted for decimals).
     */
    function airdropTokens(address recipient, uint256 amount)
        external
        onlyOwner
        validAddress(recipient)
        sufficientTokensLeft(amount, maxAirdropTokens, distributedAirdropTokens)
    {
        require(amount > 0, "Amount must be greater than zero");

        // Update state
        distributedAirdropTokens += amount;

        // Transfer tokens to recipient
        bool success = IERC20(tokenAddress).transfer(recipient, amount * (10**tokenDecimals));
        require(success, "Token transfer failed");

        emit TokensAirdropped(recipient, amount);
    }

    /**
     * @dev Allows the owner to withdraw ETH collected during pre-sale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Allows the owner to update the pre-sale price.
     * @param newPrice The new pre-sale price in wei.
     */
    function updatePreSalePrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Price must be greater than zero");
        preSalePrice = newPrice;
    }

    /**
     * @dev Interface for ERC20/BSC20 token contracts.
     */
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
    }
}
```
