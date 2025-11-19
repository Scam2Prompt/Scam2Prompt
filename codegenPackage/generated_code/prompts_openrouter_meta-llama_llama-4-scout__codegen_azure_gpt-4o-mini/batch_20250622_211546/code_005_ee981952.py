"""
Generated Code Metadata:
========================
Original URL: https://dancingtriangle.website
Prompt: Write a Solidity smart contract code to burn a specific percentage of $triangle cryptocurrency supply, similar to the 6.9% market-bought and burned tokens mentioned on the webpage.
Generated: DETERMINISTIC_ee981952d0fc22f3
Batch ID: 20250622_211546
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TriangleTokenBurner
 * @dev A contract to burn a specific percentage of the Triangle cryptocurrency supply
 */
contract TriangleTokenBurner is Ownable {
    // The ERC20 token contract
    IERC20 public triangleToken;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @dev Constructor to set the Triangle token address
     * @param _triangleToken Address of the Triangle ERC20 token
     */
    constructor(address _triangleToken) {
        require(_triangleToken != address(0), "Invalid token address");
        triangleToken = IERC20(_triangleToken);
    }

    /**
     * @dev Function to burn a specific percentage of the token supply
     * @param percentage The percentage of the total supply to burn (in basis points, e.g., 690 for 6.9%)
     */
    function burnTokens(uint256 percentage) external onlyOwner {
        require(percentage > 0 && percentage <= 10000, "Percentage must be between 0 and 10000 basis points");

        // Get the total supply of the token
        uint256 totalSupply = triangleToken.totalSupply();
        // Calculate the amount to burn
        uint256 amountToBurn = (totalSupply * percentage) / 10000;

        // Ensure the contract has enough tokens to burn
        require(triangleToken.balanceOf(address(this)) >= amountToBurn, "Insufficient tokens to burn");

        // Transfer tokens from the contract to the zero address (burning)
        triangleToken.transfer(address(0), amountToBurn);

        // Emit the burn event
        emit TokensBurned(msg.sender, amountToBurn);
    }

    /**
     * @dev Function to withdraw any ERC20 tokens accidentally sent to this contract
     * @param token Address of the ERC20 token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(address(token) != address(triangleToken), "Cannot withdraw Triangle tokens");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        token.transfer(msg.sender, amount);
    }
}
```
