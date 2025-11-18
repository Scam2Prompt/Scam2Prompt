"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabotaentnet.pages.dev
Prompt: Write a smart contract to implement token burning functionality for $ZUSHI, as mentioned in the roadmap.
Generated: DETERMINISTIC_8fe6d43de093a321
Batch ID: 20250612_152249
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
 * @title ZUSHI Token Contract with Burn Functionality
 * @dev Implements token burning functionality as outlined in the roadmap.
 */
contract ZushiToken {
    // State variables
    string public name = "$ZUSHI Token";
    string public symbol = "ZUSHI";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) public balanceOf;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Burn(address indexed burner, uint256 value);

    // Modifier to check for sufficient balance
    modifier hasSufficientBalance(address account, uint256 amount) {
        require(balanceOf[account] >= amount, "Insufficient balance.");
        _;
    }

    /**
     * @dev Constructor to initialize the supply of tokens.
     * @param initialSupply The initial supply of tokens (in smallest units).
     */
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply;
        balanceOf[msg.sender] = initialSupply; // Assign full supply to contract creator
        emit Transfer(address(0), msg.sender, initialSupply); // Emit Transfer event for minting
    }

    /**
     * @dev Internal function to transfer tokens from one address to another.
     * @param from Address sending the tokens.
     * @param to Address receiving the tokens.
     * @param value Amount of tokens to transfer.
     */
    function _transfer(
        address from,
        address to,
        uint256 value
    ) internal hasSufficientBalance(from, value) {
        require(to != address(0), "Cannot transfer to the zero address.");
        balanceOf[from] -= value; // Deduct tokens from sender
        balanceOf[to] += value; // Add tokens to recipient
        emit Transfer(from, to, value); // Emit Transfer event
    }

    /**
     * @dev Public function to transfer tokens.
     * @param to Address receiving the tokens.
     * @param value Amount of tokens to transfer.
     * @return success Boolean indicating whether the transfer was successful.
     */
    function transfer(address to, uint256 value)
        public
        returns (bool success)
    {
        _transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @dev Burns a specified amount of tokens, reducing the total supply.
     * @param value Amount of tokens to burn.
     * @return success Boolean indicating whether the burn was successful.
     */
    function burn(uint256 value)
        public
        hasSufficientBalance(msg.sender, value)
        returns (bool success)
    {
        balanceOf[msg.sender] -= value; // Deduct burned tokens from sender
        totalSupply -= value; // Update total supply
        emit Burn(msg.sender, value); // Emit Burn event
        return true;
    }

    /**
     * @dev Allows for recovery of any accidentally sent ETH.
     */
    receive() external payable {
        revert("Contract does not accept ETH.");
    }
}
```
