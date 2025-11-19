"""
Generated Code Metadata:
========================
Original URL: https://wallstreetmemes-in.pages.dev
Prompt: Develop a simple smart contract in Solidity for a token similar to $WSM, including functions for token purchase, transfer, and balance checking.
Generated: DETERMINISTIC_c51110fc2a3ef1ae
Batch ID: 20250622_211011
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
 * @title SimpleToken
 * @dev A basic ERC20-like token contract with purchase, transfer, and balance checking functionality.
 */
contract SimpleToken {
    // Token details
    string public name = "SimpleToken";
    string public symbol = "STKN";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to store balances
    mapping(address => uint256) private balances;

    // Owner of the contract
    address public owner;

    // Token price in wei (1 token = 0.001 ETH)
    uint256 public tokenPrice = 0.001 ether;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Purchase(address indexed buyer, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply; // Assign all tokens to the owner initially
    }

    /**
     * @dev Function to check the balance of an account.
     * @param account The address to query the balance of.
     * @return The balance of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function to transfer tokens to another account.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Function to purchase tokens by sending Ether.
     * @return The amount of tokens purchased.
     */
    function purchaseTokens() public payable returns (uint256) {
        require(msg.value > 0, "Ether sent must be greater than zero");

        // Calculate the number of tokens to purchase
        uint256 tokensToPurchase = msg.value / tokenPrice;
        require(tokensToPurchase > 0, "Insufficient Ether to purchase tokens");
        require(balances[owner] >= tokensToPurchase, "Not enough tokens available for purchase");

        // Transfer tokens to the buyer
        balances[owner] -= tokensToPurchase;
        balances[msg.sender] += tokensToPurchase;

        emit Purchase(msg.sender, tokensToPurchase);
        return tokensToPurchase;
    }

    /**
     * @dev Function to withdraw Ether from the contract (only owner).
     * @param amount The amount of Ether to withdraw.
     */
    function withdraw(uint256 amount) public onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfers are not allowed");
    }
}
```
