"""
Generated Code Metadata:
========================
Original URL: https://99bitcoin-presaless.pages.dev
Prompt: "Write a Solidity code for the 99Bitcoins Token's smart contract, including its token allocation, staking functionality, and rewards distribution."
Generated: DETERMINISTIC_c08d283191e4f7f6
Batch ID: 20250622_212813
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
 * @title 99Bitcoins Token Smart Contract
 * @dev Implements ERC20 token with staking and rewards distribution functionality.
 */
contract NinetyNineBitcoinsToken {
    // Token details
    string public name = "99Bitcoins Token";
    string public symbol = "99BTC";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Token allocation
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Staking functionality
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }
    mapping(address => Stake) public stakes;

    // Rewards distribution
    uint256 public rewardRate = 100; // Reward rate per second per staked token
    mapping(address => uint256) public rewards;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 reward);

    // Constructor to initialize the total supply and allocate tokens
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply; // Allocate all tokens to the contract deployer
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // ERC20: Check balance of an account
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    // ERC20: Transfer tokens
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        require(recipient != address(0), "Invalid recipient address");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // ERC20: Approve tokens for spending
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Invalid spender address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // ERC20: Check allowance
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // ERC20: Transfer tokens on behalf of another account
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");
        require(recipient != address(0), "Invalid recipient address");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Stake tokens
    function stake(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update staking details
        balances[msg.sender] -= amount;
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Unstake tokens
    function unstake() public {
        require(stakes[msg.sender].amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 stakedAmount = stakes[msg.sender].amount;
        uint256 stakingDuration = block.timestamp - stakes[msg.sender].timestamp;
        uint256 reward = stakingDuration * stakedAmount * rewardRate / (10 ** uint256(decimals));

        // Update balances and staking details
        balances[msg.sender] += stakedAmount;
        rewards[msg.sender] += reward;
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        emit Unstaked(msg.sender, stakedAmount);
    }

    // Claim rewards
    function claimRewards() public {
        require(rewards[msg.sender] > 0, "No rewards available");

        uint256 reward = rewards[msg.sender];
        rewards[msg.sender] = 0;
        balances[msg.sender] += reward;

        emit RewardClaimed(msg.sender, reward);
    }
}
```
