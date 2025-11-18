"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitamadapp.pages.dev
Prompt: Write a Solidity smart contract that implements a hyperburn mechanism for token supply management, inspired by Saitama's hyperburn feature.
Generated: DETERMINISTIC_604b4b442a63847a
Batch ID: 20250612_152249
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
 * @title HyperBurnToken
 * @dev A token contract implementing "hyperburn" functionality for token supply management.
 */
contract HyperBurnToken {
    // Token metadata
    string public name = "HyperBurnToken";
    string public symbol = "HBT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping of balances
    mapping(address => uint256) private balances;
    // Mapping for allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event HyperBurn(uint256 amountBurned);

    // Owner of the contract
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the initial supply and assign it to the owner.
     * @param initialSupply Initial token supply.
     */
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        owner = msg.sender;
        totalSupply = initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Get the balance of a given account.
     * @param account Address of the account to query.
     * @return Balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens from sender to recipient.
     * @param recipient Address of the recipient.
     * @param amount Number of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Transfer to zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Internal function to handle transfers.
     * @param sender Address initiating the transfer.
     * @param recipient Address receiving the transfer.
     * @param amount Number of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        balances[sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Approve tokens for a spender.
     * @param spender Address authorized to spend tokens.
     * @param amount Number of tokens to approve.
     * @return True if the approval is successful.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Approve to zero address is not allowed");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from an approved allowance.
     * @param sender Address from which tokens are transferred.
     * @param recipient Address to which tokens are transferred.
     * @param amount Number of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0) && recipient != address(0), "Transfer from/to zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");

        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Burn a specific amount of tokens from the total supply for hyperburn functionality.
     * @param amount Number of tokens to burn.
     * Emits a {HyperBurn} event.
     */
    function hyperBurn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(totalSupply >= amount, "Burn amount exceeds total supply");

        totalSupply -= amount;
        balances[owner] -= amount;

        emit HyperBurn(amount);
    }
}
```
