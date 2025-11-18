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

// Importing OpenZeppelin ERC20 token contract for standard functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ZushiToken
 * @dev Implementation of the ERC20 token with burning functionality
 */
contract ZushiToken is ERC20, Ownable {
    
    // Emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("ZushiToken", "ZUSHI") {
        // Minting an initial supply of tokens to the owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    /**
     * @dev Burns a specific amount of tokens from the caller's account.
     * @param amount The amount of tokens to be burned.
     */
    function burn(uint256 amount) external {
        // Ensure the amount to burn is greater than zero
        require(amount > 0, "Amount must be greater than zero");
        
        // Ensure the caller has enough tokens to burn
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the tokens
        _burn(msg.sender, amount);
        
        // Emit a TokensBurned event
        emit TokensBurned(msg.sender, amount);
    }
}
```
