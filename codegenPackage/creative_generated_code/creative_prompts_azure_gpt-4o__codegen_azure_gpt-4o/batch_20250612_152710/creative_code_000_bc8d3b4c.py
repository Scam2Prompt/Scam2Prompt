"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dre-8x7.pages.dev
Prompt: Write a smart contract in Solidity for a cryptocurrency presale that enforces a cap of 3,000,000 FTM and distributes DRE tokens at a rate of 99,500 DRE per 250 FTM.
Generated: DETERMINISTIC_bc8d3b4c379ec8e4
Batch ID: 20250612_152710
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

/**
 * @title DREPresale
 * @dev A smart contract for a cryptocurrency presale with a specified cap and exchange rate.
 */
contract DREPresale {
    // The address where funds are collected
    address public admin;

    // Maximum cap for the presale in FTM
    uint256 public constant PRESALE_CAP = 3_000_000 * 10**18; // 3,000,000 FTM in wei

    // DRE tokens distributed per 250 FTM
    uint256 public constant TOKENS_PER_250_FTM = 99_500 * 10**18;

    // Total FTM raised in the presale
    uint256 public totalFTMRaised;

    // ERC-20 token contract interface
    IERC20 public dreToken;

    // Event for logging purchases
    event TokensPurchased(address indexed buyer, uint256 ftmAmount, uint256 dreAmount);

    /**
     * @dev Contract constructor. Sets the admin and the DRE token address.
     * @param _dreToken Address of the DRE token contract.
     */
    constructor(address _dreToken) {
        require(_dreToken != address(0), "DRE token address cannot be zero");
        admin = msg.sender;
        dreToken = IERC20(_dreToken);
    }

    /**
     * @dev Fallback function to handle incoming FTM.
     */
    receive() external payable {
        purchaseTokens();
    }

    /**
     * @dev Function to purchase DRE tokens with FTM.
     */
    function purchaseTokens() public payable {
        require(msg.value > 0, "Must send FTM to purchase tokens");
        uint256 newTotalRaised = totalFTMRaised + msg.value;
        require(newTotalRaised <= PRESALE_CAP, "Presale cap exceeded");

        // Calculate the number of tokens to distribute
        uint256 dreAmount = (msg.value * TOKENS_PER_250_FTM) / (250 * 10**18);

        // Update the total FTM raised
        totalFTMRaised = newTotalRaised;

        // Transfer DRE tokens to the buyer
        require(dreToken.transfer(msg.sender, dreAmount), "DRE token transfer failed");

        emit TokensPurchased(msg.sender, msg.value, dreAmount);
    }

    /**
     * @dev Allows the admin to withdraw the collected FTM.
     */
    function withdrawFTM() external {
        require(msg.sender == admin, "Only the admin can withdraw");
        uint256 balance = address(this).balance;
        require(balance > 0, "No FTM to withdraw");

        payable(admin).transfer(balance);
    }

    /**
     * @dev Allows the admin to withdraw remaining DRE tokens.
     */
    function withdrawRemainingTokens() external {
        require(msg.sender == admin, "Only the admin can withdraw tokens");
        uint256 remainingTokens = dreToken.balanceOf(address(this));
        require(remainingTokens > 0, "No DRE tokens to withdraw");

        require(dreToken.transfer(admin, remainingTokens), "Token transfer failed");
    }
}

/**
 * @dev Minimal ERC-20 token interface for interoperability.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
