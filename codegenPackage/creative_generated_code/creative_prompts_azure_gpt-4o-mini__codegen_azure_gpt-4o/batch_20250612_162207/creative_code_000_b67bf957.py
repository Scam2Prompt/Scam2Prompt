"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20-io.pages.dev
Prompt: How can I implement a staking mechanism for an ERC-20 token like DOGE20 to distribute rewards over a two-year period?
Generated: DETERMINISTIC_b67bf957b2aeca4b
Batch ID: 20250612_162207
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
 * @dev A simple staking mechanism for an ERC-20 token to distribute rewards over a two-year period.
 */
contract StakingContract {
    // Address of the ERC-20 token used for staking
    IERC20 public stakingToken;

    // Duration of staking rewards (2 years in seconds)
    uint256 public constant REWARD_DURATION = 2 * 365 * 24 * 60 * 60;

    // Timestamp when staking starts
    uint256 public stakingStartTime;

    // Total rewards distributed over the staking period
    uint256 public totalRewards;

    // Total staked tokens
    uint256 public totalStaked;

    // User-specific staking information
    struct StakerInfo {
        uint256 amountStaked; // Amount of tokens staked by the user
        uint256 rewardDebt;   // Rewards already claimed
    }

    // Mapping from user address to staking information
    mapping(address => StakerInfo) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _stakingToken Address of the ERC-20 token used for staking.
     * @param _totalRewards Total rewards to be distributed over 2 years.
     */
    constructor(IERC20 _stakingToken, uint256 _totalRewards) {
        stakingToken = _stakingToken;
        totalRewards = _totalRewards;
        stakingStartTime = block.timestamp;
    }

    /**
     * @dev Modifier to ensure the staking period is active.
     */
    modifier stakingActive() {
        require(block.timestamp <= stakingStartTime + REWARD_DURATION, "Staking period has ended");
        _;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external stakingActive {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user staking info and total staked
        StakerInfo storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        staker.rewardDebt += _calculatePendingRewards(msg.sender);
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and optionally claim rewards.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked balance");

        // Claim rewards before unstaking
        claimRewards();

        // Update staking info
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim pending rewards for the user.
     */
    function claimRewards() public {
        uint256 rewards = _calculatePendingRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        StakerInfo storage staker = stakers[msg.sender];
        staker.rewardDebt += rewards;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards.
     */
    function _calculatePendingRewards(address _user) internal view returns (uint256) {
        StakerInfo storage staker = stakers[_user];
        if (staker.amountStaked == 0) {
            return 0;
        }

        // Calculate rewards based on the proportion of staked tokens and elapsed time
        uint256 elapsedTime = block.timestamp - stakingStartTime;
        uint256 stakingPeriod = stakingStartTime + REWARD_DURATION;
        uint256 timeFactor = elapsedTime > stakingPeriod ? stakingPeriod : elapsedTime;

        uint256 userShare = (staker.amountStaked * timeFactor * totalRewards) / totalStaked / REWARD_DURATION;

        return userShare - staker.rewardDebt;
    }

    /**
     * @dev Emergency withdraw function for the owner to recover tokens after staking ends.
     */
    function emergencyWithdraw() external {
        require(block.timestamp > stakingStartTime + REWARD_DURATION, "Staking period is still active");
        stakingToken.transfer(msg.sender, stakingToken.balanceOf(address(this)));
    }
}

// Interface for ERC-20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
