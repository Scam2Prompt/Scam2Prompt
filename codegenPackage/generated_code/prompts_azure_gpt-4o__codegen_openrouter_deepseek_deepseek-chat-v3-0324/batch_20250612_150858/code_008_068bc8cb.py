"""
Generated Code Metadata:
========================
Original URL: https://dbank-debank.github.io
Prompt: Create a smart contract that interacts with Debank's integrated protocols to optimize portfolio management and enhance security.
Generated: DETERMINISTIC_068bc8cbb439fa81
Batch ID: 20250612_150858
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IDebankIntegration {
    function getPortfolio(address user) external view returns (address[] memory tokens, uint256[] memory balances);
    function getProtocols() external view returns (address[] memory);
    function getProtocolAPY(address protocol) external view returns (uint256);
    function deposit(address protocol, address token, uint256 amount) external;
    function withdraw(address protocol, address token, uint256 amount) external;
}

contract PortfolioOptimizer is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IDebankIntegration public debankIntegration;
    address[] public supportedProtocols;
    uint256 public rebalanceThreshold; // Percentage threshold to trigger rebalance (e.g., 5 for 5%)
    uint256 public lastRebalanceTimestamp;
    uint256 public rebalanceCooldown; // Minimum seconds between rebalances

    event Deposited(address indexed protocol, address indexed token, uint256 amount);
    event Withdrawn(address indexed protocol, address indexed token, uint256 amount);
    event Rebalanced(address[] protocols, uint256[] amounts);
    event EmergencyWithdrawn(address indexed token, uint256 amount);

    constructor(
        address _debankIntegration,
        uint256 _rebalanceThreshold,
        uint256 _rebalanceCooldown
    ) {
        require(_debankIntegration != address(0), "Invalid Debank address");
        debankIntegration = IDebankIntegration(_debankIntegration);
        rebalanceThreshold = _rebalanceThreshold;
        rebalanceCooldown = _rebalanceCooldown;
        supportedProtocols = debankIntegration.getProtocols();
    }

    modifier onlyAfterCooldown() {
        require(
            block.timestamp >= lastRebalanceTimestamp + rebalanceCooldown,
            "Rebalance cooldown not passed"
        );
        _;
    }

    function setRebalanceThreshold(uint256 _threshold) external onlyOwner {
        require(_threshold > 0 && _threshold <= 100, "Invalid threshold");
        rebalanceThreshold = _threshold;
    }

    function setRebalanceCooldown(uint256 _cooldown) external onlyOwner {
        rebalanceCooldown = _cooldown;
    }

    function getCurrentAllocation() public view returns (address[] memory tokens, uint256[] memory balances) {
        return debankIntegration.getPortfolio(address(this));
    }

    function getOptimalAllocation() public view returns (address[] memory protocols, uint256[] memory amounts) {
        protocols = supportedProtocols;
        amounts = new uint256[](protocols.length);
        
        uint256 highestAPY = 0;
        uint256 optimalProtocolIndex = 0;
        
        for (uint256 i = 0; i < protocols.length; i++) {
            uint256 currentAPY = debankIntegration.getProtocolAPY(protocols[i]);
            if (currentAPY > highestAPY) {
                highestAPY = currentAPY;
                optimalProtocolIndex = i;
            }
        }
        
        amounts[optimalProtocolIndex] = 100; // 100% allocation to highest APY protocol
        return (protocols, amounts);
    }

    function shouldRebalance() public view returns (bool) {
        (, uint256[] memory currentBalances) = getCurrentAllocation();
        (, uint256[] memory optimalBalances) = getOptimalAllocation();
        
        for (uint256 i = 0; i < currentBalances.length; i++) {
            uint256 currentPercent = (currentBalances[i] * 100) / getTotalValue();
            uint256 optimalPercent = optimalBalances[i];
            
            if (absDiff(currentPercent, optimalPercent) > rebalanceThreshold) {
                return true;
            }
        }
        return false;
    }

    function rebalance() external onlyOwner onlyAfterCooldown nonReentrant {
        require(shouldRebalance(), "No rebalance needed");
        
        (address[] memory tokens, uint256[] memory balances) = getCurrentAllocation();
        (address[] memory protocols, uint256[] memory optimalAmounts) = getOptimalAllocation();
        
        // Withdraw all funds from current protocols
        for (uint256 i = 0; i < protocols.length; i++) {
            if (balances[i] > 0) {
                debankIntegration.withdraw(protocols[i], tokens[i], balances[i]);
            }
        }
        
        // Deposit according to optimal allocation
        uint256 totalValue = getTotalValue();
        for (uint256 i = 0; i < protocols.length; i++) {
            if (optimalAmounts[i] > 0) {
                uint256 depositAmount = (totalValue * optimalAmounts[i]) / 100;
                IERC20(tokens[i]).safeIncreaseAllowance(address(debankIntegration), depositAmount);
                debankIntegration.deposit(protocols[i], tokens[i], depositAmount);
                emit Deposited(protocols[i], tokens[i], depositAmount);
            }
        }
        
        lastRebalanceTimestamp = block.timestamp;
        emit Rebalanced(protocols, optimalAmounts);
    }

    function getTotalValue() public view returns (uint256) {
        (, uint256[] memory balances) = getCurrentAllocation();
        uint256 total = 0;
        for (uint256 i = 0; i < balances.length; i++) {
            total += balances[i];
        }
        return total;
    }

    function emergencyWithdraw(address token) external onlyOwner {
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");
        
        IERC20(token).safeTransfer(owner(), balance);
        emit EmergencyWithdrawn(token, balance);
    }

    function absDiff(uint256 a, uint256 b) private pure returns (uint256) {
        return a > b ? a - b : b - a;
    }
}
```
