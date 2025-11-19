"""
Generated Code Metadata:
========================
Original URL: https://czbull.com
Prompt: Write a smart contract in Solidity for a cryptocurrency token with a fixed supply of 1,000,000,000 tokens, where 100% of the liquidity pool is burned.
Generated: DETERMINISTIC_9f98e2c9c4ba1761
Batch ID: 20250622_211546
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
 * @title FixedSupplyToken
 * @dev A simple ERC20 token with a fixed supply of 1,000,000,000 tokens.
 *      100% of the liquidity pool is burned upon deployment.
 */
contract FixedSupplyToken {
    // ERC20 standard variables
    string public name = "FixedSupplyToken";
    string public symbol = "FST";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000_000 * (10 ** uint256(decimals));

    // Mapping to track balances
    mapping(address => uint256) public balanceOf;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) public allowance;

    // Events for transfer and approval
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Address of the contract deployer
    address public owner;

    /**
     * @dev Constructor initializes the token and burns the liquidity pool.
     */
    constructor() {
        owner = msg.sender;

        // Assign the total supply to the deployer
        balanceOf[owner] = totalSupply;

        // Burn the liquidity pool (100% of the supply)
        _burn(owner, totalSupply);
    }

    /**
     * @dev Internal function to handle token burning.
     * @param from Address from which tokens are burned.
     * @param value Amount of tokens to burn.
     */
    function _burn(address from, uint256 value) internal {
        require(balanceOf[from] >= value, "Insufficient balance to burn");
        balanceOf[from] -= value;
        totalSupply -= value;

        emit Transfer(from, address(0), value);
    }

    /**
     * @dev Transfer tokens to a specified address.
     * @param to The recipient address.
     * @param value The amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transfer(address to, uint256 value) public returns (bool success) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[msg.sender] >= value, "Insufficient balance");

        balanceOf[msg.sender] -= value;
        balanceOf[to] += value;

        emit Transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @dev Approve a spender to transfer tokens on behalf of the owner.
     * @param spender The address authorized to spend.
     * @param value The amount of tokens to approve.
     * @return success True if the approval is successful.
     */
    function approve(address spender, uint256 value) public returns (bool success) {
        require(spender != address(0), "Cannot approve the zero address");

        allowance[msg.sender][spender] = value;

        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param from The address to transfer tokens from.
     * @param to The recipient address.
     * @param value The amount of tokens to transfer.
     * @return success True if the transfer is successful.
     */
    function transferFrom(address from, address to, uint256 value) public returns (bool success) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balanceOf[from] >= value, "Insufficient balance");
        require(allowance[from][msg.sender] >= value, "Allowance exceeded");

        balanceOf[from] -= value;
        balanceOf[to] += value;
        allowance[from][msg.sender] -= value;

        emit Transfer(from, to, value);
        return true;
    }
}
```
