"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-dogecoin20.pages.dev
Prompt: Write a function in Solidity to implement the fixed token supply mechanism for DOGE20, ensuring no new tokens can be minted beyond the total supply of 140,000,000,000.
Generated: DETERMINISTIC_31cf8fe003550345
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
 * @dev Implementation of a fixed supply ERC20-like token.
 */
contract DOGE20 {
    // State variables
    string public name = "DOGE20";
    string public symbol = "DOGE20";
    uint8 public decimals = 18;
    uint256 public totalSupply = 140_000_000_000 * (10 ** decimals); // Fixed total supply of 140 billion tokens

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Event emitted during transfers
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted during approval changes
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor initializes the contract with the total supply assigned to the deployer.
     */
    constructor() {
        balances[msg.sender] = totalSupply; // Assign the entire fixed supply to the contract deployer
        emit Transfer(address(0), msg.sender, totalSupply); // Emit a transfer event from the zero address
    }

    /**
     * @dev Get the balance of an account.
     * @param account The address to query the balance of.
     * @return The balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens to a specific address.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "DOGE20: transfer to the zero address"); // Prevent transfers to the zero address
        require(balances[msg.sender] >= amount, "DOGE20: insufficient balance"); // Ensure sender has enough tokens

        balances[msg.sender] -= amount; // Deduct tokens from sender
        balances[recipient] += amount; // Add tokens to recipient
        emit Transfer(msg.sender, recipient, amount); // Emit transfer event

        return true;
    }

    /**
     * @dev Approve an address to spend tokens on behalf of the sender.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating success.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "DOGE20: approve to the zero address"); // Prevent approvals to the zero address

        allowances[msg.sender][spender] = amount; // Set the allowance
        emit Approval(msg.sender, spender, amount); // Emit approval event

        return true;
    }

    /**
     * @dev Transfer tokens on behalf of an account, using an allowance.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0), "DOGE20: transfer from the zero address"); // Prevent transfers from the zero address
        require(recipient != address(0), "DOGE20: transfer to the zero address"); // Prevent transfers to the zero address
        require(balances[sender] >= amount, "DOGE20: insufficient balance"); // Ensure sender has enough tokens
        require(allowances[sender][msg.sender] >= amount, "DOGE20: allowance exceeded"); // Ensure allowance is sufficient

        balances[sender] -= amount; // Deduct tokens from sender
        balances[recipient] += amount; // Add tokens to recipient
        allowances[sender][msg.sender] -= amount; // Update allowance
        emit Transfer(sender, recipient, amount); // Emit transfer event

        return true;
    }

    /**
     * @dev Get the remaining allowance for a spender on an owner's account.
     * @param owner The account that owns the tokens.
     * @param spender The account approved to spend tokens.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
