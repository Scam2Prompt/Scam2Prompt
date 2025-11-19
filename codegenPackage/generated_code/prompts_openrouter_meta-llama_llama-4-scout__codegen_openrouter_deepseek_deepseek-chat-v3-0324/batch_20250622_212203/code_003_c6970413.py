"""
Generated Code Metadata:
========================
Original URL: https://yetiouro.co
Prompt: Develop a smart contract for a token with a similar tokenomics structure to Yeti Ouro, including a well-balanced distribution, utility, and reward mechanisms.
Generated: DETERMINISTIC_c6970413ca228c7a
Batch ID: 20250622_212203
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract YetiToken is ERC20, ERC20Burnable, ERC20Snapshot, Ownable, Pausable {
    using SafeMath for uint256;

    // Token distribution percentages
    uint256 public constant TEAM_PERCENT = 15;
    uint256 public constant ECOSYSTEM_PERCENT = 25;
    uint256 public constant LIQUIDITY_PERCENT = 20;
    uint256 public constant STAKING_REWARDS_PERCENT = 30;
    uint256 public constant COMMUNITY_PERCENT = 10;

    // Addresses for distribution
    address public teamWallet;
    address public ecosystemWallet;
    address public liquidityWallet;
    address public stakingRewardsWallet;
    address public communityWallet;

    // Tax rates (in basis points, where 100 = 1%)
    uint256 public buyTaxRate = 500;  // 5%
    uint256 public sellTaxRate = 500; // 5%
    uint256 public transferTaxRate = 0; // 0%

    // Anti-whale measures
    uint256 public maxTransactionAmount;
    uint256 public maxWalletBalance;

    // Trading controls
    bool public tradingEnabled = false;

    // Mapping for excluded addresses from fees and limits
    mapping(address => bool) private _excludedFromFees;
    mapping(address => bool) private _excludedFromLimits;

    event TaxRatesUpdated(uint256 buyTaxRate, uint256 sellTaxRate, uint256 transferTaxRate);
    event TradingEnabled();
    event MaxTransactionAmountUpdated(uint256 amount);
    event MaxWalletBalanceUpdated(uint256 amount);

    constructor(
        uint256 totalSupply,
        address _teamWallet,
        address _ecosystemWallet,
        address _liquidityWallet,
        address _stakingRewardsWallet,
        address _communityWallet
    ) ERC20("Yeti Token", "YETI") {
        require(totalSupply > 0, "Total supply must be greater than 0");
        require(_teamWallet != address(0), "Team wallet cannot be zero address");
        require(_ecosystemWallet != address(0), "Ecosystem wallet cannot be zero address");
        require(_liquidityWallet != address(0), "Liquidity wallet cannot be zero address");
        require(_stakingRewardsWallet != address(0), "Staking rewards wallet cannot be zero address");
        require(_communityWallet != address(0), "Community wallet cannot be zero address");

        teamWallet = _teamWallet;
        ecosystemWallet = _ecosystemWallet;
        liquidityWallet = _liquidityWallet;
        stakingRewardsWallet = _stakingRewardsWallet;
        communityWallet = _communityWallet;

        // Calculate distribution amounts
        uint256 teamAmount = totalSupply.mul(TEAM_PERCENT).div(100);
        uint256 ecosystemAmount = totalSupply.mul(ECOSYSTEM_PERCENT).div(100);
        uint256 liquidityAmount = totalSupply.mul(LIQUIDITY_PERCENT).div(100);
        uint256 stakingRewardsAmount = totalSupply.mul(STAKING_REWARDS_PERCENT).div(100);
        uint256 communityAmount = totalSupply.mul(COMMUNITY_PERCENT).div(100);

        // Mint tokens to respective wallets
        _mint(teamWallet, teamAmount);
        _mint(ecosystemWallet, ecosystemAmount);
        _mint(liquidityWallet, liquidityAmount);
        _mint(stakingRewardsWallet, stakingRewardsAmount);
        _mint(communityWallet, communityAmount);

        // Set anti-whale measures (default 1% of total supply)
        maxTransactionAmount = totalSupply.div(100);
        maxWalletBalance = totalSupply.div(100);

        // Exclude owner and contract from fees and limits
        _excludedFromFees[owner()] = true;
        _excludedFromFees[address(this)] = true;
        _excludedFromLimits[owner()] = true;
        _excludedFromLimits[address(this)] = true;
    }

    function snapshot() public onlyOwner {
        _snapshot();
    }

    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }

    function enableTrading() external onlyOwner {
        tradingEnabled = true;
        emit TradingEnabled();
    }

    function setTaxRates(uint256 _buyTaxRate, uint256 _sellTaxRate, uint256 _transferTaxRate) external onlyOwner {
        require(_buyTaxRate <= 1000, "Buy tax rate cannot exceed 10%");
        require(_sellTaxRate <= 1000, "Sell tax rate cannot exceed 10%");
        require(_transferTaxRate <= 1000, "Transfer tax rate cannot exceed 10%");

        buyTaxRate = _buyTaxRate;
        sellTaxRate = _sellTaxRate;
        transferTaxRate = _transferTaxRate;

        emit TaxRatesUpdated(_buyTaxRate, _sellTaxRate, _transferTaxRate);
    }

    function setMaxTransactionAmount(uint256 _maxTransactionAmount) external onlyOwner {
        require(_maxTransactionAmount >= totalSupply().div(1000), "Max transaction amount too low");
        maxTransactionAmount = _maxTransactionAmount;
        emit MaxTransactionAmountUpdated(_maxTransactionAmount);
    }

    function setMaxWalletBalance(uint256 _maxWalletBalance) external onlyOwner {
        require(_maxWalletBalance >= totalSupply().div(1000), "Max wallet balance too low");
        maxWalletBalance = _maxWalletBalance;
        emit MaxWalletBalanceUpdated(_maxWalletBalance);
    }

    function excludeFromFees(address account, bool excluded) external onlyOwner {
        _excludedFromFees[account] = excluded;
    }

    function excludeFromLimits(address account, bool excluded) external onlyOwner {
        _excludedFromLimits[account] = excluded;
    }

    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override(ERC20, ERC20Snapshot) whenNotPaused {
        require(from != to, "Cannot transfer to self");

        if (!tradingEnabled) {
            require(from == owner() || to == owner(), "Trading is not enabled yet");
        }

        // Check transaction amount limit
        if (!_excludedFromLimits[from] && !_excludedFromLimits[to]) {
            require(amount <= maxTransactionAmount, "Transfer amount exceeds max transaction amount");
        }

        // Check wallet balance limit
        if (!_excludedFromLimits[to] && to != address(0)) {
            require(balanceOf(to).add(amount) <= maxWalletBalance, "Wallet balance would exceed max limit");
        }

        super._beforeTokenTransfer(from, to, amount);
    }

    function _transfer(address sender, address recipient, uint256 amount) internal override {
        if (_excludedFromFees[sender] || _excludedFromFees[recipient]) {
            super._transfer(sender, recipient, amount);
        } else {
            uint256 taxAmount = 0;
            
            // Determine tax rate based on transaction type
            if (recipient == liquidityWallet) {
                // Sell transaction
                taxAmount = amount.mul(sellTaxRate).div(10000);
            } else if (sender == liquidityWallet) {
                // Buy transaction
                taxAmount = amount.mul(buyTaxRate).div(10000);
            } else {
                // Transfer transaction
                taxAmount = amount.mul(transferTaxRate).div(10000);
            }

            if (taxAmount > 0) {
                uint256 sendAmount = amount.sub(taxAmount);
                super._transfer(sender, recipient, sendAmount);
                super._transfer(sender, stakingRewardsWallet, taxAmount);
            } else {
                super._transfer(sender, recipient, amount);
            }
        }
    }
}
```
