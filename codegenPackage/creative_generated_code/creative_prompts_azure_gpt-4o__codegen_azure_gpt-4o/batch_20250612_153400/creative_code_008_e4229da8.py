"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-dogecoin20.pages.dev
Prompt: Write a Solidity contract for the DOGE20 token that includes ERC-20 standard functionality along with staking rewards distribution.
Generated: DETERMINISTIC_e4229da830a568df
Batch ID: 20250612_153400
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
 * @title DOGE20 Token
 * @dev Implementation of the ERC-20 standard token with staking rewards functionality.
 */
contract DOGE20 {
    // Token details
    string public name = "DOGE20 Token";
    string public symbol = "DOGE20";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances and allowances mapping
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Staking data
    mapping(address => uint256) private stakedAmounts;
    mapping(address => uint256) private rewardBalances;
    uint256 public rewardPool; // Total rewards available for distribution
    uint256 public stakingRate; // Rate at which rewards are distributed (e.g., 10% annually)

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Stake(address indexed staker, uint256 amount);
    event Unstake(address indexed staker, uint256 amount);
    event ClaimReward(address indexed staker, uint256 reward);

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply, uint256 _stakingRate) {
        totalSupply = _initialSupply * (10**decimals);
        balances[msg.sender] = totalSupply; // Assign all initial tokens to deployer
        stakingRate = _stakingRate; // Set staking rate (e.g., 10%)
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // ERC-20 standard functions
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0), "Sender address cannot be zero");
        require(recipient != address(0), "Recipient address cannot be zero");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        require(balances[sender] >= amount, "Insufficient balance");
        balances[sender] -= amount;
        allowances[sender][msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Staking functions
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        stakedAmounts[msg.sender] += amount;
        emit Stake(msg.sender, amount);
    }

    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");
        stakedAmounts[msg.sender] -= amount;
        balances[msg.sender] += amount;
        emit Unstake(msg.sender, amount);
    }

    function calculateReward(address staker) public view returns (uint256) {
        uint256 reward = (stakedAmounts[staker] * stakingRate) / 100;
        return reward;
    }

    function claimReward() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No reward available");
        require(rewardPool >= reward, "Insufficient reward pool");
        rewardPool -= reward;
        rewardBalances[msg.sender] += reward;
        emit ClaimReward(msg.sender, reward);
    }

    // Owner functions
    function addRewardToPool(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        rewardPool += amount;
    }

    function withdrawReward(address recipient, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardBalances[recipient] >= amount, "Insufficient reward balance");
        rewardBalances[recipient] -= amount;
        balances[recipient] += amount;
    }
}
```
