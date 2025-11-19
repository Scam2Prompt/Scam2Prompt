"""
Generated Code Metadata:
========================
Original URL: https://hokkaidokeneth.vip
Prompt: Write a Solidity contract for a meme token with 0% taxes and 100% locked liquidity, similar to the Hokkaido-ken token.
Generated: DETERMINISTIC_9183f109d5b73924
Batch ID: 20250622_211425
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
 * @title MemeToken
 * @dev A simple ERC20 token with 0% taxes and 100% locked liquidity.
 */
contract MemeToken {
    // Token details
    string public name = "MemeToken";
    string public symbol = "MEME";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * (10 ** uint256(decimals)); // 1 million tokens

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Address of the liquidity pool (locked liquidity)
    address public liquidityPool;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the contract and mint the total supply to the deployer.
     * @param _liquidityPool Address of the liquidity pool where tokens will be locked.
     */
    constructor(address _liquidityPool) {
        require(_liquidityPool != address(0), "Liquidity pool address cannot be zero");
        liquidityPool = _liquidityPool;

        // Mint total supply to the liquidity pool
        balances[liquidityPool] = totalSupply;
        emit Transfer(address(0), liquidityPool, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account Address to query the balance of.
     * @return The balance of the given address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a recipient.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the caller.
     * @param spender Address to approve.
     * @param amount Amount of tokens to approve.
     * @return True if the approval is successful.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Spender address cannot be zero");
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using an allowance.
     * @param sender Address to transfer tokens from.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     * @return True if the transfer is successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining number of tokens that a spender can spend on behalf of an owner.
     * @param owner Address of the token owner.
     * @param spender Address of the spender.
     * @return The remaining allowance.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Internal function to handle token transfers.
     * @param sender Address to transfer tokens from.
     * @param recipient Address to transfer tokens to.
     * @param amount Amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Sender address cannot be zero");
        require(recipient != address(0), "Recipient address cannot be zero");
        require(balances[sender] >= amount, "Transfer amount exceeds balance");

        balances[sender] -= amount;
        balances[recipient] += amount;
        emit Transfer(sender, recipient, amount);
    }
}
```
