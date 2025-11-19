"""
Generated Code Metadata:
========================
Original URL: https://rangersprotocol.gitbook.io
Prompt: What is the process for creating and managing sub-chains on the Rangers Protocol? Include a code example for issuing RAP20 tokens.
Generated: DETERMINISTIC_479ab47fbd873674
Batch ID: 20250612_135144
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
 * @title RAP20 Token Contract
 * @dev This contract demonstrates the process of issuing RAP20 tokens on the Rangers Protocol.
 * RAP20 is a standard similar to ERC20, used for token management on Rangers Protocol sub-chains.
 * This example includes token creation, minting, and basic management.
 */

interface IRAP20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function allowance(address owner, address spender) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

contract RAP20Token is IRAP20 {
    // Token metadata
    string public name;
    string public symbol;
    uint8 public decimals;

    // Total supply of the token
    uint256 private _totalSupply;

    // Balances and allowances mapping
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token with metadata and initial supply.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _decimals Number of decimal places.
     * @param _initialSupply Initial supply of the token.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint8 _decimals,
        uint256 _initialSupply
    ) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        owner = msg.sender;

        // Mint the initial supply to the owner
        _mint(owner, _initialSupply);
    }

    /**
     * @dev Returns the total supply of the token.
     */
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the balance of a specific account.
     * @param account Address of the account.
     */
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @dev Transfers tokens to a recipient.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the allowance of a spender for a specific owner.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     */
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Approves a spender to spend a specific amount of tokens on behalf of the owner.
     * @param spender Address of the spender.
     * @param amount Amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) external override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from a sender to a recipient using the allowance mechanism.
     * @param sender Address of the sender.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        uint256 currentAllowance = _allowances[sender][msg.sender];
        require(currentAllowance >= amount, "Transfer amount exceeds allowance");
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, currentAllowance - amount);
        return true;
    }

    /**
     * @dev Internal function to transfer tokens between accounts.
     * @param sender Address of the sender.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Transfer amount exceeds balance");

        _balances[sender] -= amount;
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Internal function to mint new tokens.
     * @param account Address of the account to receive the tokens.
     * @param amount Amount of tokens to mint.
     */
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "Mint to the zero address");

        _totalSupply += amount;
        _balances[account] += amount;

        emit Transfer(address(0), account, amount);
    }

    /**
     * @dev Internal function to approve a spender.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     * @param amount Amount of tokens to approve.
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "Approve from the zero address");
        require(spender != address(0), "Approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Function to mint new tokens. Restricted to the owner.
     * @param account Address of the account to receive the tokens.
     * @param amount Amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }
}
```
