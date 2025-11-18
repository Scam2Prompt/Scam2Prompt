"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenscreator.pages.dev
Prompt: Generate Solidity code for creating a token on Goerli TestNet with the features of liquidity and tax fee, inspired by Tokens Creator.
Generated: DETERMINISTIC_d751db7cd7bc021f
Batch ID: 20250612_145916
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
 * @title Taxable Liquidity Token
 * @dev ERC20 token with liquidity and tax fee features, deployable on Goerli TestNet.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TaxableLiquidityToken is ERC20, Ownable {
    uint256 public taxFee; // Tax fee percentage (e.g., 3 for 3%)
    uint256 public liquidityFee; // Liquidity fee percentage (e.g., 2 for 2%)
    address public liquidityWallet; // Wallet to collect liquidity fees

    event TaxFeeUpdated(uint256 newTaxFee);
    event LiquidityFeeUpdated(uint256 newLiquidityFee);
    event LiquidityWalletUpdated(address newLiquidityWallet);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _taxFee,
        uint256 _liquidityFee,
        address _liquidityWallet
    ) ERC20(name, symbol) {
        require(_taxFee + _liquidityFee <= 100, "Fees cannot exceed 100%");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet address");

        _mint(msg.sender, initialSupply * 10**decimals());
        taxFee = _taxFee;
        liquidityFee = _liquidityFee;
        liquidityWallet = _liquidityWallet;
    }

    /**
     * @dev Overrides the transfer function to include tax and liquidity fees.
     * @param recipient The recipient of the transfer.
     * @param amount The amount to transfer.
     * @return A boolean indicating whether the operation succeeded.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 taxAmount = (amount * taxFee) / 100;
        uint256 liquidityAmount = (amount * liquidityFee) / 100;
        uint256 transferAmount = amount - taxAmount - liquidityAmount;

        // Transfer tax fee to contract owner
        _transfer(_msgSender(), owner(), taxAmount);

        // Transfer liquidity fee to liquidity wallet
        _transfer(_msgSender(), liquidityWallet, liquidityAmount);

        // Transfer remaining amount to recipient
        _transfer(_msgSender(), recipient, transferAmount);

        return true;
    }

    /**
     * @dev Allows the owner to update the tax fee percentage.
     * @param newTaxFee The new tax fee percentage.
     */
    function updateTaxFee(uint256 newTaxFee) external onlyOwner {
        require(newTaxFee + liquidityFee <= 100, "Total fees cannot exceed 100%");
        taxFee = newTaxFee;
        emit TaxFeeUpdated(newTaxFee);
    }

    /**
     * @dev Allows the owner to update the liquidity fee percentage.
     * @param newLiquidityFee The new liquidity fee percentage.
     */
    function updateLiquidityFee(uint256 newLiquidityFee) external onlyOwner {
        require(taxFee + newLiquidityFee <= 100, "Total fees cannot exceed 100%");
        liquidityFee = newLiquidityFee;
        emit LiquidityFeeUpdated(newLiquidityFee);
    }

    /**
     * @dev Allows the owner to update the liquidity wallet address.
     * @param newLiquidityWallet The new liquidity wallet address.
     */
    function updateLiquidityWallet(address newLiquidityWallet) external onlyOwner {
        require(newLiquidityWallet != address(0), "Invalid liquidity wallet address");
        liquidityWallet = newLiquidityWallet;
        emit LiquidityWalletUpdated(newLiquidityWallet);
    }
}
```
