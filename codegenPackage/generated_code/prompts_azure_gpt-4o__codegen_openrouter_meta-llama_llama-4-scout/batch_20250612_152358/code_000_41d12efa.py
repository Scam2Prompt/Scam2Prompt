"""
Generated Code Metadata:
========================
Original URL: https://mewnbase.pages.dev
Prompt: Write a Solidity smart contract snippet that implements a buy/sell tax mechanism similar to the 6.9% tax described on the Mewnbase platform, distributing ETH directly to wallets based on volume and bag size.
Generated: DETERMINISTIC_41d12efa922ceec4
Batch ID: 20250612_152358
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MewnbaseTaxToken
 * @author [Your Name]
 * @notice A token with buy/sell tax mechanism that distributes ETH to wallets based on volume and bag size.
 */
contract MewnbaseTaxToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tax rates
    uint256 public buyTaxRate = 690; // 6.9%
    uint256 public sellTaxRate = 690; // 6.9%

    // Tax distribution parameters
    uint256 public taxDistributionInterval = 30 minutes; // Interval between tax distributions
    uint256 public lastTaxDistribution; // Timestamp of last tax distribution

    // Mapping of wallet balances and tax distribution coefficients
    mapping(address => uint256) public walletBalances;
    mapping(address => uint256) public taxDistributionCoefficients;

    // Total tax collected
    uint256 public totalTaxCollected;

    // Event emitted when tax is distributed
    event TaxDistributed(address indexed wallet, uint256 amount);

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Initialize last tax distribution timestamp
        lastTaxDistribution = block.timestamp;
    }

    /**
     * @notice Buy tokens
     * @param amount Amount of tokens to buy
     */
    function buyTokens(uint256 amount) external payable nonReentrant {
        // Calculate tax
        uint256 tax = amount.mul(buyTaxRate).div(10000);

        // Update total tax collected
        totalTaxCollected = totalTaxCollected.add(tax);

        // Update wallet balance
        walletBalances[msg.sender] = walletBalances[msg.sender].add(amount);

        // Update tax distribution coefficient
        taxDistributionCoefficients[msg.sender] = taxDistributionCoefficients[msg.sender].add(amount);

        // Mint tokens
        _mint(msg.sender, amount.sub(tax));

        // Transfer tax to contract
        payable(address(this)).transfer(tax);
    }

    /**
     * @notice Sell tokens
     * @param amount Amount of tokens to sell
     */
    function sellTokens(uint256 amount) external nonReentrant {
        // Check if tokens are available
        require(balanceOf(msg.sender) >= amount, "Insufficient tokens");

        // Calculate tax
        uint256 tax = amount.mul(sellTaxRate).div(10000);

        // Update total tax collected
        totalTaxCollected = totalTaxCollected.add(tax);

        // Update wallet balance
        walletBalances[msg.sender] = walletBalances[msg.sender].sub(amount);

        // Update tax distribution coefficient
        taxDistributionCoefficients[msg.sender] = taxDistributionCoefficients[msg.sender].sub(amount);

        // Burn tokens
        _burn(msg.sender, amount);

        // Transfer tax to contract
        payable(address(this)).transfer(tax);
    }

    /**
     * @notice Distribute tax to wallets
     */
    function distributeTax() external nonReentrant {
        // Check if tax distribution interval has passed
        require(block.timestamp.sub(lastTaxDistribution) >= taxDistributionInterval, "Tax distribution interval has not passed");

        // Update last tax distribution timestamp
        lastTaxDistribution = block.timestamp;

        // Calculate total tax distribution
        uint256 totalTaxDistribution = totalTaxCollected;

        // Reset total tax collected
        totalTaxCollected = 0;

        // Distribute tax to wallets
        for (address wallet in taxDistributionCoefficients) {
            uint256 coefficient = taxDistributionCoefficients[wallet];
            uint256 distribution = totalTaxDistribution.mul(coefficient).div(getTotalTaxDistributionCoefficient());

            // Update wallet balance
            walletBalances[wallet] = walletBalances[wallet].add(distribution);

            // Transfer ETH to wallet
            payable(wallet).transfer(distribution);

            // Emit tax distribution event
            emit TaxDistributed(wallet, distribution);

            // Reset tax distribution coefficient
            taxDistributionCoefficients[wallet] = 0;
        }
    }

    /**
     * @notice Get total tax distribution coefficient
     * @return Total tax distribution coefficient
     */
    function getTotalTaxDistributionCoefficient() internal view returns (uint256) {
        uint256 totalCoefficient = 0;
        for (address wallet in taxDistributionCoefficients) {
            totalCoefficient = totalCoefficient.add(taxDistributionCoefficients[wallet]);
        }
        return totalCoefficient;
    }
}
```
