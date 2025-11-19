"""
Generated Code Metadata:
========================
Original URL: https://xai327k.com
Prompt: "Generate a smart contract code in Solidity for a token presale event similar to xAI327K, allowing bonuses up to 200%."
Generated: DETERMINISTIC_5c67e108066070b9
Batch ID: 20250622_211819
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
 * @title TokenPresale
 * @dev A smart contract for conducting a token presale event with bonuses.
 */
contract TokenPresale is Ownable {
    // The token being sold
    IERC20 public token;

    // Presale parameters
    uint256 public presaleStart;
    uint256 public presaleEnd;
    uint256 public tokenPrice; // Price per token in wei
    uint256 public totalTokensForSale;
    uint256 public tokensSold;

    // Bonus structure
    struct Bonus {
        uint256 minInvestment;
        uint256 bonusPercentage;
    }

    Bonus[] public bonuses;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonusAmount);
    event PresaleEnded();

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token Address of the token being sold.
     * @param _presaleStart Start time of the presale.
     * @param _presaleEnd End time of the presale.
     * @param _tokenPrice Price of the token in wei.
     * @param _totalTokensForSale Total tokens available for sale.
     */
    constructor(
        address _token,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice,
        uint256 _totalTokensForSale
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_presaleStart < _presaleEnd, "Invalid presale time");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_totalTokensForSale > 0, "Total tokens must be greater than zero");

        token = IERC20(_token);
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
        totalTokensForSale = _totalTokensForSale;
    }

    /**
     * @dev Function to buy tokens during the presale.
     * @param amount Amount of tokens to purchase.
     */
    function buyTokens(uint256 amount) external payable isPresaleActive {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount * tokenPrice, "Incorrect Ether value sent");
        require(tokensSold + amount <= totalTokensForSale, "Not enough tokens available");

        uint256 bonusAmount = calculateBonus(amount);
        tokensSold += amount;

        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, amount + bonusAmount), "Token transfer failed");

        emit TokensPurchased(msg.sender, amount, bonusAmount);
    }

    /**
     * @dev Function to calculate bonus based on investment amount.
     * @param amount Amount of tokens purchased.
     * @return bonusAmount The calculated bonus amount.
     */
    function calculateBonus(uint256 amount) internal view returns (uint256) {
        uint256 investment = amount * tokenPrice;
        uint256 bonusAmount = 0;

        for (uint256 i = 0; i < bonuses.length; i++) {
            if (investment >= bonuses[i].minInvestment) {
                bonusAmount = (amount * bonuses[i].bonusPercentage) / 100;
            }
        }

        return bonusAmount;
    }

    /**
     * @dev Function to add bonus tiers.
     * @param minInvestment Minimum investment to qualify for the bonus.
     * @param bonusPercentage Bonus percentage to be awarded.
     */
    function addBonus(uint256 minInvestment, uint256 bonusPercentage) external onlyOwner {
        require(bonusPercentage <= 200, "Bonus cannot exceed 200%");
        bonuses.push(Bonus(minInvestment, bonusPercentage));
    }

    /**
     * @dev Function to withdraw funds from the presale.
     */
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Function to end the presale.
     */
    function endPresale() external onlyOwner {
        presaleEnd = block.timestamp;
        emit PresaleEnded();
    }

    /**
     * @dev Function to retrieve unsold tokens after the presale.
     */
    function retrieveUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = totalTokensForSale - tokensSold;
        require(unsoldTokens > 0, "No unsold tokens to retrieve");
        require(token.transfer(owner(), unsoldTokens), "Token transfer failed");
    }
}
```
