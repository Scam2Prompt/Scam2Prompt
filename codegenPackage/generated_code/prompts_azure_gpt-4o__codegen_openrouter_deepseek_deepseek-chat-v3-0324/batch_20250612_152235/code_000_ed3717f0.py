"""
Generated Code Metadata:
========================
Original URL: https://kakaxa.pages.dev
Prompt: Write a smart contract for a meme cryptocurrency like $KAKAXA, incorporating tokenomics with percentages for liquidity pools, marketing, and holder rewards as described in the roadmap.
Generated: DETERMINISTIC_ed3717f021a0836f
Batch ID: 20250612_152235
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract KAKAXA is ERC20, Ownable {
    using SafeMath for uint256;

    // Tokenomics parameters
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant LIQUIDITY_POOL_PERCENT = 50; // 50%
    uint256 public constant MARKETING_PERCENT = 20; // 20%
    uint256 public constant HOLDER_REWARDS_PERCENT = 20; // 20%
    uint256 public constant TEAM_PERCENT = 10; // 10%

    // Addresses
    address public liquidityPoolAddress;
    address public marketingAddress;
    address public holderRewardsAddress;
    address public teamAddress;

    // Tax rates (in basis points, 100 = 1%)
    uint256 public buyTaxRate = 500; // 5%
    uint256 public sellTaxRate = 500; // 5%
    uint256 public transferTaxRate = 200; // 2%

    // Anti-whale measures
    uint256 public maxHoldPercentage = 2; // 2% of total supply
    uint256 public maxTxPercentage = 1; // 1% of total supply

    // Trading controls
    bool public tradingEnabled = false;
    mapping(address => bool) public isExcludedFromFee;

    // Events
    event TradingEnabled();
    event TaxRatesUpdated(uint256 buyTax, uint256 sellTax, uint256 transferTax);
    event MaxHoldPercentageUpdated(uint256 newPercentage);
    event MaxTxPercentageUpdated(uint256 newPercentage);
    event AddressesUpdated(
        address liquidityPool,
        address marketing,
        address holderRewards,
        address team
    );

    constructor(
        address _liquidityPoolAddress,
        address _marketingAddress,
        address _holderRewardsAddress,
        address _teamAddress
    ) ERC20("KAKAXA", "KAKAXA") {
        require(
            _liquidityPoolAddress != address(0) &&
                _marketingAddress != address(0) &&
                _holderRewardsAddress != address(0) &&
                _teamAddress != address(0),
            "Zero address not allowed"
        );

        liquidityPoolAddress = _liquidityPoolAddress;
        marketingAddress = _marketingAddress;
        holderRewardsAddress = _holderRewardsAddress;
        teamAddress = _teamAddress;

        // Mint tokens according to tokenomics
        _mint(liquidityPoolAddress, TOTAL_SUPPLY.mul(LIQUIDITY_POOL_PERCENT).div(100));
        _mint(marketingAddress, TOTAL_SUPPLY.mul(MARKETING_PERCENT).div(100));
        _mint(holderRewardsAddress, TOTAL_SUPPLY.mul(HOLDER_REWARDS_PERCENT).div(100));
        _mint(teamAddress, TOTAL_SUPPLY.mul(TEAM_PERCENT).div(100));

        // Exclude owner and contract addresses from fees
        isExcludedFromFee[owner()] = true;
        isExcludedFromFee[address(this)] = true;
        isExcludedFromFee[liquidityPoolAddress] = true;
        isExcludedFromFee[marketingAddress] = true;
        isExcludedFromFee[holderRewardsAddress] = true;
        isExcludedFromFee[teamAddress] = true;
    }

    function enableTrading() external onlyOwner {
        require(!tradingEnabled, "Trading already enabled");
        tradingEnabled = true;
        emit TradingEnabled();
    }

    function setTaxRates(
        uint256 _buyTaxRate,
        uint256 _sellTaxRate,
        uint256 _transferTaxRate
    ) external onlyOwner {
        require(
            _buyTaxRate <= 1000 && _sellTaxRate <= 1000 && _transferTaxRate <= 1000,
            "Tax rate cannot exceed 10%"
        );
        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;
        transferTaxRate = _transferTaxRate;
        emit TaxRatesUpdated(_buyTaxRate, _sellTaxRate, _transferTaxRate);
    }

    function setMaxHoldPercentage(uint256 _maxHoldPercentage) external onlyOwner {
        require(_maxHoldPercentage <= 5, "Cannot exceed 5%");
        maxHoldPercentage = _maxHoldPercentage;
        emit MaxHoldPercentageUpdated(_maxHoldPercentage);
    }

    function setMaxTxPercentage(uint256 _maxTxPercentage) external onlyOwner {
        require(_maxTxPercentage <= 5, "Cannot exceed 5%");
        maxTxPercentage = _maxTxPercentage;
        emit MaxTxPercentageUpdated(_maxTxPercentage);
    }

    function setAddresses(
        address _liquidityPoolAddress,
        address _marketingAddress,
        address _holderRewardsAddress,
        address _teamAddress
    ) external onlyOwner {
        require(
            _liquidityPoolAddress != address(0) &&
                _marketingAddress != address(0) &&
                _holderRewardsAddress != address(0) &&
                _teamAddress != address(0),
            "Zero address not allowed"
        );
        liquidityPoolAddress = _liquidityPoolAddress;
        marketingAddress = _marketingAddress;
        holderRewardsAddress = _holderRewardsAddress;
        teamAddress = _teamAddress;
        emit AddressesUpdated(
            _liquidityPoolAddress,
            _marketingAddress,
            _holderRewardsAddress,
            _teamAddress
        );
    }

    function excludeFromFee(address account, bool excluded) external onlyOwner {
        isExcludedFromFee[account] = excluded;
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        if (!tradingEnabled) {
            require(
                sender == owner() || recipient == owner(),
                "Trading is not enabled yet"
            );
        }

        // Check max transaction limit
        uint256 maxTxAmount = TOTAL_SUPPLY.mul(maxTxPercentage).div(100);
        require(amount <= maxTxAmount, "Transfer amount exceeds max transaction limit");

        // Check max holding limit (only for non-excluded addresses)
        if (!isExcludedFromFee[recipient]) {
            uint256 maxHoldAmount = TOTAL_SUPPLY.mul(maxHoldPercentage).div(100);
            require(
                balanceOf(recipient).add(amount) <= maxHoldAmount,
                "Recipient would exceed max holding limit"
            );
        }

        // Calculate tax
        uint256 taxAmount = 0;
        if (!isExcludedFromFee[sender] && !isExcludedFromFee[recipient]) {
            if (recipient == liquidityPoolAddress) {
                // Sell tax
                taxAmount = amount.mul(sellTaxRate).div(10000);
            } else if (sender == liquidityPoolAddress) {
                // Buy tax
                taxAmount = amount.mul(buyTaxRate).div(10000);
            } else {
                // Transfer tax
                taxAmount = amount.mul(transferTaxRate).div(10000);
            }
        }

        if (taxAmount > 0) {
            uint256 netAmount = amount.sub(taxAmount);
            super._transfer(sender, recipient, netAmount);
            
            // Distribute tax
            uint256 liquidityPoolShare = taxAmount.mul(50).div(100); // 50% to liquidity
            uint256 marketingShare = taxAmount.mul(30).div(100); // 30% to marketing
            uint256 holderRewardsShare = taxAmount.mul(20).div(100); // 20% to holders
            
            super._transfer(sender, liquidityPoolAddress, liquidityPoolShare);
            super._transfer(sender, marketingAddress, marketingShare);
            super._transfer(sender, holderRewardsAddress, holderRewardsShare);
        } else {
            super._transfer(sender, recipient, amount);
        }
    }
}
```
