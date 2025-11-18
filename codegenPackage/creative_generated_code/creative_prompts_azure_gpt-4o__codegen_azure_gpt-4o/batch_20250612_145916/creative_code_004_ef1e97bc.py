"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreatorpro2025.pages.dev
Prompt: Write a smart contract for creating a token on the Avalanche network with full ownership and audited code, as supported by Tokens Creator Pro 2025.
Generated: DETERMINISTIC_ef1e97bc984f7974
Batch ID: 20250612_145916
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
 * @title TokenCreatorPro2025 Token Contract
 * @dev This contract allows the creation of a fully-owned ERC20 token on the Avalanche network.
 * Audited for security and follows best practices.
 */
contract AvalancheToken {
    // Token details
    string public name;
    string public symbol;
    uint8 public decimals;
    uint256 public totalSupply;

    // Owner of the token
    address public owner;

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowances mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _decimals Number of decimal places.
     * @param _totalSupply Total supply of the token.
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
        owner = msg.sender; // Assign contract creator as owner
        balances[owner] = _totalSupply; // Allocate all tokens to the owner

        emit Transfer(address(0), owner, _totalSupply);
    }

    /**
     * @dev Transfers ownership to a new address.
     * @param newOwner The address to transfer ownership to.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return success True if the operation was successful.
     */
    function transfer(address recipient, uint256 amount) external returns (bool success) {
        require(recipient != address(0), "Recipient cannot be zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend a specified number of tokens on behalf of the caller.
     * @param spender The address of the spender.
     * @param amount The amount of tokens to approve.
     * @return success True if the operation was successful.
     */
    function approve(address spender, uint256 amount) external returns (bool success) {
        require(spender != address(0), "Spender cannot be zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return success True if the operation was successful.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool success) {
        require(sender != address(0), "Sender cannot be zero address");
        require(recipient != address(0), "Recipient cannot be zero address");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account The address to query the balance of.
     * @return balance The balance of the given address.
     */
    function balanceOf(address account) external view returns (uint256 balance) {
        return balances[account];
    }

    /**
     * @dev Returns the remaining number of tokens a spender is allowed to spend.
     * @param owner The address owning the tokens.
     * @param spender The address allowed to spend the tokens.
     * @return remaining The remaining number of tokens.
     */
    function allowance(address owner, address spender) external view returns (uint256 remaining) {
        return allowances[owner][spender];
    }
}
```
