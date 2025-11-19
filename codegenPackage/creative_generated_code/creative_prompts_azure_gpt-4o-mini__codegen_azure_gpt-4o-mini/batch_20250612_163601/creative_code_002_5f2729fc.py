"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qudefi-ai.pages.dev
Prompt: Create a sample Solidity smart contract for the QuDefi token, ensuring it includes features for automated daily snapshots and eligibility criteria for rewards distribution.
Generated: DETERMINISTIC_5f2729fc9a3ff856
Batch ID: 20250612_163601
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract QuDefiToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to store daily snapshots
    mapping(uint256 => uint256) public dailySnapshots;
    mapping(address => uint256) public lastClaimedSnapshot;
    
    // Reward eligibility threshold
    uint256 public eligibilityThreshold = 100 * 10**18; // 100 tokens
    // Reward distribution percentage
    uint256 public rewardPercentage = 5; // 5%

    // Event to be emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 rewardAmount);

    constructor() ERC20("QuDefi", "QDT") {
        _mint(msg.sender, 1000000 * 10**18); // Mint initial supply to the owner
    }

    /**
     * @dev Function to take daily snapshot of total supply.
     * Can only be called by the owner.
     */
    function takeSnapshot() external onlyOwner {
        uint256 currentDay = block.timestamp / 1 days;
        dailySnapshots[currentDay] = totalSupply();
    }

    /**
     * @dev Function to claim rewards based on daily snapshots.
     * Users must hold at least the eligibility threshold of tokens.
     */
    function claimRewards() external {
        uint256 currentDay = block.timestamp / 1 days;
        require(dailySnapshots[currentDay] > 0, "No snapshot taken today");

        // Ensure user has not claimed rewards for today's snapshot yet
        require(lastClaimedSnapshot[msg.sender] < currentDay, "Rewards already claimed for today");

        // Check if user is eligible
        require(balanceOf(msg.sender) >= eligibilityThreshold, "Insufficient balance to claim rewards");

        // Calculate reward based on 5% of the total supply
        uint256 rewardAmount = dailySnapshots[currentDay].mul(rewardPercentage).div(100);
        
        // Transfer rewards to the user
        _mint(msg.sender, rewardAmount);
        lastClaimedSnapshot[msg.sender] = currentDay; // Update last claimed snapshot

        emit RewardsDistributed(msg.sender, rewardAmount);
    }

    /**
     * @dev Admin function to update eligibility threshold.
     * @param _newThreshold New eligibility threshold.
     */
    function updateEligibilityThreshold(uint256 _newThreshold) external onlyOwner {
        eligibilityThreshold = _newThreshold;
    }

    /**
     * @dev Admin function to update reward distribution percentage.
     * @param _newPercentage New reward distribution percentage.
     */
    function updateRewardPercentage(uint256 _newPercentage) external onlyOwner {
        require(_newPercentage <= 100, "Percentage must be <= 100");
        rewardPercentage = _newPercentage;
    }
}
```
