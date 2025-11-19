"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-dashboard.pages.dev
Prompt: Write a smart contract in Solidity that enables staking for $PEPU tokens on a Layer 2 blockchain, ensuring double staking rewards as described in Pepe Unchained.
Generated: DETERMINISTIC_98c82299e4b35771
Batch ID: 20250612_153447
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

contract PEPUStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakeTime;
    }

    // The PEPU token contract
    IERC20 public immutable pepuToken;

    // Reward rate (2x multiplier)
    uint256 public constant REWARD_RATE = 2;
    uint256 public constant REWARD_PERIOD = 1 days;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping of staker addresses to their staking info
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _pepuToken) {
        require(_pepuToken != address(0), "Invalid token address");
        pepuToken = IERC20(_pepuToken);
    }

    /**
     * @notice Stake PEPU tokens to earn rewards
     * @param amount The amount of PEPU tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        Staker storage staker = stakers[msg.sender];

        // Claim any pending rewards before staking
        if (staker.amountStaked > 0) {
            _claimRewards(msg.sender);
        }

        // Transfer tokens from user to contract
        pepuToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update staker's balance and reward debt
        staker.amountStaked += amount;
        staker.rewardDebt += (amount * REWARD_RATE * (block.timestamp - staker.lastStakeTime)) / REWARD_PERIOD;
        staker.lastStakeTime = block.timestamp;

        // Update total staked
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake PEPU tokens and claim rewards
     * @param amount The amount of PEPU tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked balance");

        // Claim rewards first
        _claimRewards(msg.sender);

        // Update staker's balance
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        pepuToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        _claimRewards(msg.sender);
    }

    /**
     * @dev Internal function to calculate and transfer rewards
     * @param user The address of the staker
     */
    function _claimRewards(address user) internal {
        Staker storage staker = stakers[user];
        if (staker.amountStaked == 0) return;

        uint256 reward = calculateReward(user);
        if (reward > 0) {
            staker.rewardDebt = 0;
            staker.lastStakeTime = block.timestamp;
            pepuToken.safeTransfer(user, reward);
            emit RewardClaimed(user, reward);
        }
    }

    /**
     * @notice Calculate pending rewards for a staker
     * @param user The address of the staker
     * @return The amount of pending rewards
     */
    function calculateReward(address user) public view returns (uint256) {
        Staker memory staker = stakers[user];
        if (staker.amountStaked == 0) return 0;

        uint256 timeElapsed = block.timestamp - staker.lastStakeTime;
        uint256 newReward = (staker.amountStaked * REWARD_RATE * timeElapsed) / REWARD_PERIOD;
        return staker.rewardDebt + newReward;
    }

    /**
     * @notice Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress The address of the token to recover
     * @param amount The amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(pepuToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
