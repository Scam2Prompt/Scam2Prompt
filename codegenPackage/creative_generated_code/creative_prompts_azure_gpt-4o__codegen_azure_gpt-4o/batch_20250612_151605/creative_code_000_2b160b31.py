"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimmpeppe.web.app
Prompt: Write an Ethereum smart contract that implements a token similar to $MPEPE, including features like automatic token burning after every transaction.
Generated: DETERMINISTIC_2b160b3118c74f97
Batch ID: 20250612_151605
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
 * @title Burnable Token Contract
 * @dev Implements an ERC20-like token with automatic burning feature on every transaction.
 */
contract BurnableToken {
    // Token metadata
    string public name = "MPEPE Token";
    string public symbol = "MPEPE";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances of accounts
    mapping(address => uint256) private balances;

    // Mapping for allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Percentage of tokens to burn per transaction (1% = 100)
    uint256 public burnRate = 100; // Burn rate: 1%

    // Event declarations
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Burn(address indexed from, uint256 amount);

    // Modifier to ensure valid address
    modifier validAddress(address addr) {
        require(addr != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Constructor to initialize the total supply and assign it to the deployer.
     * @param initialSupply Initial supply of the token.
     */
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of a specific account.
     * @param account Address of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address, with automatic burning.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public validAddress(recipient) returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Calculate the burn amount
        uint256 burnAmount = (amount * burnRate) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Update balances
        balances[msg.sender] -= amount;
        balances[recipient] += transferAmount;
        totalSupply -= burnAmount;

        // Emit events
        emit Transfer(msg.sender, recipient, transferAmount);
        emit Burn(msg.sender, burnAmount);

        return true;
    }

    /**
     * @dev Approves a spender to spend a specific amount of tokens.
     * @param spender Address of the spender.
     * @param amount Amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public validAddress(spender) returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens a spender is allowed to spend.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens from one account to another, with automatic burning.
     * @param sender Address of the sender.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public validAddress(recipient) returns (bool) {
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        // Calculate the burn amount
        uint256 burnAmount = (amount * burnRate) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Update balances and allowances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;
        allowances[sender][msg.sender] -= amount;
        totalSupply -= burnAmount;

        // Emit events
        emit Transfer(sender, recipient, transferAmount);
        emit Burn(sender, burnAmount);

        return true;
    }
}
```
