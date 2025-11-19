"""
Generated Code Metadata:
========================
Original URL: https://claimfloki.pages.dev
Prompt: Generate a smart contract code for a token staking program that rewards users with a sister token, similar to how FLOKI stakers earn TOKEN.
Generated: DETERMINISTIC_d1d72483ccb757b5
Batch ID: 20250622_204726
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

/**
 * @title TokenStaking
 * @dev A smart contract for staking tokens and earning rewards in a sister token.
 */
contract TokenStaking {
    // State variables
    address public stakingToken; // Address of the token to be staked
    address public rewardToken;  // Address of the reward token
    uint256 public rewardRate;   // Reward rate per second
    uint256 public totalStaked;  // Total amount of tokens staked

    struct Stake {
        uint256 amount;          // Amount of tokens staked
        uint256 rewardDebt;      // Rewards already paid out
        uint256 lastUpdated;     // Last time the stake was updated
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor
    constructor(address _stakingToken, address _rewardToken, uint256 _rewardRate) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to ensure the caller is not a zero address.
     */
    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        Stake storage userStake = stakes[msg.sender];
        _updateRewards(msg.sender);

        // Transfer staking tokens from the user to the contract
        require(
            IERC20(stakingToken).transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        userStake.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked balance");

        _updateRewards(msg.sender);

        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer staking tokens back to the user
        require(
            IERC20(stakingToken).transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 reward = userStake.rewardDebt;
        require(reward > 0, "No rewards available");

        userStake.rewardDebt = 0;

        // Transfer reward tokens to the user
        require(
            IERC20(rewardToken).transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;

        if (timeElapsed > 0 && userStake.amount > 0) {
            uint256 pendingReward = (userStake.amount * rewardRate * timeElapsed) / 1e18;
            userStake.rewardDebt += pendingReward;
        }

        userStake.lastUpdated = block.timestamp;
    }

    /**
     * @dev View function to check pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;

        if (timeElapsed > 0 && userStake.amount > 0) {
            uint256 pendingReward = (userStake.amount * rewardRate * timeElapsed) / 1e18;
            return userStake.rewardDebt + pendingReward;
        }

        return userStake.rewardDebt;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
