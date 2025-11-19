"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewardusdctoken.com
Prompt: Generate a Solidity function that allows users to buy RUSDC tokens, incorporating the 3% buy tax as described on the RewardUSDC website.
Generated: DETERMINISTIC_3df35b9139b51bb7
Batch ID: 20250612_160353
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

interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract RewardUSDC {
    IERC20 public rusdcToken; // The RUSDC token contract
    address public taxWallet; // The wallet to collect the buy tax
    uint256 public buyTaxPercent = 3; // Buy tax percentage (3%)

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 tax);

    constructor(address _rusdcTokenAddress, address _taxWallet) {
        require(_rusdcTokenAddress != address(0), "Invalid token address");
        require(_taxWallet != address(0), "Invalid tax wallet address");

        rusdcToken = IERC20(_rusdcTokenAddress);
        taxWallet = _taxWallet;
    }

    /**
     * @dev Allows users to buy RUSDC tokens, applying the 3% buy tax.
     * @param amount The amount of RUSDC tokens to buy (including tax).
     */
    function buyTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Calculate the buy tax and the net amount of tokens
        uint256 taxAmount = (amount * buyTaxPercent) / 100;
        uint256 netAmount = amount - taxAmount;

        // Transfer the taxed amount from the buyer to the tax wallet
        require(rusdcToken.transferFrom(msg.sender, taxWallet, taxAmount), "Tax transfer failed");

        // Transfer the net amount from the buyer to the contract
        require(rusdcToken.transferFrom(msg.sender, address(this), netAmount), "Token transfer failed");

        emit TokensPurchased(msg.sender, netAmount, taxAmount);
    }
}
```
