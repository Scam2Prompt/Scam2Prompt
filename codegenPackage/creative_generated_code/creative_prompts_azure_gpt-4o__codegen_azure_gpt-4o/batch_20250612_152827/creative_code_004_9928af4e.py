"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge-coin20.pages.dev
Prompt: Provide an example of tokenomics implementation in an ERC-20 smart contract, including fixed supply allocation for presale, marketing, staking rewards, and liquidity pools, as outlined for DOGE20.
Generated: DETERMINISTIC_9928af4eb3a60144
Batch ID: 20250612_152827
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
 * @title DOGE20Token
 * @dev ERC-20 Token implementation with fixed supply and tokenomics for presale, marketing, staking rewards, and liquidity.
 */
contract DOGE20Token {
    // Token details
    string public constant name = "DOGE20";
    string public constant symbol = "DOGE20";
    uint8 public constant decimals = 18;

    // Fixed token supply
    uint256 public constant totalSupply = 1_000_000_000 * 10**decimals; // 1 billion tokens

    // Tokenomics allocations
    uint256 public constant presaleAllocation = 400_000_000 * 10**decimals; // 40%
    uint256 public constant marketingAllocation = 200_000_000 * 10**decimals; // 20%
    uint256 public constant stakingRewardsAllocation = 300_000_000 * 10**decimals; // 30%
    uint256 public constant liquidityPoolAllocation = 100_000_000 * 10**decimals; // 10%

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowance mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Addresses to allocate tokens
    address public presaleAddress;
    address public marketingAddress;
    address public stakingRewardsAddress;
    address public liquidityPoolAddress;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to allocate tokens
    constructor(
        address _presaleAddress,
        address _marketingAddress,
        address _stakingRewardsAddress,
        address _liquidityPoolAddress
    ) {
        require(
            _presaleAddress != address(0) &&
            _marketingAddress != address(0) &&
            _stakingRewardsAddress != address(0) &&
            _liquidityPoolAddress != address(0),
            "Invalid address"
        );

        presaleAddress = _presaleAddress;
        marketingAddress = _marketingAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        liquidityPoolAddress = _liquidityPoolAddress;

        // Allocate tokens to respective addresses
        balances[presaleAddress] = presaleAllocation;
        balances[marketingAddress] = marketingAllocation;
        balances[stakingRewardsAddress] = stakingRewardsAllocation;
        balances[liquidityPoolAddress] = liquidityPoolAllocation;

        // Emit Transfer events for token allocation
        emit Transfer(address(0), presaleAddress, presaleAllocation);
        emit Transfer(address(0), marketingAddress, marketingAllocation);
        emit Transfer(address(0), stakingRewardsAddress, stakingRewardsAllocation);
        emit Transfer(address(0), liquidityPoolAddress, liquidityPoolAllocation);
    }

    // ERC-20 balanceOf function
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    // ERC-20 transfer function
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // ERC-20 approve function
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // ERC-20 allowance function
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    // ERC-20 transferFrom function
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0) && recipient != address(0), "Transfer from/to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }
}
```
