"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-s.pages.dev
Prompt: Write Solidity code for a fixed-supply ERC-20 token like DOGE20, including staking reward distribution and liquidity allocation features.
Generated: DETERMINISTIC_7418a235cfc311c9
Batch ID: 20250612_152710
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
 * @title FixedSupplyERC20Token
 * @dev An ERC-20 token with fixed supply, staking rewards, and liquidity allocation functionality.
 */
contract FixedSupplyERC20Token {
    // Token details
    string public name = "DOGE20";
    string public symbol = "DOGE20";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Address balances
    mapping(address => uint256) private balances;

    // Approval allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Staking information
    mapping(address => uint256) private stakingBalance;
    mapping(address => uint256) private stakingReward;

    // Liquidity pool allocation
    address public liquidityPool;
    uint256 public liquidityAllocation;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event TokensStaked(address indexed staker, uint256 value);
    event RewardsClaimed(address indexed staker, uint256 reward);

    // Constructor sets token supply and liquidity allocation
    constructor(uint256 _initialSupply, uint256 _liquidityAllocation, address _liquidityPool) {
        require(_liquidityAllocation <= _initialSupply, "Liquidity allocation exceeds total supply");
        require(_liquidityPool != address(0), "Invalid liquidity pool address");

        totalSupply = _initialSupply;
        liquidityAllocation = _liquidityAllocation;
        liquidityPool = _liquidityPool;

        // Assign the liquidity allocation to the liquidity pool
        balances[liquidityPool] = liquidityAllocation;

        // Assign remaining supply to the contract creator
        uint256 remainingSupply = totalSupply - liquidityAllocation;
        balances[msg.sender] = remainingSupply;

        emit Transfer(address(0), liquidityPool, liquidityAllocation);
        emit Transfer(address(0), msg.sender, remainingSupply);
    }

    // ERC-20 standard functions

    /**
     * @dev Returns the balance of the specified address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to the specified address.
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Transfer to zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves the spender to spend a specified amount of tokens.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Transfer to zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance of the spender for the owner's tokens.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    // Staking functionality

    /**
     * @dev Stake tokens to earn rewards.
     */
    function stake(uint256 amount) public {
        require(amount > 0, "Cannot stake zero tokens");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        stakingBalance[msg.sender] += amount;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Calculate staking rewards based on a fixed rate.
     * For simplicity, we use a fixed reward rate of 5%.
     */
    function calculateRewards(address staker) public view returns (uint256) {
        uint256 rewardRate = 5; // 5% reward rate
        return (stakingBalance[staker] * rewardRate) / 100;
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() public {
        uint256 rewards = calculateRewards(msg.sender);
        stakingReward[msg.sender] += rewards;
        balances[msg.sender] += rewards;

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Liquidity allocation functionality

    /**
     * @dev Adjust liquidity allocation. Only contract owner can call this function.
     */
    function adjustLiquidityAllocation(uint256 newAllocation) public {
        require(msg.sender == liquidityPool, "Only liquidity pool can adjust allocation");
        require(newAllocation <= totalSupply, "New allocation exceeds total supply");

        uint256 currentAllocation = liquidityAllocation;
        liquidityAllocation = newAllocation;

        if (newAllocation > currentAllocation) {
            uint256 difference = newAllocation - currentAllocation;
            require(balances[liquidityPool] >= difference, "Insufficient liquidity pool balance");
            balances[liquidityPool] -= difference;
            balances[msg.sender] += difference;
        } else {
            uint256 difference = currentAllocation - newAllocation;
            require(balances[msg.sender] >= difference, "Insufficient sender balance");
            balances[msg.sender] -= difference;
            balances[liquidityPool] += difference;
        }
    }
}
```
