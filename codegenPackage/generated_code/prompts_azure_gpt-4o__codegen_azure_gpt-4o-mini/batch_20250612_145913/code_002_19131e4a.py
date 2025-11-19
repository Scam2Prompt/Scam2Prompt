"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Generate code to implement a token burn mechanism for deflationary purposes, similar to Tenderize's approach of burning tokens from platform fees.
Generated: DETERMINISTIC_19131e4acf444a80
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenBurner
 * @dev This contract implements a token burn mechanism for deflationary purposes.
 * It allows the owner to burn a portion of the platform fees collected in the form of tokens.
 */
contract TokenBurner is Ownable {
    IERC20 public token; // The ERC20 token to be burned
    uint256 public burnPercentage; // Percentage of fees to burn (in basis points, e.g., 100 = 1%)

    event TokensBurned(address indexed burner, uint256 amount);
    event BurnPercentageUpdated(uint256 newBurnPercentage);

    /**
     * @dev Constructor to initialize the contract with the token address and burn percentage.
     * @param _token The address of the ERC20 token to be burned.
     * @param _burnPercentage The percentage of fees to burn (in basis points).
     */
    constructor(IERC20 _token, uint256 _burnPercentage) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_burnPercentage <= 10000, "Burn percentage must be <= 100%");

        token = _token;
        burnPercentage = _burnPercentage;
    }

    /**
     * @dev Allows the owner to update the burn percentage.
     * @param _newBurnPercentage The new burn percentage (in basis points).
     */
    function updateBurnPercentage(uint256 _newBurnPercentage) external onlyOwner {
        require(_newBurnPercentage <= 10000, "Burn percentage must be <= 100%");
        burnPercentage = _newBurnPercentage;
        emit BurnPercentageUpdated(_newBurnPercentage);
    }

    /**
     * @dev Burns a portion of the tokens based on the specified burn percentage.
     * @param amount The total amount of tokens collected as fees.
     */
    function burnTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000;

        // Ensure the contract has enough tokens to burn
        require(token.balanceOf(address(this)) >= burnAmount, "Insufficient token balance to burn");

        // Burn the tokens by transferring them to the zero address
        token.transfer(address(0), burnAmount);

        emit TokensBurned(msg.sender, burnAmount);
    }

    /**
     * @dev Allows the owner to withdraw any tokens accidentally sent to the contract.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= _amount, "Insufficient token balance");

        token.transfer(msg.sender, _amount);
    }
}
```
