"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.community
Prompt: Provide a code example for implementing the Moxie Bonding Curves in a decentralized application on Farcaster.
Generated: DETERMINISTIC_e8d7625e1748df3e
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
pragma solidity ^0.8.18;

/**
 * @title MoxieBondingCurve
 * @dev Implements a bonding curve mechanism for a decentralized application on Farcaster.
 * The contract allows users to mint and sell tokens based on a bonding curve pricing model.
 */
contract MoxieBondingCurve {
    // Token details
    string public constant name = "MoxieToken";
    string public constant symbol = "MOX";
    uint8 public constant decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // Mapping of user balances
    mapping(address => uint256) public balances;

    // Parameters for the bonding curve
    uint256 public constant reserveRatio = 500000; // Reserve ratio in ppm (parts per million)
    uint256 public constant curveConstant = 1 ether; // Base constant for the curve

    // Reserve pool
    uint256 public reservePool;

    // Events
    event Mint(address indexed buyer, uint256 amount, uint256 cost);
    event Burn(address indexed seller, uint256 amount, uint256 reward);

    /**
     * @dev Modifier to ensure the caller has sufficient balance.
     * @param amount The amount to check for.
     */
    modifier hasBalance(uint256 amount) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        _;
    }

    /**
     * @dev Calculates the price to mint tokens based on the bonding curve.
     * @param tokenAmount The amount of tokens to mint.
     * @return The price in Ether.
     */
    function calculatePriceToMint(uint256 tokenAmount) public view returns (uint256) {
        uint256 supplyPlusAmount = totalSupply + tokenAmount;
        return curveConstant * supplyPlusAmount**2 / (2 * reserveRatio);
    }

    /**
     * @dev Calculates the reward for burning tokens based on the bonding curve.
     * @param tokenAmount The amount of tokens to burn.
     * @return The reward in Ether.
     */
    function calculateRewardToBurn(uint256 tokenAmount) public view returns (uint256) {
        uint256 supplyMinusAmount = totalSupply - tokenAmount;
        return curveConstant * supplyMinusAmount**2 / (2 * reserveRatio);
    }

    /**
     * @dev Allows users to mint tokens by paying Ether.
     * @param tokenAmount The amount of tokens to mint.
     */
    function mint(uint256 tokenAmount) external payable {
        uint256 price = calculatePriceToMint(tokenAmount);
        require(msg.value >= price, "Insufficient Ether sent");

        // Update state
        totalSupply += tokenAmount;
        balances[msg.sender] += tokenAmount;
        reservePool += msg.value;

        emit Mint(msg.sender, tokenAmount, msg.value);
    }

    /**
     * @dev Allows users to burn tokens and receive Ether.
     * @param tokenAmount The amount of tokens to burn.
     */
    function burn(uint256 tokenAmount) external hasBalance(tokenAmount) {
        uint256 reward = calculateRewardToBurn(tokenAmount);
        require(reservePool >= reward, "Insufficient reserve pool");

        // Update state
        totalSupply -= tokenAmount;
        balances[msg.sender] -= tokenAmount;
        reservePool -= reward;

        // Transfer reward
        (bool success, ) = msg.sender.call{value: reward}("");
        require(success, "Transfer failed");

        emit Burn(msg.sender, tokenAmount, reward);
    }

    /**
     * @dev Fallback function to handle direct Ether transfers.
     */
    receive() external payable {
        reservePool += msg.value;
    }
}
```
