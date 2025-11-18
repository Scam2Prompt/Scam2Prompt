"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hummingbirdonbnb.pages.dev
Prompt: Develop a smart contract in Solidity for a low-tax token similar to $HMNG, with 1% liquidity addition, 1% marketing fund allocation, and 1% USDT rewards distribution.
Generated: DETERMINISTIC_1051db27d1113359
Batch ID: 20250612_151343
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

// Importing OpenZeppelin's ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LowTaxToken is ERC20, Ownable {
    // Tax rates
    uint256 public constant LIQUIDITY_TAX = 1; // 1% for liquidity
    uint256 public constant MARKETING_TAX = 1; // 1% for marketing
    uint256 public constant REWARD_TAX = 1; // 1% for USDT rewards

    // Total tax rate
    uint256 public constant TOTAL_TAX = LIQUIDITY_TAX + MARKETING_TAX + REWARD_TAX;

    // Events for logging purposes
    event TaxDistributed(uint256 liquidity, uint256 marketing, uint256 rewards);

    // Constructor to set the token name and symbol
    constructor() ERC20("LowTaxToken", "LTT") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Initial mint of 1,000,000 tokens to the deployer
    }

    // Override transfer function to include tax distribution
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate tax amount
        uint256 taxAmount = (amount * TOTAL_TAX) / 100;
        uint256 amountAfterTax = amount - taxAmount;

        // Distribute taxes
        uint256 liquidityAmount = (taxAmount * LIQUIDITY_TAX) / TOTAL_TAX;
        uint256 marketingAmount = (taxAmount * MARKETING_TAX) / TOTAL_TAX;
        uint256 rewardsAmount = (taxAmount * REWARD_TAX) / TOTAL_TAX;

        // Ensure sufficient balance to cover tax
        require(balanceOf(sender) >= amount, "Insufficient balance for transfer");

        // Transfer the amount after tax to the recipient
        super._transfer(sender, recipient, amountAfterTax);

        // Here we would implement the logic to handle the distributed taxes (liquidity, marketing, rewards)
        // This example assumes that these amounts are sent to designated addresses or handled in a separate function

        // Emit event for tax distribution
        emit TaxDistributed(liquidityAmount, marketingAmount, rewardsAmount);
    }
    
    // Function to withdraw funds (onlyOwner) for marketing or liquidity
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        payable(owner()).transfer(amount);
    }

    // Fallback function to accept Ether
    receive() external payable {}

    // Function to retrieve contract balance
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
