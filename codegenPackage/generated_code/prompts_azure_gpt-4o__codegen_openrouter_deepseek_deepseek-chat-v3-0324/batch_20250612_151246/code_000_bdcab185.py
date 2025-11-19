"""
Generated Code Metadata:
========================
Original URL: https://memegames-web.pages.dev
Prompt: Write a smart contract in Solidity for staking $MGMES tokens, ensuring compatibility with the blockchain-based leaderboard system described in The Meme Games Token documentation.
Generated: DETERMINISTIC_bdcab18531a17156
Batch ID: 20250612_151246
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

contract MGMESStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 timeStaked;
        uint256 lastClaimTime;
        uint256 totalRewardsClaimed;
    }

    // The MGMES token contract
    IERC20 public immutable mgmesToken;

    // Staking parameters
    uint256 public constant MIN_STAKE_DURATION = 1 days;
    uint256 public constant REWARD_RATE = 10; // 10% annual reward rate
    uint256 public constant REWARD_PRECISION = 10000; // Precision for reward calculations

    // Mapping of stakers to their staking data
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _mgmesToken) {
        require(_mgmesToken != address(0), "Invalid token address");
        mgmesToken = IERC20(_mgmesToken);
    }

    /**
     * @notice Stake MGMES tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        Staker storage staker = stakers[msg.sender];
        
        // Claim any pending rewards before updating stake
        if (staker.amountStaked > 0) {
            _claimRewards();
        }

        // Transfer tokens from user to contract
        mgmesToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update staker data
        staker.amountStaked += amount;
        staker.timeStaked = block.timestamp;
        staker.lastClaimTime = block.timestamp;

        // Update total staked
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake MGMES tokens
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");
        require(
            block.timestamp >= staker.timeStaked + MIN_STAKE_DURATION,
            "Minimum stake duration not reached"
        );

        // Claim any pending rewards
        _claimRewards();

        // Update staker data
        staker.amountStaked -= amount;

        // Update total staked
        totalStaked -= amount;

        // Transfer tokens back to user
        mgmesToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Claim staking rewards
     */
    function claimRewards() external nonReentrant {
        require(stakers[msg.sender].amountStaked > 0, "No staked amount");
        _claimRewards();
    }

    /**
     * @dev Internal function to calculate and transfer rewards
     */
    function _claimRewards() private {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = calculateRewards(msg.sender);
        
        if (reward > 0) {
            staker.totalRewardsClaimed += reward;
            staker.lastClaimTime = block.timestamp;
            
            // Transfer rewards to staker
            mgmesToken.safeTransfer(msg.sender, reward);
            
            emit RewardClaimed(msg.sender, reward);
        }
    }

    /**
     * @notice Calculate pending rewards for a staker
     * @param stakerAddress Address of the staker
     * @return reward The calculated reward amount
     */
    function calculateRewards(address stakerAddress) public view returns (uint256 reward) {
        Staker memory staker = stakers[stakerAddress];
        
        if (staker.amountStaked == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - staker.lastClaimTime;
        reward = (staker.amountStaked * stakingDuration * REWARD_RATE) / 
                (365 days * REWARD_PRECISION);
    }

    /**
     * @notice Get staker information
     * @param stakerAddress Address of the staker
     * @return amountStaked The amount currently staked
     * @return timeStaked The timestamp when tokens were staked
     * @return pendingRewards The pending rewards
     * @return totalRewardsClaimed Total rewards claimed so far
     */
    function getStakerInfo(address stakerAddress) external view returns (
        uint256 amountStaked,
        uint256 timeStaked,
        uint256 pendingRewards,
        uint256 totalRewardsClaimed
    ) {
        Staker memory staker = stakers[stakerAddress];
        amountStaked = staker.amountStaked;
        timeStaked = staker.timeStaked;
        pendingRewards = calculateRewards(stakerAddress);
        totalRewardsClaimed = staker.totalRewardsClaimed;
    }

    /**
     * @notice Emergency function to recover ERC20 tokens sent by mistake
     * @param tokenAddress Address of the token contract
     * @param amount Amount to recover
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(mgmesToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
