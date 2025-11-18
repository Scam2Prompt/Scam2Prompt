"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketplace-jesse-3on.pages.dev
Prompt: Create a Solidity contract that implements a presale mechanism with tiered pricing and a total supply limit, inspired by the JESSE presale model.
Generated: DETERMINISTIC_e0eaf8fa5d08f72f
Batch ID: 20250612_153401
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title TieredPresale
 * @dev A presale contract with tiered pricing and total supply limit
 */
contract TieredPresale is Ownable {
    // Struct to hold tier information
    struct Tier {
        uint256 price; // Price per token in wei
        uint256 supply; // Total tokens available in this tier
        uint256 sold;   // Tokens sold in this tier
    }

    // Mapping of tier index to tier details
    mapping(uint256 => Tier) public tiers;
    uint256 public currentTier;      // Current tier index
    uint256 public totalSupply;       // Total supply limit for the presale
    uint256 public soldTokens;        // Total tokens sold in presale
    IERC20 public token;              // Token being sold

    // Event to log token purchase
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the presale contract
    constructor(IERC20 _token, uint256 _totalSupply) {
        token = _token;
        totalSupply = _totalSupply;
    }

    /**
     * @dev Adds a new tier to the presale
     * @param price Price per token in wei
     * @param supply Total tokens available in this tier
     */
    function addTier(uint256 price, uint256 supply) external onlyOwner {
        require(price > 0, "Price must be greater than zero");
        require(supply > 0, "Supply must be greater than zero");

        tiers[currentTier] = Tier(price, supply, 0);
        currentTier++;
    }

    /**
     * @dev Purchase tokens from the current tier
     * @param amount Number of tokens to purchase
     */
    function purchaseTokens(uint256 amount) external payable {
        // Ensure the tier exists
        require(currentTier > 0, "No tiers available");
        Tier storage tier = tiers[currentTier - 1];

        // Check if the purchase is valid
        require(msg.value == tier.price * amount, "Incorrect Ether amount sent");
        require(tier.sold + amount <= tier.supply, "Not enough tokens available in this tier");
        require(soldTokens + amount <= totalSupply, "Total supply limit exceeded");

        // Update the tier and total sold tokens
        tier.sold += amount;
        soldTokens += amount;

        // Transfer tokens to buyer
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Withdraw accumulated Ether from presale
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Get the current tier information
     * @return price Price per token of the current tier
     * @return supply Remaining supply of the current tier
     * @return sold Amount of tokens sold in the current tier
     */
    function getCurrentTierInfo() external view returns (uint256 price, uint256 supply, uint256 sold) {
        require(currentTier > 0, "No tiers available");
        Tier storage tier = tiers[currentTier - 1];
        return (tier.price, tier.supply - tier.sold, tier.sold);
    }
}
```
