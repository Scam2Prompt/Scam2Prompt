"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-moonbag-org.pages.dev
Prompt: Provide code for auditing an ERC20 smart contract using a blockchain security tool, ensuring compliance with standards similar to MoonBag's SCRL audit.
Generated: DETERMINISTIC_b302f1553465b2e6
Batch ID: 20250612_151726
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

/// @title ERC20 Audit Example
/// @notice This contract is an example of a basic ERC20 token implementation
/// that complies with the ERC20 standard and can be audited for security.
contract ERC20Token {
    string public name; // Name of the token
    string public symbol; // Symbol of the token
    uint8 public decimals; // Number of decimals for the token
    uint256 public totalSupply; // Total supply of the token

    mapping(address => uint256) private balances; // Mapping from account addresses to their balance
    mapping(address => mapping(address => uint256)) private allowances; // Mapping from owner to spender allowances

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /// @dev Constructor to set the token details
    /// @param _name Name of the token
    /// @param _symbol Symbol of the token
    /// @param _decimals Number of decimal places for the token
    /// @param _initialSupply Initial supply of tokens to be minted
    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply * (10 ** uint256(decimals)); // Adjust for decimals
        balances[msg.sender] = totalSupply; // Assign total supply to contract deployer

        emit Transfer(address(0), msg.sender, totalSupply); // Emit transfer event for minting
    }

    /// @notice Get the balance of a specific account
    /// @param account The address of the account to check
    /// @return The balance of the specified account
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /// @notice Transfer tokens from the caller's account to another account
    /// @param to The address of the recipient
    /// @param amount The amount of tokens to transfer
    /// @return A boolean indicating success of the transfer
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount; // Deduct amount from sender
        balances[to] += amount; // Add amount to recipient

        emit Transfer(msg.sender, to, amount); // Emit transfer event
        return true; // Indicate success
    }

    /// @notice Approve a spender to withdraw tokens from the caller's account
    /// @param spender The address of the spender
    /// @param amount The amount of tokens to approve
    /// @return A boolean indicating success of the approval
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        allowances[msg.sender][spender] = amount; // Set allowance
        emit Approval(msg.sender, spender, amount); // Emit approval event
        return true; // Indicate success
    }

    /// @notice Transfer tokens from one account to another using allowances
    /// @param from The address of the sender
    /// @param to The address of the recipient
    /// @param amount The amount of tokens to transfer
    /// @return A boolean indicating success of the transfer
    function transferFrom(address from, address to, uint256 amount) external returns (bool) {
        require(from != address(0), "Transfer from the zero address");
        require(to != address(0), "Transfer to the zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        balances[from] -= amount; // Deduct amount from sender
        balances[to] += amount; // Add amount to recipient
        allowances[from][msg.sender] -= amount; // Deduct from allowance

        emit Transfer(from, to, amount); // Emit transfer event
        return true; // Indicate success
    }

    /// @notice Get the remaining allowance for a spender
    /// @param owner The address of the token owner
    /// @param spender The address of the spender
    /// @return The remaining allowance
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
