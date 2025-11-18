"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://high-sugar-sparse.on-fleek.app
Prompt: Create a smart contract for staking GamerCoin ($GHX) on the BNB Chain. Ensure the contract includes features for calculating rewards based on the staking duration and amount.
Generated: DETERMINISTIC_1327898881c07877
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, production-ready smart contract written in Solidity for staking GamerCoin ($GHX) on the BNB Chain. It includes features for calculating rewards based on staking duration and amount.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title GamerCoin Staking Contract
 * @dev This contract allows users to stake $GHX tokens and earn rewards based on staking duration and amount.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract GamerCoinStaking {
    // Token being staked
    IERC20 public ghxToken;

    // Reward rate (e.g., 5% annualized, expressed as 0.05)
    uint256 public rewardRate;

    // Time unit for rewards calculation (in seconds, e.g., 1 year = 365 * 24 * 60 * 60)
    uint256 public constant REWARD_TIME_UNIT = 365 days;

    // Struct to hold staking data
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardsClaimed;
    }

    // Mapping of user address to their staking information
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with token and reward rate.
     * @param _ghxToken Address of the $GHX token contract.
     * @param _rewardRate Annual reward rate as a decimal (e.g., 0.05 for 5%).
     */
    constructor(IERC20 _ghxToken, uint256 _rewardRate) {
        require(address(_ghxToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        ghxToken = _ghxToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $GHX tokens in the contract.
     * @param _amount Amount of $GHX tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");

        // Transfer tokens from user to contract
        require(ghxToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            // Claim any pending rewards before restaking
            claimRewards();
        }
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards amount.
     */
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        uint256 rewards = (userStake.amount * rewardRate * stakingDuration) / REWARD_TIME_UNIT;

        return rewards - userStake.rewardsClaimed;
    }

    /**
     * @dev Claim pending rewards for the sender.
     */
    function claimRewards() public {
        Stake storage userStake = stakes[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update claimed rewards
        userStake.rewardsClaimed += rewards;

        // Transfer rewards to user
        require(ghxToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Unstake $GHX tokens and claim any pending rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount");

        // Claim pending rewards
        claimRewards();

        // Transfer staked tokens back to the user
        uint256 unstakeAmount = userStake.amount;
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.rewardsClaimed = 0;

        require(ghxToken.transfer(msg.sender, unstakeAmount), "Unstake transfer failed");

        emit Unstaked(msg.sender, unstakeAmount);
    }

    /**
     * @dev View staked amount for a user.
     * @param _user Address of the user.
     * @return Staked amount.
     */
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }
}
```
