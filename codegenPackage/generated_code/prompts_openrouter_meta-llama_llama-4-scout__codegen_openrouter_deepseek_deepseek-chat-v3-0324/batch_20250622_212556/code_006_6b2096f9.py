"""
Generated Code Metadata:
========================
Original URL: https://kishu.finance
Prompt: Develop a simple smart contract in Solidity to automate the distribution of rewards to Kishu Inu token holders.
Generated: DETERMINISTIC_6b2096f96e7a3d03
Batch ID: 20250622_212556
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

contract KishuRewardDistributor is Ownable {
    using SafeMath for uint256;

    IERC20 public kishuToken;
    uint256 public totalDistributed;
    uint256 public rewardPerToken;
    uint256 public lastDistributionTime;
    uint256 public distributionInterval;

    mapping(address => uint256) public lastClaimTime;
    mapping(address => uint256) public rewards;

    event RewardDistributed(address indexed holder, uint256 amount);
    event TokensDeposited(uint256 amount);
    event DistributionIntervalUpdated(uint256 newInterval);

    constructor(address _kishuTokenAddress, uint256 _distributionInterval) {
        require(_kishuTokenAddress != address(0), "Invalid token address");
        kishuToken = IERC20(_kishuTokenAddress);
        distributionInterval = _distributionInterval;
        lastDistributionTime = block.timestamp;
    }

    function depositTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(
            kishuToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        totalDistributed = totalDistributed.add(amount);
        rewardPerToken = rewardPerToken.add(amount);
        emit TokensDeposited(amount);
    }

    function updateDistributionInterval(uint256 _newInterval) external onlyOwner {
        require(_newInterval > 0, "Interval must be greater than 0");
        distributionInterval = _newInterval;
        emit DistributionIntervalUpdated(_newInterval);
    }

    function calculateReward(address holder, uint256 holderBalance) public view returns (uint256) {
        if (holderBalance == 0) return 0;
        return holderBalance.mul(rewardPerToken).div(kishuToken.totalSupply());
    }

    function claimReward() external {
        require(block.timestamp >= lastDistributionTime.add(distributionInterval), "Distribution interval not passed");
        uint256 holderBalance = kishuToken.balanceOf(msg.sender);
        require(holderBalance > 0, "No tokens held");

        uint256 reward = calculateReward(msg.sender, holderBalance);
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0;
        lastClaimTime[msg.sender] = block.timestamp;

        require(kishuToken.transfer(msg.sender, reward), "Reward transfer failed");
        emit RewardDistributed(msg.sender, reward);
    }

    function getPendingReward(address holder) external view returns (uint256) {
        uint256 holderBalance = kishuToken.balanceOf(holder);
        return calculateReward(holder, holderBalance);
    }

    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(
            kishuToken.transfer(msg.sender, amount),
            "Transfer failed"
        );
    }
}
```
