"""
Generated Code Metadata:
========================
Original URL: https://dragonxwin.pages.dev
Prompt: Generate a Solidity contract that allows users to stake TitanX and claim rewards based on the current staking metrics provided by DragonX.
Generated: DETERMINISTIC_428234ac88719011
Batch ID: 20250612_155226
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TitanX Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake TitanX and claim rewards based on the current staking metrics provided by DragonX.
 */
contract TitanXStaking is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // Mapping of reward rates based on staking metrics
    mapping (uint256 => RewardRate) public rewardRates;

    // Address of TitanX token
    address public titanXAddress;

    // Address of reward token
    address public rewardTokenAddress;

    // Address of DragonX metrics provider
    address public dragonXMetricsProvider;

    // Event emitted when user stakes TitanX
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes TitanX
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Struct to store user staking information
    struct UserStakingInfo {
        uint256 stakedAmount;
        uint256 lastStakedTimestamp;
    }

    // Struct to store reward rates
    struct RewardRate {
        uint256 rate;
        uint256 startTimestamp;
        uint256 endTimestamp;
    }

    /**
     * @notice Constructor
     * @param _titanXAddress Address of TitanX token
     * @param _rewardTokenAddress Address of reward token
     * @param _dragonXMetricsProvider Address of DragonX metrics provider
     */
    constructor(address _titanXAddress, address _rewardTokenAddress, address _dragonXMetricsProvider) public {
        titanXAddress = _titanXAddress;
        rewardTokenAddress = _rewardTokenAddress;
        dragonXMetricsProvider = _dragonXMetricsProvider;
    }

    /**
     * @notice Stake TitanX
     * @param _amount Amount of TitanX to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Invalid stake amount");

        // Transfer TitanX from user to contract
        IERC20(titanXAddress).safeTransferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.add(_amount);
        userStakingInfos[msg.sender].lastStakedTimestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake TitanX
     * @param _amount Amount of TitanX to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Invalid unstake amount");
        require(userStakingInfos[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        // Update user staking information
        userStakingInfos[msg.sender].stakedAmount = userStakingInfos[msg.sender].stakedAmount.sub(_amount);

        // Transfer TitanX from contract to user
        IERC20(titanXAddress).safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public {
        // Calculate reward amount
        uint256 rewardAmount = calculateRewardAmount(msg.sender);

        // Transfer reward to user
        IERC20(rewardTokenAddress).safeTransfer(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Calculate reward amount for user
     * @param _user Address of user
     * @return Reward amount
     */
    function calculateRewardAmount(address _user) internal view returns (uint256) {
        // Get current staking metrics from DragonX
        uint256 currentStakingMetrics = getCurrentStakingMetrics();

        // Get user's staked amount and last staked timestamp
        uint256 stakedAmount = userStakingInfos[_user].stakedAmount;
        uint256 lastStakedTimestamp = userStakingInfos[_user].lastStakedTimestamp;

        // Calculate reward rate
        uint256 rewardRate = getRewardRate(currentStakingMetrics);

        // Calculate reward amount
        uint256 rewardAmount = stakedAmount.mul(rewardRate).mul(block.timestamp.sub(lastStakedTimestamp)).div(1e18);

        return rewardAmount;
    }

    /**
     * @notice Get current staking metrics from DragonX
     * @return Current staking metrics
     */
    function getCurrentStakingMetrics() internal view returns (uint256) {
        // Call DragonX metrics provider to get current staking metrics
        // For demonstration purposes, assume metrics provider returns a fixed value
        return 1000;
    }

    /**
     * @notice Get reward rate based on current staking metrics
     * @param _currentStakingMetrics Current staking metrics
     * @return Reward rate
     */
    function getRewardRate(uint256 _currentStakingMetrics) internal view returns (uint256) {
        // For demonstration purposes, assume reward rate is fixed
        return 10;
    }

    /**
     * @notice Update reward rates
     * @param _rewardRates Array of reward rates
     */
    function updateRewardRates(RewardRate[] memory _rewardRates) public onlyOwner {
        for (uint256 i = 0; i < _rewardRates.length; i++) {
            rewardRates[_rewardRates[i].startTimestamp] = _rewardRates[i];
        }
    }

    /**
     * @notice Withdraw tokens from contract
     * @param _token Address of token to withdraw
     * @param _amount Amount of token to withdraw
     */
    function withdrawTokens(address _token, uint256 _amount) public onlyOwner {
        IERC20(_token).safeTransfer(msg.sender, _amount);
    }
}
```
