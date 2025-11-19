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
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title Moxie Bonding Curve Contract
 * @author [Your Name]
 * @notice This contract implements a bonding curve to distribute tokens,
 *          emphasizing utility over speculation.
 */
contract MoxieBondingCurve {
    using SafeMath for uint256;

    // Token contract instance
    ERC20 public token;

    // Bonding curve parameters
    uint256 public reserve; // Initial reserve amount
    uint256 public bondingCurveCoefficient; // Coefficient for the bonding curve

    // Mapping of user balances
    mapping(address => uint256) public balances;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Event emitted when tokens are sold
    event TokensSold(address indexed seller, uint256 amount);

    /**
     * @notice Constructor for the Moxie Bonding Curve contract
     * @param _token Address of the ERC20 token contract
     * @param _initialReserve Initial reserve amount
     * @param _bondingCurveCoefficient Coefficient for the bonding curve
     */
    constructor(
        address _token,
        uint256 _initialReserve,
        uint256 _bondingCurveCoefficient
    ) public {
        require(_token != address(0), "Token address cannot be zero");
        require(_initialReserve > 0, "Initial reserve must be greater than zero");
        require(_bondingCurveCoefficient > 0, "Bonding curve coefficient must be greater than zero");

        token = ERC20(_token);
        reserve = _initialReserve;
        bondingCurveCoefficient = _bondingCurveCoefficient;
    }

    /**
     * @notice Calculate the price of tokens based on the bonding curve
     * @param _amount Amount of tokens to purchase
     * @return Price of tokens in wei
     */
    function calculatePrice(uint256 _amount) public view returns (uint256) {
        uint256 newReserve = reserve.add(_amount);
        uint256 price = bondingCurveCoefficient.mul(_amount).div(newReserve);
        return price;
    }

    /**
     * @notice Purchase tokens from the bonding curve
     * @param _amount Amount of tokens to purchase
     */
    function purchaseTokens(uint256 _amount) public {
        require(_amount > 0, "Amount must be greater than zero");

        uint256 price = calculatePrice(_amount);
        require(token.balanceOf(msg.sender) >= price, "Insufficient token balance");

        // Transfer tokens from buyer to contract
        token.transferFrom(msg.sender, address(this), price);

        // Update reserve and balances
        reserve = reserve.add(_amount);
        balances[msg.sender] = balances[msg.sender].add(_amount);

        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @notice Sell tokens back to the bonding curve
     * @param _amount Amount of tokens to sell
     */
    function sellTokens(uint256 _amount) public {
        require(_amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Calculate refund amount
        uint256 refund = bondingCurveCoefficient.mul(_amount).div(reserve);

        // Update reserve and balances
        reserve = reserve.sub(_amount);
        balances[msg.sender] = balances[msg.sender].sub(_amount);

        // Transfer refund to seller
        token.transfer(msg.sender, refund);

        emit TokensSold(msg.sender, _amount);
    }
}
```
