"""
Generated Code Metadata:
========================
Original URL: https://hjiihhhgg.pages.dev
Prompt: Explain how to implement a staking mechanism for tokens in a decentralized Dapp environment.
Generated: DETERMINISTIC_63c969408dd4f483
Batch ID: 20250612_163400
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
 * @dev A simple staking mechanism for ERC20 tokens in a decentralized application.
 */
contract TokenStaking {
    // ERC20 token interface
    IERC20 public stakingToken;

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Mapping to track the timestamp of when a user last staked
    mapping(address => uint256) public stakingTimestamps;

    // Reward rate per second (e.g., 1 token per second)
    uint256 public rewardRate;

    // Mapping to track rewards earned by users
    mapping(address => uint256) public rewards;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the ERC20 token to be staked.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");

        // Update rewards before modifying staked balance
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staked balance and timestamp
        stakedBalances[msg.sender] += _amount;
        stakingTimestamps[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw 0 tokens");
        require(
            stakedBalances[msg.sender] >= _amount,
            "Insufficient staked balance"
        );

        // Update rewards before modifying staked balance
        _updateRewards(msg.sender);

        // Update staked balance
        stakedBalances[msg.sender] -= _amount;

        // Transfer tokens back to the user
        require(
            stakingToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim earned rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset rewards balance
        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(
            stakingToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        uint256 stakedAmount = stakedBalances[_user];
        if (stakedAmount > 0) {
            uint256 timeStaked = block.timestamp - stakingTimestamps[_user];
            uint256 newRewards = timeStaked * rewardRate * stakedAmount;
            rewards[_user] += newRewards;
        }
        stakingTimestamps[_user] = block.timestamp;
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        uint256 stakedAmount = stakedBalances[_user];
        if (stakedAmount == 0) {
            return rewards[_user];
        }
        uint256 timeStaked = block.timestamp - stakingTimestamps[_user];
        uint256 newRewards = timeStaked * rewardRate * stakedAmount;
        return rewards[_user] + newRewards;
    }
}

/**
 * @dev Minimal ERC20 interface for interacting with the staking token.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
