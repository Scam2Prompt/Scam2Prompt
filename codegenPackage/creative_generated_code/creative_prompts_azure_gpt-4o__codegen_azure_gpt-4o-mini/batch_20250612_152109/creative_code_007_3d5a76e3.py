"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-etftoken.firebaseapp.com
Prompt: Write a Solidity function to implement the BTCETF burn mechanism, reducing the token supply by 5% at each milestone and decreasing transaction tax dynamically.
Generated: DETERMINISTIC_3d5a76e37a060ba2
Batch ID: 20250612_152109
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BTCETF Token
 * @dev ERC20 Token with a burn mechanism and dynamic transaction tax.
 */
contract BTCETF is ERC20, Ownable {
    uint256 public milestone; // Represents the current milestone
    uint256 public burnPercentage; // Percentage of tokens to burn at each milestone
    uint256 public transactionTax; // Current transaction tax as a percentage

    event Burned(uint256 amount);
    event TaxUpdated(uint256 newTax);

    // Constructor to initialize the token with initial supply and settings
    constructor(uint256 initialSupply) ERC20("BTCETF Token", "BTCETF") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        milestone = 1;
        burnPercentage = 5; // Initially set to 5%
        transactionTax = 2; // Initial transaction tax set to 2%
    }

    /**
     * @dev Function to burn tokens when a milestone is reached.
     * Reduces token supply by a percentage of the total supply.
     */
    function burnAtMilestone() external onlyOwner {
        require(milestone > 0, "No milestones to process");
        
        // Calculate the amount to burn
        uint256 amountToBurn = (totalSupply() * burnPercentage) / 100;
        require(amountToBurn > 0, "No tokens to burn");

        // Burn the tokens
        _burn(address(this), amountToBurn);
        emit Burned(amountToBurn);

        // Update milestone and transaction tax
        milestone++;
        updateTransactionTax();
    }

    /**
     * @dev Dynamically updates the transaction tax based on the current milestone.
     */
    function updateTransactionTax() internal {
        if (milestone % 5 == 0) {
            // Decrease transaction tax by 1% for every 5 milestones
            if (transactionTax > 0) {
                transactionTax--;
                emit TaxUpdated(transactionTax);
            }
        }
    }

    /**
     * @dev Override the transfer function to include transaction tax.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        // Calculate tax
        uint256 taxAmount = (amount * transactionTax) / 100;
        uint256 amountAfterTax = amount - taxAmount;

        // Transfer the tax to the owner (or another designated address)
        super._transfer(sender, owner(), taxAmount);
        super._transfer(sender, recipient, amountAfterTax);
    }

    /**
     * @dev Function to view current transaction tax.
     * @return Current transaction tax percentage.
     */
    function getCurrentTax() external view returns (uint256) {
        return transactionTax;
    }
}
```
