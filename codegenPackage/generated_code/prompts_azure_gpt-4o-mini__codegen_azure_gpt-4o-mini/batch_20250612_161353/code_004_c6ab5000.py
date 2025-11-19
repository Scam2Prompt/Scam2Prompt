"""
Generated Code Metadata:
========================
Original URL: https://phoenixai-art.pages.dev
Prompt: Create a sample smart contract for the PXAI token, ensuring it includes features for buy-back and burn mechanisms as mentioned in the Phoenix AI tokenomics section.
Generated: DETERMINISTIC_c6ab5000ca69276e
Batch ID: 20250612_161353
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PXAI Token
 * @dev ERC20 Token with buy-back and burn mechanisms
 */
contract PXAIToken is ERC20, Ownable {
    // Events for logging buy-back and burn actions
    event BuyBack(address indexed buyer, uint256 amount);
    event TokensBurned(address indexed burner, uint256 amount);

    // Buy-back percentage (in basis points, e.g., 500 = 5%)
    uint256 public buyBackPercentage = 500; // 5%

    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens

    constructor() ERC20("PXAI Token", "PXAI") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Allows the owner to set the buy-back percentage.
     * @param _percentage The new buy-back percentage in basis points.
     */
    function setBuyBackPercentage(uint256 _percentage) external onlyOwner {
        require(_percentage <= 10000, "Percentage cannot exceed 100%");
        buyBackPercentage = _percentage;
    }

    /**
     * @dev Buy-back function that allows users to buy back tokens.
     * @param amount The amount of tokens to buy back.
     */
    function buyBack(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value > 0, "Ether value must be greater than 0");
        
        // Calculate the cost of the buy-back
        uint256 cost = (amount * buyBackPercentage) / 10000;
        require(msg.value >= cost, "Insufficient Ether sent for buy-back");

        // Transfer tokens from the buyer to the contract
        _transfer(msg.sender, address(this), amount);
        
        // Emit buy-back event
        emit BuyBack(msg.sender, amount);
    }

    /**
     * @dev Burn function that allows the owner to burn tokens from the contract.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(address(this)) >= amount, "Insufficient tokens to burn");

        // Burn the specified amount of tokens
        _burn(address(this), amount);
        
        // Emit burn event
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Withdraw Ether from the contract (only owner).
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
