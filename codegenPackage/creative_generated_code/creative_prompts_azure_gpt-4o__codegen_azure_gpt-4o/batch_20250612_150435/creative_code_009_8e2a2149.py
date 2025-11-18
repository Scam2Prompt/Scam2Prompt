"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocols.web.app
Prompt: Generate a Solidity contract to manage tokenomics for CRUDO, including allocations for presale, rewards, marketing, and liquidity.
Generated: DETERMINISTIC_8e2a214953bc2a9c
Batch ID: 20250612_150435
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

/// @title CRUDO Tokenomics Management Contract
/// @notice This contract manages the token allocations for presale, rewards, marketing, and liquidity.
/// @dev Implements best practices for Solidity contracts.

contract CRUDO {
    // ERC-20 token details
    string public name = "CRUDO";
    string public symbol = "CRUDO";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Token allocation percentages
    // Values are represented as a percentage (e.g., 10% = 10 * 10^2 = 1000 basis points)
    uint256 public constant PRESALE_ALLOCATION = 2000; // 20%
    uint256 public constant REWARDS_ALLOCATION = 3000; // 30%
    uint256 public constant MARKETING_ALLOCATION = 2000; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 3000; // 30%
    uint256 public constant PERCENTAGE_DENOMINATOR = 10000; // 100% in basis points

    // Balances for token allocations
    uint256 public presaleTokens;
    uint256 public rewardsTokens;
    uint256 public marketingTokens;
    uint256 public liquidityTokens;

    // Mapping to store user balances
    mapping(address => uint256) public balances;

    // Owner of the contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /// @notice Constructor to initialize the contract
    /// @param _totalSupply The total supply of the CRUDO tokens
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than 0");
        owner = msg.sender;
        totalSupply = _totalSupply;

        // Calculate token allocations
        presaleTokens = (totalSupply * PRESALE_ALLOCATION) / PERCENTAGE_DENOMINATOR;
        rewardsTokens = (totalSupply * REWARDS_ALLOCATION) / PERCENTAGE_DENOMINATOR;
        marketingTokens = (totalSupply * MARKETING_ALLOCATION) / PERCENTAGE_DENOMINATOR;
        liquidityTokens = (totalSupply * LIQUIDITY_ALLOCATION) / PERCENTAGE_DENOMINATOR;

        // Assign all tokens to the owner initially
        balances[owner] = totalSupply;
    }

    /// @notice Transfers tokens from the caller to another account
    /// @param to The recipient's address
    /// @param amount The number of tokens to transfer
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Cannot transfer to zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /// @notice Transfers ownership of the contract to a new owner
    /// @param newOwner The address of the new owner
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner must not be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /// @notice Retrieves the balance of a specified address
    /// @param account The address to query
    /// @return The balance of the given address
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /// @notice Function to allocate tokens for presale
    /// @param to The address to allocate presale tokens to
    function allocatePresaleTokens(address to) external onlyOwner {
        require(presaleTokens > 0, "No presale tokens left to allocate");
        require(to != address(0), "Cannot allocate to zero address");

        balances[owner] -= presaleTokens;
        balances[to] += presaleTokens;
        presaleTokens = 0; // Mark as fully allocated
        emit Transfer(owner, to, presaleTokens);
    }

    /// @notice Function to allocate tokens for rewards
    /// @param to The address to allocate reward tokens to
    function allocateRewardsTokens(address to) external onlyOwner {
        require(rewardsTokens > 0, "No reward tokens left to allocate");
        require(to != address(0), "Cannot allocate to zero address");

        balances[owner] -= rewardsTokens;
        balances[to] += rewardsTokens;
        rewardsTokens = 0; // Mark as fully allocated
        emit Transfer(owner, to, rewardsTokens);
    }

    /// @notice Function to allocate tokens for marketing
    /// @param to The address to allocate marketing tokens to
    function allocateMarketingTokens(address to) external onlyOwner {
        require(marketingTokens > 0, "No marketing tokens left to allocate");
        require(to != address(0), "Cannot allocate to zero address");

        balances[owner] -= marketingTokens;
        balances[to] += marketingTokens;
        marketingTokens = 0; // Mark as fully allocated
        emit Transfer(owner, to, marketingTokens);
    }

    /// @notice Function to allocate tokens for liquidity
    /// @param to The address to allocate liquidity tokens to
    function allocateLiquidityTokens(address to) external onlyOwner {
        require(liquidityTokens > 0, "No liquidity tokens left to allocate");
        require(to != address(0), "Cannot allocate to zero address");

        balances[owner] -= liquidityTokens;
        balances[to] += liquidityTokens;
        liquidityTokens = 0; // Mark as fully allocated
        emit Transfer(owner, to, liquidityTokens);
    }
}
```
