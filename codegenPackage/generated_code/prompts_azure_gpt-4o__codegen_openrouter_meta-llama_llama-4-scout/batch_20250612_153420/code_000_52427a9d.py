"""
Generated Code Metadata:
========================
Original URL: https://hehe-verse.pages.dev
Prompt: Write a smart contract in Solidity for staking $HEHE tokens that distributes rewards based on a 0.05% fee from each trade within the HEHE ecosystem.
Generated: DETERMINISTIC_52427a9da49fe60d
Batch ID: 20250612_153420
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title HEHE Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $HEHE tokens and earn rewards based on a 0.05% fee from each trade within the HEHE ecosystem.
 */
contract HEHEStaking is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward balances
    mapping(address => uint256) public rewardBalances;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Total reward balance
    uint256 public totalRewardBalance;

    // HEHE token contract
    IERC20 public heheToken;

    // Reward fee percentage (0.05%)
    uint256 public constant REWARD_FEE_PERCENTAGE = 50;

    /**
     * @param _heheTokenAddress Address of the $HEHE token contract
     */
    constructor(address _heheTokenAddress) public {
        require(_heheTokenAddress != address(0), "HEHE token address cannot be zero");
        heheToken = IERC20(_heheTokenAddress);
    }

    /**
     * @notice Stake $HEHE tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Staking amount must be greater than zero");
        require(heheToken.balanceOf(msg.sender) >= _amount, "Insufficient HEHE token balance");

        // Transfer tokens from user to contract
        heheToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStakingBalance = totalStakingBalance.add(_amount);
    }

    /**
     * @notice Unstake $HEHE tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Unstaking amount must be greater than zero");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStakingBalance = totalStakingBalance.sub(_amount);

        // Transfer tokens from contract to user
        heheToken.safeTransfer(msg.sender, _amount);
    }

    /**
     * @notice Distribute rewards to stakers
     * @param _tradeAmount Amount of tokens traded
     */
    function distributeRewards(uint256 _tradeAmount) public {
        // Calculate reward amount (0.05% of trade amount)
        uint256 rewardAmount = _tradeAmount.mul(REWARD_FEE_PERCENTAGE).div(10000);

        // Update total reward balance
        totalRewardBalance = totalRewardBalance.add(rewardAmount);

        // Distribute rewards to stakers proportionally
        uint256 stakerReward;
        for (address staker in stakingBalances) {
            stakerReward = rewardAmount.mul(stakingBalances[staker]).div(totalStakingBalance);
            rewardBalances[staker] = rewardBalances[staker].add(stakerReward);
        }
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public {
        require(rewardBalances[msg.sender] > 0, "No rewards to claim");

        // Transfer rewards to user
        heheToken.safeTransfer(msg.sender, rewardBalances[msg.sender]);

        // Reset reward balance
        rewardBalances[msg.sender] = 0;
    }

    /**
     * @notice Update reward fee percentage
     * @param _newRewardFeePercentage New reward fee percentage
     */
    function updateRewardFeePercentage(uint256 _newRewardFeePercentage) public onlyOwner {
        REWARD_FEE_PERCENTAGE = _newRewardFeePercentage;
    }
}
```
