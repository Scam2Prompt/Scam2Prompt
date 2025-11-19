"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe2024.space
Prompt: Generate a smart contract in Solidity for a token similar to PEPE 2024, using the contract address 0xeb429fb576efe6e36a916a94051b18036e532c7d.
Generated: DETERMINISTIC_642a05ba45453fb1
Batch ID: 20250612_160507
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
 * @title PEPE2024 Token Contract
 * @dev ERC-20 token implementation for PEPE-like token
 */
contract PEPE2024Token {
    // Token metadata
    string public constant name = "PEPE2024";
    string public constant symbol = "PEPE2024";
    uint8 public constant decimals = 18;

    // Total token supply
    uint256 public totalSupply;

    // Address of the contract owner
    address public owner;

    // Mapping to store balances
    mapping(address => uint256) private balances;

    // Mapping for allowance (spender => amount)
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Modifier to restrict function access to owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "PEPE2024Token: Caller is not the owner");
        _;
    }

    /**
     * @dev Contract constructor that sets the total supply and allocates to the owner
     */
    constructor() {
        owner = 0xeb429fb576EFE6E36A916a94051B18036e532C7D; // Preset owner address
        totalSupply = 1_000_000_000 * (10 ** uint256(decimals)); // 1 billion tokens
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply); // Emit transfer from the zero address
    }

    /**
     * @dev Function to check the balance of an account
     * @param account Address of the account
     * @return Balance of the account
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens to a specified address
     * @param recipient Address to transfer to
     * @param amount Amount of tokens to transfer
     * @return Success Boolean indicating success of transfer
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        require(recipient != address(0), "PEPE2024Token: Transfer to the zero address");
        require(balances[msg.sender] >= amount, "PEPE2024Token: Insufficient balance");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);

        return true;
    }

    /**
     * @dev Approve a spender to use a specified amount of tokens
     * @param spender Address of the spender
     * @param amount Amount of tokens to approve
     * @return Success Boolean indicating success of approval
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "PEPE2024Token: Approve to the zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @dev Check the allowance for a spender from an owner
     * @param owner Address of the owner
     * @param spender Address of the spender
     * @return Remaining allowance
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Transfer tokens from one address to another using allowance
     * @param sender Address of the sender
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     * @return Success Boolean indicating success of transfer
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(sender != address(0), "PEPE2024Token: Transfer from the zero address");
        require(recipient != address(0), "PEPE2024Token: Transfer to the zero address");
        require(balances[sender] >= amount, "PEPE2024Token: Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "PEPE2024Token: Transfer amount exceeds allowance");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);

        return true;
    }

    /**
     * @dev Mint new tokens and add to total supply
     * @param amount Amount of tokens to mint
     */
    function mint(uint256 amount) public onlyOwner {
        require(amount > 0, "PEPE2024Token: Mint amount must be greater than 0");
        
        totalSupply += amount;
        balances[owner] += amount;

        emit Transfer(address(0), owner, amount);
    }

    /**
     * @dev Burn tokens and reduce total supply
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public onlyOwner {
        require(amount > 0, "PEPE2024Token: Burn amount must be greater than 0");
        require(balances[owner] >= amount, "PEPE2024Token: Insufficient balance to burn");

        totalSupply -= amount;
        balances[owner] -= amount;

        emit Transfer(owner, address(0), amount);
    }
}
```
