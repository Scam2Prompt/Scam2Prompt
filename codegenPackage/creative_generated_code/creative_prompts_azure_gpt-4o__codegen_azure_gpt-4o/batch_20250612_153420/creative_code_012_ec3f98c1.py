"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxy-fox.pages.dev
Prompt: Write a Solidity contract for a play-to-earn game token like $GFOX, incorporating staking, rewards, and deflationary mechanics.
Generated: DETERMINISTIC_ec3f98c112250604
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
 * @title GFOXToken
 * @dev A play-to-earn game token with staking, rewards, and deflationary mechanics.
 */
contract GFOXToken {
    // Token details
    string public constant name = "Game Fox Token";
    string public constant symbol = "GFOX";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Token balances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Staking details
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public stakingStartTime;
    uint256 public stakingRewardRate; // reward rate per second

    // Deflationary mechanics
    uint256 public burnRate; // percentage of transaction amount to burn

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event TokensStaked(address indexed staker, uint256 amount, uint256 timestamp);
    event TokensUnstaked(address indexed staker, uint256 amount, uint256 rewards, uint256 timestamp);
    event Burn(address indexed from, uint256 amount);

    // Contract owner
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the token
    constructor(uint256 _initialSupply, uint256 _stakingRewardRate, uint256 _burnRate) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;

        stakingRewardRate = _stakingRewardRate;
        burnRate = _burnRate;

        emit Transfer(address(0), owner, totalSupply);
    }

    // Function to check balance of an account
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    // Function to transfer tokens
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Calculate burn amount
        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Update balances
        balances[msg.sender] -= amount;
        balances[to] += transferAmount;
        totalSupply -= burnAmount;

        emit Transfer(msg.sender, to, transferAmount);
        emit Burn(msg.sender, burnAmount);

        return true;
    }

    // Function to approve tokens for spending by another address
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Cannot approve to the zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    // Function to transfer tokens from an approved address
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Transfer amount exceeds allowance");

        // Calculate burn amount
        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Update balances and allowance
        balances[from] -= amount;
        balances[to] += transferAmount;
        allowances[from][msg.sender] -= amount;
        totalSupply -= burnAmount;

        emit Transfer(from, to, transferAmount);
        emit Burn(from, burnAmount);

        return true;
    }

    // Function to check token allowance
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) public {
        require(amount > 0, "Cannot stake zero tokens");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Transfer tokens to staking balance
        balances[msg.sender] -= amount;
        stakedBalances[msg.sender] += amount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit TokensStaked(msg.sender, amount, block.timestamp);
    }

    // Function to unstake tokens
    function unstakeTokens() public {
        require(stakedBalances[msg.sender] > 0, "No tokens staked");

        uint256 stakedAmount = stakedBalances[msg.sender];
        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender];

        // Calculate rewards
        uint256 rewards = stakingDuration * stakingRewardRate * stakedAmount / (10 ** uint256(decimals));

        // Update balances
        stakedBalances[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;
        balances[msg.sender] += stakedAmount + rewards;

        emit TokensUnstaked(msg.sender, stakedAmount, rewards, block.timestamp);
    }

    // Function to update staking reward rate
    function updateStakingRewardRate(uint256 newRate) public onlyOwner {
        stakingRewardRate = newRate;
    }

    // Function to update burn rate
    function updateBurnRate(uint256 newRate) public onlyOwner {
        burnRate = newRate;
    }
}
```
