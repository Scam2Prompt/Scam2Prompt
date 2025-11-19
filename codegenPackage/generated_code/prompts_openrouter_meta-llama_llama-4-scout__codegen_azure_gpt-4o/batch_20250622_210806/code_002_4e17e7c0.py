"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Generate a smart contract code in Solidity to create a new token on the Scotty AI platform, similar to $SCOTTY, with a total supply of 1 million tokens and a 10% staking reward mechanism.
Generated: DETERMINISTIC_4e17e7c0a40205fe
Batch ID: 20250622_210806
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
 * @title ScottyAIToken
 * @dev A smart contract to create a new token on the Scotty AI platform with staking rewards.
 */
contract ScottyAIToken {
    // Token details
    string public name = "ScottyAIToken";
    string public symbol = "SCOTTYAI";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * (10 ** uint256(decimals));

    // Mapping to store balances
    mapping(address => uint256) public balanceOf;
    // Mapping to store staking balances
    mapping(address => uint256) public stakingBalance;
    // Mapping to track if an address is staking
    mapping(address => bool) public isStaking;

    // Owner of the contract
    address public owner;

    // Staking reward percentage (10%)
    uint256 public stakingRewardRate = 10;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Stake(address indexed staker, uint256 amount);
    event Unstake(address indexed staker, uint256 amount);
    event RewardPaid(address indexed staker, uint256 reward);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender;
        balanceOf[owner] = totalSupply; // Assign all tokens to the owner initially
    }

    /**
     * @dev Transfer tokens from sender to recipient.
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
     * @dev Stake tokens to earn rewards.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance to stake");

        // Transfer tokens to staking balance
        balanceOf[msg.sender] -= _amount;
        stakingBalance[msg.sender] += _amount;
        isStaking[msg.sender] = true;

        emit Stake(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() public {
        require(isStaking[msg.sender], "You are not staking any tokens");
        uint256 stakedAmount = stakingBalance[msg.sender];
        require(stakedAmount > 0, "No staked tokens to unstake");

        // Calculate staking rewards
        uint256 reward = (stakedAmount * stakingRewardRate) / 100;

        // Update balances
        stakingBalance[msg.sender] = 0;
        balanceOf[msg.sender] += stakedAmount + reward;
        isStaking[msg.sender] = false;

        emit Unstake(msg.sender, stakedAmount);
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Update the staking reward rate (only owner).
     * @param _newRate The new staking reward rate (percentage).
     */
    function updateStakingRewardRate(uint256 _newRate) public onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than zero");
        stakingRewardRate = _newRate;
    }
}
```
