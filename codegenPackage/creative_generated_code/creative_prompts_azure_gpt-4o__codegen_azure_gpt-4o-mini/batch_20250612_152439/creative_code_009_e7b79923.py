"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eveyry.pages.dev
Prompt: Write a Solidity contract to manage token burning (10% of payouts) as part of Everyworld's ecosystem economic equilibrium.
Generated: DETERMINISTIC_e7b79923ca064291
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

// Importing OpenZeppelin's ERC20 interface and Ownable for ownership control
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenBurnManager
 * @dev This contract manages token burning as part of the Everyworld ecosystem.
 *      It burns 10% of every payout to maintain economic equilibrium.
 */
contract TokenBurnManager is Ownable {
    IERC20 public token;  // The ERC20 token that will be managed for burning

    // Event to log the burn operation
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor to set the token address.
     * @param _token Address of the ERC20 token to manage.
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Burns 10% of the specified amount, transferring it to the zero address.
     * @param amount The amount to process the burn from.
     */
    function burnTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        uint256 burnAmount = (amount * 10) / 100; // Calculate 10% to burn

        // Ensure the contract has enough tokens to burn
        uint256 tokenBalance = token.balanceOf(address(this));
        require(tokenBalance >= burnAmount, "Not enough tokens to burn");

        // Transfer the tokens to the zero address (burning)
        token.transfer(address(0), burnAmount);

        // Emit an event for the burn
        emit TokensBurned(msg.sender, burnAmount);
    }

    /**
     * @dev Withdraw tokens from the contract (only owner can withdraw).
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        uint256 tokenBalance = token.balanceOf(address(this));
        require(tokenBalance >= amount, "Not enough tokens to withdraw");

        // Transfer tokens to the owner
        token.transfer(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to set a new token.
     * @param _token New token address.
     */
    function setToken(IERC20 _token) external onlyOwner {
        require(address(_token) != address(0), "New token address cannot be zero");
        token = _token;
    }
}
```
