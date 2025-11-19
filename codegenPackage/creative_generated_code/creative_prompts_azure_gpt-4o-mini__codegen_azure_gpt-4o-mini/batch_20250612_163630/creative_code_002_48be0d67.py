"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dripdrip.pages.dev
Prompt: Create a Solidity contract that implements a burn mechanism for the $DRIP token, considering the 33% burnt liquidity mentioned on the site.
Generated: DETERMINISTIC_48be0d6753b4080e
Batch ID: 20250612_163630
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

contract DripToken is ERC20, Ownable {
    // Event to log the burn actions
    event TokensBurned(address indexed burner, uint256 amount);

    // Percentage of tokens to be burned from liquidity (represented in basis points)
    uint256 public constant BURN_PERCENTAGE = 3300; // 33% represented in basis points (10000 = 100%)

    // Constructor to initialize the token
    constructor(uint256 initialSupply) ERC20("DripToken", "DRIP") {
        // Mint the initial supply to the deployer
        _mint(msg.sender, initialSupply);
    }

    /**
     * @notice Function to burn a specified amount of tokens
     * @param amount The amount of tokens to be burnt
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Calculate the amount to be burned based on the specified percentage
        uint256 burnAmount = (amount * BURN_PERCENTAGE) / 10000;

        // Perform the burn operation
        _burn(msg.sender, burnAmount);

        // Emit the burn event
        emit TokensBurned(msg.sender, burnAmount);
    }

    /**
     * @notice Function to retrieve the current burn percentage
     * @return The current burn percentage in basis points
     */
    function getBurnPercentage() external pure returns (uint256) {
        return BURN_PERCENTAGE;
    }
}
```
