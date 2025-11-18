"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-coincreator.pages.dev
Prompt: Write a Solidity function to handle token ownership and ensure 100% ownership for the creator, based on the features highlighted on eth-coincreator.pages.dev.
Generated: DETERMINISTIC_ff72fd298312b38e
Batch ID: 20250612_154321
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
 * @title TokenOwnership
 * @dev This contract handles token ownership and ensures the creator owns 100% of the tokens.
 */
contract TokenOwnership {
    address public creator;
    uint256 public totalSupply;
    mapping(address => uint256) public balances;

    /**
     * @dev Constructor that initializes the token and assigns all tokens to the creator.
     * @param _totalSupply The total supply of tokens.
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than 0");

        creator = msg.sender; // Set the creator to the contract deployer
        totalSupply = _totalSupply; // Initialize the total supply
        balances[creator] = _totalSupply; // Assign the entire supply to the creator
    }

    /**
     * @dev Returns the balance of the specified address.
     * @param _account The address to query the balance of.
     * @return The balance of the specified address.
     */
    function balanceOf(address _account) public view returns (uint256) {
        return balances[_account];
    }

    /**
     * @dev Transfers tokens to a specified address.
     * @param _to The address to transfer tokens to.
     * @param _amount The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _amount) external {
        require(_to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Safely transfer tokens
        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        emit Transfer(msg.sender, _to, _amount);
    }

    /**
     * @dev Emitted when tokens are transferred from one address to another.
     * @param from The address transferring the tokens.
     * @param to The address receiving the tokens.
     * @param value The amount of tokens transferred.
     */
    event Transfer(address indexed from, address indexed to, uint256 value);
}
```
