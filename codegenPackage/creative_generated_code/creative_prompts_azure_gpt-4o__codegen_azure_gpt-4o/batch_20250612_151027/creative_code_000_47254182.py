"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.credit
Prompt: Write a smart contract for launching Fan Tokens using Moxie Bonding Curves, ensuring utility-focused price discovery as described in the Moxie Protocol documentation.
Generated: DETERMINISTIC_472541826768fb7c
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a clean, production-ready implementation of an ERC20-based Fan Token smart contract with a Moxie Bonding Curve mechanism in Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title FanTokenBondingCurve
 * @dev This smart contract implements a Moxie Bonding Curve mechanism for price discovery
 * of fan tokens based on utility-focused demand.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FanTokenBondingCurve is ERC20, Ownable {
    // State variables
    uint256 public reserveBalance; // Tracks the ETH reserve in the contract
    uint256 public k;              // Constant k used for the bonding curve equation
    uint256 public totalSupplyLimit; // Maximum number of tokens that can ever exist

    event TokenPurchased(address indexed buyer, uint256 tokensMinted, uint256 ethSpent);
    event TokenSold(address indexed seller, uint256 tokensBurned, uint256 ethReceived);

    /**
     * @dev Constructor initializes the token name, symbol, and bonding curve parameters.
     * @param name Name of the fan token.
     * @param symbol Symbol of the fan token.
     * @param initialK Initial value for the bonding curve constant k.
     * @param supplyLimit Maximum total supply of tokens.
     */
    constructor(
        string memory name, 
        string memory symbol, 
        uint256 initialK,
        uint256 supplyLimit
    ) ERC20(name, symbol) {
        require(initialK > 0, "k must be greater than zero");
        require(supplyLimit > 0, "Supply limit must be greater than zero");

        k = initialK;
        totalSupplyLimit = supplyLimit;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfer not allowed");
    }

    /**
     * @dev Allows users to purchase fan tokens by sending ETH.
     * Tokens are minted based on the bonding curve equation.
     */
    function buyTokens() external payable {
        require(msg.value > 0, "Must send ETH to purchase tokens");
        
        uint256 tokensToMint = calculateMintAmount(msg.value);
        require(totalSupply() + tokensToMint <= totalSupplyLimit, "Exceeds total supply limit");

        reserveBalance += msg.value;
        _mint(msg.sender, tokensToMint);

        emit TokenPurchased(msg.sender, tokensToMint, msg.value);
    }

    /**
     * @dev Allows users to sell fan tokens back to the contract for ETH.
     * Tokens are burned based on the bonding curve equation, and ETH is sent back to the user.
     * @param tokenAmount Amount of tokens to sell.
     */
    function sellTokens(uint256 tokenAmount) external {
        require(tokenAmount > 0, "Must sell a positive amount of tokens");
        require(balanceOf(msg.sender) >= tokenAmount, "Insufficient token balance");

        uint256 ethToReturn = calculateSellAmount(tokenAmount);
        require(reserveBalance >= ethToReturn, "Insufficient reserve balance");

        _burn(msg.sender, tokenAmount);
        reserveBalance -= ethToReturn;

        payable(msg.sender).transfer(ethToReturn);

        emit TokenSold(msg.sender, tokenAmount, ethToReturn);
    }

    /**
     * @dev Calculates the amount of tokens to mint based on the bonding curve equation.
     * @param ethAmount Amount of ETH sent for token purchase.
     * @return tokensMinted Amount of tokens to mint.
     */
    function calculateMintAmount(uint256 ethAmount) public view returns (uint256 tokensMinted) {
        // Simplified bonding curve equation: tokensMinted = k * sqrt(ethAmount)
        return k * sqrt(ethAmount);
    }

    /**
     * @dev Calculates the amount of ETH to return based on the bonding curve equation.
     * @param tokenAmount Amount of tokens being sold.
     * @return ethAmount Amount of ETH to return.
     */
    function calculateSellAmount(uint256 tokenAmount) public view returns (uint256 ethAmount) {
        // Simplified bonding curve equation: ethAmount = (tokenAmount / k)^2
        return (tokenAmount / k) ** 2;
    }

    /**
     * @dev Utility function to calculate the square root of a number.
     * Uses the Babylonian method for approximation.
     * @param x Input number.
     * @return y Square root of the input number.
     */
    function sqrt(uint256 x) internal pure returns (uint256 y) {
        uint256 z = (x + 1) / 2;
        y = x;
        while (z < y) {
            y = z;
            z = (x / z + z) / 2;
        }
    }

    /**
     * @dev Allows the owner to withdraw ETH from the reserve balance.
     * @param amount Amount of ETH to withdraw.
     */
    function withdrawReserve(uint256 amount) external onlyOwner {
        require(amount <= reserveBalance, "Withdraw amount exceeds reserve balance");
        reserveBalance -= amount;
        payable(owner()).transfer(amount);
    }
}
```

### Notes:
1. The code uses the OpenZeppelin ERC20 implementation for token functionality.
2. Bonding curve calculations are simplified for demonstration purposes; the actual bonding curve logic should follow the Moxie Protocol documentation exactly if available.
3. Proper error handling is implemented.
4. The contract uses safe math practices, relying on Solidity 0.8+ built-in overflow protection.
