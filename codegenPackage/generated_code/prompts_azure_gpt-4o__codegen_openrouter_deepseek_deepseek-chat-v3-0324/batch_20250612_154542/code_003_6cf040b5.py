"""
Generated Code Metadata:
========================
Original URL: https://broccoliclaim.web.app
Prompt: Create a smart contract for managing token rewards distribution, inspired by the Broccoli platform's single-transaction claim functionality.
Generated: DETERMINISTIC_6cf040b545fec229
Batch ID: 20250612_154542
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

contract TokenRewards is Ownable, ReentrancyGuard {
    IERC20 public rewardToken;
    uint256 public totalRewardsDistributed;
    uint256 public totalParticipants;

    struct Reward {
        uint256 amount;
        uint256 claimedAt;
        bool isClaimed;
    }

    mapping(address => Reward) public rewards;
    mapping(address => bool) public whitelistedDistributors;

    event RewardAdded(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event DistributorAdded(address indexed distributor);
    event DistributorRemoved(address indexed distributor);

    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    modifier onlyDistributor() {
        require(
            whitelistedDistributors[msg.sender] || msg.sender == owner(),
            "Not authorized"
        );
        _;
    }

    function addDistributor(address _distributor) external onlyOwner {
        require(_distributor != address(0), "Invalid address");
        require(!whitelistedDistributors[_distributor], "Already a distributor");
        whitelistedDistributors[_distributor] = true;
        emit DistributorAdded(_distributor);
    }

    function removeDistributor(address _distributor) external onlyOwner {
        require(whitelistedDistributors[_distributor], "Not a distributor");
        delete whitelistedDistributors[_distributor];
        emit DistributorRemoved(_distributor);
    }

    function addReward(address _user, uint256 _amount) external onlyDistributor {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Amount must be positive");

        if (rewards[_user].amount == 0) {
            totalParticipants += 1;
        }

        rewards[_user].amount += _amount;
        totalRewardsDistributed += _amount;

        emit RewardAdded(_user, _amount);
    }

    function claimReward() external nonReentrant {
        Reward storage reward = rewards[msg.sender];
        require(reward.amount > 0, "No rewards to claim");
        require(!reward.isClaimed, "Reward already claimed");

        uint256 amount = reward.amount;
        reward.amount = 0;
        reward.isClaimed = true;
        reward.claimedAt = block.timestamp;

        require(
            rewardToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit RewardClaimed(msg.sender, amount);
    }

    function getRewardAmount(address _user) external view returns (uint256) {
        return rewards[_user].amount;
    }

    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(
            rewardToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );
    }

    function getContractBalance() external view returns (uint256) {
        return rewardToken.balanceOf(address(this));
    }
}
```
