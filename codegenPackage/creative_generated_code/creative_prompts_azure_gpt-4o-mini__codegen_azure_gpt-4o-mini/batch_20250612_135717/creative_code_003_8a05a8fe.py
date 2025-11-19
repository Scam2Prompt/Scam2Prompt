"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apedcoin.com
Prompt: Develop a Solidity function to implement the liquidity burn feature mentioned in the APED roadmap.
Generated: DETERMINISTIC_8a05a8feba8e3206
Batch ID: 20250612_135717
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LiquidityBurn
 * @dev Contract to implement liquidity burn feature
 */
contract LiquidityBurn is Ownable {
    IERC20 public token; // The ERC20 token to burn
    uint256 public burnRate; // Percentage to burn (in basis points, e.g., 100 = 1%)

    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Sets the token and burn rate.
     * @param _token Address of the ERC20 token to be burned.
     * @param _burnRate The burn rate as a percentage (in basis points).
     */
    constructor(IERC20 _token, uint256 _burnRate) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_burnRate <= 10000, "Burn rate must be <= 100%");

        token = _token;
        burnRate = _burnRate;
    }

    /**
     * @dev Burns a specified amount of tokens from the sender's balance.
     * @param amount The amount of tokens to burn.
     */
    function burnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Calculate the amount to burn based on the burn rate
        uint256 amountToBurn = (amount * burnRate) / 10000;

        // Transfer tokens from the sender to the contract for burning
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Burn the tokens by sending them to the zero address
        _burnTokens(amountToBurn);

        emit TokensBurned(msg.sender, amountToBurn);
    }

    /**
     * @dev Internal function to burn tokens by transferring to the zero address.
     * @param amount The amount of tokens to burn.
     */
    function _burnTokens(uint256 amount) internal {
        require(amount > 0, "Burn amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance in contract for burn");

        // Transfer tokens to the zero address (effectively burning them)
        token.transfer(address(0), amount);
    }

    /**
     * @dev Allows the owner to update the burn rate.
     * @param newBurnRate The new burn rate as a percentage (in basis points).
     */
    function setBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= 10000, "Burn rate must be <= 100%");
        burnRate = newBurnRate;
    }
}
```
