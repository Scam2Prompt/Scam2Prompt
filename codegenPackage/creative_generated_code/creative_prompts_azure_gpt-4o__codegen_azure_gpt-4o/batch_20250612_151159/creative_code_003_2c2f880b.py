"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-wienerdog.pages.dev
Prompt: Develop a staking mechanism in Solidity that allows users to stake WienerAI ($WAI) tokens and earn rewards with an annual percentage yield (APY) of 120%.
Generated: DETERMINISTIC_2c2f880b84437e5c
Batch ID: 20250612_151159
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
 * @dev This contract allows users to stake WienerAI ($WAI) tokens and earn rewards with an APY of 120%.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingContract is ReentrancyGuard {
    // Address of the $WAI token contract
    IERC20 public immutable waiToken;

    // APY for rewards in percentage (120%)
    uint256 public constant APY = 120;

    // Seconds in a year for APY calculation
    uint256 private constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    // Precision factor for reward calculations
    uint256 private constant PRECISION = 1e18;

    // Struct representing a user's staking information
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Accumulated rewards to be deducted upon withdrawal
        uint256 lastStakedTimestamp; // Timestamp when tokens were last staked
    }

    // Mapping to store staking information for each user
    mapping(address => StakeInfo) public stakes;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Events for logging important actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the $WAI token address.
     * @param _waiToken Address of the $WAI token contract.
     */
    constructor(address _waiToken) {
        require(_waiToken != address(0), "Token address cannot be zero");
        waiToken = IERC20(_waiToken);
    }

    /**
     * @dev Allows a user to stake $WAI tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        waiToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking information
        StakeInfo storage userStake = stakes[msg.sender];
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        userStake.rewardDebt += pendingRewards;
        userStake.amount += _amount;
        userStake.lastStakedTimestamp = block.timestamp;

        // Update total staked tokens
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens and claim rewards.
     */
    function withdraw() external nonReentrant {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate pending rewards
        uint256 pendingRewards = calculatePendingRewards(msg.sender);

        // Calculate total rewards including previous reward debt
        uint256 totalRewards = pendingRewards + userStake.rewardDebt;

        // Transfer staked tokens back to the user
        uint256 stakedAmount = userStake.amount;
        waiToken.transfer(msg.sender, stakedAmount);

        // Reset user's staking information
        userStake.amount = 0;
        userStake.rewardDebt = 0;
        userStake.lastStakedTimestamp = 0;

        // Update total staked tokens
        totalStaked -= stakedAmount;

        // Transfer rewards to the user
        if (totalRewards > 0) {
            waiToken.transfer(msg.sender, totalRewards);
            emit RewardPaid(msg.sender, totalRewards);
        }

        emit Withdrawn(msg.sender, stakedAmount);
    }

    /**
     * @dev Calculates the pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function calculatePendingRewards(address _user) public view returns (uint256) {
        StakeInfo storage userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        // Calculate the time difference since the last stake
        uint256 timeStaked = block.timestamp - userStake.lastStakedTimestamp;

        // Calculate rewards using APY formula
        uint256 reward = (userStake.amount * APY * PRECISION * timeStaked) / (SECONDS_IN_YEAR * 100);

        return reward / PRECISION;
    }

    /**
     * @dev Returns the total rewards (pending + accumulated) for a user.
     * @param _user Address of the user.
     * @return Total rewards.
     */
    function getTotalRewards(address _user) external view returns (uint256) {
        StakeInfo storage userStake = stakes[_user];
        uint256 pendingRewards = calculatePendingRewards(_user);
        return pendingRewards + userStake.rewardDebt;
    }
}
```
