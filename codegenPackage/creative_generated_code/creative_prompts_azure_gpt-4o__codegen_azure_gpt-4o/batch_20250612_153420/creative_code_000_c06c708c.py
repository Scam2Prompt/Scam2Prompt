"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxy-fox.pages.dev
Prompt: Write a smart contract in Solidity for a deflationary token similar to $GFOX, including a burn mechanism that reduces the token supply with every transaction.
Generated: DETERMINISTIC_c06c708c439ac170
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
pragma solidity ^0.8.17;

/**
 * @title DeflationaryToken
 * @dev A deflationary ERC20 token with a burn mechanism that reduces token supply with every transaction.
 */
contract DeflationaryToken {
    // State variables
    string public name = "DeflationaryToken";
    string public symbol = "DFT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping for balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Burn rate (e.g., 2% burn on every transaction)
    uint256 public burnRate = 2;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed from, uint256 value);

    constructor(uint256 _initialSupply) {
        // Mint initial supply to the contract creator
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply;
        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account The address of the account to query.
     * @return balance The balance of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to another address with burn mechanism.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return success True if the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Update balances
        balances[msg.sender] -= amount;
        balances[recipient] += transferAmount;
        totalSupply -= burnAmount;

        // Emit events
        emit Burn(msg.sender, burnAmount);
        emit Transfer(msg.sender, recipient, transferAmount);

        return true;
    }

    /**
     * @dev Approves the spender to spend a specific amount of tokens on behalf of the caller.
     * @param spender The address allowed to spend the tokens.
     * @param amount The amount of tokens to approve.
     * @return success True if the approval was successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another with burn mechanism.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     * @return success True if the transfer was successful.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 transferAmount = amount - burnAmount;

        // Update balances and allowances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        allowances[sender][msg.sender] -= amount;
        totalSupply -= burnAmount;

        // Emit events
        emit Burn(sender, burnAmount);
        emit Transfer(sender, recipient, transferAmount);

        return true;
    }

    /**
     * @dev Returns the remaining number of tokens the spender is allowed to spend on behalf of the owner.
     * @param owner The address owning the tokens.
     * @param spender The address allowed to spend the tokens.
     * @return remainingAllowance The remaining allowance.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
