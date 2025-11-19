"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-io.web.app
Prompt: How can I implement a staking smart contract for DOGE20 on Ethereum to distribute rewards over two years?
Generated: DETERMINISTIC_a06ab84aeead537c
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingContract
 * @dev A smart contract to allow DOGE20 token staking and reward distribution
 *      over a two-year period.
 */
contract StakingContract {
    // Address of the DOGE20 token contract
    IERC20 public dogeToken;

    // Duration of staking rewards in seconds (2 years = 730 days)
    uint256 public constant REWARD_DURATION = 730 days;

    // Reward distribution start and end timestamps
    uint256 public rewardStartTimestamp;
    uint256 public rewardEndTimestamp;

    // Total rewards allocated for distribution
    uint256 public totalRewardPool;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping of user balances and reward tracking
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public lastClaimedTimestamp;
    mapping(address => uint256) public unclaimedRewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the staking contract.
     * @param _dogeToken Address of the DOGE20 token contract.
     * @param _totalRewardPool Total rewards allocated for distribution.
     */
    constructor(address _dogeToken, uint256 _totalRewardPool) {
        require(_dogeToken != address(0), "Invalid token address");
        require(_totalRewardPool > 0, "Reward pool must be greater than zero");

        dogeToken = IERC20(_dogeToken);
        totalRewardPool = _totalRewardPool;

        rewardStartTimestamp = block.timestamp;
        rewardEndTimestamp = block.timestamp + REWARD_DURATION;
    }

    /**
     * @dev Allows users to stake DOGE20 tokens.
     * @param _amount Amount of DOGE20 tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(block.timestamp < rewardEndTimestamp, "Staking period has ended");

        // Update unclaimed rewards before changing the staked amount
        _updateRewards(msg.sender);

        // Transfer DOGE20 tokens from the user to the contract
        require(dogeToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their DOGE20 tokens.
     * @param _amount Amount of DOGE20 tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update unclaimed rewards before changing the staked amount
        _updateRewards(msg.sender);

        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer DOGE20 tokens back to the user
        require(dogeToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 rewardToClaim = unclaimedRewards[msg.sender];
        require(rewardToClaim > 0, "No rewards to claim");

        unclaimedRewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(dogeToken.transfer(msg.sender, rewardToClaim), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardToClaim);
    }

    /**
     * @dev Internal function to update staking rewards for a user.
     * @param _user Address of the user to update rewards for.
     */
    function _updateRewards(address _user) internal {
        uint256 lastTimestamp = lastClaimedTimestamp[_user];
        uint256 stakedAmount = stakedBalances[_user];

        if (stakedAmount > 0 && block.timestamp > rewardStartTimestamp) {
            uint256 startTime = lastTimestamp > rewardStartTimestamp ? lastTimestamp : rewardStartTimestamp;
            uint256 endTime = block.timestamp > rewardEndTimestamp ? rewardEndTimestamp : block.timestamp;

            if (startTime < endTime) {
                uint256 rewardPeriod = endTime - startTime;
                uint256 reward = (stakedAmount * totalRewardPool * rewardPeriod) / (totalStaked * REWARD_DURATION);

                unclaimedRewards[_user] += reward;
            }
        }

        lastClaimedTimestamp[_user] = block.timestamp;
    }

    /**
     * @dev Returns the pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards amount.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        uint256 lastTimestamp = lastClaimedTimestamp[_user];
        uint256 stakedAmount = stakedBalances[_user];

        if (stakedAmount > 0 && block.timestamp > rewardStartTimestamp) {
            uint256 startTime = lastTimestamp > rewardStartTimestamp ? lastTimestamp : rewardStartTimestamp;
            uint256 endTime = block.timestamp > rewardEndTimestamp ? rewardEndTimestamp : block.timestamp;

            if (startTime < endTime) {
                uint256 rewardPeriod = endTime - startTime;
                uint256 pendingReward = (stakedAmount * totalRewardPool * rewardPeriod) / (totalStaked * REWARD_DURATION);

                return unclaimedRewards[_user] + pendingReward;
            }
        }

        return unclaimedRewards[_user];
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
