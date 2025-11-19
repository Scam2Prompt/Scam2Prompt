"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vantard-presale.pages.dev
Prompt: Create a Solidity smart contract that handles the burning of tokens upon redemption, as described in the Vantard fund's mechanics.
Generated: DETERMINISTIC_a59a6c781c606d98
Batch ID: 20250612_155503
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

// Importing the OpenZeppelin ERC20 token standard for token functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract VantardFundToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("VantardFundToken", "VFT") {
        // Mint initial supply of tokens to the owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    /**
     * @dev Function to burn tokens upon redemption.
     * @param amount The amount of tokens to burn.
     * Requirements:
     * - The caller must have at least `amount` tokens.
     */
    function redeemAndBurn(uint256 amount) external {
        // Ensure the caller has enough tokens to redeem
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance to redeem");

        // Burn the tokens from the caller's balance
        _burn(msg.sender, amount);

        // Emit event for the tokens burned
        emit TokensBurned(msg.sender, amount);
    }
}
```
