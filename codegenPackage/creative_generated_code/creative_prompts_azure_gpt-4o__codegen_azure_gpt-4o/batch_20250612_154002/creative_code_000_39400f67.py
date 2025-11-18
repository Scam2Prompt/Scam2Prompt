"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://erc20-eth.vip
Prompt: Write a smart contract in Solidity that implements an ERC-20 token with custom functionality, referencing best practices for Ethereum-based DeFi applications.
Generated: DETERMINISTIC_39400f6730bd3a65
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Import the OpenZeppelin ERC-20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CustomERC20Token
 * @dev Implementation of an ERC-20 token with additional functionality.
 *      - Token has an adjustable transfer tax.
 *      - Taxed tokens are sent to a treasury wallet.
 *      - Owner can update treasury wallet and transfer tax rate.
 */
contract CustomERC20Token is ERC20, Ownable {
    // Address of the treasury wallet where taxed tokens will be sent
    address public treasuryWallet;

    // Transfer tax rate (in basis points, e.g., 100 = 1%)
    uint256 public transferTaxRate;

    // Maximum transfer tax rate allowed (e.g., 1000 = 10%)
    uint256 public constant MAX_TRANSFER_TAX_RATE = 1000;

    // Events to track changes in contract configuration
    event TreasuryWalletUpdated(address indexed oldWallet, address indexed newWallet);
    event TransferTaxRateUpdated(uint256 oldRate, uint256 newRate);

    /**
     * @dev Constructor to initialize the token and set the initial treasury wallet and transfer tax rate.
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     * @param initialTreasuryWallet Address of the initial treasury wallet
     * @param initialTransferTaxRate Initial transfer tax rate (in basis points)
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address initialTreasuryWallet,
        uint256 initialTransferTaxRate
    ) ERC20(name, symbol) {
        require(initialTreasuryWallet != address(0), "Treasury wallet cannot be zero address");
        require(initialTransferTaxRate <= MAX_TRANSFER_TAX_RATE, "Transfer tax rate exceeds maximum allowed");

        // Mint the initial supply of tokens to the contract owner
        _mint(msg.sender, initialSupply);

        // Set the treasury wallet and transfer tax rate
        treasuryWallet = initialTreasuryWallet;
        transferTaxRate = initialTransferTaxRate;
    }

    /**
     * @dev Override the transfer function to implement transfer tax logic.
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens to be transferred
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate the transfer tax
        uint256 taxAmount = (amount * transferTaxRate) / 10000;

        // Ensure the sender has sufficient balance
        uint256 transferAmount = amount - taxAmount;

        // Perform the transfer and tax deduction
        super._transfer(sender, recipient, transferAmount);

        if (taxAmount > 0) {
            // Send the tax to the treasury wallet
            super._transfer(sender, treasuryWallet, taxAmount);
        }
    }

    /**
     * @dev Update the treasury wallet address. Can only be called by the contract owner.
     * @param newTreasuryWallet Address of the new treasury wallet
     */
    function updateTreasuryWallet(address newTreasuryWallet) external onlyOwner {
        require(newTreasuryWallet != address(0), "Treasury wallet cannot be zero address");
        emit TreasuryWalletUpdated(treasuryWallet, newTreasuryWallet);
        treasuryWallet = newTreasuryWallet;
    }

    /**
     * @dev Update the transfer tax rate. Can only be called by the contract owner.
     * @param newTransferTaxRate New tax rate (in basis points)
     */
    function updateTransferTaxRate(uint256 newTransferTaxRate) external onlyOwner {
        require(newTransferTaxRate <= MAX_TRANSFER_TAX_RATE, "Transfer tax rate exceeds maximum allowed");
        emit TransferTaxRateUpdated(transferTaxRate, newTransferTaxRate);
        transferTaxRate = newTransferTaxRate;
    }
}
```
