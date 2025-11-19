"""
Generated Code Metadata:
========================
Original URL: https://daddysunversity.com
Prompt: Create a Solidity smart contract that allows users to stake $DADDY tokens and earn rewards based on their holdings.
Generated: DETERMINISTIC_a1637c71fada9b6f
Batch ID: 20250612_163338
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

/**
 * @title DaddyTokenStaking
 * @dev A contract that allows users to stake $DADDY tokens and earn rewards.
 */
contract DaddyTokenStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // The staking token (DADDY)
    IERC20 public immutable stakingToken;

    // Reward rate (reward tokens per second per staked token)
    uint256 public rewardRate;

    // Duration of the reward period (seconds)
    uint256 public rewardDuration;

    // Timestamp when rewards finish
    uint256 public finishAt;

    // Last time reward was updated
    uint256 public updatedAt;

    // Reward per token stored
    uint256 public rewardPerTokenStored;

    // User rewards per token paid
    mapping(address => uint256) public userRewardPerTokenPaid;

    // User rewards
    mapping(address => uint256) public rewards;

    // Total staked amount
    uint256 public totalStaked;

    // User staked balances
    mapping(address => uint256) public balances;

    /**
     * @dev Constructor.
     * @param _stakingToken Address of the staking token (DADDY)
     */
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @dev Modifier to update reward for a user.
     * @param _account The address of the user to update rewards for.
     */
    modifier updateReward(address _account) {
        rewardPerTokenStored = rewardPerToken();
        updatedAt = lastTimeRewardApplicable();

        if (_account != address(0)) {
            rewards[_account] = earned(_account);
            userRewardPerTokenPaid[_account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Returns the last time reward is applicable.
     * @return The last applicable timestamp.
     */
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp < finishAt ? block.timestamp : finishAt;
    }

    /**
     * @dev Calculates the reward per token.
     * @return The reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }

        return
            rewardPerTokenStored +
            (rewardRate * (lastTimeRewardApplicable() - updatedAt) * 1e18) /
            totalStaked;
    }

    /**
     * @dev Calculates the earned rewards for a user.
     * @param _account The address of the user.
     * @return The amount of rewards earned.
     */
    function earned(address _account) public view returns (uint256) {
        return
            (balances[_account] *
                (rewardPerToken() - userRewardPerTokenPaid[_account])) /
            1e18 +
            rewards[_account];
    }

    /**
     * @dev Stakes tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant updateReward(msg.sender) {
        require(_amount > 0, "Amount must be greater than 0");
        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        balances[msg.sender] += _amount;
        totalStaked += _amount;
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraws staked tokens.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external nonReentrant updateReward(msg.sender) {
        require(_amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] -= _amount;
        totalStaked -= _amount;
        stakingToken.safeTransfer(msg.sender, _amount);
        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claims earned rewards.
     */
    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        stakingToken.safeTransfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Sets the reward parameters.
     * @param _rewardRate The reward rate (tokens per second).
     * @param _duration The duration of the reward period (seconds).
     */
    function setRewards(uint256 _rewardRate, uint256 _duration) external onlyOwner {
        require(_duration > 0, "Duration must be greater than 0");
        finishAt = block.timestamp + _duration;
        updatedAt = block.timestamp;
        rewardRate = _rewardRate;
        rewardDuration = _duration;
        emit RewardAdded(_rewardRate, _duration);
    }

    /**
     * @dev Emergency withdraws all staked tokens without claiming rewards.
     */
    function emergencyWithdraw() external nonReentrant {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No tokens to withdraw");
        balances[msg.sender] = 0;
        totalStaked -= amount;
        stakingToken.safeTransfer(msg.sender, amount);
        emit EmergencyWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Recovers any ERC20 tokens sent to the contract by mistake.
     * @param _tokenAddress The address of the token to recover.
     * @param _amount The amount of tokens to recover.
     */
    function recoverERC20(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(_tokenAddress).safeTransfer(owner(), _amount);
        emit Recovered(_tokenAddress, _amount);
    }

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardAdded(uint256 rewardRate, uint256 duration);
    event EmergencyWithdrawn(address indexed user, uint256 amount);
    event Recovered(address token, uint256 amount);
}
```
