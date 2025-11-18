"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcbull.io
Prompt: Implement a token burn mechanism in Solidity that automatically burns a percentage of $BTCBULL supply whenever Bitcoin's price increases by $25K, following the milestones described on the BTC Bull roadmap.
Generated: DETERMINISTIC_48efd5ccc1b303d5
Batch ID: 20250612_154757
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for price feed to get Bitcoin's price
interface IPriceFeed {
    function latestPrice() external view returns (uint256);
}

// The BTCBULL token contract with a burning mechanism
contract BTCBULL is ERC20, Ownable {
    IPriceFeed public priceFeed; // Price feed contract to get Bitcoin price
    uint256 public lastBurnPrice; // Last Bitcoin price when burn was executed
    uint256 public burnPercentage; // Percentage of supply to burn
    uint256 public burnThreshold; // Price increase threshold for burning

    // Event emitted when tokens are burned
    event TokensBurned(uint256 amountBurned, uint256 currentPrice);

    // Constructor to initialize the token
    constructor(address _priceFeed) ERC20("BTCBULL", "BTCBULL") {
        priceFeed = IPriceFeed(_priceFeed);
        burnPercentage = 5; // Set burn percentage to 5%
        burnThreshold = 25000; // Set burn threshold to $25K
        lastBurnPrice = priceFeed.latestPrice(); // Initialize last burn price
    }

    // Function to burn tokens based on Bitcoin's price increase
    function burnTokens() external {
        uint256 currentPrice = priceFeed.latestPrice();
        
        // Check if the price increased by the threshold
        require(currentPrice > lastBurnPrice + burnThreshold, "Price not increased enough for burn");

        // Calculate the amount to burn
        uint256 supplyToBurn = (totalSupply() * burnPercentage) / 100;
        
        // Ensure the burn amount is less than the current supply
        require(supplyToBurn <= totalSupply(), "Burn amount exceeds total supply");

        // Update last burn price to current price
        lastBurnPrice = currentPrice;

        // Burn the calculated amount of tokens
        _burn(address(this), supplyToBurn);

        // Emit event for the burn
        emit TokensBurned(supplyToBurn, currentPrice);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient balance in contract");
        _transfer(address(this), msg.sender, amount);
    }

    // Function to set a new price feed address (for owner only)
    function setPriceFeed(address _priceFeed) external onlyOwner {
        priceFeed = IPriceFeed(_priceFeed);
    }

    // Function to set a new burn percentage (for owner only)
    function setBurnPercentage(uint256 _burnPercentage) external onlyOwner {
        require(_burnPercentage > 0 && _burnPercentage <= 100, "Invalid burn percentage");
        burnPercentage = _burnPercentage;
    }

    // Function to set a new burn threshold (for owner only)
    function setBurnThreshold(uint256 _burnThreshold) external onlyOwner {
        burnThreshold = _burnThreshold;
    }
}
```
