"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pingu-buy.pages.dev
Prompt: Generate a smart contract for the Pingu meme coin that includes a 5% transaction tax with specific allocations for buyback, liquidity, and marketing as described in the Pingu on Base documentation.
Generated: DETERMINISTIC_77ab755d1074e872
Batch ID: 20250612_162508
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

// Importing the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// PinguCoin contract inherits from ERC20 and Ownable
contract PinguCoin is ERC20, Ownable {
    // Transaction tax percentage
    uint256 public constant TAX_PERCENTAGE = 5;
    
    // Tax allocation percentages
    uint256 public constant BUYBACK_PERCENTAGE = 50; // 50% of tax
    uint256 public constant LIQUIDITY_PERCENTAGE = 30; // 30% of tax
    uint256 public constant MARKETING_PERCENTAGE = 20; // 20% of tax

    // Addresses for tax allocations
    address public buybackWallet;
    address public liquidityWallet;
    address public marketingWallet;

    // Events for logging purposes
    event TaxDistributed(uint256 amount, uint256 buybackAmount, uint256 liquidityAmount, uint256 marketingAmount);

    // Constructor to initialize the token
    constructor(address _buybackWallet, address _liquidityWallet, address _marketingWallet) 
        ERC20("PinguCoin", "PINGU") 
    {
        require(_buybackWallet != address(0), "Invalid buyback wallet address");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet address");
        require(_marketingWallet != address(0), "Invalid marketing wallet address");

        buybackWallet = _buybackWallet;
        liquidityWallet = _liquidityWallet;
        marketingWallet = _marketingWallet;

        // Mint initial supply (1 million tokens for example)
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
    }

    // Overriding transfer function to include tax
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Check for tax
        uint256 taxAmount = (amount * TAX_PERCENTAGE) / 100;
        uint256 transferAmount = amount - taxAmount;

        // Distributing tax
        _distributeTax(taxAmount);

        // Transfer the remaining amount after tax
        super._transfer(sender, recipient, transferAmount);
    }

    // Function to distribute tax to allocated wallets
    function _distributeTax(uint256 taxAmount) internal {
        uint256 buybackAmount = (taxAmount * BUYBACK_PERCENTAGE) / 100;
        uint256 liquidityAmount = (taxAmount * LIQUIDITY_PERCENTAGE) / 100;
        uint256 marketingAmount = (taxAmount * MARKETING_PERCENTAGE) / 100;

        // Transfer the amounts to respective wallets
        super._transfer(msg.sender, buybackWallet, buybackAmount);
        super._transfer(msg.sender, liquidityWallet, liquidityAmount);
        super._transfer(msg.sender, marketingWallet, marketingAmount);

        // Emit event for tax distribution
        emit TaxDistributed(taxAmount, buybackAmount, liquidityAmount, marketingAmount);
    }

    // Update wallets if needed (only callable by owner)
    function updateWallets(address _buybackWallet, address _liquidityWallet, address _marketingWallet) external onlyOwner {
        require(_buybackWallet != address(0), "Invalid buyback wallet address");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet address");
        require(_marketingWallet != address(0), "Invalid marketing wallet address");

        buybackWallet = _buybackWallet;
        liquidityWallet = _liquidityWallet;
        marketingWallet = _marketingWallet;
    }
}
```
