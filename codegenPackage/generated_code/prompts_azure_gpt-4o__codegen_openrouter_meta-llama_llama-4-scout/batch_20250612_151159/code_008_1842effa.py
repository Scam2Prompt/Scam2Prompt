"""
Generated Code Metadata:
========================
Original URL: https://kelllpppp-maiiiinnn812983128389123.pages.dev
Prompt: Develop a smart contract that integrates rsETH for managing multiple restaking rewards without token lock-up.
Generated: DETERMINISTIC_1842effa6deb4a82
Batch ID: 20250612_151159
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RestakingRewardsManager
 * @author [Your Name]
 * @notice Manages multiple restaking rewards without token lock-up using rsETH.
 */
contract RestakingRewardsManager {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Mapping of reward tokens to their respective restaking rewards
    mapping(address => mapping(address => uint256)) public restakingRewards;

    // Mapping of reward tokens to their total restaked amounts
    mapping(address => uint256) public totalRestakedAmounts;

    // Mapping of user addresses to their restaking rewards
    mapping(address => mapping(address => uint256)) public userRestakingRewards;

    // Mapping of user addresses to their total restaked amounts
    mapping(address => uint256) public userTotalRestakedAmounts;

    // Event emitted when a new reward token is added
    event RewardTokenAdded(address indexed rewardToken);

    // Event emitted when a new restaking reward is added
    event RestakingRewardAdded(address indexed rewardToken, address indexed restakingToken, uint256 rewardAmount);

    // Event emitted when a user restakes a reward
    event UserRestaked(address indexed user, address indexed rewardToken, uint256 amount);

    // Event emitted when a user claims a restaking reward
    event RestakingRewardClaimed(address indexed user, address indexed rewardToken, uint256 amount);

    /**
     * @notice Adds a new reward token to the contract.
     * @param _rewardToken The address of the reward token to add.
     */
    function addRewardToken(address _rewardToken) public {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        emit RewardTokenAdded(_rewardToken);
    }

    /**
     * @notice Adds a new restaking reward for a reward token.
     * @param _rewardToken The address of the reward token.
     * @param _restakingToken The address of the restaking token.
     * @param _rewardAmount The amount of the restaking reward.
     */
    function addRestakingReward(address _rewardToken, address _restakingToken, uint256 _rewardAmount) public {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_restakingToken != address(0), "Restaking token address cannot be zero");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        restakingRewards[_rewardToken][_restakingToken] = _rewardAmount;
        totalRestakedAmounts[_rewardToken] = totalRestakedAmounts[_rewardToken].add(_rewardAmount);
        emit RestakingRewardAdded(_rewardToken, _restakingToken, _rewardAmount);
    }

    /**
     * @notice Restakes a reward for a user.
     * @param _user The address of the user.
     * @param _rewardToken The address of the reward token.
     * @param _amount The amount of the reward to restake.
     */
    function restake(address _user, address _rewardToken, uint256 _amount) public {
        require(_user != address(0), "User address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_amount > 0, "Restaking amount must be greater than zero");

        IERC20(_rewardToken).safeTransferFrom(msg.sender, address(this), _amount);
        userTotalRestakedAmounts[_user] = userTotalRestakedAmounts[_user].add(_amount);
        userRestakingRewards[_user][_rewardToken] = userRestakingRewards[_user][_rewardToken].add(_amount);
        emit UserRestaked(_user, _rewardToken, _amount);
    }

    /**
     * @notice Claims a restaking reward for a user.
     * @param _user The address of the user.
     * @param _rewardToken The address of the reward token.
     */
    function claimRestakingReward(address _user, address _rewardToken) public {
        require(_user != address(0), "User address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");

        uint256 rewardAmount = userRestakingRewards[_user][_rewardToken];
        require(rewardAmount > 0, "User has no restaking rewards to claim");

        userRestakingRewards[_user][_rewardToken] = 0;
        IERC20(_rewardToken).safeTransfer(_user, rewardAmount);
        emit RestakingRewardClaimed(_user, _rewardToken, rewardAmount);
    }

    /**
     * @notice Updates the restaking reward for a reward token and restaking token.
     * @param _rewardToken The address of the reward token.
     * @param _restakingToken The address of the restaking token.
     * @param _newRewardAmount The new amount of the restaking reward.
     */
    function updateRestakingReward(address _rewardToken, address _restakingToken, uint256 _newRewardAmount) public {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_restakingToken != address(0), "Restaking token address cannot be zero");
        require(_newRewardAmount >= 0, "New reward amount must be greater than or equal to zero");

        uint256 oldRewardAmount = restakingRewards[_rewardToken][_restakingToken];
        restakingRewards[_rewardToken][_restakingToken] = _newRewardAmount;
        totalRestakedAmounts[_rewardToken] = totalRestakedAmounts[_rewardToken].sub(oldRewardAmount).add(_newRewardAmount);
    }

    /**
     * @notice Withdraws a reward token from the contract.
     * @param _rewardToken The address of the reward token to withdraw.
     * @param _amount The amount of the reward token to withdraw.
     */
    function withdrawRewardToken(address _rewardToken, uint256 _amount) public {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_amount > 0, "Withdrawal amount must be greater than zero");

        IERC20(_rewardToken).safeTransfer(msg.sender, _amount);
    }
}
```
