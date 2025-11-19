"""
Generated Code Metadata:
========================
Original URL: https://web3-eot.pages.dev
Prompt: Generate a smart contract code for a token rewards system, like the $ECORA rewards system on Web3eco, that allows users to claim rewards for planting trees and absorbing CO2.
Generated: DETERMINISTIC_07c20e2ddba077ab
Batch ID: 20250622_210914
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
 * @title EcoRewardsToken
 * @dev A smart contract for a token rewards system that incentivizes users to plant trees and absorb CO2.
 */
contract EcoRewardsToken {
    // Token details
    string public name = "EcoRewardsToken";
    string public symbol = "ECORA";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances of users
    mapping(address => uint256) public balanceOf;

    // Mapping to track rewards claimed by users
    mapping(address => uint256) public rewardsClaimed;

    // Owner of the contract
    address public owner;

    // Event declarations
    event Transfer(address indexed from, address indexed to, uint256 value);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balanceOf[owner] = totalSupply; // Assign all tokens to the owner initially
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfer tokens from one address to another.
     * @param _to The recipient address.
     * @param _value The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(_to != address(0), "Invalid recipient address");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Claim rewards for planting trees and absorbing CO2.
     * @param _amount The amount of rewards to claim.
     */
    function claimRewards(uint256 _amount) public returns (bool success) {
        require(_amount > 0, "Reward amount must be greater than zero");
        require(balanceOf[owner] >= _amount, "Insufficient reward pool");

        // Simulate verification of tree planting and CO2 absorption (to be implemented off-chain)
        // For example, integrate with an oracle or external system to verify the user's actions.

        balanceOf[owner] -= _amount;
        balanceOf[msg.sender] += _amount;
        rewardsClaimed[msg.sender] += _amount;

        emit RewardClaimed(msg.sender, _amount);
        return true;
    }

    /**
     * @dev Mint new tokens to the reward pool.
     * @param _amount The amount of tokens to mint.
     */
    function mint(uint256 _amount) public onlyOwner {
        require(_amount > 0, "Mint amount must be greater than zero");

        uint256 mintAmount = _amount * (10 ** uint256(decimals));
        totalSupply += mintAmount;
        balanceOf[owner] += mintAmount;

        emit Transfer(address(0), owner, mintAmount);
    }

    /**
     * @dev Burn tokens from the reward pool.
     * @param _amount The amount of tokens to burn.
     */
    function burn(uint256 _amount) public onlyOwner {
        require(_amount > 0, "Burn amount must be greater than zero");
        require(balanceOf[owner] >= _amount, "Insufficient balance to burn");

        uint256 burnAmount = _amount * (10 ** uint256(decimals));
        totalSupply -= burnAmount;
        balanceOf[owner] -= burnAmount;

        emit Transfer(owner, address(0), burnAmount);
    }
}
```
