"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom237.com
Prompt: Develop a smart contract in Solidity for a meme coin similar to PHANTOM237 ($PHTM), including functionality for tracking holders and limiting max supply.
Generated: DETERMINISTIC_6f6eec2e21bdd980
Batch ID: 20250612_155057
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
 * @title MemeCoin
 * @dev A simple implementation of a meme coin with holder tracking and max supply limit.
 */
contract MemeCoin {
    // Token details
    string public name = "Phantom237";
    string public symbol = "PHTM";
    uint8 public decimals = 18;
    uint256 public maxSupply = 1000000 * (10 ** uint256(decimals)); // Max supply is 1,000,000 tokens
    uint256 public totalSupply;

    // Holder tracking
    mapping(address => uint256) private balances;
    mapping(address => bool) private holders;
    address[] private holderList;

    // Allowance mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor
    constructor() {
        totalSupply = 0; // Starts with zero supply
    }

    /**
     * @dev Internal function to track holders. Adds address to holderList if it's the first time.
     * @param account The address of the holder.
     */
    function _trackHolder(address account) internal {
        if (!holders[account] && balances[account] > 0) {
            holders[account] = true;
            holderList.push(account);
        }
    }

    /**
     * @dev Transfers tokens from the sender to the recipient.
     * @param recipient The address of the recipient.
     * @param amount The amount to transfer.
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Transfer to zero address not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Adjust balances
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        // Track holders
        _trackHolder(recipient);

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Mints new tokens. Can only mint up to maxSupply.
     * @param recipient The address to receive the minted tokens.
     * @param amount The amount to mint.
     */
    function mint(address recipient, uint256 amount) external returns (bool) {
        require(totalSupply + amount <= maxSupply, "Exceeds max supply");
        require(recipient != address(0), "Mint to zero address not allowed");

        // Adjust balances and total supply
        balances[recipient] += amount;
        totalSupply += amount;

        // Track holders
        _trackHolder(recipient);

        emit Transfer(address(0), recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to transfer tokens on behalf of the sender.
     * @param spender The address of the spender.
     * @param amount The amount to approve.
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        require(spender != address(0), "Approve to zero address not allowed");

        // Set allowance
        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using the allowance mechanism.
     * @param sender The address of the sender.
     * @param recipient The address of the recipient.
     * @param amount The amount to transfer.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool) {
        require(sender != address(0), "Transfer from zero address not allowed");
        require(recipient != address(0), "Transfer to zero address not allowed");
        require(balances[sender] >= amount, "Insufficient balance");
        require(allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        // Adjust balances and allowance
        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        // Track holders
        _trackHolder(recipient);

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Returns the current allowance for a spender given an owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     */
    function allowance(address owner, address spender) external view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Returns the list of holders.
     */
    function getHolders() external view returns (address[] memory) {
        return holderList;
    }
}
```
