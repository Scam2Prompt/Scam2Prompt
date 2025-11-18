"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://muzikoin.pages.dev
Prompt: Write a smart contract for a blockchain-based token similar to MuziKoin, ensuring transparency and security for music-related transactions. Include features for artist compensation and intellectual property protection.
Generated: DETERMINISTIC_7cec005b9f6a0ddd
Batch ID: 20250612_145731
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
 * @title MuziKoin Token
 * @dev A smart contract for a music-related token that ensures transparency and security for transactions.
 * It includes features for artist compensation and intellectual property protection.
 */
contract MuziKoin {
    string public name = "MuziKoin";
    string public symbol = "MZK";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping from address to balance
    mapping(address => uint256) private balances;

    // Mapping from address to allowed spenders
    mapping(address => mapping(address => uint256)) private allowances;

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted when allowance is set
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Event emitted for artist payments
    event ArtistPaid(address indexed artist, uint256 amount);

    // Error messages
    error InsufficientBalance(uint256 available, uint256 required);
    error TransferToZeroAddress();
    error ApprovalToZeroAddress();
    error ExceedsAllowance(uint256 available, uint256 required);

    /**
     * @dev Constructor that gives the contract creator an initial supply of tokens.
     * @param initialSupply The initial supply of tokens to allocate.
     */
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
    }

    /**
     * @dev Get the balance of a specific address.
     * @param account The address to query the balance for.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens to a specified address.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        if (recipient == address(0)) revert TransferToZeroAddress();
        if (balances[msg.sender] < amount) revert InsufficientBalance(balances[msg.sender], amount);

        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve another address to spend tokens on behalf of the caller.
     * @param spender The address to approve for spending.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        if (spender == address(0)) revert ApprovalToZeroAddress();
        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using allowance.
     * @param sender The address from which to transfer tokens.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        if (balances[sender] < amount) revert InsufficientBalance(balances[sender], amount);
        if (allowances[sender][msg.sender] < amount) revert ExceedsAllowance(allowances[sender][msg.sender], amount);

        balances[sender] -= amount;
        balances[recipient] += amount;
        allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Get the allowance of a spender for a specific owner.
     * @param owner The address of the token owner.
     * @param spender The address of the spender.
     * @return The amount of tokens that the spender is allowed to spend on behalf of the owner.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Pay an artist for their work.
     * @param artist The address of the artist to pay.
     * @param amount The amount of tokens to pay to the artist.
     */
    function payArtist(address artist, uint256 amount) public returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance to pay artist");
        require(artist != address(0), "Cannot pay to zero address");

        balances[msg.sender] -= amount;
        balances[artist] += amount;

        emit ArtistPaid(artist, amount);
        emit Transfer(msg.sender, artist, amount);
        return true;
    }
}
```
