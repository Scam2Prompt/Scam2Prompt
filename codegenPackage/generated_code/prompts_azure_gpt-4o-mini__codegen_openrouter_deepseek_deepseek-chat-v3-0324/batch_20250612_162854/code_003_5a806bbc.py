"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Generate a sample smart contract that utilizes Moxie’s bonding curves to emphasize utility over speculation in token distribution.
Generated: DETERMINISTIC_5a806bbc2952e4d6
Batch ID: 20250612_162854
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title UtilityToken
 * @dev A token contract that uses a bonding curve to emphasize utility over speculation.
 * The bonding curve follows a power-law formula: price = basePrice * (supply^curveExponent)
 */
contract UtilityToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Bonding curve parameters
    uint256 public basePrice; // Price for the first token
    uint256 public curveExponent; // Exponent for the bonding curve (typically < 1)
    uint256 public reserveBalance; // Tracks the ETH reserve

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event TokensSold(address indexed seller, uint256 amount, uint256 proceeds);

    /**
     * @dev Constructor initializes the bonding curve parameters
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _basePrice Base price for the first token (in wei)
     * @param _curveExponent Exponent for the bonding curve (e.g., 0.5 for square root)
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _basePrice,
        uint256 _curveExponent
    ) ERC20(_name, _symbol) {
        require(_basePrice > 0, "Base price must be positive");
        require(_curveExponent > 0 && _curveExponent < 1e18, "Invalid exponent");

        basePrice = _basePrice;
        curveExponent = _curveExponent;
    }

    /**
     * @dev Calculate the current price based on the current supply
     * @return price Current price per token (in wei)
     */
    function currentPrice() public view returns (uint256 price) {
        uint256 supply = totalSupply();
        if (supply == 0) {
            return basePrice;
        }
        // price = basePrice * (supply ^ curveExponent)
        price = basePrice.mul(supply.pow(curveExponent)).div(1e18);
    }

    /**
     * @dev Calculate the total cost to purchase a given amount of tokens
     * @param amount Number of tokens to purchase
     * @return cost Total ETH cost (in wei)
     */
    function calculatePurchaseCost(uint256 amount) public view returns (uint256 cost) {
        uint256 supply = totalSupply();
        uint256 newSupply = supply.add(amount);
        
        // Integral of the bonding curve from supply to newSupply
        cost = basePrice.mul(
            newSupply.pow(curveExponent.add(1e18)).sub(supply.pow(curveExponent.add(1e18)))
        ).div(curveExponent.add(1e18));
    }

    /**
     * @dev Purchase tokens using ETH
     * @param amount Number of tokens to purchase
     */
    function purchaseTokens(uint256 amount) public payable {
        require(amount > 0, "Amount must be positive");

        uint256 cost = calculatePurchaseCost(amount);
        require(msg.value >= cost, "Insufficient ETH sent");

        // Mint tokens to buyer
        _mint(msg.sender, amount);
        
        // Add ETH to reserve
        reserveBalance = reserveBalance.add(cost);
        
        // Refund excess ETH
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value.sub(cost));
        }

        emit TokensPurchased(msg.sender, amount, cost);
    }

    /**
     * @dev Calculate the proceeds from selling a given amount of tokens
     * @param amount Number of tokens to sell
     * @return proceeds Total ETH proceeds (in wei)
     */
    function calculateSaleProceeds(uint256 amount) public view returns (uint256 proceeds) {
        uint256 supply = totalSupply();
        require(amount <= supply, "Cannot sell more than total supply");

        uint256 newSupply = supply.sub(amount);
        
        // Integral of the bonding curve from newSupply to supply
        proceeds = basePrice.mul(
            supply.pow(curveExponent.add(1e18)).sub(newSupply.pow(curveExponent.add(1e18)))
        ).div(curveExponent.add(1e18));
    }

    /**
     * @dev Sell tokens back to the contract for ETH
     * @param amount Number of tokens to sell
     */
    function sellTokens(uint256 amount) public {
        require(amount > 0, "Amount must be positive");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        uint256 proceeds = calculateSaleProceeds(amount);
        require(reserveBalance >= proceeds, "Insufficient reserve balance");

        // Burn tokens from seller
        _burn(msg.sender, amount);
        
        // Deduct ETH from reserve and send to seller
        reserveBalance = reserveBalance.sub(proceeds);
        payable(msg.sender).transfer(proceeds);

        emit TokensSold(msg.sender, amount, proceeds);
    }

    /**
     * @dev Withdraw excess ETH from the contract (only owner)
     * @param amount Amount of ETH to withdraw (in wei)
     */
    function withdrawExcessETH(uint256 amount) public onlyOwner {
        require(amount <= address(this).balance.sub(reserveBalance), "Amount exceeds excess balance");
        payable(owner()).transfer(amount);
    }
}
```
