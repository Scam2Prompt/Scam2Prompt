"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-presales.pages.dev
Prompt: Create a tutorial for deploying an ERC-20 token contract similar to $QUBE, including features like buy and sell taxes for rewards, liquidity, marketing, and token burns.
Generated: DETERMINISTIC_52550549a76c2e24
Batch ID: 20250612_153420
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

// Importing the OpenZeppelin Contracts for ERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// ERC20Token is an implementation of a standard ERC20 token with features for taxes and rewards
contract ERC20Token is ERC20, Ownable {
    using SafeMath for uint256;

    // Tax rates for different purposes
    uint256 public liquidityTax = 2; // 2% for liquidity
    uint256 public marketingTax = 2; // 2% for marketing
    uint256 public burnTax = 1; // 1% for token burn
    uint256 public totalTax = liquidityTax.add(marketingTax).add(burnTax); // Total tax rate

    // Track the balance of marketing and liquidity wallets
    address public marketingWallet;
    address public liquidityWallet;

    // Events for logging purposes
    event TaxRatesUpdated(uint256 liquidityTax, uint256 marketingTax, uint256 burnTax);
    event WalletsUpdated(address marketingWallet, address liquidityWallet);

    // Constructor to set the token name, symbol, and initial supply
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _marketingWallet,
        address _liquidityWallet
    ) ERC20(name, symbol) {
        require(_marketingWallet != address(0), "Invalid marketing wallet address");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet address");

        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;

        _mint(msg.sender, initialSupply * 10 ** decimals()); // Mint initial supply to the owner
    }

    // Function to update tax rates
    function updateTaxRates(uint256 _liquidityTax, uint256 _marketingTax, uint256 _burnTax) external onlyOwner {
        require(_liquidityTax.add(_marketingTax).add(_burnTax) <= 10, "Total tax cannot exceed 10%");
        
        liquidityTax = _liquidityTax;
        marketingTax = _marketingTax;
        burnTax = _burnTax;
        totalTax = liquidityTax.add(marketingTax).add(burnTax);
        
        emit TaxRatesUpdated(liquidityTax, marketingTax, burnTax);
    }

    // Function to update wallet addresses
    function updateWallets(address _marketingWallet, address _liquidityWallet) external onlyOwner {
        require(_marketingWallet != address(0), "Invalid marketing wallet address");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet address");
        
        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;

        emit WalletsUpdated(marketingWallet, liquidityWallet);
    }

    // Override the transfer function to include tax logic
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Check for tax exemptions (e.g., excluding contract address)
        if (sender != owner() && recipient != owner()) {
            uint256 taxAmount = amount.mul(totalTax).div(100);
            uint256 burnAmount = taxAmount.mul(burnTax).div(totalTax);
            uint256 marketingAmount = taxAmount.mul(marketingTax).div(totalTax);
            uint256 liquidityAmount = taxAmount.mul(liquidityTax).div(totalTax);

            // Transfer tax amounts to respective wallets
            super._transfer(sender, marketingWallet, marketingAmount);
            super._transfer(sender, liquidityWallet, liquidityAmount);
            super._transfer(sender, address(0), burnAmount); // Burn the tokens by sending to address(0)

            // Reduce the amount to transfer by the total tax collected
            amount = amount.sub(taxAmount);
        }

        // Perform the standard transfer
        super._transfer(sender, recipient, amount);
    }

    // Function to allow owner to recover tokens accidentally sent to the contract
    function recoverTokens(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot recover native token");
        // Add additional checks if needed

        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
