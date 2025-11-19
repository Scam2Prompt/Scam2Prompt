"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://czbull.com
Prompt: Create a smart contract in Solidity for a token similar to $WINDY, including features like a burn mechanism and a fixed supply of 1,000,000,000 tokens.
Generated: DETERMINISTIC_5f8b9898bbfbcc20
Batch ID: 20250612_155903
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title WindyToken
 * @dev ERC20 Token with a burn mechanism and a fixed supply of 1,000,000,000 tokens
 */
contract WindyToken is ERC20, Ownable {
    // Total supply of the token
    uint256 private constant _totalSupply = 1_000_000_000 * 10 ** 18; // 1 billion tokens with 18 decimals

    // Event for burn activity
    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @dev Constructor that sets the token name and symbol
     */
    constructor() ERC20("Windy Token", "WINDY") {
        _mint(msg.sender, _totalSupply); // Mint the total supply to the contract deployer
    }

    /**
     * @dev Function to burn tokens from caller's account
     * @param amount The amount of tokens to be burned
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount); // Burn the tokens
        emit TokensBurned(msg.sender, amount); // Emit burn event
    }

    /**
     * @dev Function to retrieve the total supply of the tokens
     * @return The total supply of the tokens
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply; // Return fixed total supply
    }
}
```
