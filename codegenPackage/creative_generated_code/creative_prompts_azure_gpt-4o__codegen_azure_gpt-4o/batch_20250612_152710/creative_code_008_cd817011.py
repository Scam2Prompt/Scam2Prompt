"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-token.pages.dev
Prompt: Write a Solidity contract for managing the fixed supply of DOGE20 tokens and preventing inflation, as described in the tokenomics section of the Dogecoin20 site.
Generated: DETERMINISTIC_cd817011a71b78e8
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
 * @title DOGE20 Token Contract
 * @dev Fixed supply token with no inflation mechanism.
 *      This contract follows the ERC20 standard.
 */
contract DOGE20Token {
    // Token details
    string public name = "DOGE20";
    string public symbol = "DOGE20";
    uint8 public decimals = 18;

    // Fixed total supply of tokens
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Contract owner address
    address public owner;

    /**
     * @dev Modifier to restrict certain functions to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor initializes the token contract with a fixed supply and assigns all tokens to the owner.
     * @param initialSupply The fixed supply of tokens (in wei units, adjusted for decimals).
     */
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = initialSupply;
        owner = msg.sender;
        balances[owner] = totalSupply; // Assign all tokens to the owner
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account Address to query the balance for.
     * @return The balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param to The recipient address.
     * @param amount The number of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;
        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves another address to spend tokens on behalf of the caller.
     * @param spender The address authorized to spend tokens.
     * @param amount The number of tokens they are authorized to spend.
     * @return A boolean indicating success.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of another address, subject to allowance.
     * @param from The address to transfer tokens from.
     * @param to The recipient address.
     * @param amount The number of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Transfer amount exceeds allowance");

        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;
        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Returns the current allowance for a spender on behalf of an owner.
     * @param owner The address of the token owner.
     * @param spender The address authorized to spend tokens.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
