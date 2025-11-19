"""
Generated Code Metadata:
========================
Original URL: https://follow-neotokyo.pages.dev
Prompt: Generate a smart contract code snippet for a crypto token, such as $BYTES, used for transactions in a gaming community like Neo Tokyo.
Generated: DETERMINISTIC_8ff422b3adb94711
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title BYTES Token
 * @dev ERC20 Token implementation for the Neo Tokyo gaming community.
 */
contract BYTES {
    // Token details
    string public name = "BYTES";
    string public symbol = "BYTES";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to store balances
    mapping(address => uint256) private balances;

    // Mapping to store allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Owner of the contract
    address public owner;

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token supply and assign it to the owner.
     * @param initialSupply The initial supply of tokens.
     */
    constructor(uint256 initialSupply) {
        owner = msg.sender;
        totalSupply = initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;
        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Function to check the balance of a given address.
     * @param account The address to query the balance of.
     * @return The balance of the given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function to transfer tokens to a specified address.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Function to approve another address to spend tokens on behalf of the caller.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating success.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to the zero address");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Function to check the allowance of a spender for a given owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @return The remaining allowance for the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Function to transfer tokens on behalf of an owner, given approval.
     * @param sender The address of the token owner.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Function to mint new tokens. Restricted to the contract owner.
     * @param amount The amount of tokens to mint.
     */
    function mint(uint256 amount) public onlyOwner {
        uint256 mintAmount = amount * (10 ** uint256(decimals));
        totalSupply += mintAmount;
        balances[owner] += mintAmount;
        emit Transfer(address(0), owner, mintAmount);
    }

    /**
     * @dev Function to burn tokens. Restricted to the contract owner.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public onlyOwner {
        require(balances[owner] >= amount, "Insufficient balance to burn");

        uint256 burnAmount = amount * (10 ** uint256(decimals));
        totalSupply -= burnAmount;
        balances[owner] -= burnAmount;
        emit Transfer(owner, address(0), burnAmount);
    }
}
```
