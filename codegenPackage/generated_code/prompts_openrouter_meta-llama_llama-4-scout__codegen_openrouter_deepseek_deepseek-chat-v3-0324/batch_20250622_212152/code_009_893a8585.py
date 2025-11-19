"""
Generated Code Metadata:
========================
Original URL: https://aave.org
Prompt: "Propose a use case for the Aave Protocol's composability feature, enabling the creation of diverse products and applications."
Generated: DETERMINISTIC_893a8585c1c03e66
Batch ID: 20250622_212152
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

import "@aave/core-v3/contracts/interfaces/IPool.sol";
import "@aave/core-v3/contracts/interfaces/IPoolAddressesProvider.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title YieldOptimizer
 * @notice A smart contract that leverages Aave Protocol's composability
 *         to optimize yield by automatically moving funds between
 *         supply and borrow positions based on market conditions.
 */
contract YieldOptimizer is Ownable {
    IPoolAddressesProvider public immutable addressesProvider;
    IPool public immutable pool;
    
    IERC20 public immutable stablecoin;
    IERC20 public immutable variableYieldAsset;
    
    uint256 public lastRebalanceTimestamp;
    uint256 public rebalanceInterval;
    
    event Deposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Rebalanced(uint256 timestamp);
    
    /**
     * @param _addressesProvider Aave PoolAddressesProvider address
     * @param _stablecoin Stablecoin token address (e.g., USDC)
     * @param _variableYieldAsset Variable yield asset address (e.g., WETH)
     * @param _rebalanceInterval Seconds between rebalances
     */
    constructor(
        address _addressesProvider,
        address _stablecoin,
        address _variableYieldAsset,
        uint256 _rebalanceInterval
    ) {
        addressesProvider = IPoolAddressesProvider(_addressesProvider);
        pool = IPool(addressesProvider.getPool());
        
        stablecoin = IERC20(_stablecoin);
        variableYieldAsset = IERC20(_variableYieldAsset);
        
        rebalanceInterval = _rebalanceInterval;
        
        // Approve Aave Pool to spend tokens
        stablecoin.approve(address(pool), type(uint256).max);
        variableYieldAsset.approve(address(pool), type(uint256).max);
    }
    
    /**
     * @notice Deposit stablecoins to earn yield
     * @param amount Amount of stablecoins to deposit
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        stablecoin.transferFrom(msg.sender, address(this), amount);
        pool.supply(address(stablecoin), amount, address(this), 0);
        
        emit Deposited(msg.sender, amount);
    }
    
    /**
     * @notice Execute rebalance strategy
     * @dev Checks if rebalance interval has passed and executes strategy
     */
    function rebalance() external {
        require(
            block.timestamp >= lastRebalanceTimestamp + rebalanceInterval,
            "Rebalance interval not reached"
        );
        
        // Check current borrowing rates
        (, , uint256 stableRate) = pool.getReserveData(address(stablecoin));
        (, , uint256 variableRate) = pool.getReserveData(address(variableYieldAsset));
        
        // Example strategy: If stable borrowing rate is lower than variable yield rate,
        // borrow stablecoins to buy more yield asset
        if (stableRate < variableRate) {
            _executeLeverageStrategy();
        } else {
            _executeDeleveragingStrategy();
        }
        
        lastRebalanceTimestamp = block.timestamp;
        emit Rebalanced(block.timestamp);
    }
    
    /**
     * @notice Internal function to execute leverage strategy
     */
    function _executeLeverageStrategy() internal {
        // Get current stablecoin balance
        uint256 stableBalance = stablecoin.balanceOf(address(this));
        
        // Borrow additional stablecoins if possible
        uint256 borrowAmount = stableBalance / 2; // Example: borrow 50% of current balance
        pool.borrow(address(stablecoin), borrowAmount, 1, 0, address(this));
        
        // Use borrowed funds to supply more yield asset
        pool.supply(address(variableYieldAsset), borrowAmount, address(this), 0);
        
        emit Borrowed(address(this), borrowAmount);
    }
    
    /**
     * @notice Internal function to execute deleveraging strategy
     */
    function _executeDeleveragingStrategy() internal {
        // Withdraw some yield asset
        uint256 yieldAssetBalance = variableYieldAsset.balanceOf(address(this));
        uint256 withdrawAmount = yieldAssetBalance / 2; // Example: withdraw 50%
        pool.withdraw(address(variableYieldAsset), withdrawAmount, address(this));
        
        // Repay stablecoin debt
        uint256 debt = pool.getUserAccountData(address(this)).totalDebtETH;
        if (debt > 0) {
            uint256 repayAmount = debt / 2; // Example: repay 50% of debt
            pool.repay(address(stablecoin), repayAmount, 1, address(this));
        }
        
        emit Repaid(address(this), withdrawAmount);
    }
    
    /**
     * @notice Withdraw funds from the optimizer
     * @param amount Amount of stablecoins to withdraw
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        
        pool.withdraw(address(stablecoin), amount, msg.sender);
        emit Withdrawn(msg.sender, amount);
    }
    
    /**
     * @notice Set new rebalance interval
     * @param newInterval New interval in seconds
     */
    function setRebalanceInterval(uint256 newInterval) external onlyOwner {
        require(newInterval > 0, "Interval must be greater than 0");
        rebalanceInterval = newInterval;
    }
    
    /**
     * @notice Emergency function to withdraw all funds
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stablecoin.balanceOf(address(this));
        if (balance > 0) {
            pool.withdraw(address(stablecoin), balance, msg.sender);
        }
        
        uint256 yieldBalance = variableYieldAsset.balanceOf(address(this));
        if (yieldBalance > 0) {
            pool.withdraw(address(variableYieldAsset), yieldBalance, msg.sender);
        }
    }
}
```
