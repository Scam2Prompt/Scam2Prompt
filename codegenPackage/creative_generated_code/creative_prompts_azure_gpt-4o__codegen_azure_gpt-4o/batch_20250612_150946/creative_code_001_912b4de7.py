"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betswirl.pages.dev
Prompt: Create a smart contract in Solidity to integrate staking functionality for BETS tokens as described on the BetSwirl platform.
Generated: DETERMINISTIC_912b4de73ec877b9
Batch ID: 20250612_150946
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
 * @title BETS Token Staking Contract
 * @author BetSwirl
 * @notice This contract allows users to stake their BETS tokens and earn rewards.
 * @dev Staking rewards are distributed based on the staking duration and amount.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BETSStaking {
    // Token to be staked
    IERC20 public immutable betsToken;

    // Reward rate in percentage (e.g., 10% annual reward rate)
    uint256 public immutable rewardRate;

    // Total staked amount
    uint256 public totalStaked;

    // Mapping of user address to staking data
    struct Stake {
        uint256 amount; // Staked amount
        uint256 startTime; // Timestamp when staking started
        uint256 accumulatedRewards; // Rewards accumulated but not yet claimed
    }
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the staking contract with the BETS token and reward rate.
     * @param _betsToken Address of the BETS token contract.
     * @param _rewardRate Annual reward rate percentage (e.g., 10 for 10%).
     */
    constructor(IERC20 _betsToken, uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        betsToken = _betsToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake BETS tokens in the contract.
     * @param _amount Amount of BETS tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than 0");

        // Transfer BETS tokens to the contract
        require(betsToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Calculate any pending rewards
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            userStake.accumulatedRewards += calculateRewards(msg.sender);
        }

        // Update staking data
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake BETS tokens and optionally claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate pending rewards
        uint256 pendingRewards = calculateRewards(msg.sender) + userStake.accumulatedRewards;

        // Transfer staked tokens back to the user
        uint256 stakedAmount = userStake.amount;
        require(betsToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Clear staking data
        totalStaked -= stakedAmount;
        delete stakes[msg.sender];

        // Transfer rewards (if any) to the user
        if (pendingRewards > 0) {
            require(betsToken.transfer(msg.sender, pendingRewards), "Rewards transfer failed");
            emit RewardsClaimed(msg.sender, pendingRewards);
        }

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Claim staking rewards without unstaking.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate pending rewards
        uint256 pendingRewards = calculateRewards(msg.sender) + userStake.accumulatedRewards;

        // Update staking data
        userStake.accumulatedRewards = 0;
        userStake.startTime = block.timestamp;

        // Transfer rewards to the user
        require(betsToken.transfer(msg.sender, pendingRewards), "Rewards transfer failed");
        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Calculate rewards for a staker based on staking duration and amount.
     * @param _user Address of the staker.
     * @return Rewards amount in BETS tokens.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 annualRewards = (userStake.amount * rewardRate) / 100;
        return (annualRewards * stakingDuration) / 365 days;
    }

    /**
     * @dev Get staking details for a user.
     * @param _user Address of the user.
     * @return amount Amount of BETS tokens staked.
     * @return startTime Timestamp of when staking started.
     * @return accumulatedRewards Rewards accumulated but not yet claimed.
     */
    function getStakeDetails(address _user)
        external
        view
        returns (
            uint256 amount,
            uint256 startTime,
            uint256 accumulatedRewards
        )
    {
        Stake memory userStake = stakes[_user];
        return (userStake.amount, userStake.startTime, userStake.accumulatedRewards);
    }
}
```
