"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ai-presale.pages.dev
Prompt: Write a smart contract in Solidity that implements a staking mechanism similar to WienerAI, where users can stake tokens and earn rewards based on an annual percentage yield (APY). Include a function to calculate rewards dynamically.
Generated: DETERMINISTIC_f5dd856820be1bfc
Batch ID: 20250612_151232
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
 * @dev Implements a staking mechanism where users can stake tokens and earn rewards based on an annual percentage yield (APY).
 */
contract StakingContract {
    // ERC20 token interface
    IERC20 public stakingToken;

    // APY in percentage (e.g., 10 for 10%)
    uint256 public annualPercentageYield;

    // Precision factor for calculating rewards
    uint256 private constant REWARD_PRECISION = 1e18;

    // Struct to store staking information of a user
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping to track staker information
    mapping(address => Staker) public stakers;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the token to be staked.
     * @param _apy Annual percentage yield (e.g., 10 for 10% APY).
     */
    constructor(address _stakingToken, uint256 _apy) {
        require(_stakingToken != address(0), "Invalid token address");
        require(_apy > 0, "APY must be greater than zero");

        stakingToken = IERC20(_stakingToken);
        annualPercentageYield = _apy;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker's data
        Staker storage staker = stakers[msg.sender];

        // Calculate any pending rewards before updating staked amount
        uint256 pendingRewards = calculateRewards(msg.sender);
        staker.rewardDebt += pendingRewards;

        staker.stakedAmount += _amount;
        staker.lastStakedTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Unstaking amount must be greater than zero");
        require(staker.stakedAmount >= _amount, "Insufficient staked balance");

        // Calculate pending rewards before unstaking
        uint256 pendingRewards = calculateRewards(msg.sender);
        staker.rewardDebt += pendingRewards;

        staker.stakedAmount -= _amount;
        if (staker.stakedAmount == 0) {
            staker.lastStakedTime = 0; // Reset staking time if no tokens remain staked
        }

        totalStaked -= _amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards earned from staking.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];

        // Calculate pending rewards
        uint256 pendingRewards = calculateRewards(msg.sender);
        uint256 totalRewards = staker.rewardDebt + pendingRewards;

        require(totalRewards > 0, "No rewards available");

        // Reset reward debt
        staker.rewardDebt = 0;
        staker.lastStakedTime = block.timestamp;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, totalRewards);

        emit RewardClaimed(msg.sender, totalRewards);
    }

    /**
     * @dev Calculate rewards dynamically based on the staking amount and time elapsed.
     * @param _staker Address of the staker.
     * @return Rewards earned by the staker.
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];

        if (staker.stakedAmount == 0 || staker.lastStakedTime == 0) {
            return 0;
        }

        // Calculate time elapsed since last staking
        uint256 timeElapsed = block.timestamp - staker.lastStakedTime;

        // Annual reward rate (APY) applied
        uint256 annualRewards = (staker.stakedAmount * annualPercentageYield) / 100;

        // Calculate proportional rewards based on time elapsed (seconds in a year = 365 * 24 * 60 * 60)
        uint256 rewards = (annualRewards * timeElapsed * REWARD_PRECISION) / (365 * 24 * 60 * 60 * REWARD_PRECISION);

        return rewards;
    }

    /**
     * @dev Utility function to retrieve the total rewards available for a user.
     * @param _staker Address of the staker.
     * @return Total rewards including pending rewards and reward debt.
     */
    function totalRewards(address _staker) external view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 pendingRewards = calculateRewards(_staker);
        return staker.rewardDebt + pendingRewards;
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
