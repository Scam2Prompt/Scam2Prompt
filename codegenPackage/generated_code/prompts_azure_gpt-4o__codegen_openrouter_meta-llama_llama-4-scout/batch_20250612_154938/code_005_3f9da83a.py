"""
Generated Code Metadata:
========================
Original URL: https://riarus.ru
Prompt: Create a smart contract in Solidity that interacts with Perpetual Protocol's staking mechanism to automate staking and reward distribution for PERP token holders.
Generated: DETERMINISTIC_3f9da83a2804e99a
Batch ID: 20250612_154938
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
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title Perpetual Protocol Staking Contract
 * @author [Your Name]
 * @notice This contract automates staking and reward distribution for PERP token holders
 *         interacting with Perpetual Protocol's staking mechanism.
 */
contract PerpetualStaking {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward claims
    mapping(address => uint256) public rewardClaims;

    // PERP token contract
    IERC20 public perpToken;

    // Perpetual Protocol staking contract
    address public perpetualStakingContract;

    // Reward distribution interval in seconds
    uint256 public rewardDistributionInterval;

    // Timestamp of last reward distribution
    uint256 public lastRewardDistribution;

    // Total rewards available for distribution
    uint256 public totalRewards;

    /**
     * @notice Constructor
     * @param _perpToken PERP token contract address
     * @param _perpetualStakingContract Perpetual Protocol staking contract address
     * @param _rewardDistributionInterval Reward distribution interval in seconds
     */
    constructor(
        address _perpToken,
        address _perpetualStakingContract,
        uint256 _rewardDistributionInterval
    ) public {
        perpToken = IERC20(_perpToken);
        perpetualStakingContract = _perpetualStakingContract;
        rewardDistributionInterval = _rewardDistributionInterval;
        lastRewardDistribution = block.timestamp;
    }

    /**
     * @notice Stake PERP tokens
     * @param _amount Amount of PERP tokens to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Invalid stake amount");

        // Transfer PERP tokens to staking contract
        perpToken.safeTransferFrom(msg.sender, perpetualStakingContract, _amount);

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
    }

    /**
     * @notice Unstake PERP tokens
     * @param _amount Amount of PERP tokens to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);

        // Transfer PERP tokens from staking contract to user
        perpToken.safeTransfer(msg.sender, _amount);
    }

    /**
     * @notice Distribute rewards to stakers
     */
    function distributeRewards() public {
        // Check if reward distribution interval has passed
        require(block.timestamp.sub(lastRewardDistribution) >= rewardDistributionInterval, "Reward distribution interval has not passed");

        // Update last reward distribution timestamp
        lastRewardDistribution = block.timestamp;

        // Calculate total staking balance
        uint256 totalStakingBalance = 0;
        for (address user in stakingBalances) {
            totalStakingBalance = totalStakingBalance.add(stakingBalances[user]);
        }

        // Distribute rewards to stakers
        for (address user in stakingBalances) {
            uint256 userReward = totalRewards.mul(stakingBalances[user]).div(totalStakingBalance);
            rewardClaims[user] = rewardClaims[user].add(userReward);

            // Transfer rewards to user
            perpToken.safeTransfer(user, userReward);
        }

        // Reset total rewards
        totalRewards = 0;
    }

    /**
     * @notice Add rewards to be distributed
     * @param _amount Amount of rewards to add
     */
    function addRewards(uint256 _amount) public {
        // Transfer rewards to contract
        perpToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update total rewards
        totalRewards = totalRewards.add(_amount);
    }

    /**
     * @notice Get user's staking balance
     * @param _user User address
     * @return User's staking balance
     */
    function getStakingBalance(address _user) public view returns (uint256) {
        return stakingBalances[_user];
    }

    /**
     * @notice Get user's reward claim
     * @param _user User address
     * @return User's reward claim
     */
    function getRewardClaim(address _user) public view returns (uint256) {
        return rewardClaims[_user];
    }
}
```
