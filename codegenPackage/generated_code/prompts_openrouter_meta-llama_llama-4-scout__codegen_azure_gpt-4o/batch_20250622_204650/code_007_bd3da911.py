"""
Generated Code Metadata:
========================
Original URL: https://ondo-foundation.pages.dev
Prompt: Design a smart contract using Solidity that enables the tokenization of real-world assets (RWAs) on a blockchain, inspired by the Ondo Foundation's work.
Generated: DETERMINISTIC_bd3da9119d916700
Batch ID: 20250622_204650
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
 * @title RealWorldAssetToken
 * @dev A smart contract for tokenizing real-world assets (RWAs) on the blockchain.
 * Inspired by the Ondo Foundation's work.
 */
contract RealWorldAssetToken {
    // State variables
    string public name; // Name of the token
    string public symbol; // Symbol of the token
    uint8 public decimals; // Number of decimal places
    uint256 public totalSupply; // Total supply of tokens

    // Mapping to track balances of token holders
    mapping(address => uint256) private balances;

    // Mapping to track allowances for token transfers
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event AssetTokenized(address indexed owner, string assetDetails, uint256 tokenAmount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token contract.
     * @param _name Name of the token.
     * @param _symbol Symbol of the token.
     * @param _decimals Number of decimal places.
     * @param _initialSupply Initial supply of tokens.
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
<<<<<<< HEAD
        totalSupply = _initialSupply * (10**uint256(_decimals));
        owner = msg.sender;
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
=======
        totalSupply = _initialSupply;
        owner = msg.sender;
        balances[owner] = _initialSupply;

        emit Transfer(address(0), owner, _initialSupply);
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    }

    /**
     * @dev Function to tokenize a real-world asset.
     * @param assetDetails Details of the asset being tokenized.
     * @param tokenAmount Amount of tokens to mint for the asset.
     */
    function tokenizeAsset(string memory assetDetails, uint256 tokenAmount) external onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than zero");

<<<<<<< HEAD
        uint256 mintAmount = tokenAmount * (10**uint256(decimals));
        totalSupply += mintAmount;
        balances[owner] += mintAmount;

        emit AssetTokenized(owner, assetDetails, mintAmount);
        emit Transfer(address(0), owner, mintAmount);
    }

    /**
     * @dev Function to check the balance of a specific address.
     * @param account Address to query the balance of.
     * @return Balance of the specified address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function to transfer tokens to a specific address.
     * @param to Address to transfer tokens to.
     * @param value Amount of tokens to transfer.
     * @return Success status of the transfer.
=======
        totalSupply += tokenAmount;
        balances[owner] += tokenAmount;

        emit AssetTokenized(owner, assetDetails, tokenAmount);
        emit Transfer(address(0), owner, tokenAmount);
    }

    /**
     * @dev Function to transfer tokens to another address.
     * @param to Address to transfer tokens to.
     * @param value Amount of tokens to transfer.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
     */
    function transfer(address to, uint256 value) external returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= value, "Insufficient balance");

        balances[msg.sender] -= value;
        balances[to] += value;

        emit Transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @dev Function to approve another address to spend tokens on behalf of the caller.
     * @param spender Address to approve.
     * @param value Amount of tokens to approve.
<<<<<<< HEAD
     * @return Success status of the approval.
     */
    function approve(address spender, uint256 value) external returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");

=======
     */
    function approve(address spender, uint256 value) external returns (bool) {
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        allowances[msg.sender][spender] = value;

        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @dev Function to transfer tokens on behalf of another address.
     * @param from Address to transfer tokens from.
     * @param to Address to transfer tokens to.
     * @param value Amount of tokens to transfer.
<<<<<<< HEAD
     * @return Success status of the transfer.
     */
    function transferFrom(
        address from,
        address to,
        uint256 value
    ) external returns (bool) {
=======
     */
    function transferFrom(address from, address to, uint256 value) external returns (bool) {
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[from] >= value, "Insufficient balance");
        require(allowances[from][msg.sender] >= value, "Allowance exceeded");

        balances[from] -= value;
        balances[to] += value;
        allowances[from][msg.sender] -= value;

        emit Transfer(from, to, value);
        return true;
    }

    /**
<<<<<<< HEAD
     * @dev Function to check the allowance of a spender for a specific owner.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     * @return Remaining allowance for the spender.
=======
     * @dev Function to check the balance of an address.
     * @param account Address to check the balance of.
     * @return Balance of the address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function to check the allowance of a spender for a specific owner.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     * @return Allowance of the spender.
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
