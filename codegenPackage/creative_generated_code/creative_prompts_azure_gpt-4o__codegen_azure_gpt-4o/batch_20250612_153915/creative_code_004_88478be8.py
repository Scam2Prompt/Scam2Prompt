"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonbrowser.ru
Prompt: Write a smart contract for a GameFi application on the TON blockchain, incorporating features for memecoin transactions.
Generated: DETERMINISTIC_88478be8d8026d53
Batch ID: 20250612_153915
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
 * @title GameFiMemecoinContract
 * @notice A smart contract for GameFi applications on the TON blockchain that supports memecoin transactions.
 * @dev This contract is built for general use cases and adheres to best practices.
 */
contract GameFiMemecoinContract {
    // Events
    event Transfer(address indexed from, address indexed to, uint256 amount);
    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed from, uint256 amount);

    // State variables
    address public owner;
    string public constant name = "GameFiMemecoin";
    string public constant symbol = "GMC";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Modifier to restrict access to owner functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @notice Constructor initializes the contract owner and sets an initial supply of memecoins.
     * @param initialSupply The initial supply of memecoins.
     */
    constructor(uint256 initialSupply) {
        owner = msg.sender;
        mint(msg.sender, initialSupply);
    }

    /**
     * @notice Get the balance of an account.
     * @param account The address of the account.
     * @return The balance of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @notice Transfer memecoins from the sender to a recipient.
     * @param recipient The address of the recipient.
     * @param amount The amount to transfer.
     * @return A boolean value indicating whether the operation succeeded.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @notice Approve a spender to spend tokens on behalf of the sender.
     * @param spender The address of the spender.
     * @param amount The amount to approve.
     * @return A boolean value indicating whether the operation succeeded.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address not allowed");

        allowances[msg.sender][spender] = amount;
        return true;
    }

    /**
     * @notice Transfer tokens on behalf of an account.
     * @param sender The address of the sender.
     * @param recipient The address of the recipient.
     * @param amount The amount to transfer.
     * @return A boolean value indicating whether the operation succeeded.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address not allowed");
        require(recipient != address(0), "Transfer to the zero address not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @notice Mint new tokens and add them to an account's balance.
     * @param account The address of the account to mint tokens for.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) public onlyOwner {
        require(account != address(0), "Mint to the zero address not allowed");

        totalSupply += amount;
        balances[account] += amount;

        emit Mint(account, amount);
    }

    /**
     * @notice Burn tokens from an account's balance, reducing total supply.
     * @param account The address of the account to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burn(address account, uint256 amount) public onlyOwner {
        require(account != address(0), "Burn from the zero address not allowed");
        require(balances[account] >= amount, "Insufficient balance to burn");

        totalSupply -= amount;
        balances[account] -= amount;

        emit Burn(account, amount);
    }

    /**
     * @notice Check the allowance of a spender for a given owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @return The allowance of the spender for the owner.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
