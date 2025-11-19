"""
Generated Code Metadata:
========================
Original URL: https://rocketspool.pages.dev
Prompt: Write a Solidity function to simulate the penalty minimization mechanism used in Rocket Pool, where losses from bad nodes are socialized across the network.
Generated: DETERMINISTIC_c3248da4f26f9691
Batch ID: 20250612_151918
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

/**
 * @title Rocket Pool Penalty Simulation
 * @dev Simulates the penalty minimization mechanism where losses from bad nodes are socialized
 */
contract RocketPoolPenaltySimulation {
    // Total ETH staked in the network
    uint256 public totalStakedETH;
    
    // Total ETH lost due to bad nodes
    uint256 public totalLostETH;
    
    // Mapping of staker addresses to their staked ETH amounts
    mapping(address => uint256) public stakerBalances;
    
    // Events
    event Staked(address indexed staker, uint256 amount);
    event PenaltyApplied(uint256 totalLost);
    event LossSocialized(address indexed staker, uint256 amountLost);
    
    /**
     * @dev Stake ETH into the network
     * @param _amount Amount of ETH to stake
     */
    function stakeETH(uint256 _amount) external payable {
        require(msg.value == _amount, "Incorrect ETH amount");
        require(_amount > 0, "Cannot stake 0 ETH");
        
        stakerBalances[msg.sender] += _amount;
        totalStakedETH += _amount;
        
        emit Staked(msg.sender, _amount);
    }
    
    /**
     * @dev Apply penalty from bad nodes (only callable by owner/DAO in real implementation)
     * @param _lostAmount Amount of ETH lost due to bad nodes
     */
    function applyPenalty(uint256 _lostAmount) external {
        require(_lostAmount > 0, "Lost amount must be positive");
        require(_lostAmount <= totalStakedETH, "Cannot lose more than total staked");
        
        totalLostETH += _lostAmount;
        totalStakedETH -= _lostAmount;
        
        emit PenaltyApplied(_lostAmount);
    }
    
    /**
     * @dev Calculate and distribute the socialized loss to all stakers proportionally
     */
    function socializeLoss() external {
        require(totalLostETH > 0, "No losses to socialize");
        require(totalStakedETH > 0, "No staked ETH to socialize across");
        
        uint256 lossPerStaker = totalLostETH * 1e18 / totalStakedETH;
        
        // Iterate through all stakers (in real implementation would use more efficient method)
        // This is simplified for demonstration
        address[] memory stakers = _getAllStakers();
        
        for (uint256 i = 0; i < stakers.length; i++) {
            address staker = stakers[i];
            uint256 stakerBalance = stakerBalances[staker];
            
            if (stakerBalance > 0) {
                uint256 stakerLoss = (stakerBalance * lossPerStaker) / 1e18;
                stakerBalances[staker] -= stakerLoss;
                
                emit LossSocialized(staker, stakerLoss);
            }
        }
        
        totalLostETH = 0;
    }
    
    /**
     * @dev Internal function to get all stakers (simplified for demo)
     * @return Array of staker addresses
     */
    function _getAllStakers() internal pure returns (address[] memory) {
        // In production, you would use a more efficient method to track stakers
        // This is just for demonstration purposes
        revert("Implement proper staker tracking in production");
    }
    
    /**
     * @dev Allow stakers to withdraw their ETH after penalties
     */
    function withdraw() external {
        uint256 balance = stakerBalances[msg.sender];
        require(balance > 0, "No ETH to withdraw");
        
        stakerBalances[msg.sender] = 0;
        totalStakedETH -= balance;
        
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "ETH transfer failed");
    }
}
```
