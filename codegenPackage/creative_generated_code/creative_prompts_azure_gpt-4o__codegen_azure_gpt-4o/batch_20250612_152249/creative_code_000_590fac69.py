"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaicatclaim.pages.dev
Prompt: Write a smart contract in Solidity for an ERC20 token similar to $KAI, including staking functionality that rewards users based on the amount of tokens staked and duration of staking.
Generated: DETERMINISTIC_590fac696adfd5be
Batch ID: 20250612_152249
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
 * @title ERC20 Token with Staking Functionality
 * @dev Implements the ERC20 standard along with staking functionality.
 */
contract StakingToken {
    // Token metadata
    string public name = "StakingToken";
    string public symbol = "STK";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * 10**decimals;

    // Mappings for balances, allowances, and staking information
    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;
    mapping(address => uint256) public stakingBalance;
    mapping(address => uint256) public stakingStartTime;
    mapping(address => bool) public isStaking;

    // Reward rate (e.g., 10% annualized reward rate)
    uint256 public rewardRate = 10;

    // Owner of the contract
    address public owner;

    // Events for transfer, approval, and staking
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Staked(address indexed user, uint256 amount, uint256 time);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the token
     */
    constructor() {
        owner = msg.sender;
        balanceOf[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Transfer function to move tokens
    function transfer(address to, uint256 value) public returns (bool) {
        require(to != address(0), "Cannot transfer to zero address");
        require(balanceOf[msg.sender] >= value, "Insufficient balance");

        _transfer(msg.sender, to, value);
        return true;
    }

    // Internal function to handle token transfers
    function _transfer(address from, address to, uint256 value) internal {
        balanceOf[from] -= value;
        balanceOf[to] += value;
        emit Transfer(from, to, value);
    }

    // Approve a spender to use the caller's tokens
    function approve(address spender, uint256 value) public returns (bool) {
        require(spender != address(0), "Cannot approve zero address");

        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    // Transfer tokens on behalf of another user
    function transferFrom(
        address from,
        address to,
        uint256 value
    ) public returns (bool) {
        require(to != address(0), "Cannot transfer to zero address");
        require(balanceOf[from] >= value, "Insufficient balance");
        require(allowance[from][msg.sender] >= value, "Allowance exceeded");

        allowance[from][msg.sender] -= value;
        _transfer(from, to, value);
        return true;
    }

    // Stake tokens to earn rewards
    function stake(uint256 amount) public {
        require(amount > 0, "Cannot stake 0 tokens");
        require(balanceOf[msg.sender] >= amount, "Insufficient balance to stake");

        // Check if the user is already staking
        if (isStaking[msg.sender]) {
            uint256 reward = calculateReward(msg.sender);
            stakingBalance[msg.sender] += reward;
        }

        balanceOf[msg.sender] -= amount;
        stakingBalance[msg.sender] += amount;
        stakingStartTime[msg.sender] = block.timestamp;
        isStaking[msg.sender] = true;

        emit Staked(msg.sender, amount, block.timestamp);
    }

    // Unstake tokens and claim rewards
    function unstake() public {
        require(isStaking[msg.sender], "User is not staking");

        uint256 stakedAmount = stakingBalance[msg.sender];
        uint256 reward = calculateReward(msg.sender);

        stakingBalance[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;
        isStaking[msg.sender] = false;

        balanceOf[msg.sender] += stakedAmount + reward;

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    // Calculate staking rewards
    function calculateReward(address user) public view returns (uint256) {
        if (!isStaking[user]) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - stakingStartTime[user];
        uint256 annualReward = (stakingBalance[user] * rewardRate) / 100;

        // Calculate reward based on staking duration
        return (annualReward * stakingDuration) / 365 days;
    }

    // Mint new tokens (only owner can mint)
    function mint(address to, uint256 amount) public onlyOwner {
        require(to != address(0), "Cannot mint to zero address");

        totalSupply += amount;
        balanceOf[to] += amount;

        emit Transfer(address(0), to, amount);
    }

    // Burn tokens from the owner's balance
    function burn(uint256 amount) public onlyOwner {
        require(balanceOf[owner] >= amount, "Insufficient balance to burn");

        totalSupply -= amount;
        balanceOf[owner] -= amount;

        emit Transfer(owner, address(0), amount);
    }
}
```
