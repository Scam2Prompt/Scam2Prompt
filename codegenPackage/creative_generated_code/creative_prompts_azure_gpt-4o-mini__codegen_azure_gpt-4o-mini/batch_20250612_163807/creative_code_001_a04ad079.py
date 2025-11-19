"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hummingbirdonbnb.pages.dev
Prompt: Write a smart contract for a token that applies a 3% transaction tax, distributing 1% to marketing, 1% to liquidity, and 1% as rewards to holders, as seen in Hummingbird Finance.
Generated: DETERMINISTIC_a04ad07923e55351
Batch ID: 20250612_163807
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract HummingbirdToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Transaction tax percentage
    uint256 public transactionTaxPercentage = 3;
    
    // Distribution percentages
    uint256 public marketingShare = 1;  // 1% for marketing
    uint256 public liquidityShare = 1;   // 1% for liquidity
    uint256 public rewardsShare = 1;     // 1% for rewards

    address public marketingWallet; // Wallet for marketing funds
    address public liquidityWallet;  // Wallet for liquidity funds

    mapping(address => bool) public isExcludedFromTax; // Exclusion list

    event TaxUpdated(uint256 newTaxPercentage);
    event WalletUpdated(address marketingWallet, address liquidityWallet);

    constructor(address _marketingWallet, address _liquidityWallet) ERC20("HummingbirdToken", "HBT") {
        require(_marketingWallet != address(0), "Marketing wallet cannot be the zero address");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be the zero address");

        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;

        // Mint initial supply to the owner
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to update the wallet addresses
    function updateWallets(address _marketingWallet, address _liquidityWallet) external onlyOwner {
        require(_marketingWallet != address(0), "Marketing wallet cannot be the zero address");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be the zero address");
        
        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;

        emit WalletUpdated(marketingWallet, liquidityWallet);
    }

    // Function to exclude an address from transaction tax
    function excludeFromTax(address account) external onlyOwner {
        isExcludedFromTax[account] = true;
    }

    // Function to include an address back to transaction tax
    function includeInTax(address account) external onlyOwner {
        isExcludedFromTax[account] = false;
    }

    // Override the transfer function to implement the transaction tax
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        uint256 taxAmount = 0;

        // Apply tax if sender is not excluded
        if(!isExcludedFromTax[sender]) {
            taxAmount = amount.mul(transactionTaxPercentage).div(100);
            uint256 marketingAmount = taxAmount.mul(marketingShare).div(transactionTaxPercentage);
            uint256 liquidityAmount = taxAmount.mul(liquidityShare).div(transactionTaxPercentage);
            uint256 rewardsAmount = taxAmount.mul(rewardsShare).div(transactionTaxPercentage);

            // Distributing the tax
            super._transfer(sender, marketingWallet, marketingAmount);
            super._transfer(sender, liquidityWallet, liquidityAmount);
            // Rewards distribution logic can be implemented here

            // Reduce the amount to be sent to recipient by the tax amount
            amount = amount.sub(taxAmount);
        }

        // Proceed with the normal transfer
        super._transfer(sender, recipient, amount);
    }
}
```
