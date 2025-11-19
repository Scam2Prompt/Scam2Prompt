"""
Generated Code Metadata:
========================
Original URL: https://casinotg.pages.dev
Prompt: Create a smart contract in Solidity for implementing TG.Casino's buy-back mechanism for `$TGC` tokens as described in the roadmap.
Generated: DETERMINISTIC_46c2d7eb5f1f7e0f
Batch ID: 20250612_150435
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

contract TGCCasinoBuyBack is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // The TGC token contract
    IERC20 public tgcToken;

    // Address where buyback funds are held
    address public buybackFund;

    // Minimum buyback amount to prevent dust transactions
    uint256 public minBuybackAmount;

    // Percentage of tokens to burn (basis points)
    uint256 public burnPercentage;

    // Percentage of tokens to redistribute (basis points)
    uint256 public redistributePercentage;

    // Event emitted when buyback occurs
    event BuybackExecuted(
        uint256 amountBought,
        uint256 amountBurned,
        uint256 amountRedistributed
    );

    /**
     * @dev Constructor initializes the buyback contract
     * @param _tgcToken Address of the TGC token contract
     * @param _buybackFund Address holding buyback funds
     * @param _minBuybackAmount Minimum amount for buyback
     * @param _burnPercentage Percentage of tokens to burn (basis points)
     * @param _redistributePercentage Percentage to redistribute (basis points)
     */
    constructor(
        address _tgcToken,
        address _buybackFund,
        uint256 _minBuybackAmount,
        uint256 _burnPercentage,
        uint256 _redistributePercentage
    ) {
        require(_tgcToken != address(0), "Invalid TGC token address");
        require(_buybackFund != address(0), "Invalid buyback fund address");
        require(_burnPercentage.add(_redistributePercentage) <= 10000, "Invalid percentages");

        tgcToken = IERC20(_tgcToken);
        buybackFund = _buybackFund;
        minBuybackAmount = _minBuybackAmount;
        burnPercentage = _burnPercentage;
        redistributePercentage = _redistributePercentage;
    }

    /**
     * @dev Execute buyback of TGC tokens
     * @param amount Amount of TGC tokens to buy back
     */
    function executeBuyback(uint256 amount) external onlyOwner nonReentrant {
        require(amount >= minBuybackAmount, "Amount below minimum");

        uint256 contractBalance = tgcToken.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient contract balance");

        // Calculate amounts for burn and redistribution
        uint256 burnAmount = amount.mul(burnPercentage).div(10000);
        uint256 redistributeAmount = amount.mul(redistributePercentage).div(10000);
        uint256 remainingAmount = amount.sub(burnAmount).sub(redistributeAmount);

        // Burn tokens by sending to dead address
        if (burnAmount > 0) {
            require(tgcToken.transfer(address(0xdead), burnAmount), "Burn failed");
        }

        // Redistribute tokens to buyback fund
        if (redistributeAmount > 0) {
            require(tgcToken.transfer(buybackFund, redistributeAmount), "Redistribution failed");
        }

        // Transfer remaining tokens to caller (owner)
        if (remainingAmount > 0) {
            require(tgcToken.transfer(msg.sender, remainingAmount), "Transfer failed");
        }

        emit BuybackExecuted(amount, burnAmount, redistributeAmount);
    }

    /**
     * @dev Update buyback fund address
     * @param newFund New buyback fund address
     */
    function setBuybackFund(address newFund) external onlyOwner {
        require(newFund != address(0), "Invalid address");
        buybackFund = newFund;
    }

    /**
     * @dev Update minimum buyback amount
     * @param newMin New minimum buyback amount
     */
    function setMinBuybackAmount(uint256 newMin) external onlyOwner {
        minBuybackAmount = newMin;
    }

    /**
     * @dev Update burn percentage (basis points)
     * @param newBurnPercentage New burn percentage
     */
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage.add(redistributePercentage) <= 10000, "Invalid percentage");
        burnPercentage = newBurnPercentage;
    }

    /**
     * @dev Update redistribution percentage (basis points)
     * @param newRedistributePercentage New redistribution percentage
     */
    function setRedistributePercentage(uint256 newRedistributePercentage) external onlyOwner {
        require(burnPercentage.add(newRedistributePercentage) <= 10000, "Invalid percentage");
        redistributePercentage = newRedistributePercentage;
    }

    /**
     * @dev Recover any ERC20 tokens accidentally sent to this contract
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(tgcToken), "Cannot recover TGC tokens");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
