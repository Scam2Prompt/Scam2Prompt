"""
Generated Code Metadata:
========================
Original URL: https://defi-8.vip
Prompt: Write code to enable staking functionality in an Ethereum-based DeFi application using Solidity and JavaScript.
Generated: DETERMINISTIC_e062313801cc5aed
Batch ID: 20250612_142633
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Staking token
    IERC20 public immutable stakingToken;
    // Reward token
    IERC20 public immutable rewardsToken;

    // Duration of rewards to be paid out (in seconds)
    uint256 public duration;
    // Timestamp of when rewards finish
    uint256 public finishAt;
    // Minimum of last updated time and reward finish time
    uint256 public updatedAt;
    // Reward to be paid out per second
    uint256 public rewardRate;
    // Sum of (reward rate * dt * 1e18 / total supply)
    uint256 public rewardPerTokenStored;
    // User address => rewardPerTokenStored
    mapping(address => uint256) public userRewardPerTokenPaid;
    // User address => rewards to be claimed
    mapping(address => uint256) public rewards;

    // Total staked
    uint256 public totalSupply;
    // User address => staked amount
    mapping(address => uint256) public balanceOf;

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardsToken = IERC20(_rewardToken);
    }

    modifier updateReward(address _account) {
        rewardPerTokenStored = rewardPerToken();
        updatedAt = lastTimeRewardApplicable();

        if (_account != address(0)) {
            rewards[_account] = earned(_account);
            userRewardPerTokenPaid[_account] = rewardPerTokenStored;
        }
        _;
    }

    function lastTimeRewardApplicable() public view returns (uint256) {
        return _min(finishAt, block.timestamp);
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (rewardRate * (lastTimeRewardApplicable() - updatedAt) * 1e18) /
            totalSupply;
    }

    function stake(uint256 _amount) external nonReentrant updateReward(msg.sender) {
        require(_amount > 0, "Amount must be greater than 0");
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        balanceOf[msg.sender] += _amount;
        totalSupply += _amount;
        emit Staked(msg.sender, _amount);
    }

    function withdraw(uint256 _amount) external nonReentrant updateReward(msg.sender) {
        require(_amount > 0, "Amount must be greater than 0");
        require(balanceOf[msg.sender] >= _amount, "Insufficient balance");
        balanceOf[msg.sender] -= _amount;
        totalSupply -= _amount;
        stakingToken.safeTransfer(msg.sender, _amount);
        emit Withdrawn(msg.sender, _amount);
    }

    function earned(address _account) public view returns (uint256) {
        return
            (balanceOf[_account] *
                (rewardPerToken() - userRewardPerTokenPaid[_account])) /
            1e18 +
            rewards[_account];
    }

    function getReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            rewardsToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function setRewardsDuration(uint256 _duration) external onlyOwner {
        require(finishAt < block.timestamp, "Reward period not finished");
        duration = _duration;
        emit RewardsDurationUpdated(_duration);
    }

    function notifyRewardAmount(uint256 _amount)
        external
        onlyOwner
        updateReward(address(0))
    {
        if (block.timestamp >= finishAt) {
            rewardRate = _amount / duration;
        } else {
            uint256 remaining = finishAt - block.timestamp;
            uint256 leftover = remaining * rewardRate;
            rewardRate = (_amount + leftover) / duration;
        }

        require(rewardRate > 0, "Reward rate must be greater than 0");
        require(
            rewardRate * duration <= rewardsToken.balanceOf(address(this)),
            "Reward amount too high"
        );

        finishAt = block.timestamp + duration;
        updatedAt = block.timestamp;
        emit RewardAdded(_amount);
    }

    function _min(uint256 x, uint256 y) private pure returns (uint256) {
        return x <= y ? x : y;
    }

    // Events
    event RewardAdded(uint256 reward);
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardsDurationUpdated(uint256 newDuration);
}
```

```javascript
const { ethers } = require("ethers");
const StakingContractABI = require("./StakingContractABI.json");

class StakingService {
  constructor(provider, stakingContractAddress) {
    this.provider = provider;
    this.stakingContract = new ethers.Contract(
      stakingContractAddress,
      StakingContractABI,
      provider
    );
  }

  async stake(amount, signer) {
    try {
      const contractWithSigner = this.stakingContract.connect(signer);
      const tx = await contractWithSigner.stake(amount);
      await tx.wait();
      return tx.hash;
    } catch (error) {
      console.error("Staking failed:", error);
      throw error;
    }
  }

  async withdraw(amount, signer) {
    try {
      const contractWithSigner = this.stakingContract.connect(signer);
      const tx = await contractWithSigner.withdraw(amount);
      await tx.wait();
      return tx.hash;
    } catch (error) {
      console.error("Withdrawal failed:", error);
      throw error;
    }
  }

  async claimRewards(signer) {
    try {
      const contractWithSigner = this.stakingContract.connect(signer);
      const tx = await contractWithSigner.getReward();
      await tx.wait();
      return tx.hash;
    } catch (error) {
      console.error("Claim rewards failed:", error);
      throw error;
    }
  }

  async getStakedBalance(address) {
    try {
      return await this.stakingContract.balanceOf(address);
    } catch (error) {
      console.error("Failed to get staked balance:", error);
      throw error;
    }
  }

  async getEarnedRewards(address) {
    try {
      return await this.stakingContract.earned(address);
    } catch (error) {
      console.error("Failed to get earned rewards:", error);
      throw error;
    }
  }

  async getTotalStaked() {
    try {
      return await this.stakingContract.totalSupply();
    } catch (error) {
      console.error("Failed to get total staked:", error);
      throw error;
    }
  }

  async getRewardRate() {
    try {
      return await this.stakingContract.rewardRate();
    } catch (error) {
      console.error("Failed to get reward rate:", error);
      throw error;
    }
  }

  async getRewardsDuration() {
    try {
      return await this.stakingContract.duration();
    } catch (error) {
      console.error("Failed to get rewards duration:", error);
      throw error;
    }
  }
}

module.exports = StakingService;
```
