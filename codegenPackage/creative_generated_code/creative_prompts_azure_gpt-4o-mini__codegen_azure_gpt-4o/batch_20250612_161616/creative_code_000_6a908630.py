"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rebelsatoshi-en.web.app
Prompt: Generate a smart contract for the $RBLZ token on the Ethereum blockchain, ensuring it has no buy or sell tax as described on the Rebel Satoshi website.
Generated: DETERMINISTIC_6a90863093b9ad4e
Batch ID: 20250612_161616
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
 * @title RBLZ Token Smart Contract
 * @dev ERC20 Implementation for the Rebel Satoshi $RBLZ Token
 */
contract RBLZToken {
    // Token details
    string public name = "Rebel Satoshi";
    string public symbol = "RBLZ";
    uint8 public decimals = 18;

    // Total supply of the token
    uint256 public totalSupply;

    // Mapping to store balances
    mapping(address => uint256) private balances;

    // Mapping to store allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Ownership of the contract
    address public owner;

    // Events for logging important actions
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set initial token supply and allocate it to the deployer
     * @param _initialSupply Initial token supply in wei (smallest unit of the token)
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply;
        balances[owner] = _initialSupply;

        emit Transfer(address(0), owner, _initialSupply); // Log token creation
    }

    /**
     * @dev Function to check the balance of a given address
     * @param account Address to query the balance of
     * @return The balance of the address
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function to transfer tokens to a specific address
     * @param to Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @return Boolean indicating success or failure
     */
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Function to approve an address to spend tokens on behalf of the caller
     * @param spender Address to approve
     * @param amount Amount of tokens to approve
     * @return Boolean indicating success or failure
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Function to transfer tokens on behalf of the token owner
     * @param from Address to transfer tokens from
     * @param to Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @return Boolean indicating success or failure
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) external returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;

        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Function to check the allowance of a spender for a given owner
     * @param owner Address of the token owner
     * @param spender Address of the spender
     * @return Remaining amount the spender is allowed to spend
     */
    function allowance(
        address owner,
        address spender
    ) external view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Function to mint new tokens (restricted to owner)
     * @param account Address to allocate minted tokens to
     * @param amount Amount of tokens to mint
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Cannot mint to the zero address");

        totalSupply += amount;
        balances[account] += amount;

        emit Transfer(address(0), account, amount);
    }

    /**
     * @dev Function to burn tokens (restricted to owner)
     * @param account Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function burn(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "Cannot burn from the zero address");
        require(balances[account] >= amount, "Insufficient balance");

        totalSupply -= amount;
        balances[account] -= amount;

        emit Transfer(account, address(0), amount);
    }
}
```
