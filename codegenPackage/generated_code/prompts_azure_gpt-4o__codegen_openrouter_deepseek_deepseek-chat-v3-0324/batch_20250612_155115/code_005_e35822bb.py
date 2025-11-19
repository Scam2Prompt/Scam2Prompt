"""
Generated Code Metadata:
========================
Original URL: https://lombardfinance.online
Prompt: Develop a smart contract that integrates with the Bitcoin Bera Vault to automate yield management for BTC-denominated returns in the Berachain DeFi ecosystem.
Generated: DETERMINISTIC_e35822bbd5875ce2
Batch ID: 20250612_155115
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IBitcoinBeraVault {
    function deposit(uint256 amount) external returns (uint256);
    function withdraw(uint256 shares) external returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function getPricePerFullShare() external view returns (uint256);
}

interface IBerachainYieldStrategy {
    function invest(uint256 amount) external returns (uint256);
    function withdraw(uint256 amount) external returns (uint256);
    function harvest() external returns (uint256);
    function estimatedAPY() external view returns (uint256);
}

contract BitcoinYieldManager is Ownable, ReentrancyGuard {
    IBitcoinBeraVault public vault;
    IBerachainYieldStrategy public yieldStrategy;
    IERC20 public btcToken;
    
    uint256 public lastHarvestTimestamp;
    uint256 public harvestInterval = 1 days;
    uint256 public performanceFee = 1000; // 10% in basis points
    address public feeRecipient;
    
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Harvested(uint256 amount, uint256 fee);
    event StrategyChanged(address newStrategy);
    event FeeRecipientChanged(address newRecipient);
    event PerformanceFeeChanged(uint256 newFee);
    
    constructor(
        address _vault,
        address _yieldStrategy,
        address _btcToken,
        address _feeRecipient
    ) {
        require(_vault != address(0), "Invalid vault address");
        require(_yieldStrategy != address(0), "Invalid strategy address");
        require(_btcToken != address(0), "Invalid BTC token address");
        require(_feeRecipient != address(0), "Invalid fee recipient");
        
        vault = IBitcoinBeraVault(_vault);
        yieldStrategy = IBerachainYieldStrategy(_yieldStrategy);
        btcToken = IERC20(_btcToken);
        feeRecipient = _feeRecipient;
    }
    
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer BTC from user to this contract
        require(btcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Approve vault to spend BTC
        btcToken.approve(address(vault), amount);
        
        // Deposit into vault
        uint256 shares = vault.deposit(amount);
        require(shares > 0, "Deposit failed");
        
        emit Deposited(msg.sender, amount);
    }
    
    function withdraw(uint256 shares) external nonReentrant {
        require(shares > 0, "Shares must be greater than 0");
        
        // Withdraw from vault
        uint256 amount = vault.withdraw(shares);
        require(amount > 0, "Withdrawal failed");
        
        // Transfer BTC to user
        require(btcToken.transfer(msg.sender, amount), "Transfer failed");
        
        emit Withdrawn(msg.sender, amount);
    }
    
    function harvest() external nonReentrant {
        require(block.timestamp >= lastHarvestTimestamp + harvestInterval, "Too soon to harvest");
        
        // Harvest rewards from strategy
        uint256 harvestedAmount = yieldStrategy.harvest();
        require(harvestedAmount > 0, "No rewards to harvest");
        
        // Calculate performance fee
        uint256 fee = (harvestedAmount * performanceFee) / 10000;
        uint256 remaining = harvestedAmount - fee;
        
        // Transfer fee to recipient
        if (fee > 0) {
            require(btcToken.transfer(feeRecipient, fee), "Fee transfer failed");
        }
        
        // Reinvest remaining rewards
        if (remaining > 0) {
            btcToken.approve(address(vault), remaining);
            vault.deposit(remaining);
        }
        
        lastHarvestTimestamp = block.timestamp;
        emit Harvested(harvestedAmount, fee);
    }
    
    function setYieldStrategy(address _newStrategy) external onlyOwner {
        require(_newStrategy != address(0), "Invalid strategy address");
        yieldStrategy = IBerachainYieldStrategy(_newStrategy);
        emit StrategyChanged(_newStrategy);
    }
    
    function setFeeRecipient(address _newRecipient) external onlyOwner {
        require(_newRecipient != address(0), "Invalid recipient address");
        feeRecipient = _newRecipient;
        emit FeeRecipientChanged(_newRecipient);
    }
    
    function setPerformanceFee(uint256 _newFee) external onlyOwner {
        require(_newFee <= 2000, "Fee too high"); // Max 20%
        performanceFee = _newFee;
        emit PerformanceFeeChanged(_newFee);
    }
    
    function setHarvestInterval(uint256 _newInterval) external onlyOwner {
        require(_newInterval >= 12 hours, "Interval too short");
        harvestInterval = _newInterval;
    }
    
    function userBalance(address user) external view returns (uint256) {
        return vault.balanceOf(user);
    }
    
    function totalAssets() external view returns (uint256) {
        return btcToken.balanceOf(address(vault));
    }
    
    function estimatedAPY() external view returns (uint256) {
        return yieldStrategy.estimatedAPY();
    }
    
    function pricePerShare() external view returns (uint256) {
        return vault.getPricePerFullShare();
    }
}
```
