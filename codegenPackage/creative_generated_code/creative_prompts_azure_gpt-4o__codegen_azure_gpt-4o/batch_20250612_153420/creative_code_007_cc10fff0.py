"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claiming.pages.dev
Prompt: Write a Solidity contract that ensures DOGE20 tokens are stored securely in wallets compatible with ERC-20 standards, while enabling staking functionality.
Generated: DETERMINISTIC_cc10fff0ab9fbd0c
Batch ID: 20250612_153420
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
 * @title DOGE20TokenStaking
 * @dev ERC-20 compatible contract for DOGE20 token handling with staking functionality.
 */
contract DOGE20TokenStaking {
    // ERC-20 State Variables
    string public constant name = "DOGE20 Token";
    string public constant symbol = "DOGE20";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Staking State Variables
    mapping(address => uint256) private stakes;
    mapping(address => uint256) private stakingStartTime;
    uint256 public stakingRewardRate = 5; // Reward rate per year (in %)

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount, uint256 reward);

    // Constructor
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * 10**decimals;
        balances[msg.sender] = totalSupply;
    }

    // ERC-20 Functions

    /**
     * @dev Returns the balance of a given account.
     * @param account The account to query the balance of.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to the specified address.
     * @param to The recipient address.
     * @param value The amount to transfer.
     */
    function transfer(address to, uint256 value) public returns (bool) {
        require(to != address(0), "Invalid address");
        require(balances[msg.sender] >= value, "Insufficient balance");

        balances[msg.sender] -= value;
        balances[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @dev Approves a spender to use the caller's tokens.
     * @param spender The spender's address.
     * @param value The amount to approve.
     */
    function approve(address spender, uint256 value) public returns (bool) {
        require(spender != address(0), "Invalid address");

        allowances[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @dev Returns the remaining approved balance for a spender.
     * @param owner The token owner.
     * @param spender The spender's address.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens from one account to another, utilizing the approved allowance.
     * @param from The sender's address.
     * @param to The recipient's address.
     * @param value The amount to transfer.
     */
    function transferFrom(address from, address to, uint256 value) public returns (bool) {
        require(to != address(0), "Invalid address");
        require(balances[from] >= value, "Insufficient balance");
        require(allowances[from][msg.sender] >= value, "Allowance exceeded");

        balances[from] -= value;
        balances[to] += value;
        allowances[from][msg.sender] -= value;
        emit Transfer(from, to, value);
        return true;
    }

    // Staking Functions

    /**
     * @dev Allows a user to stake tokens.
     * @param amount The amount to stake.
     */
    function stake(uint256 amount) public {
        require(amount > 0, "Cannot stake zero tokens");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        stakes[msg.sender] += amount;
        stakingStartTime[msg.sender] = block.timestamp;
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows a user to unstake tokens and claim rewards.
     */
    function unstake() public {
        require(stakes[msg.sender] > 0, "No tokens to unstake");

        uint256 stakedAmount = stakes[msg.sender];
        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender];
        uint256 reward = calculateReward(stakedAmount, stakingDuration);

        stakes[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;
        balances[msg.sender] += stakedAmount + reward;

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Calculates the reward for staking based on the duration.
     * @param stakedAmount The staked token amount.
     * @param stakingDuration The duration for which tokens are staked (in seconds).
     */
    function calculateReward(uint256 stakedAmount, uint256 stakingDuration) public view returns (uint256) {
        uint256 reward = (stakedAmount * stakingRewardRate * stakingDuration) / (365 days * 100);
        return reward;
    }

    /**
     * @dev Returns the staked balance of a given account.
     * @param account The account to query the staked balance of.
     */
    function stakedBalance(address account) public view returns (uint256) {
        return stakes[account];
    }
}
```
