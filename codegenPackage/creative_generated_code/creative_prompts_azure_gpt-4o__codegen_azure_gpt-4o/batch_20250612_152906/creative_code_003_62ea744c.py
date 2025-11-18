"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kayentest2.pages.dev
Prompt: Create a smart contract in Solidity for implementing a deflationary mechanism and yield rewards, inspired by the KAYEN Protocol's dual-token model on the Chiliz Chain.
Generated: DETERMINISTIC_62ea744c4659fa4a
Batch ID: 20250612_152906
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
 * @title Deflationary and Yield Rewards Smart Contract
 * @dev Implements a dual-token model inspired by KAYEN Protocol,
 * with deflationary mechanisms and yield rewards on the Chiliz Chain.
 */
contract DeflationaryYieldToken {
    // Token variables
    string public name = "DeflationaryYieldToken";
    string public symbol = "DYT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // State variables
    uint256 public burnRate; // Percentage of tokens burned on transfers
    uint256 public rewardRate; // Percentage of tokens distributed as rewards
    address[] public holders; // Array to track all token holders
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed from, uint256 value);
    event RewardDistributed(address indexed to, uint256 value);

    /**
     * @dev Constructor sets the initial supply, burn rate, and reward rate.
     * @param initialSupply Total initial token supply
     * @param _burnRate Burn rate as a percentage (e.g., 2 for 2%)
     * @param _rewardRate Reward rate as a percentage (e.g., 1 for 1%)
     */
    constructor(uint256 initialSupply, uint256 _burnRate, uint256 _rewardRate) {
        require(_burnRate + _rewardRate <= 100, "Invalid rates configuration");

        totalSupply = initialSupply * (10 ** uint256(decimals));
        _balances[msg.sender] = totalSupply;
        burnRate = _burnRate;
        rewardRate = _rewardRate;

        // Add the contract creator to holders list
        holders.push(msg.sender);
    }

    /**
     * @dev Returns the balance of the specified address.
     * @param account Address to query
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens to a recipient, applying burn and reward mechanisms.
     * @param recipient Recipient address
     * @param amount Amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to zero address not allowed");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 rewardAmount = (amount * rewardRate) / 100;
        uint256 transferAmount = amount - burnAmount - rewardAmount;

        // Perform token burning
        _burn(msg.sender, burnAmount);

        // Distribute rewards
        _distributeRewards(rewardAmount);

        // Transfer tokens
        _balances[msg.sender] -= amount;
        _balances[recipient] += transferAmount;

        // Add recipient to holders list if not already present
        if (_balances[recipient] > 0 && !_isHolder(recipient)) {
            holders.push(recipient);
        }

        emit Transfer(msg.sender, recipient, transferAmount);
        return true;
    }

    /**
     * @dev Approves another address to spend tokens on behalf of the sender.
     * @param spender Address authorized to spend
     * @param amount Maximum amount they can spend
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approval to zero address not allowed");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from an approved address to a recipient.
     * @param sender Address from which tokens are sent
     * @param recipient Recipient address
     * @param amount Amount of tokens to transfer
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from zero address not allowed");
        require(recipient != address(0), "Transfer to zero address not allowed");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 rewardAmount = (amount * rewardRate) / 100;
        uint256 transferAmount = amount - burnAmount - rewardAmount;

        // Perform token burning
        _burn(sender, burnAmount);

        // Distribute rewards
        _distributeRewards(rewardAmount);

        // Transfer tokens
        _balances[sender] -= amount;
        _balances[recipient] += transferAmount;

        _allowances[sender][msg.sender] -= amount;

        // Add recipient to holders list if not already present
        if (_balances[recipient] > 0 && !_isHolder(recipient)) {
            holders.push(recipient);
        }

        emit Transfer(sender, recipient, transferAmount);
        return true;
    }

    /**
     * @dev Internal function to burn tokens.
     * @param account Address whose tokens are burned
     * @param amount Amount of tokens to burn
     */
    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "Burn from zero address not allowed");
        require(_balances[account] >= amount, "Burn amount exceeds balance");

        _balances[account] -= amount;
        totalSupply -= amount;

        emit Burn(account, amount);
    }

    /**
     * @dev Internal function to distribute rewards to all holders.
     * @param rewardAmount Total reward amount to distribute
     */
    function _distributeRewards(uint256 rewardAmount) internal {
        require(holders.length > 0, "No holders to distribute rewards");

        uint256 rewardPerHolder = rewardAmount / holders.length;

        for (uint256 i = 0; i < holders.length; i++) {
            address holder = holders[i];
            _balances[holder] += rewardPerHolder;
            emit RewardDistributed(holder, rewardPerHolder);
        }
    }

    /**
     * @dev Checks if the address is already a token holder.
     * @param account Address to check
     */
    function _isHolder(address account) internal view returns (bool) {
        for (uint256 i = 0; i < holders.length; i++) {
            if (holders[i] == account) {
                return true;
            }
        }
        return false;
    }
}
```
