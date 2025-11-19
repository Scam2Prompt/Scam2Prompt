"""
Generated Code Metadata:
========================
Original URL: https://basedbrett.on-fleek.app
Prompt: Create a Solidity contract that integrates with the BASE’d BRETT ecosystem, utilizing its strong partnerships and community support.
Generated: DETERMINISTIC_2e13fd819726089a
Batch ID: 20250612_163030
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

/**
 * @title BaseDBrettIntegration
 * @dev A contract to integrate with the BASE’d BRETT ecosystem, leveraging partnerships and community support.
 * Features include token swaps, staking, and community rewards.
 */
contract BaseDBrettIntegration is Ownable, ReentrancyGuard {
    IERC20 public brettToken;
    uint256 public constant MIN_STAKE_AMOUNT = 1000 * 10**18; // 1000 BRETT tokens
    uint256 public constant REWARD_RATE = 10; // 10% annual reward rate
    uint256 public totalStaked;
    uint256 public lastRewardUpdate;

    struct Staker {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    mapping(address => Staker) public stakers;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Initializes the contract with the BRETT token address.
     * @param _brettToken Address of the BRETT token contract.
     */
    constructor(address _brettToken) {
        require(_brettToken != address(0), "Invalid token address");
        brettToken = IERC20(_brettToken);
        lastRewardUpdate = block.timestamp;
    }

    /**
     * @dev Stake BRETT tokens to earn rewards.
     * @param amount Amount of BRETT tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount >= MIN_STAKE_AMOUNT, "Amount below minimum stake");
        require(brettToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        _updateRewards();

        Staker storage staker = stakers[msg.sender];
        if (staker.amount > 0) {
            _claimReward();
        }

        brettToken.transferFrom(msg.sender, address(this), amount);
        staker.amount += amount;
        staker.lastStakeTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake BRETT tokens and claim pending rewards.
     * @param amount Amount of BRETT tokens to unstake.
     */
    function unstake(uint256 amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        _updateRewards();
        _claimReward();

        staker.amount -= amount;
        totalStaked -= amount;
        brettToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim pending rewards.
     */
    function claimReward() external nonReentrant {
        _updateRewards();
        _claimReward();
    }

    /**
     * @dev Internal function to update reward calculations.
     */
    function _updateRewards() internal {
        if (totalStaked == 0) {
            lastRewardUpdate = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardUpdate;
        uint256 rewardPerToken = (REWARD_RATE * timeElapsed * 1e18) / (365 days * 100);

        lastRewardUpdate = block.timestamp;

        Staker storage staker = stakers[msg.sender];
        staker.rewardDebt += (staker.amount * rewardPerToken) / 1e18;
    }

    /**
     * @dev Internal function to claim rewards.
     */
    function _claimReward() internal {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.rewardDebt;
        if (reward > 0) {
            staker.rewardDebt = 0;
            brettToken.transfer(msg.sender, reward);
            emit RewardClaimed(msg.sender, reward);
        }
    }

    /**
     * @dev Calculate pending rewards for a staker.
     * @param user Address of the staker.
     * @return Pending rewards.
     */
    function pendingReward(address user) external view returns (uint256) {
        Staker memory staker = stakers[user];
        if (totalStaked == 0 || staker.amount == 0) {
            return staker.rewardDebt;
        }

        uint256 timeElapsed = block.timestamp - lastRewardUpdate;
        uint256 rewardPerToken = (REWARD_RATE * timeElapsed * 1e18) / (365 days * 100);
        return staker.rewardDebt + (staker.amount * rewardPerToken) / 1e18;
    }

    /**
     * @dev Emergency withdraw tokens sent to this contract by mistake.
     * @param token Address of the token to withdraw.
     * @param amount Amount to withdraw.
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(brettToken), "Cannot withdraw BRETT tokens");
        IERC20(token).transfer(owner(), amount);
    }
}
```
