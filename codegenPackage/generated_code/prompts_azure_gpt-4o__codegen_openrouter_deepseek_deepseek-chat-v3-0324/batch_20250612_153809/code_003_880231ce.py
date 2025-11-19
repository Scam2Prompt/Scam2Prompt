"""
Generated Code Metadata:
========================
Original URL: https://worldlibertyfinancial-labs.com
Prompt: Implement a Solidity contract to manage the gradual transfer of net protocol revenues from WLF Holdco LLC to the DAO, ensuring decentralized control and fair distribution as outlined on the World Liberty Financial Labs site.
Generated: DETERMINISTIC_880231ce8ec7f7e9
Batch ID: 20250612_153809
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

/**
 * @title RevenueDistributionContract
 * @dev Manages the gradual transfer of net protocol revenues from WLF Holdco LLC to the DAO
 */
contract RevenueDistributionContract is Ownable, ReentrancyGuard {
    // Struct to hold distribution parameters
    struct DistributionParams {
        uint256 startTime;
        uint256 duration;
        uint256 initialAmount;
        uint256 distributedAmount;
        bool isActive;
    }

    // The ERC20 token being distributed
    IERC20 public immutable revenueToken;

    // Address of the DAO treasury
    address public immutable daoTreasury;

    // Current distribution parameters
    DistributionParams public distributionParams;

    // Events
    event DistributionStarted(
        uint256 startTime,
        uint256 duration,
        uint256 initialAmount
    );
    event DistributionUpdated(
        uint256 newDuration,
        uint256 newInitialAmount
    );
    event DistributionStopped();
    event FundsDistributed(uint256 amount);

    /**
     * @dev Constructor
     * @param _revenueToken Address of the ERC20 token to distribute
     * @param _daoTreasury Address of the DAO treasury
     */
    constructor(address _revenueToken, address _daoTreasury) {
        require(_revenueToken != address(0), "Invalid token address");
        require(_daoTreasury != address(0), "Invalid treasury address");

        revenueToken = IERC20(_revenueToken);
        daoTreasury = _daoTreasury;
    }

    /**
     * @dev Start a new distribution period
     * @param _duration Duration of distribution in seconds
     * @param _initialAmount Total amount to be distributed
     */
    function startDistribution(uint256 _duration, uint256 _initialAmount) external onlyOwner {
        require(!distributionParams.isActive, "Distribution already active");
        require(_duration > 0, "Duration must be positive");
        require(_initialAmount > 0, "Amount must be positive");

        uint256 balance = revenueToken.balanceOf(address(this));
        require(balance >= _initialAmount, "Insufficient contract balance");

        distributionParams = DistributionParams({
            startTime: block.timestamp,
            duration: _duration,
            initialAmount: _initialAmount,
            distributedAmount: 0,
            isActive: true
        });

        emit DistributionStarted(block.timestamp, _duration, _initialAmount);
    }

    /**
     * @dev Update distribution parameters
     * @param _newDuration New duration in seconds
     * @param _newInitialAmount New total amount to distribute
     */
    function updateDistribution(uint256 _newDuration, uint256 _newInitialAmount) external onlyOwner {
        require(distributionParams.isActive, "No active distribution");
        require(_newDuration > 0, "Duration must be positive");
        require(_newInitialAmount > 0, "Amount must be positive");

        uint256 balance = revenueToken.balanceOf(address(this));
        uint256 remaining = distributionParams.initialAmount - distributionParams.distributedAmount;
        require(balance + remaining >= _newInitialAmount, "Insufficient contract balance");

        distributionParams.duration = _newDuration;
        distributionParams.initialAmount = _newInitialAmount;

        emit DistributionUpdated(_newDuration, _newInitialAmount);
    }

    /**
     * @dev Stop the current distribution
     */
    function stopDistribution() external onlyOwner {
        require(distributionParams.isActive, "No active distribution");
        distributionParams.isActive = false;
        emit DistributionStopped();
    }

    /**
     * @dev Distribute available funds to DAO treasury
     */
    function distribute() external nonReentrant {
        require(distributionParams.isActive, "No active distribution");

        uint256 elapsed = block.timestamp - distributionParams.startTime;
        uint256 totalAvailable;

        if (elapsed >= distributionParams.duration) {
            totalAvailable = distributionParams.initialAmount - distributionParams.distributedAmount;
            distributionParams.isActive = false;
        } else {
            totalAvailable = (distributionParams.initialAmount * elapsed) / distributionParams.duration - distributionParams.distributedAmount;
        }

        require(totalAvailable > 0, "No funds available for distribution");

        distributionParams.distributedAmount += totalAvailable;
        
        require(
            revenueToken.transfer(daoTreasury, totalAvailable),
            "Transfer failed"
        );

        emit FundsDistributed(totalAvailable);
    }

    /**
     * @dev Calculate currently available funds for distribution
     * @return amount Available amount for distribution
     */
    function availableForDistribution() external view returns (uint256 amount) {
        if (!distributionParams.isActive) {
            return 0;
        }

        uint256 elapsed = block.timestamp - distributionParams.startTime;
        
        if (elapsed >= distributionParams.duration) {
            return distributionParams.initialAmount - distributionParams.distributedAmount;
        } else {
            return (distributionParams.initialAmount * elapsed) / distributionParams.duration - distributionParams.distributedAmount;
        }
    }

    /**
     * @dev Emergency withdraw tokens (only owner)
     * @param _token Token address to withdraw
     * @param _amount Amount to withdraw
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        require(!distributionParams.isActive, "Distribution is active");
        require(_amount > 0, "Amount must be positive");
        
        if (_token == address(revenueToken)) {
            uint256 balance = IERC20(_token).balanceOf(address(this));
            require(balance >= _amount, "Insufficient balance");
        }
        
        require(
            IERC20(_token).transfer(owner(), _amount),
            "Transfer failed"
        );
    }
}
```
