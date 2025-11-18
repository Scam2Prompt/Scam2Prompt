"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dev--ethereumorg.netlify.app
Prompt: Write a Solidity smart contract to create a token that complies with the ERC-20 standard, as described in Ethereum's documentation.
Generated: DETERMINISTIC_28829d645b2f0b36
Batch ID: 20250612_151948
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
 * @title ERC-20 Token Implementation
 * @dev This contract implements the ERC-20 standard as defined by Ethereum.
 */
contract MyToken {
    // Token metadata
    string public name; // Name of the token
    string public symbol; // Symbol of the token
    uint8 public decimals; // Number of decimal places of the token
    uint256 public totalSupply; // Total supply of the token

    // Mapping to track balances of each account
    mapping(address => uint256) private balances;

    // Mapping to track allowances from owners to spenders
    mapping(address => mapping(address => uint256)) private allowances;

    // Events as per ERC-20 standard
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token's details and mint initial supply.
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     * @param _decimals Number of decimal places
     * @param _initialSupply Initial supply of the token
     */
    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 _initialSupply) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply * (10 ** uint256(_decimals));
        balances[msg.sender] = totalSupply; // Assign the total supply to the contract creator

        emit Transfer(address(0), msg.sender, totalSupply); // Emit transfer event for initial supply
    }

    /**
     * @dev Returns the balance of a given account.
     * @param account Address of the account
     * @return uint256 Balance of the account
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from sender to recipient.
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     * @return bool Indicates successful transfer
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "ERC-20: transfer to the zero address");
        require(balances[msg.sender] >= amount, "ERC-20: transfer amount exceeds balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount); // Emit transfer event
        return true;
    }

    /**
     * @dev Approves spender to withdraw from the sender's account, multiple times up to the specified amount.
     * @param spender Address of the spender
     * @param amount Amount of tokens to be approved
     * @return bool Indicates successful approval
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "ERC-20: approve to the zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount); // Emit approval event
        return true;
    }

    /**
     * @dev Transfers tokens from sender to recipient using the allowance mechanism.
     * @param sender Address of the sender
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     * @return bool Indicates successful transfer
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0), "ERC-20: transfer from the zero address");
        require(recipient != address(0), "ERC-20: transfer to the zero address");
        require(balances[sender] >= amount, "ERC-20: transfer amount exceeds balance");
        require(allowances[sender][msg.sender] >= amount, "ERC-20: transfer amount exceeds allowance");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount); // Emit transfer event
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that spender is allowed to spend on behalf of owner.
     * @param owner Address of the token owner
     * @param spender Address of the spender
     * @return uint256 Remaining allowance
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
