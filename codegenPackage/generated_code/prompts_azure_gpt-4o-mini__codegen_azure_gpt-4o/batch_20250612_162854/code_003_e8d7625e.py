"""
Generated Code Metadata:
========================
Original URL: https://moxie.community
Prompt: Provide a code example for implementing the Moxie Bonding Curves in a decentralized application on Farcaster.
Generated: DETERMINISTIC_e8d7625e1748df3e
Batch ID: 20250612_162854
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
 * @title MoxieBondingCurve
 * @dev Implements a bonding curve mechanism for a decentralized application on Farcaster.
 *      This contract allows users to mint and burn tokens based on a bonding curve pricing model.
 */
contract MoxieBondingCurve {
    // State variables
    uint256 public totalSupply; // Total supply of tokens
    uint256 public reserveBalance; // Reserve balance in the contract
    uint256 public constant RESERVE_RATIO = 500000; // Reserve ratio (in ppm, parts per million)
    uint256 public constant PRECISION = 1e18; // Precision for calculations

    mapping(address => uint256) public balances; // User balances

    // Events
    event Mint(address indexed user, uint256 amount, uint256 cost);
    event Burn(address indexed user, uint256 amount, uint256 refund);

    /**
     * @dev Modifier to ensure a valid input amount.
     * @param _amount The amount to validate.
     */
    modifier validAmount(uint256 _amount) {
        require(_amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Calculates the price to mint a given amount of tokens based on the bonding curve.
     * @param _amount The amount of tokens to mint.
     * @return The cost in reserve currency.
     */
    function calculateMintPrice(uint256 _amount) public view returns (uint256) {
        uint256 newSupply = totalSupply + _amount;
        uint256 cost = (reserveBalance * (newSupply**2 - totalSupply**2)) / (totalSupply**2);
        return cost;
    }

    /**
     * @dev Calculates the refund for burning a given amount of tokens based on the bonding curve.
     * @param _amount The amount of tokens to burn.
     * @return The refund in reserve currency.
     */
    function calculateBurnRefund(uint256 _amount) public view returns (uint256) {
        uint256 newSupply = totalSupply - _amount;
        uint256 refund = (reserveBalance * (totalSupply**2 - newSupply**2)) / (totalSupply**2);
        return refund;
    }

    /**
     * @dev Mints tokens based on the bonding curve pricing model.
     * @param _amount The amount of tokens to mint.
     */
    function mint(uint256 _amount) external payable validAmount(_amount) {
        uint256 cost = calculateMintPrice(_amount);
        require(msg.value >= cost, "Insufficient funds sent");

        // Update state
        totalSupply += _amount;
        reserveBalance += cost;
        balances[msg.sender] += _amount;

        emit Mint(msg.sender, _amount, cost);

        // Refund excess funds if any
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }
    }

    /**
     * @dev Burns tokens and refunds reserve currency based on the bonding curve pricing model.
     * @param _amount The amount of tokens to burn.
     */
    function burn(uint256 _amount) external validAmount(_amount) {
        require(balances[msg.sender] >= _amount, "Insufficient token balance");

        uint256 refund = calculateBurnRefund(_amount);

        // Update state
        totalSupply -= _amount;
        reserveBalance -= refund;
        balances[msg.sender] -= _amount;

        emit Burn(msg.sender, _amount, refund);

        // Transfer refund to the user
        payable(msg.sender).transfer(refund);
    }

    /**
     * @dev Fallback function to accept Ether directly.
     */
    receive() external payable {
        reserveBalance += msg.value;
    }
}
```
