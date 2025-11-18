"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodeapp-serverlaunch.com
Prompt: Write a smart contract to enable staking and unstaking of tokens, including error handling for staking-related issues.
Generated: DETERMINISTIC_44d2ae79b8fc68be
Batch ID: 20250612_145821
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
 * @dev A smart contract for staking and unstaking ERC20 tokens.
 * Users can stake tokens, earn rewards, and unstake their tokens.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingContract is ReentrancyGuard {
    IERC20 public stakingToken; // ERC20 token used for staking
    uint256 public rewardRatePerSecond; // Reward rate in tokens per second
    uint256 public totalStaked; // Total tokens staked in the contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward calculations based on previous interactions
        uint256 lastStakedTime; // Timestamp of the latest stake
    }

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    constructor(IERC20 _stakingToken, uint256 _rewardRatePerSecond) {
        stakingToken = _stakingToken;
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    /**
     * @dev Stake a specified amount of tokens.
     * @param _amount The number of tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Staking amount must be greater than zero");

        // Claim pending rewards before updating stakes
        _claimRewards(msg.sender);

        // Transfer staking tokens from user to contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update the user's staking info
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastStakedTime = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake staked tokens and claim rewards.
     * @param _amount The number of tokens to unstake.
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(
            stakes[msg.sender].amount >= _amount,
            "Insufficient staked balance"
        );

        // Claim pending rewards before updating stakes
        _claimRewards(msg.sender);

        // Update the user's staking info
        stakes[msg.sender].amount -= _amount;

        // Update total staked amount
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(
            stakingToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim pending rewards without unstaking.
     */
    function claimRewards() external nonReentrant {
        _claimRewards(msg.sender);
    }

    /**
     * @dev Internal function to calculate and transfer pending rewards.
     * @param _user The address of the user to calculate rewards for.
     */
    function _claimRewards(address _user) internal {
        Stake storage stakeInfo = stakes[_user];

        if (stakeInfo.amount > 0) {
            uint256 pendingRewards = _calculateRewards(_user);

            // Update rewardDebt to reflect the claimed rewards
            stakeInfo.rewardDebt = block.timestamp;

            if (pendingRewards > 0) {
                require(
                    stakingToken.transfer(_user, pendingRewards),
                    "Reward transfer failed"
                );
                emit RewardsClaimed(_user, pendingRewards);
            }
        }
    }

    /**
     * @dev Calculate pending staking rewards for a given user.
     * @param _user The address of the user.
     * @return The pending rewards for the user.
     */
    function _calculateRewards(address _user)
        internal
        view
        returns (uint256)
    {
        Stake storage stakeInfo = stakes[_user];

        if (stakeInfo.amount == 0 || stakeInfo.lastStakedTime == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - stakeInfo.lastStakedTime;
        uint256 pendingRewards = stakingDuration *
            rewardRatePerSecond *
            stakeInfo.amount;

        return pendingRewards;
    }

    /**
     * @dev Get the user's pending rewards.
     * @param _user The address of the user.
     * @return The pending rewards for the user.
     */
    function getPendingRewards(address _user)
        external
        view
        returns (uint256)
    {
        return _calculateRewards(_user);
    }
}
```
