"""
Generated Code Metadata:
========================
Original URL: https://hehe-dapps.pages.dev
Prompt: Develop a simple smart contract in Solidity that allows users to stake $HEHE tokens and earn a percentage boost in rewards, as described in the $HEHE ecosystem.
Generated: DETERMINISTIC_0ffb27497a9d804a
Batch ID: 20250622_205751
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract HEHEStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Staking token (HEHE)
    IERC20 public stakingToken;

    // Staking parameters
    uint256 public constant REWARD_RATE = 10; // 10% annual reward rate
    uint256 public constant BOOST_RATE = 5;   // 5% additional boost
    uint256 public constant MIN_STAKE_DURATION = 7 days;
    uint256 public totalStaked;

    // Stakeholder information
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        bool isBoosted;
    }

    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount, bool isBoosted);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @notice Stake HEHE tokens to earn rewards
     * @param amount Amount of tokens to stake
     * @param useBoost Whether to use the reward boost
     */
    function stake(uint256 amount, bool useBoost) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount == 0, "Already staked");

        stakes[msg.sender] = Stake({
            amount: amount,
            stakedAt: block.timestamp,
            isBoosted: useBoost
        });

        totalStaked += amount;

        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount, useBoost);
    }

    /**
     * @notice Unstake tokens and claim rewards
     */
    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        require(
            block.timestamp >= userStake.stakedAt + MIN_STAKE_DURATION,
            "Minimum stake duration not reached"
        );

        uint256 stakedAmount = userStake.amount;
        uint256 reward = calculateReward(msg.sender);

        totalStaked -= stakedAmount;
        delete stakes[msg.sender];

        uint256 totalToTransfer = stakedAmount + reward;
        stakingToken.safeTransfer(msg.sender, totalToTransfer);

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @notice Calculate reward for a staker
     * @param staker Address of the staker
     * @return reward Calculated reward amount
     */
    function calculateReward(address staker) public view returns (uint256 reward) {
        Stake memory userStake = stakes[staker];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.stakedAt;
        uint256 annualReward = (userStake.amount * REWARD_RATE) / 100;
        uint256 baseReward = (annualReward * stakingDuration) / 365 days;

        if (userStake.isBoosted) {
            uint256 boostAmount = (baseReward * BOOST_RATE) / 100;
            reward = baseReward + boostAmount;
        } else {
            reward = baseReward;
        }
    }

    /**
     * @notice Emergency withdraw without rewards
     */
    function emergencyWithdraw() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");

        uint256 amount = userStake.amount;
        totalStaked -= amount;
        delete stakes[msg.sender];

        stakingToken.safeTransfer(msg.sender, amount);

        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @notice Recover any ERC20 tokens sent to the contract by mistake
     * @param tokenAddress Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
