"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mogan.pages.dev
Prompt: Write a tutorial for deploying a new ERC-20 token on Ethereum with features similar to $MOG, emphasizing community-driven growth and cultural branding.
Generated: DETERMINISTIC_c441f985c17a8153
Batch ID: 20250612_151027
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
 * @title CommunityToken
 * @dev An ERC-20 token designed for community-driven growth and cultural branding.
 */
contract CommunityToken {
    // Mapping to keep track of balances
    mapping(address => uint256) private _balances;

    // Mapping for allowances (approve and transferFrom functionality)
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Token metadata
    string private _name;
    string private _symbol;
    uint8 private _decimals;

    // Ownership for administrative tasks
    address private _owner;

    // Events for logging token transfers, approvals, and ownership transfers
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Constructor to initialize the token and set its metadata.
     * @param name_ The name of the token.
     * @param symbol_ The symbol of the token.
     * @param totalSupply_ The initial total supply of the token.
     */
    constructor(string memory name_, string memory symbol_, uint256 totalSupply_) {
        require(totalSupply_ > 0, "Total supply must be greater than zero");

        _name = name_;
        _symbol = symbol_;
        _decimals = 18; // Standard for ERC-20 tokens
        _totalSupply = totalSupply_ * (10**_decimals); // Adjust for decimals
        _owner = msg.sender; // Set the deployer as the owner

        // Assign all tokens to the deployer
        _balances[_owner] = _totalSupply;

        // Emit transfer event for initial distribution to deployer
        emit Transfer(address(0), _owner, _totalSupply);
    }

    // ERC-20 standard functions -----------------------------------

    /**
     * @dev Returns the name of the token.
     */
    function name() external view returns (string memory) {
        return _name;
    }

    /**
     * @dev Returns the symbol of the token.
     */
    function symbol() external view returns (string memory) {
        return _symbol;
    }

    /**
     * @dev Returns the number of decimals for the token.
     */
    function decimals() external view returns (uint8) {
        return _decimals;
    }

    /**
     * @dev Returns the total supply of the token.
     */
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account The address to query the balance for.
     */
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend a specified amount of tokens.
     * @param spender The address authorized to spend.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the allowance for a spender on behalf of an owner.
     * @param owner The address that owns the tokens.
     * @param spender The address authorized to spend the tokens.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens on behalf of an owner (used for approved transfers).
     * @param sender The address of the token owner.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(_allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    /**
     * @dev Internal function to handle transfers.
     * @param sender The address sending tokens.
     * @param recipient The address receiving tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from zero address");
        require(recipient != address(0), "Transfer to zero address");
        require(_balances[sender] >= amount, "Transfer amount exceeds balance");

        _balances[sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Internal function to approve spending of tokens.
     * @param owner The address owning the tokens.
     * @param spender The address authorized to spend the tokens.
     * @param amount The amount of tokens to approve.
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "Approve from zero address");
        require(spender != address(0), "Approve to zero address");

        _allowances[owner][spender] = amount;

        emit Approval(owner, spender, amount);
    }

    // Ownership-specific functions -----------------------------------

    /**
     * @dev Returns the address of the contract owner.
     */
    function owner() external view returns (address) {
        return _owner;
    }

    /**
     * @dev Allows the current owner to transfer ownership of the contract.
     * @param newOwner The address to transfer ownership to.
     */
    function transferOwnership(address newOwner) external {
        require(msg.sender == _owner, "Caller is not the owner");
        require(newOwner != address(0), "New owner is the zero address");

        emit OwnershipTransferred(_owner, newOwner);
        _owner = newOwner;
    }
}
```
