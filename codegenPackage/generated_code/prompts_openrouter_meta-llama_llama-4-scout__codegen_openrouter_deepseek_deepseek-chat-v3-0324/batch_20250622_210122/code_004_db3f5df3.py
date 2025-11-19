"""
Generated Code Metadata:
========================
Original URL: https://ketoken.com
Prompt: "Create a simple blockchain-based loyalty program using Solidity and Ethereum, inspired by KeToken's use case for customer retention and employee incentives."
Generated: DETERMINISTIC_db3f5df31b754f2c
Batch ID: 20250622_210122
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
 * @title LoyaltyToken
 * @dev A simple ERC20-based loyalty program token for customer retention and employee incentives
 */
contract LoyaltyToken {
    string public constant name = "LoyaltyToken";
    string public constant symbol = "LTK";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    address public owner;
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event TokensMinted(address indexed to, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    constructor(uint256 initialSupply) {
        owner = msg.sender;
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Transfer ownership of the contract to a new account
     * @param newOwner The address to transfer ownership to
     */
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Get the token balance of a specified address
     * @param account The address to query the balance of
     * @return The balance of the specified address
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens to a specified address
     * @param recipient The address to transfer to
     * @param amount The amount to be transferred
     * @return success Boolean indicating whether the operation succeeded
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve the passed address to spend the specified amount of tokens on behalf of msg.sender
     * @param spender The address which will spend the funds
     * @param amount The amount of tokens to be spent
     * @return success Boolean indicating whether the operation succeeded
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another
     * @param sender The address which you want to send tokens from
     * @param recipient The address which you want to transfer to
     * @param amount The amount of tokens to be transferred
     * @return success Boolean indicating whether the operation succeeded
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, allowances[sender][msg.sender] - amount);
        return true;
    }

    /**
     * @dev Function to mint tokens
     * @param to The address that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Function to burn tokens
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Internal function to transfer tokens
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Insufficient balance");

        balances[sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Internal function to mint tokens
     */
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "Mint to the zero address");

        totalSupply += amount;
        balances[account] += amount;
        emit Transfer(address(0), account, amount);
        emit TokensMinted(account, amount);
    }

    /**
     * @dev Internal function to burn tokens
     */
    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "Burn from the zero address");
        require(balances[account] >= amount, "Insufficient balance");

        balances[account] -= amount;
        totalSupply -= amount;
        emit Transfer(account, address(0), amount);
        emit TokensBurned(account, amount);
    }

    /**
     * @dev Internal function to approve token spending
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "Approve from the zero address");
        require(spender != address(0), "Approve to the zero address");

        allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Function to check remaining allowance
     * @param owner The address which owns the funds
     * @param spender The address which will spend the funds
     * @return remaining The remaining allowance
     */
    function allowance(address owner, address spender) public view returns (uint256 remaining) {
        return allowances[owner][spender];
    }
}
```
