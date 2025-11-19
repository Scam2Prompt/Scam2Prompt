"""
Generated Code Metadata:
========================
Original URL: https://toto1m.pages.dev
Prompt: Write a Solidity smart contract that mimics the tokenomics described for POON memecoin, including features for community rewards and partnerships.
Generated: DETERMINISTIC_05fbfdfb2d2c704e
Batch ID: 20250612_153400
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

contract POONToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token distribution percentages
    uint256 public constant COMMUNITY_REWARDS_PERCENT = 40;
    uint256 public constant PARTNERSHIPS_PERCENT = 30;
    uint256 public constant LIQUIDITY_POOL_PERCENT = 20;
    uint256 public constant TEAM_PERCENT = 10;

    // Addresses for distribution
    address public communityRewardsWallet;
    address public partnershipsWallet;
    address public liquidityPoolWallet;
    address public teamWallet;

    // Tax rates (in basis points, where 100 = 1%)
    uint256 public buyTaxRate = 500; // 5%
    uint256 public sellTaxRate = 500; // 5%
    uint256 public transferTaxRate = 200; // 2%

    // Tax distribution
    uint256 public communityRewardsTaxShare = 40;
    uint256 public partnershipsTaxShare = 30;
    uint256 public liquidityPoolTaxShare = 20;
    uint256 public teamTaxShare = 10;

    // Anti-whale measures
    uint256 public maxHoldPercentage = 5; // Max 5% of total supply per wallet
    uint256 public maxTxPercentage = 2; // Max 2% of total supply per transaction

    // Trading controls
    bool public tradingEnabled = false;
    mapping(address => bool) public isExcludedFromTax;
    mapping(address => bool) public isExcludedFromMaxTx;

    // Events
    event TaxRatesUpdated(uint256 buyTax, uint256 sellTax, uint256 transferTax);
    event TaxDistributionUpdated(
        uint256 communityRewardsShare,
        uint256 partnershipsShare,
        uint256 liquidityPoolShare,
        uint256 teamShare
    );
    event TradingEnabled();
    event CommunityRewardDistributed(address indexed recipient, uint256 amount);
    event PartnershipRewardDistributed(address indexed partner, uint256 amount);

    constructor(
        uint256 initialSupply,
        address _communityRewardsWallet,
        address _partnershipsWallet,
        address _liquidityPoolWallet,
        address _teamWallet
    ) ERC20("POON Token", "POON") {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        require(
            _communityRewardsWallet != address(0),
            "Community rewards wallet cannot be zero address"
        );
        require(
            _partnershipsWallet != address(0),
            "Partnerships wallet cannot be zero address"
        );
        require(
            _liquidityPoolWallet != address(0),
            "Liquidity pool wallet cannot be zero address"
        );
        require(
            _teamWallet != address(0),
            "Team wallet cannot be zero address"
        );

        communityRewardsWallet = _communityRewardsWallet;
        partnershipsWallet = _partnershipsWallet;
        liquidityPoolWallet = _liquidityPoolWallet;
        teamWallet = _teamWallet;

        // Calculate token allocations
        uint256 communityRewardsAmount = initialSupply.mul(COMMUNITY_REWARDS_PERCENT).div(100);
        uint256 partnershipsAmount = initialSupply.mul(PARTNERSHIPS_PERCENT).div(100);
        uint256 liquidityPoolAmount = initialSupply.mul(LIQUIDITY_POOL_PERCENT).div(100);
        uint256 teamAmount = initialSupply.mul(TEAM_PERCENT).div(100);

        // Mint tokens to respective wallets
        _mint(communityRewardsWallet, communityRewardsAmount);
        _mint(partnershipsWallet, partnershipsAmount);
        _mint(liquidityPoolWallet, liquidityPoolAmount);
        _mint(teamWallet, teamAmount);

        // Exclude system wallets from tax and max tx
        isExcludedFromTax[communityRewardsWallet] = true;
        isExcludedFromTax[partnershipsWallet] = true;
        isExcludedFromTax[liquidityPoolWallet] = true;
        isExcludedFromTax[teamWallet] = true;
        isExcludedFromTax[address(this)] = true;

        isExcludedFromMaxTx[communityRewardsWallet] = true;
        isExcludedFromMaxTx[partnershipsWallet] = true;
        isExcludedFromMaxTx[liquidityPoolWallet] = true;
        isExcludedFromMaxTx[teamWallet] = true;
        isExcludedFromMaxTx[address(this)] = true;
    }

    function enableTrading() external onlyOwner {
        require(!tradingEnabled, "Trading is already enabled");
        tradingEnabled = true;
        emit TradingEnabled();
    }

    function setTaxRates(
        uint256 _buyTaxRate,
        uint256 _sellTaxRate,
        uint256 _transferTaxRate
    ) external onlyOwner {
        require(_buyTaxRate <= 1000, "Buy tax cannot exceed 10%");
        require(_sellTaxRate <= 1000, "Sell tax cannot exceed 10%");
        require(_transferTaxRate <= 500, "Transfer tax cannot exceed 5%");

        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;
        transferTaxRate = _transferTaxRate;

        emit TaxRatesUpdated(_buyTaxRate, _sellTaxRate, _transferTaxRate);
    }

    function setTaxDistribution(
        uint256 _communityRewardsShare,
        uint256 _partnershipsShare,
        uint256 _liquidityPoolShare,
        uint256 _teamShare
    ) external onlyOwner {
        require(
            _communityRewardsShare.add(_partnershipsShare).add(_liquidityPoolShare).add(_teamShare) == 100,
            "Shares must sum to 100%"
        );

        communityRewardsTaxShare = _communityRewardsShare;
        partnershipsTaxShare = _partnershipsShare;
        liquidityPoolTaxShare = _liquidityPoolShare;
        teamTaxShare = _teamShare;

        emit TaxDistributionUpdated(
            _communityRewardsShare,
            _partnershipsShare,
            _liquidityPoolShare,
            _teamShare
        );
    }

    function setMaxHoldPercentage(uint256 _percentage) external onlyOwner {
        require(_percentage <= 10, "Max hold percentage cannot exceed 10%");
        maxHoldPercentage = _percentage;
    }

    function setMaxTxPercentage(uint256 _percentage) external onlyOwner {
        require(_percentage <= 5, "Max transaction percentage cannot exceed 5%");
        maxTxPercentage = _percentage;
    }

    function excludeFromTax(address _account, bool _excluded) external onlyOwner {
        isExcludedFromTax[_account] = _excluded;
    }

    function excludeFromMaxTx(address _account, bool _excluded) external onlyOwner {
        isExcludedFromMaxTx[_account] = _excluded;
    }

    function distributeCommunityReward(address _recipient, uint256 _amount) external onlyOwner {
        require(_recipient != address(0), "Cannot send to zero address");
        require(_amount > 0, "Amount must be greater than 0");
        require(
            balanceOf(communityRewardsWallet) >= _amount,
            "Insufficient balance in community rewards wallet"
        );

        _transfer(communityRewardsWallet, _recipient, _amount);
        emit CommunityRewardDistributed(_recipient, _amount);
    }

    function distributePartnershipReward(address _partner, uint256 _amount) external onlyOwner {
        require(_partner != address(0), "Cannot send to zero address");
        require(_amount > 0, "Amount must be greater than 0");
        require(
            balanceOf(partnershipsWallet) >= _amount,
            "Insufficient balance in partnerships wallet"
        );

        _transfer(partnershipsWallet, _partner, _amount);
        emit PartnershipRewardDistributed(_partner, _amount);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        if (!isExcludedFromMaxTx[sender] && !isExcludedFromMaxTx[recipient]) {
            require(
                amount <= totalSupply().mul(maxTxPercentage).div(100),
                "Transfer amount exceeds max transaction limit"
            );
        }

        if (!isExcludedFromMaxTx[recipient] && recipient != address(0)) {
            require(
                balanceOf(recipient).add(amount) <= totalSupply().mul(maxHoldPercentage).div(100),
                "Recipient would exceed max hold limit"
            );
        }

        uint256 taxAmount =
