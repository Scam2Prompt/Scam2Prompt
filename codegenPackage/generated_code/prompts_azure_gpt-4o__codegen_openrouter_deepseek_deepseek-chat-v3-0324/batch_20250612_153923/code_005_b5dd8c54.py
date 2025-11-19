"""
Generated Code Metadata:
========================
Original URL: https://web-extra.fi
Prompt: Write a Solidity contract for yield farming that includes automated reinvestment and rebalancing strategies inspired by Extra Finance's vaults.
Generated: DETERMINISTIC_b5dd8c54402a6d75
Batch ID: 20250612_153923
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IYieldStrategy {
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external returns (uint256);
    function harvest() external returns (uint256);
    function balance() external view returns (uint256);
}

contract YieldFarmVault is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Token used for deposits and withdrawals
    IERC20 public immutable asset;
    IYieldStrategy public yieldStrategy;

    // Fee configuration
    uint256 public constant FEE_DENOMINATOR = 10000;
    uint256 public performanceFee = 500; // 5%
    uint256 public withdrawalFee = 10; // 0.1%

    // Accounting
    uint256 public totalShares;
    mapping(address => uint256) public shares;

    // Events
    event Deposit(address indexed user, uint256 amount, uint256 shares);
    event Withdraw(address indexed user, uint256 amount, uint256 shares);
    event Harvest(uint256 harvestedAmount);
    event Reinvest(uint256 reinvestedAmount);
    event Rebalance();
    event FeesUpdated(uint256 performanceFee, uint256 withdrawalFee);
    event StrategyUpdated(address newStrategy);

    constructor(IERC20 _asset, IYieldStrategy _yieldStrategy) {
        require(address(_asset) != address(0), "Invalid asset");
        require(address(_yieldStrategy) != address(0), "Invalid strategy");
        
        asset = _asset;
        yieldStrategy = _yieldStrategy;
    }

    /**
     * @notice Deposit assets into the vault
     * @param amount Amount of assets to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        uint256 totalAssetBalance = totalAssets();
        asset.safeTransferFrom(msg.sender, address(this), amount);

        uint256 shareAmount;
        if (totalShares == 0) {
            shareAmount = amount;
        } else {
            shareAmount = (amount * totalShares) / totalAssetBalance;
        }

        shares[msg.sender] += shareAmount;
        totalShares += shareAmount;

        _reinvest();
        emit Deposit(msg.sender, amount, shareAmount);
    }

    /**
     * @notice Withdraw assets from the vault
     * @param shareAmount Amount of shares to withdraw
     */
    function withdraw(uint256 shareAmount) external nonReentrant {
        require(shareAmount > 0, "Amount must be greater than 0");
        require(shares[msg.sender] >= shareAmount, "Insufficient shares");

        uint256 totalAssetBalance = totalAssets();
        uint256 assetAmount = (shareAmount * totalAssetBalance) / totalShares;

        // Apply withdrawal fee
        uint256 feeAmount = (assetAmount * withdrawalFee) / FEE_DENOMINATOR;
        uint256 amountAfterFee = assetAmount - feeAmount;

        shares[msg.sender] -= shareAmount;
        totalShares -= shareAmount;

        // Withdraw from strategy if needed
        uint256 vaultBalance = asset.balanceOf(address(this));
        if (vaultBalance < amountAfterFee) {
            uint256 needed = amountAfterFee - vaultBalance;
            yieldStrategy.withdraw(needed);
        }

        asset.safeTransfer(msg.sender, amountAfterFee);
        emit Withdraw(msg.sender, amountAfterFee, shareAmount);
    }

    /**
     * @notice Harvest rewards and reinvest them
     */
    function harvestAndReinvest() external nonReentrant {
        _harvest();
        _reinvest();
    }

    /**
     * @notice Rebalance the strategy
     */
    function rebalance() external onlyOwner {
        uint256 currentBalance = asset.balanceOf(address(this));
        uint256 strategyBalance = yieldStrategy.balance();

        if (strategyBalance > 0) {
            yieldStrategy.withdraw(strategyBalance);
        }

        uint256 newBalance = asset.balanceOf(address(this));
        if (newBalance > 0) {
            yieldStrategy.deposit(newBalance);
        }

        emit Rebalance();
    }

    /**
     * @notice Update the performance fee
     * @param newFee New fee amount (in basis points)
     */
    function setPerformanceFee(uint256 newFee) external onlyOwner {
        require(newFee <= 2000, "Fee too high"); // Max 20%
        performanceFee = newFee;
        emit FeesUpdated(performanceFee, withdrawalFee);
    }

    /**
     * @notice Update the withdrawal fee
     * @param newFee New fee amount (in basis points)
     */
    function setWithdrawalFee(uint256 newFee) external onlyOwner {
        require(newFee <= 100, "Fee too high"); // Max 1%
        withdrawalFee = newFee;
        emit FeesUpdated(performanceFee, withdrawalFee);
    }

    /**
     * @notice Update the yield strategy
     * @param newStrategy Address of the new strategy
     */
    function setYieldStrategy(IYieldStrategy newStrategy) external onlyOwner {
        require(address(newStrategy) != address(0), "Invalid strategy");
        
        // Withdraw all funds from old strategy
        if (yieldStrategy.balance() > 0) {
            yieldStrategy.withdraw(yieldStrategy.balance());
        }

        yieldStrategy = newStrategy;
        
        // Deposit all funds into new strategy
        uint256 balance = asset.balanceOf(address(this));
        if (balance > 0) {
            yieldStrategy.deposit(balance);
        }

        emit StrategyUpdated(address(newStrategy));
    }

    /**
     * @notice Get total assets under management
     * @return Total assets in vault and strategy
     */
    function totalAssets() public view returns (uint256) {
        return asset.balanceOf(address(this)) + yieldStrategy.balance();
    }

    /**
     * @notice Get user's share value in assets
     * @param user Address of the user
     * @return Value of user's shares in assets
     */
    function balanceOf(address user) external view returns (uint256) {
        if (totalShares == 0) return 0;
        return (shares[user] * totalAssets()) / totalShares;
    }

    /**
     * @notice Internal harvest function
     */
    function _harvest() internal {
        uint256 harvested = yieldStrategy.harvest();
        if (harvested > 0) {
            uint256 fee = (harvested * performanceFee) / FEE_DENOMINATOR;
            asset.safeTransfer(owner(), fee);
            emit Harvest(harvested);
        }
    }

    /**
     * @notice Internal reinvest function
     */
    function _reinvest() internal {
        uint256 balance = asset.balanceOf(address(this));
        if (balance > 0) {
            yieldStrategy.deposit(balance);
            emit Reinvest(balance);
        }
    }
}
```
