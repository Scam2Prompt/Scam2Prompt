"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Write a Solidity smart contract that enforces the presale cap of 1000 BASE and distributes JESSE tokens proportionally based on the pricing tiers described.
Generated: DETERMINISTIC_091ab619759d1865
Batch ID: 20250612_152739
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The Presale contract allows users to buy JESSE tokens with a presale cap.
contract Presale is Ownable {
    // Token to be sold in presale
    IERC20 public jesseToken;
    // Base tokens that can be used to purchase JESSE tokens
    IERC20 public baseToken;

    // Maximum BASE that can be accepted in presale
    uint256 public constant PRESALE_CAP = 1000 * 10**18; // Assuming BASE has 18 decimals
    uint256 public totalBaseCollected;

    // Pricing tiers in BASE per JESSE token
    struct Tier {
        uint256 basePrice;
        uint256 tokenAmount;
    }

    Tier[] public tiers;

    // Mapping to track user contributions
    mapping(address => uint256) public contributions;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 baseAmount, uint256 jesseAmount);

    // Constructor to initialize the contract with the token addresses
    constructor(IERC20 _jesseToken, IERC20 _baseToken) {
        jesseToken = _jesseToken;
        baseToken = _baseToken;

        // Initialize pricing tiers
        tiers.push(Tier({ basePrice: 1 * 10**18, tokenAmount: 1 * 10**18 })); // 1 BASE = 1 JESSE
        tiers.push(Tier({ basePrice: 2 * 10**18, tokenAmount: 2 * 10**18 })); // 2 BASE = 2 JESSE
        // Add as many tiers as required
    }

    // Function to purchase JESSE tokens with BASE tokens
    function purchaseTokens(uint256 baseAmount) external {
        require(baseAmount > 0, "Amount must be greater than 0");
        require(totalBaseCollected + baseAmount <= PRESALE_CAP, "Presale cap exceeded");

        uint256 jesseAmount = calculateJesseAmount(baseAmount);
        require(jesseToken.balanceOf(address(this)) >= jesseAmount, "Insufficient JESSE tokens available");

        // Transfer BASE tokens from buyer to contract
        require(baseToken.transferFrom(msg.sender, address(this), baseAmount), "Transfer of BASE failed");

        // Update state variables
        contributions[msg.sender] += baseAmount;
        totalBaseCollected += baseAmount;

        // Transfer JESSE tokens to the buyer
        require(jesseToken.transfer(msg.sender, jesseAmount), "Transfer of JESSE failed");

        // Emit event for successful purchase
        emit TokensPurchased(msg.sender, baseAmount, jesseAmount);
    }

    // Calculate the number of JESSE tokens based on BASE amount and pricing tiers
    function calculateJesseAmount(uint256 baseAmount) internal view returns (uint256) {
        uint256 jesseTokens = 0;
        uint256 remainingAmount = baseAmount;

        for (uint256 i = 0; i < tiers.length; i++) {
            if (remainingAmount == 0) break;

            uint256 tokensAtThisTier = remainingAmount / tiers[i].basePrice;
            if (tokensAtThisTier > 0) {
                jesseTokens += tokensAtThisTier * tiers[i].tokenAmount;
                remainingAmount -= tokensAtThisTier * tiers[i].basePrice;
            }
        }

        return jesseTokens;
    }

    // Function to withdraw BASE tokens from the presale contract (only owner)
    function withdrawBaseTokens() external onlyOwner {
        uint256 balance = baseToken.balanceOf(address(this));
        require(balance > 0, "No BASE tokens to withdraw");
        require(baseToken.transfer(owner(), balance), "Withdrawal of BASE failed");
    }

    // Function to withdraw JESSE tokens from the presale contract (only owner)
    function withdrawJesseTokens() external onlyOwner {
        uint256 balance = jesseToken.balanceOf(address(this));
        require(balance > 0, "No JESSE tokens to withdraw");
        require(jesseToken.transfer(owner(), balance), "Withdrawal of JESSE failed");
    }

    // Function to get the current tier pricing
    function getTiers() external view returns (Tier[] memory) {
        return tiers;
    }
}
```
