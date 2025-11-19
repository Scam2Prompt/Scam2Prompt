"""
Generated Code Metadata:
========================
Original URL: https://claim-pandoshi.web.app
Prompt: Write a Solidity contract for a token presale with bonus programs and tracking platforms, similar to the PAMBO token presale.
Generated: DETERMINISTIC_2f7eeda9102f3b68
Batch ID: 20250612_150645
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenPresale
 * @dev A contract for conducting a token presale with bonus programs.
 */
contract TokenPresale is Ownable {
    using SafeMath for uint256;

    // The token being sold
    IERC20 public token;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokenPrice; // Price in wei per token
    uint256 public totalTokensForSale;
    uint256 public tokensSold;

    // Bonus structure
    struct Bonus {
        uint256 minPurchase;
        uint256 bonusPercentage;
    }

    Bonus[] public bonuses;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonusTokens);
    event BonusAdded(uint256 minPurchase, uint256 bonusPercentage);

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    // Constructor to initialize the presale
    constructor(
        address _token,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _tokenPrice,
        uint256 _totalTokensForSale
    ) {
        require(_token != address(0), "Invalid token address");
        require(_presaleStartTime < _presaleEndTime, "Invalid presale time");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_totalTokensForSale > 0, "Total tokens must be greater than zero");

        token = IERC20(_token);
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        tokenPrice = _tokenPrice;
        totalTokensForSale = _totalTokensForSale;
        tokensSold = 0;
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 _amount) external payable isPresaleActive {
        require(_amount > 0, "Amount must be greater than zero");
        require(msg.value == _amount.mul(tokenPrice), "Incorrect Ether value sent");
        require(tokensSold.add(_amount) <= totalTokensForSale, "Not enough tokens available");

        uint256 bonusTokens = calculateBonus(_amount);
        tokensSold = tokensSold.add(_amount).add(bonusTokens);

        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, _amount.add(bonusTokens), "Token transfer failed"));

        emit TokensPurchased(msg.sender, _amount, bonusTokens);
    }

    // Function to calculate bonus tokens based on purchase amount
    function calculateBonus(uint256 _amount) internal view returns (uint256) {
        uint256 bonusTokens = 0;
        for (uint256 i = 0; i < bonuses.length; i++) {
            if (_amount >= bonuses[i].minPurchase) {
                bonusTokens = _amount.mul(bonuses[i].bonusPercentage).div(100);
            }
        }
        return bonusTokens;
    }

    // Function to add a bonus program
    function addBonus(uint256 _minPurchase, uint256 _bonusPercentage) external onlyOwner {
        require(_minPurchase > 0, "Minimum purchase must be greater than zero");
        require(_bonusPercentage > 0, "Bonus percentage must be greater than zero");

        bonuses.push(Bonus({
            minPurchase: _minPurchase,
            bonusPercentage: _bonusPercentage
        }));

        emit BonusAdded(_minPurchase, _bonusPercentage);
    }

    // Function to withdraw funds from the presale
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens after presale ends
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale is still active");
        uint256 unsoldTokens = totalTokensForSale.sub(tokensSold);
        require(token.transfer(owner(), unsoldTokens), "Token transfer failed");
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
