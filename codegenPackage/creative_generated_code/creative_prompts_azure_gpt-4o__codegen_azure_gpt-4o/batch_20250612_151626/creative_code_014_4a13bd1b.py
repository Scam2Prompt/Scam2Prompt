"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogee1.pages.dev
Prompt: Write a Solidity contract for DOGE20 tokenomics that enforces the fixed supply and allocates tokens according to the presale, marketing, treasury, staking rewards, and liquidity provisions.
Generated: DETERMINISTIC_4a13bd1b8a82710d
Batch ID: 20250612_151626
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
 * @title DOGE20 Token Contract
 * @dev Implements tokenomics with fixed supply and allocation for presale, marketing, treasury, staking rewards, and liquidity.
 */
contract DOGE20 {
    // ERC-20 Token Standards
    string public name = "DOGE20";
    string public symbol = "DOGE20";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000_000 * (10 ** uint256(decimals)); // Fixed supply: 1 billion tokens

    // Allocations
    uint256 public presaleAllocation = (totalSupply * 50) / 100;  // 50% of total supply
    uint256 public marketingAllocation = (totalSupply * 10) / 100; // 10% of total supply
    uint256 public treasuryAllocation = (totalSupply * 15) / 100;  // 15% of total supply
    uint256 public stakingRewardsAllocation = (totalSupply * 20) / 100; // 20% of total supply
    uint256 public liquidityProvisionAllocation = (totalSupply * 5) / 100; // 5% of total supply

    // Balances mapping
    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to allocate tokens during deployment
    constructor(
        address presaleAddress,
        address marketingAddress,
        address treasuryAddress,
        address stakingRewardsAddress,
        address liquidityProvisionAddress
    ) {
        require(
            presaleAddress != address(0) &&
            marketingAddress != address(0) &&
            treasuryAddress != address(0) &&
            stakingRewardsAddress != address(0) &&
            liquidityProvisionAddress != address(0),
            "Invalid address provided."
        );

        // Allocate tokens to respective addresses
        balances[presaleAddress] = presaleAllocation;
        balances[marketingAddress] = marketingAllocation;
        balances[treasuryAddress] = treasuryAllocation;
        balances[stakingRewardsAddress] = stakingRewardsAllocation;
        balances[liquidityProvisionAddress] = liquidityProvisionAllocation;

        // Emit transfer events for transparency
        emit Transfer(address(0), presaleAddress, presaleAllocation);
        emit Transfer(address(0), marketingAddress, marketingAllocation);
        emit Transfer(address(0), treasuryAddress, treasuryAllocation);
        emit Transfer(address(0), stakingRewardsAddress, stakingRewardsAllocation);
        emit Transfer(address(0), liquidityProvisionAddress, liquidityProvisionAllocation);
    }

    /**
     * @dev Transfer tokens from the caller to another address.
     * @param to Address to transfer tokens to.
     * @param value Amount of tokens to transfer.
     */
    function transfer(address to, uint256 value) external returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address.");
        require(balances[msg.sender] >= value, "Insufficient balance.");

        balances[msg.sender] -= value;
        balances[to] += value;

        emit Transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @dev Approve another address to spend tokens on behalf of the caller.
     * @param spender Address to approve.
     * @param value Amount of tokens to approve.
     */
    function approve(address spender, uint256 value) external returns (bool) {
        require(spender != address(0), "Cannot approve the zero address.");

        allowances[msg.sender][spender] = value;

        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @dev Transfer tokens on behalf of the owner (requires prior approval).
     * @param from Address to transfer tokens from.
     * @param to Address to transfer tokens to.
     * @param value Amount of tokens to transfer.
     */
    function transferFrom(address from, address to, uint256 value) external returns (bool) {
        require(from != address(0) && to != address(0), "Cannot transfer from/to the zero address.");
        require(balances[from] >= value, "Insufficient balance.");
        require(allowances[from][msg.sender] >= value, "Transfer amount exceeds allowance.");

        balances[from] -= value;
        balances[to] += value;
        allowances[from][msg.sender] -= value;

        emit Transfer(from, to, value);
        return true;
    }

    /**
     * @dev Check the balance of a given address.
     * @param account Address to query balance for.
     * @return Balance of the given address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Check the allowance of a spender for a given owner.
     * @param owner Address of the token owner.
     * @param spender Address of the approved spender.
     * @return Remaining allowance for the spender.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
