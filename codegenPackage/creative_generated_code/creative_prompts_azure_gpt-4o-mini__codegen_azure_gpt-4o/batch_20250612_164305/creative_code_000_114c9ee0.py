"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicrx6mxjdmgvh7372dgpwudwaunxrrcmmzyotodztwlzppzgiu5xm.ipfs.dweb.link
Prompt: Generate a smart contract in Solidity for a meme token similar to ANDY, using the contract address 0x18A8BD1fe17A1BB9FFB39eCD83E9489cfD17a022 as a reference.
Generated: DETERMINISTIC_114c9ee04055b899
Batch ID: 20250612_164305
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
 * @title MemeToken
 * @dev An ERC20-like meme token contract
 */
contract MemeToken {
    // Token details
    string public name = "MemeToken";       // Name of the token
    string public symbol = "MEME";          // Symbol of the token
    uint8 public decimals = 18;             // Decimal precision
    uint256 public totalSupply = 1000000 * (10 ** uint256(decimals)); // Total supply

    // Balances for each account
    mapping(address => uint256) private balances;
    // Allowances for transfers
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the contract
    constructor() {
        // Assign total supply to the contract deployer
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Returns the balance of the given address.
     * @param account Address to query the balance of.
     * @return Balance of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a given address.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return True if the transfer succeeds, false otherwise.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender Address to be approved.
     * @param amount Amount of tokens to approve.
     * @return True if the approval succeeds, false otherwise.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");

        // Set the allowance
        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using allowance mechanism.
     * @param sender Address to transfer tokens from.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return True if the transfer succeeds, false otherwise.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        // Perform the transfer
        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance of a spender for a given owner.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     * @return Remaining allowance for the spender.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
