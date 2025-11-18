"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rewardusdctoken.com
Prompt: Write a Solidity function to calculate and distribute USDC rewards to holders of RUSDC tokens based on transaction fees collected from buy and sell operations.
Generated: DETERMINISTIC_09817cb8c407c089
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the RUSDC token
interface IRUSDC is IERC20 {
    function totalSupply() external view returns (uint256);
}

contract RewardDistributor is Ownable {
    // State variables
    IRUSDC public rusdcToken;  // Instance of the RUSDC token
    IERC20 public usdcToken;    // Instance of the USDC token
    
    // Mapping to track USDC rewards for each holder
    mapping(address => uint256) public rewards;
    
    // Total fees collected for reward distribution
    uint256 public totalFeesCollected;

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 amount);

    // Constructor to set the token addresses
    constructor(address _rusdcToken, address _usdcToken) {
        rusdcToken = IRUSDC(_rusdcToken);
        usdcToken = IERC20(_usdcToken);
    }

    // Function to collect fees and accumulate rewards
    function collectFees(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer USDC fees from the owner to this contract
        bool success = usdcToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed");

        totalFeesCollected += amount;
    }

    // Function to distribute rewards to RUSDC token holders
    function distributeRewards() external onlyOwner {
        uint256 totalSupply = rusdcToken.totalSupply();
        require(totalSupply > 0, "No RUSDC supply");

        // Calculate reward per token
        uint256 rewardPerToken = totalFeesCollected / totalSupply;

        // Distribute rewards to all RUSDC holders
        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = rusdcToken.holderAt(i); // Placeholder for a function to get holder
            uint256 holderBalance = rusdcToken.balanceOf(holder);

            if (holderBalance > 0) {
                // Calculate rewards for the holder
                uint256 holderReward = holderBalance * rewardPerToken;
                rewards[holder] += holderReward;
            }
        }

        // Reset accumulated fees after distribution
        totalFeesCollected = 0;

        emit RewardsDistributed(totalFeesCollected);
    }

    // Function to withdraw accumulated USDC rewards
    function withdrawRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to withdraw");

        // Reset the user's reward balance before transfer to prevent reentrancy
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        bool success = usdcToken.transfer(msg.sender, reward);
        require(success, "Transfer failed");
    }
}
```
