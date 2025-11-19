"""
Generated Code Metadata:
========================
Original URL: https://bull-dogito-com.pages.dev
Prompt: Generate a smart contract code snippet in Solidity for the token buyback and burn mechanism described in BULLDOGITO's tokenomics.
Generated: DETERMINISTIC_0e98d95767254b8d
Batch ID: 20250622_211533
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract BulldogitoBuybackBurn is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    IERC20 public token;
    address public treasury;
    uint256 public buybackPercentage; // Percentage of treasury funds to use for buyback (e.g., 1000 = 10%)
    uint256 public minBuybackAmount; // Minimum token balance required to trigger buyback
    uint256 public lastBuybackTime;
    uint256 public buybackCooldown; // Time between buybacks (in seconds)

    event BuybackAndBurn(uint256 amountBought, uint256 amountBurned);
    event TreasuryUpdated(address newTreasury);
    event BuybackPercentageUpdated(uint256 newPercentage);
    event MinBuybackAmountUpdated(uint256 newAmount);
    event BuybackCooldownUpdated(uint256 newCooldown);

    constructor(
        address _token,
        address _treasury,
        uint256 _buybackPercentage,
        uint256 _minBuybackAmount,
        uint256 _buybackCooldown
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_treasury != address(0), "Treasury address cannot be zero");
        require(_buybackPercentage <= 10000, "Percentage cannot exceed 100%");

        token = IERC20(_token);
        treasury = _treasury;
        buybackPercentage = _buybackPercentage;
        minBuybackAmount = _minBuybackAmount;
        buybackCooldown = _buybackCooldown;
    }

    function executeBuyback() external nonReentrant {
        require(
            block.timestamp >= lastBuybackTime + buybackCooldown,
            "Buyback cooldown not elapsed"
        );

        uint256 treasuryBalance = token.balanceOf(treasury);
        require(treasuryBalance >= minBuybackAmount, "Insufficient treasury balance");

        uint256 buybackAmount = treasuryBalance.mul(buybackPercentage).div(10000);
        
        // Transfer tokens from treasury to this contract
        require(
            token.transferFrom(treasury, address(this), buybackAmount),
            "Transfer from treasury failed"
        );

        // Burn the tokens by sending to address(0)
        token.transfer(address(0), buybackAmount);

        lastBuybackTime = block.timestamp;
        emit BuybackAndBurn(buybackAmount, buybackAmount);
    }

    function setTreasury(address _treasury) external onlyOwner {
        require(_treasury != address(0), "Treasury address cannot be zero");
        treasury = _treasury;
        emit TreasuryUpdated(_treasury);
    }

    function setBuybackPercentage(uint256 _buybackPercentage) external onlyOwner {
        require(_buybackPercentage <= 10000, "Percentage cannot exceed 100%");
        buybackPercentage = _buybackPercentage;
        emit BuybackPercentageUpdated(_buybackPercentage);
    }

    function setMinBuybackAmount(uint256 _minBuybackAmount) external onlyOwner {
        minBuybackAmount = _minBuybackAmount;
        emit MinBuybackAmountUpdated(_minBuybackAmount);
    }

    function setBuybackCooldown(uint256 _buybackCooldown) external onlyOwner {
        buybackCooldown = _buybackCooldown;
        emit BuybackCooldownUpdated(_buybackCooldown);
    }
}
```
