"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lingoclaims.pages.dev
Prompt: Create a smart contract in Solidity that implements a utility token similar to Lingo, ensuring compliance with non-security token standards.
Generated: DETERMINISTIC_b70c44c84b0f7bfa
Batch ID: 20250612_151232
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
 * @title UtilityToken
 * @dev Implements an ERC-20 compliant utility token similar to Lingo.
 * This contract ensures compliance with non-security token standards.
 */
contract UtilityToken {
    // Token details
    string public name = "UtilityToken";
    string public symbol = "UTK";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the total supply
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than zero");
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply; // Assign all tokens to the contract deployer
        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    /**
     * @dev Returns the balance of a specific address.
     * @param account The address to query the balance of.
     * @return The balance of the given address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param recipient The address to transfer to.
     * @param amount The amount to be transferred.
     * @return A boolean indicating whether the operation succeeded.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance for transfer");

        balances[msg.sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the caller.
     * @param spender The address authorized to spend.
     * @param amount The amount to be approved.
     * @return A boolean indicating whether the operation succeeded.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");

        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param sender The address from which tokens are transferred.
     * @param recipient The address to transfer to.
     * @param amount The amount to be transferred.
     * @return A boolean indicating whether the operation succeeded.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(balances[sender] >= amount, "Insufficient balance for transfer");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance of a spender for a given owner.
     * @param owner The address which owns the tokens.
     * @param spender The address authorized to spend the tokens.
     * @return The remaining allowance for the spender.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Allows the owner to burn tokens, reducing total supply.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(balances[msg.sender] >= amount, "Insufficient balance to burn");
        balances[msg.sender] -= amount;
        totalSupply -= amount;
        emit Transfer(msg.sender, address(0), amount);
    }

    /**
     * @dev Allows the owner to mint new tokens, increasing total supply.
     * @param amount The amount of tokens to mint.
     */
    function mint(uint256 amount) external {
        require(amount > 0, "Minting amount must be greater than zero");
        balances[msg.sender] += amount;
        totalSupply += amount;
        emit Transfer(address(0), msg.sender, amount);
    }
}
```
