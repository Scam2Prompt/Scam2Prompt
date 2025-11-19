"""
Generated Code Metadata:
========================
Original URL: https://usdart.top
Prompt: Generate a smart contract that facilitates reward distribution when a wallet is connected, as described in the REWARD Portal v2.
Generated: DETERMINISTIC_03b00214ac853558
Batch ID: 20250612_150658
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

contract RewardPortalV2 is Ownable, ReentrancyGuard {
    IERC20 public rewardToken;
    uint256 public rewardAmount;
    uint256 public cooldownPeriod;
    mapping(address => uint256) public lastClaimTime;

    event RewardClaimed(address indexed user, uint256 amount);
    event RewardTokenUpdated(address indexed newToken);
    event RewardAmountUpdated(uint256 newAmount);
    event CooldownUpdated(uint256 newCooldown);

    constructor(
        address _rewardToken,
        uint256 _rewardAmount,
        uint256 _cooldownPeriod
    ) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
        rewardAmount = _rewardAmount;
        cooldownPeriod = _cooldownPeriod;
    }

    function setRewardToken(address _newToken) external onlyOwner {
        require(_newToken != address(0), "Invalid token address");
        rewardToken = IERC20(_newToken);
        emit RewardTokenUpdated(_newToken);
    }

    function setRewardAmount(uint256 _newAmount) external onlyOwner {
        rewardAmount = _newAmount;
        emit RewardAmountUpdated(_newAmount);
    }

    function setCooldownPeriod(uint256 _newCooldown) external onlyOwner {
        cooldownPeriod = _newCooldown;
        emit CooldownUpdated(_newCooldown);
    }

    function claimReward() external nonReentrant {
        require(
            block.timestamp >= lastClaimTime[msg.sender] + cooldownPeriod,
            "Cooldown period not passed"
        );

        uint256 contractBalance = rewardToken.balanceOf(address(this));
        require(contractBalance >= rewardAmount, "Insufficient contract balance");

        lastClaimTime[msg.sender] = block.timestamp;
        bool success = rewardToken.transfer(msg.sender, rewardAmount);
        require(success, "Token transfer failed");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    function withdrawTokens(uint256 _amount) external onlyOwner {
        uint256 contractBalance = rewardToken.balanceOf(address(this));
        require(contractBalance >= _amount, "Insufficient contract balance");

        bool success = rewardToken.transfer(owner(), _amount);
        require(success, "Token transfer failed");
    }

    function getTimeUntilNextClaim(address _user) external view returns (uint256) {
        uint256 nextClaimTime = lastClaimTime[_user] + cooldownPeriod;
        if (block.timestamp >= nextClaimTime) {
            return 0;
        } else {
            return nextClaimTime - block.timestamp;
        }
    }
}
```
