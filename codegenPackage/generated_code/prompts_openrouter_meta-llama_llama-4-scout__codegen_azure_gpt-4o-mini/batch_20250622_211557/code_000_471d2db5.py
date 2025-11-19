"""
Generated Code Metadata:
========================
Original URL: https://erc20-creator.pages.dev
Prompt: Write a Solidity smart contract code for creating an ERC20 token with liquidity and tax fee on Ethereum network.
Generated: DETERMINISTIC_471d2db53855ab05
Batch ID: 20250622_211557
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

// Importing the ERC20 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Creating the ERC20Token contract that inherits from ERC20 and Ownable
contract ERC20Token is ERC20, Ownable {
    // State variables for liquidity and tax fees
    uint256 public liquidityFee; // Fee for liquidity
    uint256 public taxFee;       // Tax fee
    address public liquidityWallet; // Wallet to receive liquidity fees

    // Events for logging fee changes
    event FeesUpdated(uint256 liquidityFee, uint256 taxFee);
    event LiquidityWalletUpdated(address indexed newWallet);

    // Constructor to initialize the token with name, symbol, and fees
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _liquidityFee,
        uint256 _taxFee,
        address _liquidityWallet
    ) ERC20(name, symbol) {
        require(_liquidityFee + _taxFee <= 100, "Total fee must be <= 100");
        liquidityFee = _liquidityFee;
        taxFee = _taxFee;
        liquidityWallet = _liquidityWallet;

        // Mint the initial supply to the contract deployer
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    // Function to update the liquidity and tax fees
    function updateFees(uint256 _liquidityFee, uint256 _taxFee) external onlyOwner {
        require(_liquidityFee + _taxFee <= 100, "Total fee must be <= 100");
        liquidityFee = _liquidityFee;
        taxFee = _taxFee;
        emit FeesUpdated(liquidityFee, taxFee);
    }

    // Function to update the liquidity wallet address
    function updateLiquidityWallet(address _liquidityWallet) external onlyOwner {
        require(_liquidityWallet != address(0), "Invalid address");
        liquidityWallet = _liquidityWallet;
        emit LiquidityWalletUpdated(_liquidityWallet);
    }

    // Override the _transfer function to include fee logic
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate fees
        uint256 liquidityAmount = (amount * liquidityFee) / 100;
        uint256 taxAmount = (amount * taxFee) / 100;
        uint256 totalFee = liquidityAmount + taxAmount;

        // Ensure the sender has enough balance
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Transfer the fee amounts to the liquidity wallet
        if (liquidityAmount > 0) {
            super._transfer(sender, liquidityWallet, liquidityAmount);
        }
        if (taxAmount > 0) {
            super._transfer(sender, owner(), taxAmount); // Send tax to owner
        }

        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, amount - totalFee);
    }
}
```
