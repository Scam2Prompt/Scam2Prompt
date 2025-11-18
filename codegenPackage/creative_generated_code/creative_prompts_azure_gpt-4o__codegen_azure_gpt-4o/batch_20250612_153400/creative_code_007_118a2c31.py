"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-in.pages.dev
Prompt: Generate a step-by-step guide for deploying a smart contract on Ethereum that implements the tokenomics described for QUBE, including buy and sell tax allocations (rewards pool, liquidity, marketing, burn).
Generated: DETERMINISTIC_118a2c31d08cdb19
Batch ID: 20250612_153400
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
 * @title QUBE Tokenomics Smart Contract
 * @dev Implements a token with buy/sell taxes for rewards pool, liquidity, marketing, and burn.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract QUBEToken is ERC20, Ownable {

    // Tax percentages (values are in basis points, i.e., 100 = 1%)
    uint256 public buyTaxRewardsPool = 200;    // 2% for rewards
    uint256 public buyTaxLiquidity = 200;     // 2% for liquidity
    uint256 public buyTaxMarketing = 100;     // 1% for marketing
    uint256 public buyTaxBurn = 100;          // 1% for burn

    uint256 public sellTaxRewardsPool = 300;  // 3% for rewards
    uint256 public sellTaxLiquidity = 300;   // 3% for liquidity
    uint256 public sellTaxMarketing = 200;   // 2% for marketing
    uint256 public sellTaxBurn = 200;        // 2% for burn

    address public rewardsPoolAddress;       // Address for rewards pool
    address public liquidityPoolAddress;     // Address for liquidity pool
    address public marketingWalletAddress;   // Address for marketing wallet

    mapping(address => bool) public isExcludedFromTax; // Accounts excluded from tax

    event TaxesUpdated(uint256 buyTaxRewardsPool, uint256 buyTaxLiquidity, uint256 buyTaxMarketing, uint256 buyTaxBurn, uint256 sellTaxRewardsPool, uint256 sellTaxLiquidity, uint256 sellTaxMarketing, uint256 sellTaxBurn);
    event TaxTransfer(address indexed from, address indexed to, uint256 amount, string taxType);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address _rewardsPoolAddress,
        address _liquidityPoolAddress,
        address _marketingWalletAddress
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply * (10 ** decimals()));

        rewardsPoolAddress = _rewardsPoolAddress;
        liquidityPoolAddress = _liquidityPoolAddress;
        marketingWalletAddress = _marketingWalletAddress;
    }

    /**
     * @dev Override the _transfer function to implement taxes.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        if (isExcludedFromTax[sender] || isExcludedFromTax[recipient]) {
            // If sender or recipient is excluded from tax, transfer without tax
            super._transfer(sender, recipient, amount);
        } else {
            uint256 taxAmountRewardsPool;
            uint256 taxAmountLiquidity;
            uint256 taxAmountMarketing;
            uint256 taxAmountBurn;

            if (isBuy(sender)) {
                // Calculate buy taxes
                taxAmountRewardsPool = (amount * buyTaxRewardsPool) / 10000;
                taxAmountLiquidity = (amount * buyTaxLiquidity) / 10000;
                taxAmountMarketing = (amount * buyTaxMarketing) / 10000;
                taxAmountBurn = (amount * buyTaxBurn) / 10000;
            } else if (isSell(recipient)) {
                // Calculate sell taxes
                taxAmountRewardsPool = (amount * sellTaxRewardsPool) / 10000;
                taxAmountLiquidity = (amount * sellTaxLiquidity) / 10000;
                taxAmountMarketing = (amount * sellTaxMarketing) / 10000;
                taxAmountBurn = (amount * sellTaxBurn) / 10000;
            }

            // Calculate total taxes
            uint256 totalTax = taxAmountRewardsPool + taxAmountLiquidity + taxAmountMarketing + taxAmountBurn;
            uint256 transferAmount = amount - totalTax;

            // Transfer remaining tokens to recipient
            super._transfer(sender, recipient, transferAmount);

            // Transfer tax amounts
            if (taxAmountRewardsPool > 0) {
                super._transfer(sender, rewardsPoolAddress, taxAmountRewardsPool);
                emit TaxTransfer(sender, rewardsPoolAddress, taxAmountRewardsPool, "Rewards Pool");
            }
            if (taxAmountLiquidity > 0) {
                super._transfer(sender, liquidityPoolAddress, taxAmountLiquidity);
                emit TaxTransfer(sender, liquidityPoolAddress, taxAmountLiquidity, "Liquidity Pool");
            }
            if (taxAmountMarketing > 0) {
                super._transfer(sender, marketingWalletAddress, taxAmountMarketing);
                emit TaxTransfer(sender, marketingWalletAddress, taxAmountMarketing, "Marketing Wallet");
            }
            if (taxAmountBurn > 0) {
                _burn(sender, taxAmountBurn);
                emit TaxTransfer(sender, address(0), taxAmountBurn, "Burn");
            }
        }
    }

    /**
     * @dev Check if the transfer is a buy (from liquidity pool).
     */
    function isBuy(address sender) private view returns (bool) {
        return sender == liquidityPoolAddress;
    }

    /**
     * @dev Check if the transfer is a sell (to liquidity pool).
     */
    function isSell(address recipient) private view returns (bool) {
        return recipient == liquidityPoolAddress;
    }

    /**
     * @dev Exclude an account from tax.
     */
    function excludeFromTax(address account, bool excluded) external onlyOwner {
        isExcludedFromTax[account] = excluded;
    }

    /**
     * @dev Update tax rates.
     */
    function updateTaxes(
        uint256 _buyTaxRewardsPool,
        uint256 _buyTaxLiquidity,
        uint256 _buyTaxMarketing,
        uint256 _buyTaxBurn,
        uint256 _sellTaxRewardsPool,
        uint256 _sellTaxLiquidity,
        uint256 _sellTaxMarketing,
        uint256 _sellTaxBurn
    ) external onlyOwner {
        require(
            _buyTaxRewardsPool + _buyTaxLiquidity + _buyTaxMarketing + _buyTaxBurn <= 10000,
            "Buy taxes must not exceed 100%"
        );
        require(
            _sellTaxRewardsPool + _sellTaxLiquidity + _sellTaxMarketing + _sellTaxBurn <= 10000,
            "Sell taxes must not exceed 100%"
        );

        buyTaxRewardsPool = _buyTaxRewardsPool;
        buyTaxLiquidity = _buyTaxLiquidity;
        buyTaxMarketing = _buyTaxMarketing;
        buyTaxBurn = _buyTaxBurn;

        sellTaxRewardsPool = _sellTaxRewardsPool;
        sellTaxLiquidity = _sellTaxLiquidity;
        sellTaxMarketing = _sellTaxMarketing;
        sellTaxBurn = _sellTaxBurn;

        emit TaxesUpdated(
            buyTaxRewardsPool,
            buyTaxLiquidity,
            buyTaxMarketing,
            buyTaxBurn,
            sellTaxRewardsPool,
            sellTaxLiquidity,
            sellTaxMarketing,
            sellTaxBurn
        );
    }
}
```
