"""
Generated Code Metadata:
========================
Original URL: https://marketplace-jesse-3on.pages.dev
Prompt: Create a Solidity contract that implements a presale mechanism with tiered pricing and a total supply limit, inspired by the JESSE presale model.
Generated: DETERMINISTIC_e0eaf8fa5d08f72f
Batch ID: 20250612_153401
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
 * @title TieredPresale
 * @dev A contract for a tiered presale mechanism with a total supply limit.
 */
contract TieredPresale is Ownable {
    // Token to be sold in the presale
    IERC20 public token;

    // Total supply limit for the presale
    uint256 public totalSupplyLimit;

    // Amount of tokens sold
    uint256 public tokensSold;

    // Presale tiers with pricing
    struct Tier {
        uint256 price; // Price per token in wei
        uint256 supply; // Number of tokens available in this tier
    }

    // Array of tiers
    Tier[] public tiers;

    // Mapping to track contributions of each buyer
    mapping(address => uint256) public contributions;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token Address of the ERC20 token to be sold.
     * @param _totalSupplyLimit Total supply limit for the presale.
     */
    constructor(IERC20 _token, uint256 _totalSupplyLimit) {
        token = _token;
        totalSupplyLimit = _totalSupplyLimit;
    }

    /**
     * @dev Add a new tier to the presale.
     * @param _price Price per token for this tier.
     * @param _supply Number of tokens available in this tier.
     */
    function addTier(uint256 _price, uint256 _supply) external onlyOwner {
        require(_supply > 0, "Supply must be greater than zero");
        tiers.push(Tier({ price: _price, supply: _supply }));
    }

    /**
     * @dev Purchase tokens from the presale.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(tokensSold + _amount <= totalSupplyLimit, "Exceeds total supply limit");
        
        uint256 totalCost = calculateCost(_amount);
        require(msg.value >= totalCost, "Insufficient funds sent");

        // Update state
        tokensSold += _amount;
        contributions[msg.sender] += _amount;

        // Transfer tokens to the buyer
        token.transfer(msg.sender, _amount);

        // Emit event
        emit TokensPurchased(msg.sender, _amount, totalCost);

        // Refund excess funds
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    /**
     * @dev Calculate the cost of purchasing a given amount of tokens.
     * @param _amount Number of tokens to purchase.
     * @return totalCost The total cost in wei.
     */
    function calculateCost(uint256 _amount) internal view returns (uint256 totalCost) {
        uint256 remainingAmount = _amount;

        for (uint256 i = 0; i < tiers.length; i++) {
            if (remainingAmount == 0) break;

            Tier storage tier = tiers[i];
            if (tier.supply > 0) {
                uint256 tokensToBuy = remainingAmount > tier.supply ? tier.supply : remainingAmount;
                totalCost += tokensToBuy * tier.price;
                remainingAmount -= tokensToBuy;
            }
        }

        require(remainingAmount == 0, "Not enough tokens available in tiers");
    }

    /**
     * @dev Withdraw funds from the contract.
     */
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Get the number of tiers available.
     * @return The number of tiers.
     */
    function getTierCount() external view returns (uint256) {
        return tiers.length;
    }

    /**
     * @dev Get details of a specific tier.
     * @param _index Index of the tier.
     * @return price Price per token for the tier.
     * @return supply Number of tokens available in the tier.
     */
    function getTier(uint256 _index) external view returns (uint256 price, uint256 supply) {
        require(_index < tiers.length, "Tier index out of bounds");
        Tier storage tier = tiers[_index];
        return (tier.price, tier.supply);
    }
}
```
