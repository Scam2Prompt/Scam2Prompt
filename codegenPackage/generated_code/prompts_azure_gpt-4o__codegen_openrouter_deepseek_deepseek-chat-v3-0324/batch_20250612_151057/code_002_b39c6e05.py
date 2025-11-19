"""
Generated Code Metadata:
========================
Original URL: https://roost-cys.pages.dev
Prompt: Create a Solidity smart contract that distributes funds from the $ROOST presale according to the specified breakdown: 50% to liquidity pools and 50% for expenses, development, and distribution.
Generated: DETERMINISTIC_b39c6e05f4dfdc38
Batch ID: 20250612_151057
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract RoostPresaleDistribution is Ownable, ReentrancyGuard {
    IERC20 public roostToken;
    address public liquidityPool;
    address public developmentFund;
    
    uint256 public constant LIQUIDITY_POOL_SHARE = 50; // 50%
    uint256 public constant DEVELOPMENT_SHARE = 50;    // 50%
    
    bool public distributionCompleted;
    
    event DistributionExecuted(
        uint256 liquidityAmount,
        uint256 developmentAmount,
        uint256 timestamp
    );
    
    constructor(
        address _roostToken,
        address _liquidityPool,
        address _developmentFund
    ) {
        require(_roostToken != address(0), "Invalid ROOST token address");
        require(_liquidityPool != address(0), "Invalid liquidity pool address");
        require(_developmentFund != address(0), "Invalid development fund address");
        
        roostToken = IERC20(_roostToken);
        liquidityPool = _liquidityPool;
        developmentFund = _developmentFund;
    }
    
    function distribute() external onlyOwner nonReentrant {
        require(!distributionCompleted, "Distribution already completed");
        
        uint256 contractBalance = roostToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to distribute");
        
        uint256 liquidityAmount = (contractBalance * LIQUIDITY_POOL_SHARE) / 100;
        uint256 developmentAmount = (contractBalance * DEVELOPMENT_SHARE) / 100;
        
        // Ensure total distribution equals contract balance (handles rounding errors)
        if (liquidityAmount + developmentAmount < contractBalance) {
            developmentAmount += contractBalance - (liquidityAmount + developmentAmount);
        }
        
        require(roostToken.transfer(liquidityPool, liquidityAmount), "Liquidity transfer failed");
        require(roostToken.transfer(developmentFund, developmentAmount), "Development transfer failed");
        
        distributionCompleted = true;
        
        emit DistributionExecuted(liquidityAmount, developmentAmount, block.timestamp);
    }
    
    function updateLiquidityPool(address _newLiquidityPool) external onlyOwner {
        require(_newLiquidityPool != address(0), "Invalid liquidity pool address");
        require(!distributionCompleted, "Distribution already completed");
        liquidityPool = _newLiquidityPool;
    }
    
    function updateDevelopmentFund(address _newDevelopmentFund) external onlyOwner {
        require(_newDevelopmentFund != address(0), "Invalid development fund address");
        require(!distributionCompleted, "Distribution already completed");
        developmentFund = _newDevelopmentFund;
    }
    
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(roostToken) || !distributionCompleted, "Cannot withdraw ROOST after distribution");
        IERC20(_token).transfer(owner(), _amount);
    }
}
```
