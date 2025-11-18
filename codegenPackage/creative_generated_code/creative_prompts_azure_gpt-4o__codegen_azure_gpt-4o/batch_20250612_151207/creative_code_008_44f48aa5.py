"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Write a function in Solidity to burn tokens and update the circulating supply, similar to the tokenomics described for Blockchain Bets.
Generated: DETERMINISTIC_44f48aa52c57b1fd
Batch ID: 20250612_151207
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
 * @title TokenBurnable
 * @dev A smart contract to burn tokens and update circulating supply.
 */
contract TokenBurnable {
    // State variables
    string public name = "Blockchain Bets Token";
    string public symbol = "BBT";
    uint8 public decimals = 18;
    uint256 public totalSupply; // The total supply of tokens
    uint256 public circulatingSupply; // The circulating supply of tokens

    // Mapping to track balances of addresses
    mapping(address => uint256) public balances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Burn(address indexed burner, uint256 value);

    // Constructor to initialize token supply
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10**uint256(decimals));
        circulatingSupply = totalSupply;
        balances[msg.sender] = totalSupply;
    }

    /**
     * @dev Modifier to check if the caller has enough tokens to burn.
     * @param _amount The amount of tokens to burn.
     */
    modifier hasEnoughTokens(uint256 _amount) {
        require(balances[msg.sender] >= _amount, "Insufficient balance to burn tokens");
        _;
    }

    /**
     * @dev Burns a specific amount of tokens and updates the circulating supply.
     * @param _amount The amount of tokens to burn.
     */
    function burn(uint256 _amount) external hasEnoughTokens(_amount) {
        // Ensure the amount is greater than zero
        require(_amount > 0, "Amount to burn must be greater than zero");

        // Deduct the tokens from the caller's balance
        balances[msg.sender] -= _amount;

        // Update the circulating supply
        circulatingSupply -= _amount;

        // Emit a burn event
        emit Burn(msg.sender, _amount);
    }

    /**
     * @dev Transfers tokens from the caller to another address.
     * @param _to The recipient address.
     * @param _amount The amount of tokens to transfer.
     */
    function transfer(address _to, uint256 _amount) external {
        // Ensure the sender has enough balance
        require(balances[msg.sender] >= _amount, "Insufficient balance to transfer");
        require(_to != address(0), "Cannot transfer to the zero address");
        require(_amount > 0, "Transfer amount must be greater than zero");

        // Update balances
        balances[msg.sender] -= _amount;
        balances[_to] += _amount;

        // Emit a transfer event
        emit Transfer(msg.sender, _to, _amount);
    }

    /**
     * @dev Returns the balance of a specific account.
     * @param _account The address of the account.
     * @return The balance of the account.
     */
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }
}
```
