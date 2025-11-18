"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheemspet.web.app
Prompt: Write code to implement a token burning mechanism similar to $Cheems, where users can burn tokens to reduce the circulating supply. Use Solidity for the smart contract.
Generated: DETERMINISTIC_88ca9dd0a43683c8
Batch ID: 20250612_153812
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
 * @title CheemsToken
 * @dev A simple ERC20-compatible token with a burn mechanism
 */
contract CheemsToken {
    // ERC20 token standard variables
    string public name = "CheemsToken";
    string public symbol = "CHEEMS";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping for balances
    mapping(address => uint256) private balances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Burn(address indexed burner, uint256 value);

    // Constructor to initialize total supply and assign all tokens to the deployer
    constructor(uint256 _initialSupply) {
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    // Function to check balance of an account
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    // Internal function to transfer tokens
    function _transfer(address from, address to, uint256 value) internal {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[from] >= value, "Insufficient balance");

        balances[from] -= value;
        balances[to] += value;
        emit Transfer(from, to, value);
    }

    // Public function for users to transfer tokens
    function transfer(address to, uint256 value) public returns (bool) {
        _transfer(msg.sender, to, value);
        return true;
    }

    // Function to burn tokens and reduce the total supply
    function burn(uint256 value) public returns (bool) {
        require(balances[msg.sender] >= value, "Insufficient balance to burn");

        // Deduct the tokens from the caller's balance
        balances[msg.sender] -= value;

        // Reduce the total supply
        totalSupply -= value;

        emit Burn(msg.sender, value);
        return true;
    }
}
```
