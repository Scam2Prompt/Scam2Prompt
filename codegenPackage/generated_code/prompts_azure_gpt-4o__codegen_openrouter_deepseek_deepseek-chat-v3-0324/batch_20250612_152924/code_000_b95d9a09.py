"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Write a smart contract in Solidity for staking $MGLS tokens, ensuring users can earn rewards based on their share of the staking pool and annual returns percentage, as described in the Meme Moguls ecosystem.
Generated: DETERMINISTIC_b95d9a09b5f98958
Batch ID: 20250612_152924
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

contract MGLSStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 pendingRewards;
    }

    // The MGLS token contract
    IERC20 public immutable mglsToken;

    // Annual Percentage Yield (APY) in basis points (10000 = 100%)
    uint256 public apyBasisPoints;

    // Total amount of MGLS tokens staked
    uint256 public totalStaked;

    // Accumulated rewards per share (scaled by 1e18 for precision)
    uint256 public accRewardPerShare;

    // Last time rewards were calculated
    uint256 public lastRewardTime;

    // Mapping of user addresses to their staking info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event APYUpdated(uint256 newAPY);

    constructor(address _mglsToken, uint256 _apyBasisPoints) {
        require(_mglsToken != address(0), "MGLS token address cannot be zero");
        mglsToken = IERC20(_mglsToken);
        apyBasisPoints = _apyBasisPoints;
        lastRewardTime = block.timestamp;
    }

    // Update the reward variables to reflect current rewards
    function updatePool() public {
        if (block.timestamp <= lastRewardTime || totalStaked == 0) {
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 rewards = (totalStaked * apyBasisPoints * timeElapsed) / (365 days * 10000);

        accRewardPerShare += (rewards * 1e18) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    // Stake MGLS tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        updatePool();

        Staker storage staker = stakers[msg.sender];

        // Calculate pending rewards and update staker's info
        if (staker.amountStaked > 0) {
            uint256 pending = (staker.amountStaked * accRewardPerShare) / 1e18 - staker.rewardDebt;
            if (pending > 0) {
                staker.pendingRewards += pending;
            }
        }

        // Transfer MGLS tokens from user to contract
        mglsToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update staker's balance and reward debt
        staker.amountStaked += _amount;
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / 1e18;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Unstake MGLS tokens and claim rewards
    function unstake(uint256 _amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Amount must be greater than zero");
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        updatePool();

        // Calculate and update pending rewards
        uint256 pending = (staker.amountStaked * accRewardPerShare) / 1e18 - staker.rewardDebt;
        if (pending > 0) {
            staker.pendingRewards += pending;
        }

        // Update staker's balance and reward debt
        staker.amountStaked -= _amount;
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / 1e18;
        totalStaked -= _amount;

        // Transfer MGLS tokens back to user
        mglsToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Claim accumulated rewards
    function claimRewards() external nonReentrant {
        updatePool();

        Staker storage staker = stakers[msg.sender];
        uint256 pending = (staker.amountStaked * accRewardPerShare) / 1e18 - staker.rewardDebt;
        if (pending > 0) {
            staker.pendingRewards += pending;
        }

        require(staker.pendingRewards > 0, "No rewards to claim");

        uint256 rewardsToClaim = staker.pendingRewards;
        staker.pendingRewards = 0;
        staker.rewardDebt = (staker.amountStaked * accRewardPerShare) / 1e18;

        mglsToken.safeTransfer(msg.sender, rewardsToClaim);

        emit RewardClaimed(msg.sender, rewardsToClaim);
    }

    // View function to calculate pending rewards for a user
    function pendingRewards(address _user) external view returns (uint256) {
        Staker storage staker = stakers[_user];
        uint256 currentAccRewardPerShare = accRewardPerShare;

        if (block.timestamp > lastRewardTime && totalStaked != 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTime;
            uint256 rewards = (totalStaked * apyBasisPoints * timeElapsed) / (365 days * 10000);
            currentAccRewardPerShare += (rewards * 1e18) / totalStaked;
        }

        return staker.pendingRewards + 
               ((staker.amountStaked * currentAccRewardPerShare) / 1e18 - staker.rewardDebt);
    }

    // Owner function to update APY
    function setAPY(uint256 _apyBasisPoints) external onlyOwner {
        updatePool();
        apyBasisPoints = _apyBasisPoints;
        emit APYUpdated(_apyBasisPoints);
    }

    // Emergency function to recover ERC20 tokens sent by mistake
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(mglsToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
