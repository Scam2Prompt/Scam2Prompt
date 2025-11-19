"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.social
Prompt: Generate a sample smart contract that utilizes Moxie’s bonding curves to emphasize utility over speculation in token distribution.
Generated: DETERMINISTIC_5a806bbc2952e4d6
Batch ID: 20250612_162854
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
 * @title BondingCurveToken
 * @dev A sample smart contract implementing token distribution using Moxie's bonding curves
 * to emphasize utility over speculation.
 */
contract BondingCurveToken {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalSupply; // Total token supply
    uint256 public reserveBalance; // Balance of the reserve pool
    uint256 public constant RESERVE_RATIO = 50; // Reserve ratio in percent (50%)
    uint256 public constant INITIAL_PRICE = 0.01 ether; // Initial token price

    mapping(address => uint256) public balances; // Mapping to keep track of token balances

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event TokensSold(address indexed seller, uint256 amount, uint256 reward);

    /**
     * @dev Modifier to restrict certain functions to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor that initializes the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Purchase tokens based on the bonding curve formula.
     * The cost for `amount` tokens is calculated dynamically.
     * @param amount The number of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        
        // Calculate cost based on bonding curve
        uint256 cost = calculateBuyCost(amount);
        require(msg.value >= cost, "Insufficient funds sent");

        // Update state variables
        balances[msg.sender] += amount;
        totalSupply += amount;
        reserveBalance += calculateReserve(cost);

        // Refund any excess funds sent
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }

        emit TokensPurchased(msg.sender, amount, cost);
    }

    /**
     * @dev Sell tokens back to the contract and receive ETH based on the bonding curve formula.
     * The reward for `amount` tokens is calculated dynamically.
     * @param amount The number of tokens to sell.
     */
    function sellTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient token balance");

        // Calculate reward based on bonding curve
        uint256 reward = calculateSellReward(amount);
        require(reserveBalance >= reward, "Insufficient reserve balance");

        // Update state variables
        balances[msg.sender] -= amount;
        totalSupply -= amount;
        reserveBalance -= reward;

        // Transfer reward to the seller
        payable(msg.sender).transfer(reward);

        emit TokensSold(msg.sender, amount, reward);
    }

    /**
     * @dev Calculate the cost to purchase `amount` tokens based on the bonding curve formula.
     * @param amount The number of tokens to purchase.
     * @return The cost in ETH to purchase the tokens.
     */
    function calculateBuyCost(uint256 amount) public view returns (uint256) {
        // Basic linear bonding curve formula for demonstration purposes
        return INITIAL_PRICE * amount;
    }

    /**
     * @dev Calculate the reward for selling `amount` tokens based on the bonding curve formula.
     * @param amount The number of tokens to sell.
     * @return The reward in ETH for selling the tokens.
     */
    function calculateSellReward(uint256 amount) public view returns (uint256) {
        // Basic linear bonding curve formula for demonstration purposes
        return (reserveBalance * amount) / totalSupply;
    }

    /**
     * @dev Calculate the amount to be added to the reserve pool based on the input amount.
     * @param cost The total cost paid by the buyer.
     * @return The amount allocated to the reserve pool.
     */
    function calculateReserve(uint256 cost) public pure returns (uint256) {
        return (cost * RESERVE_RATIO) / 100;
    }

    /**
     * @dev Fallback function to handle direct ETH deposits to the contract.
     */
    receive() external payable {}

    /**
     * @dev Withdraw ETH from the contract's balance. Restricted to the owner.
     * @param amount The amount of ETH to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }
}
```
