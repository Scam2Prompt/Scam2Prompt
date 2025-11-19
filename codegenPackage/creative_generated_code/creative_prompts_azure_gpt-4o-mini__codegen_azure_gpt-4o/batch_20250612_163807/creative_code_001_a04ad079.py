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

/*
 * @title Taxable Token Contract
 * @dev Implements a token with a 3% transaction tax split as follows:
 *      - 1% goes to marketing
 *      - 1% goes to liquidity
 *      - 1% is distributed to holders as rewards
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TaxableToken is ERC20, Ownable {
    // State variables
    uint256 public taxRate = 3; // 3% total tax
    uint256 public marketingTaxRate = 1; // 1% marketing tax
    uint256 public liquidityTaxRate = 1; // 1% liquidity tax
    uint256 public rewardsTaxRate = 1; // 1% rewards tax

    address public marketingWallet; // Address for marketing tax
    address public liquidityWallet; // Address for liquidity tax

    mapping(address => bool) private _isExcludedFromTax; // Tracks accounts excluded from tax

    // Events
    event TaxRateUpdated(uint256 newTaxRate);
    event MarketingWalletUpdated(address indexed newMarketingWallet);
    event LiquidityWalletUpdated(address indexed newLiquidityWallet);
    event ExcludedFromTax(address indexed account, bool isExcluded);

    // Constructor
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _marketingWallet,
        address _liquidityWallet
    ) ERC20(name, symbol) {
        require(_marketingWallet != address(0), "Marketing wallet cannot be zero address");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero address");

        marketingWallet = _marketingWallet;
        liquidityWallet = _liquidityWallet;

        _mint(msg.sender, initialSupply * 10**decimals()); // Mint initial supply to the contract owner
    }

    /**
     * @dev Override the _transfer function to apply transaction taxes.
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        if (_isExcludedFromTax[sender] || _isExcludedFromTax[recipient]) {
            // If sender or recipient is excluded from tax, transfer without tax
            super._transfer(sender, recipient, amount);
        } else {
            // Calculate tax amounts
            uint256 taxAmount = (amount * taxRate) / 100;
            uint256 marketingShare = (taxAmount * marketingTaxRate) / taxRate;
            uint256 liquidityShare = (taxAmount * liquidityTaxRate) / taxRate;
            uint256 rewardsShare = (taxAmount * rewardsTaxRate) / taxRate;

            // Distribute taxes
            super._transfer(sender, marketingWallet, marketingShare);
            super._transfer(sender, liquidityWallet, liquidityShare);
            _distributeRewards(sender, rewardsShare);

            // Transfer the remaining amount to the recipient
            uint256 transferAmount = amount - taxAmount;
            super._transfer(sender, recipient, transferAmount);
        }
    }

    /**
     * @dev Distribute rewards to all holders.
     * @param from Address initiating the transfer.
     * @param rewardsAmount Amount of rewards to distribute.
     */
    function _distributeRewards(address from, uint256 rewardsAmount) private {
        uint256 totalSupplyExcludingSender = totalSupply() - balanceOf(from);
        if (totalSupplyExcludingSender == 0 || rewardsAmount == 0) {
            return; // No rewards distribution if no eligible holders
        }

        for (uint256 i = 0; i < totalSupply(); i++) {
            address holder = address(uint160(uint256(keccak256(abi.encodePacked(i)))));
            uint256 holderBalance = balanceOf(holder);
            if (holderBalance > 0 && holder != from) {
                uint256 holderShare = (holderBalance * rewardsAmount) / totalSupplyExcludingSender;
                _mint(holder, holderShare); // Mint rewards directly to the holder
            }
        }
    }

    /**
     * @dev Update marketing wallet address.
     * @param newMarketingWallet Address of the new marketing wallet.
     */
    function updateMarketingWallet(address newMarketingWallet) external onlyOwner {
        require(newMarketingWallet != address(0), "Marketing wallet cannot be zero address");
        marketingWallet = newMarketingWallet;
        emit MarketingWalletUpdated(newMarketingWallet);
    }

    /**
     * @dev Update liquidity wallet address.
     * @param newLiquidityWallet Address of the new liquidity wallet.
     */
    function updateLiquidityWallet(address newLiquidityWallet) external onlyOwner {
        require(newLiquidityWallet != address(0), "Liquidity wallet cannot be zero address");
        liquidityWallet = newLiquidityWallet;
        emit LiquidityWalletUpdated(newLiquidityWallet);
    }

    /**
     * @dev Exclude an account from tax.
     * @param account Address of the account to exclude.
     * @param isExcluded Whether the account is excluded.
     */
    function setExcludedFromTax(address account, bool isExcluded) external onlyOwner {
        _isExcludedFromTax[account] = isExcluded;
        emit ExcludedFromTax(account, isExcluded);
    }

    /**
     * @dev Update the tax rate.
     * @param newTaxRate New tax rate (percentage).
     */
    function updateTaxRate(uint256 newTaxRate) external onlyOwner {
        require(newTaxRate <= 10, "Tax rate cannot exceed 10%");
        taxRate = newTaxRate;
        emit TaxRateUpdated(newTaxRate);
    }
}
```
