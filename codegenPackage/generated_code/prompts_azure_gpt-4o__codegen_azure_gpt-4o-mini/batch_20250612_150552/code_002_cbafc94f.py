"""
Generated Code Metadata:
========================
Original URL: https://burncat-buy.pages.dev
Prompt: Develop a Solidity smart contract to implement a dynamic tax system for token transactions, where the tax starts at 50% for the first 20 minutes after listing and decreases to 1% thereafter, as described for $BCAT.
Generated: DETERMINISTIC_cbafc94fef168cf9
Batch ID: 20250612_150552
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

/**
 * @title DynamicTaxToken
 * @dev A token with a dynamic tax system that decreases over time.
 */
contract DynamicTaxToken is ERC20, Ownable {
    // Tax rates
    uint256 public constant INITIAL_TAX_RATE = 50; // 50%
    uint256 public constant FINAL_TAX_RATE = 1;    // 1%
    uint256 public constant TAX_DECREASE_DURATION = 20 minutes; // Duration for initial tax rate

    // Timestamp when the contract was deployed
    uint256 public listingTime;

    // Event to log tax changes
    event TaxRateChanged(uint256 newTaxRate);

    constructor() ERC20("DynamicTaxToken", "DTT") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
        listingTime = block.timestamp; // Set listing time to current block timestamp
    }

    /**
     * @dev Calculates the current tax rate based on the time since listing.
     * @return The current tax rate as a percentage.
     */
    function getCurrentTaxRate() public view returns (uint256) {
        if (block.timestamp < listingTime + TAX_DECREASE_DURATION) {
            return INITIAL_TAX_RATE; // Return initial tax rate if within the first 20 minutes
        } else {
            return FINAL_TAX_RATE; // Return final tax rate after 20 minutes
        }
    }

    /**
     * @dev Overrides the transfer function to apply tax on transfers.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 taxRate = getCurrentTaxRate();
        uint256 taxAmount = (amount * taxRate) / 100; // Calculate tax amount
        uint256 amountAfterTax = amount - taxAmount; // Calculate amount after tax

        // Ensure the sender has enough balance after tax
        require(balanceOf(msg.sender) >= amount, "Insufficient balance for transfer");

        // Transfer the tax amount to the contract owner
        _transfer(msg.sender, owner(), taxAmount);
        // Transfer the remaining amount to the recipient
        _transfer(msg.sender, recipient, amountAfterTax);

        return true;
    }

    /**
     * @dev Allows the owner to withdraw any tokens sent to the contract.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(this), "Cannot withdraw native tokens");
        IERC20(token).transfer(owner(), amount);
    }
}
```
