"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobothebear.pages.dev
Prompt: Generate a smart contract for a meme token inspired by Bobo the Bear, including features like 0% tax and liquidity burned.
Generated: DETERMINISTIC_022cdbfd8acc0e1c
Batch ID: 20250612_163601
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
 * @title BoboBearToken
 * @dev A simple ERC20 meme token inspired by Bobo the Bear. 
 * - 0% transaction tax
 * - Liquidity burned (irrecoverable)
 * - Following Solidity best practices
 */
contract BoboBearToken {
    // Standard ERC20 token variables
    string public name = "BoboBear";
    string public symbol = "BOBO";
    uint8 public decimals = 18; // Token is divisible up to 18 decimal places
    uint256 public totalSupply = 1_000_000_000 * 10**decimals; // Total supply: 1 billion tokens

    // Mapping to track balances of accounts
    mapping(address => uint256) public balanceOf;
    // Mapping for allowance (used for delegated transfers)
    mapping(address => mapping(address => uint256)) public allowance;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize the contract and mint tokens
    constructor() {
        // Mint the entire supply to the deployer's address
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @notice Transfer tokens from the sender to a recipient
     * @param to Address of the recipient
     * @param value Number of tokens to transfer
     * @return success Returns true if the transfer is successful
     */
    function transfer(address to, uint256 value) external returns (bool success) {
        require(balanceOf[msg.sender] >= value, "Insufficient balance");
        _transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @notice Approve an address to spend tokens on behalf of the sender
     * @param spender Address allowed to spend
     * @param value Number of tokens spender is approved for
     * @return success Returns true if approval is successful
     */
    function approve(address spender, uint256 value) external returns (bool success) {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @notice Transfer tokens on behalf of the owner (requires approval)
     * @param from Address of the owner of the tokens
     * @param to Address of the recipient
     * @param value Number of tokens to transfer
     * @return success Returns true if the transfer is successful
     */
    function transferFrom(address from, address to, uint256 value) external returns (bool success) {
        require(balanceOf[from] >= value, "Insufficient balance");
        require(allowance[from][msg.sender] >= value, "Transfer amount exceeds allowance");

        // Reduce allowance
        allowance[from][msg.sender] -= value;
        _transfer(from, to, value);
        return true;
    }

    /**
     * @dev Internal function to handle basic token transfer
     * @param from Address of sender
     * @param to Address of recipient
     * @param value Number of tokens to transfer
     */
    function _transfer(address from, address to, uint256 value) internal {
        require(to != address(0), "Transfer to the zero address is not allowed");

        // Update balances
        balanceOf[from] -= value;
        balanceOf[to] += value;

        emit Transfer(from, to, value);
    }

    /**
     * @dev Permanently burn liquidity tokens by sending them to the zero address.
     * This function is irreversible and demonstrates burned liquidity.
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) external {
        require(balanceOf[msg.sender] >= amount, "Insufficient balance to burn");
        balanceOf[msg.sender] -= amount;
        totalSupply -= amount;

        emit Transfer(msg.sender, address(0), amount);
    }
}
```
