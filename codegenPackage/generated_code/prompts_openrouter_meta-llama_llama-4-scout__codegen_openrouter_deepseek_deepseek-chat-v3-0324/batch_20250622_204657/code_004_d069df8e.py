"""
Generated Code Metadata:
========================
Original URL: https://ackinacki.live
Prompt: Develop a tokenomics model for a new blockchain project inspired by Acki Nacki's $NACKL and $SHELL token system.
Generated: DETERMINISTIC_d069df8e792f5790
Batch ID: 20250622_204657
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

contract TokenomicsToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tokenomics parameters
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant INITIAL_SUPPLY = 100_000_000 * 10**18; // 100 million tokens
    uint256 public constant TREASURY_PERCENT = 20; // 20% to treasury
    uint256 public constant DEVELOPMENT_PERCENT = 15; // 15% to development
    uint256 public constant COMMUNITY_PERCENT = 10; // 10% to community
    uint256 public constant LIQUIDITY_PERCENT = 5; // 5% to liquidity
    uint256 public constant STAKING_REWARDS_PERCENT = 50; // 50% to staking rewards

    // Addresses
    address public treasuryWallet;
    address public developmentWallet;
    address public communityWallet;
    address public liquidityWallet;
    address public stakingContract;

    // Tax parameters
    uint256 public buyTax = 5; // 5% buy tax
    uint256 public sellTax = 10; // 10% sell tax
    uint256 public transferTax = 2; // 2% transfer tax
    address public taxWallet;

    // Anti-whale parameters
    uint256 public maxHoldPercentage = 5; // 5% max wallet holding
    uint256 public maxTxPercentage = 1; // 1% max transaction amount

    // Trading controls
    bool public tradingEnabled = false;
    mapping(address => bool) public isExcludedFromTax;
    mapping(address => bool) public isExcludedFromMaxHold;

    event TokensMinted(address indexed to, uint256 amount);
    event TradingEnabled(bool enabled);
    event TaxUpdated(uint256 buyTax, uint256 sellTax, uint256 transferTax);
    event MaxHoldUpdated(uint256 percentage);
    event MaxTxUpdated(uint256 percentage);

    constructor(
        address _treasuryWallet,
        address _developmentWallet,
        address _communityWallet,
        address _liquidityWallet,
        address _taxWallet
    ) ERC20("TokenomicsToken", "TKN") {
        require(_treasuryWallet != address(0), "Invalid treasury wallet");
        require(_developmentWallet != address(0), "Invalid development wallet");
        require(_communityWallet != address(0), "Invalid community wallet");
        require(_liquidityWallet != address(0), "Invalid liquidity wallet");
        require(_taxWallet != address(0), "Invalid tax wallet");

        treasuryWallet = _treasuryWallet;
        developmentWallet = _developmentWallet;
        communityWallet = _communityWallet;
        liquidityWallet = _liquidityWallet;
        taxWallet = _taxWallet;

        // Exclude system wallets from tax and max hold
        isExcludedFromTax[_treasuryWallet] = true;
        isExcludedFromTax[_developmentWallet] = true;
        isExcludedFromTax[_communityWallet] = true;
        isExcludedFromTax[_liquidityWallet] = true;
        isExcludedFromTax[_taxWallet] = true;
        isExcludedFromTax[address(this)] = true;

        isExcludedFromMaxHold[_treasuryWallet] = true;
        isExcludedFromMaxHold[_developmentWallet] = true;
        isExcludedFromMaxHold[_communityWallet] = true;
        isExcludedFromMaxHold[_liquidityWallet] = true;
        isExcludedFromMaxHold[_taxWallet] = true;
        isExcludedFromMaxHold[address(this)] = true;

        // Initial token distribution
        uint256 treasuryAmount = INITIAL_SUPPLY.mul(TREASURY_PERCENT).div(100);
        uint256 developmentAmount = INITIAL_SUPPLY.mul(DEVELOPMENT_PERCENT).div(100);
        uint256 communityAmount = INITIAL_SUPPLY.mul(COMMUNITY_PERCENT).div(100);
        uint256 liquidityAmount = INITIAL_SUPPLY.mul(LIQUIDITY_PERCENT).div(100);
        uint256 stakingAmount = INITIAL_SUPPLY.mul(STAKING_REWARDS_PERCENT).div(100);

        _mint(_treasuryWallet, treasuryAmount);
        _mint(_developmentWallet, developmentAmount);
        _mint(_communityWallet, communityAmount);
        _mint(_liquidityWallet, liquidityAmount);
        _mint(address(this), stakingAmount);

        emit TokensMinted(_treasuryWallet, treasuryAmount);
        emit TokensMinted(_developmentWallet, developmentAmount);
        emit TokensMinted(_communityWallet, communityAmount);
        emit TokensMinted(_liquidityWallet, liquidityAmount);
        emit TokensMinted(address(this), stakingAmount);
    }

    function setStakingContract(address _stakingContract) external onlyOwner {
        require(_stakingContract != address(0), "Invalid staking contract");
        stakingContract = _stakingContract;
        isExcludedFromTax[_stakingContract] = true;
        isExcludedFromMaxHold[_stakingContract] = true;
    }

    function enableTrading() external onlyOwner {
        require(!tradingEnabled, "Trading already enabled");
        tradingEnabled = true;
        emit TradingEnabled(true);
    }

    function disableTrading() external onlyOwner {
        require(tradingEnabled, "Trading already disabled");
        tradingEnabled = false;
        emit TradingEnabled(false);
    }

    function setTaxes(
        uint256 _buyTax,
        uint256 _sellTax,
        uint256 _transferTax
    ) external onlyOwner {
        require(_buyTax <= 20, "Buy tax too high");
        require(_sellTax <= 20, "Sell tax too high");
        require(_transferTax <= 10, "Transfer tax too high");

        buyTax = _buyTax;
        sellTax = _sellTax;
        transferTax = _transferTax;

        emit TaxUpdated(_buyTax, _sellTax, _transferTax);
    }

    function setMaxHoldPercentage(uint256 _percentage) external onlyOwner {
        require(_percentage >= 1 && _percentage <= 10, "Invalid percentage");
        maxHoldPercentage = _percentage;
        emit MaxHoldUpdated(_percentage);
    }

    function setMaxTxPercentage(uint256 _percentage) external onlyOwner {
        require(_percentage >= 0.1 ether && _percentage <= 5 ether, "Invalid percentage");
        maxTxPercentage = _percentage;
        emit MaxTxUpdated(_percentage);
    }

    function excludeFromTax(address _account, bool _excluded) external onlyOwner {
        isExcludedFromTax[_account] = _excluded;
    }

    function excludeFromMaxHold(address _account, bool _excluded) external onlyOwner {
        isExcludedFromMaxHold[_account] = _excluded;
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
                sender == owner() || recipient == owner() || isExcludedFromTax[sender] || isExcludedFromTax[recipient],
                "Trading is disabled"
            );
        }

        // Check max transaction limit
        if (!isExcludedFromMaxHold[sender] && !isExcludedFromMaxHold[recipient]) {
            require(amount <= MAX_SUPPLY.mul(maxTxPercentage).div(100), "Transfer amount exceeds max transaction limit");
        }

        // Check max wallet holding
        if (!isExcludedFromMaxHold[recipient] && recipient != stakingContract) {
            require(
                balanceOf(recipient).add(amount) <= MAX_SUPPLY.mul(maxHoldPercentage).div(100),
                "Recipient would exceed max wallet limit"
            );
        }

        uint256 taxAmount = 0;
        if (!isExcludedFromTax[sender] && !isExcludedFromTax[recipient]) {
            if (sender == liquidityWallet) {
                // Buy transaction
                taxAmount = amount.mul(buyTax).div(100);
            } else if (recipient == liquidityWallet) {
                // Sell transaction
                taxAmount = amount.mul(sellTax).div(100);
            } else {
                // Transfer transaction
                taxAmount = amount.mul(transferTax).div(100);
            }

            if (taxAmount > 0) {
                super._transfer(sender, taxWallet, taxAmount);
                amount = amount.sub(taxAmount);
            }
        }
