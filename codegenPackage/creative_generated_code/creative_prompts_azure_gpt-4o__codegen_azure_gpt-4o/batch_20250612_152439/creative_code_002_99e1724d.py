"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefxyz.pages.dev
Prompt: Create a Solidity function that implements a token burn mechanism for a deflationary token like BEEF Coin, ensuring the total supply decreases over time.
Generated: DETERMINISTIC_99e1724d113a2157
Batch ID: 20250612_152439
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
 * @title DeflationaryToken
 * @dev This contract implements a basic ERC20 token with a burn mechanism to reduce total supply over time.
 */
contract DeflationaryToken {
    // Token metadata
    string public name = "BEEF Coin";
    string public symbol = "BEEF";
    uint8 public decimals = 18;

    // Total supply of tokens
    uint256 public totalSupply;

    // Mapping of balances for token holders
    mapping(address => uint256) public balanceOf;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Burn(address indexed burner, uint256 value);

    /**
     * @dev Constructor to initialize the token with a fixed supply.
     * @param _initialSupply The initial supply of the token in smallest units (e.g., wei for 18 decimals).
     */
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply;
        balanceOf[msg.sender] = _initialSupply; // Assign all tokens to the deployer.
        emit Transfer(address(0), msg.sender, _initialSupply);
    }

    /**
     * @dev Internal function to transfer tokens from one address to another.
     * @param _from The address sending the tokens.
     * @param _to The address receiving the tokens.
     * @param _value The amount of tokens to transfer.
     */
    function _transfer(
        address _from,
        address _to,
        uint256 _value
    ) internal {
        require(_to != address(0), "Cannot transfer to the zero address"); // Prevent transfer to zero address.
        require(balanceOf[_from] >= _value, "Insufficient balance"); // Check sender's balance.
        balanceOf[_from] -= _value; // Deduct from sender.
        balanceOf[_to] += _value; // Add to recipient.
        emit Transfer(_from, _to, _value);
    }

    /**
     * @dev Public function to transfer tokens to another address.
     * @param _to The address receiving the tokens.
     * @param _value The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {
        _transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Public function to burn tokens and reduce the total supply.
     * @param _value The amount of tokens to burn.
     */
    function burn(uint256 _value) public returns (bool success) {
        require(balanceOf[msg.sender] >= _value, "Insufficient balance to burn"); // Check if the sender has enough tokens.
        balanceOf[msg.sender] -= _value; // Deduct tokens from the sender's balance.
        totalSupply -= _value; // Reduce the total supply.
        emit Burn(msg.sender, _value); // Emit burn event.
        emit Transfer(msg.sender, address(0), _value); // Emit transfer to the zero address for transparency.
        return true;
    }
}
```
