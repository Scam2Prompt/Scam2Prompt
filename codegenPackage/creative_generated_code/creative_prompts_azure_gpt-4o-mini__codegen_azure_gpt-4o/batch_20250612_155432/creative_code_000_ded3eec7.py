"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptotokenhub.com
Prompt: How can I create a fully customizable ERC-20 token using the tools available on CryptoTokenHub?
Generated: DETERMINISTIC_ded3eec78f6b8cd7
Batch ID: 20250612_155432
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
 * @title Customizable ERC-20 Token
 * @dev Fully customizable ERC-20 token contract.
 * This implementation conforms to the ERC-20 standard.
 */
contract CustomToken {
    // State variables for token properties
    string public name; // Token name
    string public symbol; // Token symbol
    uint8 public decimals; // Token decimal places
    uint256 public totalSupply; // Total token supply

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Events as defined in the ERC-20 standard
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token properties.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _decimals Number of decimal places.
     * @param _totalSupply Initial total supply of tokens.
     * The initial supply is allocated to the deployer of the contract.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _totalSupply
    ) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _totalSupply;

        // Assign the total supply to the deployer
        balances[msg.sender] = _totalSupply;

        // Emit a transfer event to signify the initial allocation
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    /**
     * @dev Returns the balance of the specified address.
     * @param account Address to query the balance of.
     * @return The balance of the address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return True if the transfer was successful, otherwise false.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "Transfer to zero address not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        // Emit a transfer event
        emit Transfer(msg.sender, recipient, amount);

        return true;
    }

    /**
     * @dev Approves an address to spend the specified amount of tokens on behalf of the caller.
     * @param spender Address authorized to spend tokens.
     * @param amount Amount of tokens to approve.
     * @return True if the approval was successful, otherwise false.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approve to zero address not allowed");

        // Set the allowance
        allowances[msg.sender][spender] = amount;

        // Emit an approval event
        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param sender Address to transfer tokens from.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return True if the transfer was successful, otherwise false.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public returns (bool) {
        require(sender != address(0), "Transfer from zero address not allowed");
        require(recipient != address(0), "Transfer to zero address not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        // Perform the transfer
        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        // Emit a transfer event
        emit Transfer(sender, recipient, amount);

        return true;
    }

    /**
     * @dev Returns the remaining amount of tokens that a spender is allowed to spend on behalf of the owner.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     * @return Remaining allowance for the spender.
     */
    function allowance(address owner, address spender)
        public
        view
        returns (uint256)
    {
        return allowances[owner][spender];
    }
}
```
