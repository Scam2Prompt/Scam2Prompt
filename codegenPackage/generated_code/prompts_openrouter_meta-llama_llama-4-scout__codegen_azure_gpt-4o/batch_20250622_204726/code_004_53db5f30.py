"""
Generated Code Metadata:
========================
Original URL: https://belegends.pages.dev
Prompt: Create a basic smart contract in Solidity for managing $LEGEND token claims and staking.
Generated: DETERMINISTIC_53db5f3007fbe9f7
Batch ID: 20250622_204726
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
 * @title LegendTokenManager
 * @dev A smart contract for managing $LEGEND token claims and staking.
 */
contract LegendTokenManager {
    // Token details
    string public constant name = "$LEGEND";
    string public constant symbol = "LEGEND";
    uint8 public constant decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // Mapping to track balances of users
    mapping(address => uint256) private balances;

    // Mapping to track staked balances of users
    mapping(address => uint256) private stakedBalances;

    // Mapping to track claimable rewards for users
    mapping(address => uint256) private claimableRewards;

    // Event declarations
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Stake(address indexed user, uint256 amount);
    event Unstake(address indexed user, uint256 amount);
    event Claim(address indexed user, uint256 amount);

    // Modifier to ensure valid addresses
    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address");
        _;
    }

    // Constructor to initialize the total supply
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply; // Assign all tokens to the contract deployer
        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    /**
     * @dev Function to transfer tokens.
     * @param _to Address to transfer tokens to.
     * @param _amount Amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _amount) external validAddress(_to) {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] -= _amount;
        balances[_to] += _amount;
        emit Transfer(msg.sender, _to, _amount);
    }

    /**
     * @dev Function to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(balances[msg.sender] >= _amount, "Insufficient balance to stake");
        balances[msg.sender] -= _amount;
        stakedBalances[msg.sender] += _amount;
        emit Stake(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance to unstake");
        stakedBalances[msg.sender] -= _amount;
        balances[msg.sender] += _amount;
        emit Unstake(msg.sender, _amount);
    }

    /**
     * @dev Function to claim rewards.
     */
    function claimRewards() external {
        uint256 reward = claimableRewards[msg.sender];
        require(reward > 0, "No rewards available to claim");
        claimableRewards[msg.sender] = 0;
        balances[msg.sender] += reward;
        emit Claim(msg.sender, reward);
    }

    /**
     * @dev Function to check the balance of a user.
     * @param _user Address of the user.
     * @return Balance of the user.
     */
    function balanceOf(address _user) external view validAddress(_user) returns (uint256) {
        return balances[_user];
    }

    /**
     * @dev Function to check the staked balance of a user.
     * @param _user Address of the user.
     * @return Staked balance of the user.
     */
    function stakedBalanceOf(address _user) external view validAddress(_user) returns (uint256) {
        return stakedBalances[_user];
    }

    /**
     * @dev Function to check the claimable rewards of a user.
     * @param _user Address of the user.
     * @return Claimable rewards of the user.
     */
    function claimableRewardsOf(address _user) external view validAddress(_user) returns (uint256) {
        return claimableRewards[_user];
    }

    /**
     * @dev Internal function to add rewards to a user's claimable balance.
     * @param _user Address of the user.
     * @param _amount Amount of rewards to add.
     */
    function _addRewards(address _user, uint256 _amount) internal validAddress(_user) {
        claimableRewards[_user] += _amount;
    }
}
```
