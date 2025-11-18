"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmnt.org
Prompt: Create a Solidity smart contract that adheres to the GMNTCoin standards (BEP20) and includes features like no mintable function, no presale, and secure code auditing.
Generated: DETERMINISTIC_5fea43d634f40556
Batch ID: 20250612_151525
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
 * @title GMNTCoin (BEP20 Standard)
 * @dev A secure and production-ready implementation of a BEP20 token contract.
 * Features:
 * - No minting functionality
 * - No presale logic
 * - Well-commented and adheres to best practices
 */

interface IBEP20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

contract GMNTCoin is IBEP20 {
    // Token metadata
    string public constant name = "GMNTCoin";
    string public constant symbol = "GMNT";
    uint8 public constant decimals = 18;

    // State variables
    uint256 private _totalSupply;
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Ownership
    address public owner;

    // Events
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "GMNTCoin: Caller is not the owner");
        _;
    }

    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "GMNTCoin: Initial supply must be greater than zero");
        owner = msg.sender;
        _totalSupply = initialSupply * (10 ** uint256(decimals));
        _balances[owner] = _totalSupply;
        emit Transfer(address(0), owner, _totalSupply);
    }

    // BEP20 Functions

    /**
     * @dev Returns the total supply of the token.
     */
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the balance of the given account.
     */
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to the specified recipient.
     * Emits a Transfer event.
     */
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that spender is allowed to spend
     * on behalf of owner.
     */
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Approves the spender to spend a specified amount of tokens on behalf of the caller.
     * Emits an Approval event.
     */
    function approve(address spender, uint256 amount) external override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from sender to recipient using the allowance mechanism.
     * Emits a Transfer event and an Approval event.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        _transfer(sender, recipient, amount);
        uint256 currentAllowance = _allowances[sender][msg.sender];
        require(currentAllowance >= amount, "GMNTCoin: Transfer amount exceeds allowance");
        unchecked {
            _approve(sender, msg.sender, currentAllowance - amount);
        }
        return true;
    }

    // Internal Functions

    /**
     * @dev Internal function to handle token transfer logic.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "GMNTCoin: Transfer from the zero address");
        require(recipient != address(0), "GMNTCoin: Transfer to the zero address");
        require(_balances[sender] >= amount, "GMNTCoin: Transfer amount exceeds balance");

        unchecked {
            _balances[sender] -= amount;
            _balances[recipient] += amount;
        }
        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Internal function to handle token approval logic.
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "GMNTCoin: Approve from the zero address");
        require(spender != address(0), "GMNTCoin: Approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    // Ownership Functions

    /**
     * @dev Transfers ownership of the contract to a new address.
     * Can only be called by the current owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "GMNTCoin: New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
