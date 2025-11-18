"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-in.web.app
Prompt: Write a smart contract in Solidity that implements a burn mechanism for $MPEPE tokens after every transaction, as described in the Mpeppe ecosystem.
Generated: DETERMINISTIC_c436013ea1ccc92c
Batch ID: 20250612_154115
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
 * @title MPEPE Token Contract
 * @dev ERC20 Token implementation with burn mechanism after every transaction.
 */
contract MPEPE {
    // Token details
    string public name = "MPEPE";
    string public symbol = "MPEPE";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to keep track of balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Event declarations
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Burn percentage per transaction
    uint256 public burnPercentage = 2; // 2% burn per transaction

    /**
     * @dev Constructor to initialize the total supply and assign it to the contract deployer.
     * @param _initialSupply Initial supply of the token.
     */
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of tokens held by the given address.
     * @param account The address to query the balance of.
     * @return The token balance of the address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address with burn mechanism.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return Whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Internal function to handle token transfers with burn mechanism.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");

        // Calculate burn amount and final transfer amount
        uint256 burnAmount = (amount * burnPercentage) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Update balances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;

        // Burn the tokens
        totalSupply -= burnAmount;

        // Emit transfer event
        emit Transfer(sender, recipient, transferAmount);
        emit Transfer(sender, address(0), burnAmount); // Burn event
    }

    /**
     * @dev Approves the specified address to spend a certain amount of tokens.
     * @param spender The address allowed to spend the tokens.
     * @param amount The amount of tokens to approve.
     * @return Whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using allowance mechanism with burn.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     * @return Whether the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        // Reduce the allowance
        allowances[sender][msg.sender] -= amount;

        // Execute the transfer
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the allowance of a spender on a specific account.
     * @param owner The address owning the tokens.
     * @param spender The address allowed to spend the tokens.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
