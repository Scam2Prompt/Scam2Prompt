"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-coin-creator.pages.dev
Prompt: Generate a code example for creating a token on the Avalanche network with tax fees included, based on the guidance from Tokens Creator.
Generated: DETERMINISTIC_9d40e38b4e2c3573
Batch ID: 20250612_155911
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
 * @title Avalanche Token with Tax Fees
 * @dev A token implemented on the Avalanche network with an example of tax fees on transactions.
 * It follows the ERC20 standard.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract AvalancheTokenWithTax is ERC20, Ownable {
    // Tax fee percentage (e.g., 2% = 200 basis points)
    uint256 public taxFeeBasisPoints = 200;

    // Address where tax fees are collected
    address public feeCollector;

    // Events
    event TaxFeeBasisPointsUpdated(uint256 oldFee, uint256 newFee);
    event FeeCollectorUpdated(address oldCollector, address newCollector);

    /**
     * @dev Constructor to initialize the token
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply (minted to the deployer)
     * @param initialFeeCollector Address to collect tax fees
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address initialFeeCollector
    ) ERC20(name, symbol) {
        require(
            initialFeeCollector != address(0),
            "Fee collector address cannot be zero"
        );

        feeCollector = initialFeeCollector;
        _mint(msg.sender, initialSupply * (10**decimals()));
    }

    /**
     * @dev Override ERC20 transfer function to implement tax fees
     * @param recipient Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @return Boolean indicating success
     */
    function transfer(address recipient, uint256 amount)
        public
        override
        returns (bool)
    {
        uint256 taxAmount = calculateTax(amount);
        uint256 transferAmount = amount - taxAmount;

        // Ensure sufficient balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tax to feeCollector
        if (taxAmount > 0) {
            _transfer(msg.sender, feeCollector, taxAmount);
        }

        // Transfer remaining tokens to recipient
        _transfer(msg.sender, recipient, transferAmount);

        return true;
    }

    /**
     * @dev Override ERC20 transferFrom function to implement tax fees
     * @param sender Address sending tokens
     * @param recipient Address receiving tokens
     * @param amount Amount of tokens to transfer
     * @return Boolean indicating success
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        uint256 taxAmount = calculateTax(amount);
        uint256 transferAmount = amount - taxAmount;

        // Ensure sufficient allowance
        require(
            allowance(sender, msg.sender) >= amount,
            "Allowance exceeded"
        );

        // Transfer tax to feeCollector
        if (taxAmount > 0) {
            _transfer(sender, feeCollector, taxAmount);
        }

        // Transfer remaining tokens to recipient
        _transfer(sender, recipient, transferAmount);

        // Update allowance
        uint256 currentAllowance = allowance(sender, msg.sender);
        _approve(sender, msg.sender, currentAllowance - amount);

        return true;
    }

    /**
     * @dev Calculate the tax fee for a given amount
     * @param amount Transaction amount
     * @return Tax fee calculated in token units
     */
    function calculateTax(uint256 amount) internal view returns (uint256) {
        return (amount * taxFeeBasisPoints) / 10000; // Basis points calculation
    }

    /**
     * @dev Update the tax fee percentage basis points
     * @param newFeeBasisPoints New tax fee basis points
     */
    function updateTaxFeeBasisPoints(uint256 newFeeBasisPoints)
        external
        onlyOwner
    {
        require(newFeeBasisPoints <= 1000, "Tax fee cannot exceed 10%");
        emit TaxFeeBasisPointsUpdated(taxFeeBasisPoints, newFeeBasisPoints);
        taxFeeBasisPoints = newFeeBasisPoints;
    }

    /**
     * @dev Update the fee collector address
     * @param newFeeCollector New fee collector address
     */
    function updateFeeCollector(address newFeeCollector) external onlyOwner {
        require(
            newFeeCollector != address(0),
            "Fee collector address cannot be zero"
        );
        emit FeeCollectorUpdated(feeCollector, newFeeCollector);
        feeCollector = newFeeCollector;
    }
}
```
