"""
Generated Code Metadata:
========================
Original URL: https://proposal-ownthedoge.com
Prompt: Generate a smart contract in Solidity for distributing rewards to $DOG and $COCORO holders, referencing the voting system mentioned on the website.
Generated: DETERMINISTIC_a8a64d2580606582
Batch ID: 20250612_154631
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract RewardDistributor is Ownable {
    using SafeMath for uint256;

    // Token contracts
    IERC20 public dogToken;
    IERC20 public cocoroToken;
    IERC20 public rewardToken;

    // Reward parameters
    uint256 public rewardPeriod; // In blocks
    uint256 public lastDistributionBlock;
    uint256 public totalRewardPerPeriod;

    // Voting weights (set by governance)
    uint256 public dogWeight = 1;
    uint256 public cocoroWeight = 1;

    // Track claimed rewards
    mapping(address => uint256) public lastClaimedBlock;
    mapping(address => uint256) public pendingRewards;

    // Events
    event RewardsDistributed(uint256 totalDistributed);
    event RewardClaimed(address indexed user, uint256 amount);
    event WeightsUpdated(uint256 newDogWeight, uint256 newCocoroWeight);

    constructor(
        address _dogToken,
        address _cocoroToken,
        address _rewardToken,
        uint256 _rewardPeriod,
        uint256 _totalRewardPerPeriod
    ) {
        require(_dogToken != address(0), "Invalid DOG token address");
        require(_cocoroToken != address(0), "Invalid COCORO token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardPeriod > 0, "Reward period must be positive");
        require(_totalRewardPerPeriod > 0, "Reward amount must be positive");

        dogToken = IERC20(_dogToken);
        cocoroToken = IERC20(_cocoroToken);
        rewardToken = IERC20(_rewardToken);
        rewardPeriod = _rewardPeriod;
        totalRewardPerPeriod = _totalRewardPerPeriod;
        lastDistributionBlock = block.number;
    }

    /**
     * @dev Update voting weights (only callable by owner/governance)
     */
    function updateWeights(uint256 newDogWeight, uint256 newCocoroWeight) external onlyOwner {
        require(newDogWeight > 0 && newCocoroWeight > 0, "Weights must be positive");
        dogWeight = newDogWeight;
        cocoroWeight = newCocoroWeight;
        emit WeightsUpdated(newDogWeight, newCocoroWeight);
    }

    /**
     * @dev Distribute rewards to all eligible holders
     */
    function distributeRewards() external {
        require(block.number >= lastDistributionBlock + rewardPeriod, "Reward period not elapsed");

        uint256 currentBlock = block.number;
        uint256 blocksSinceLast = currentBlock.sub(lastDistributionBlock);
        lastDistributionBlock = currentBlock;

        uint256 totalDog = dogToken.totalSupply();
        uint256 totalCocoro = cocoroToken.totalSupply();

        // Calculate weighted total
        uint256 weightedTotal = totalDog.mul(dogWeight).add(totalCocoro.mul(cocoroWeight));
        require(weightedTotal > 0, "No tokens staked");

        // Transfer reward tokens from owner to contract
        rewardToken.transferFrom(owner(), address(this), totalRewardPerPeriod);

        emit RewardsDistributed(totalRewardPerPeriod);
    }

    /**
     * @dev Calculate pending rewards for a user
     */
    function calculatePendingRewards(address user) public view returns (uint256) {
        if (lastClaimedBlock[user] >= lastDistributionBlock) {
            return pendingRewards[user];
        }

        uint256 dogBalance = dogToken.balanceOf(user);
        uint256 cocoroBalance = cocoroToken.balanceOf(user);

        uint256 weightedBalance = dogBalance.mul(dogWeight).add(cocoroBalance.mul(cocoroWeight));
        uint256 totalWeighted = dogToken.totalSupply().mul(dogWeight).add(cocoroToken.totalSupply().mul(cocoroWeight));

        if (totalWeighted == 0) {
            return 0;
        }

        uint256 share = weightedBalance.mul(totalRewardPerPeriod).div(totalWeighted);
        return pendingRewards[user].add(share);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external {
        uint256 rewardAmount = calculatePendingRewards(msg.sender);
        require(rewardAmount > 0, "No rewards to claim");

        pendingRewards[msg.sender] = 0;
        lastClaimedBlock[msg.sender] = block.number;

        rewardToken.transfer(msg.sender, rewardAmount);
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Update reward parameters (only callable by owner)
     */
    function updateRewardParameters(uint256 newRewardPeriod, uint256 newTotalReward) external onlyOwner {
        require(newRewardPeriod > 0, "Reward period must be positive");
        require(newTotalReward > 0, "Reward amount must be positive");
        
        rewardPeriod = newRewardPeriod;
        totalRewardPerPeriod = newTotalReward;
    }

    /**
     * @dev Emergency withdraw tokens (only callable by owner)
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```
