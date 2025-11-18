"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinguonbase-claims.pages.dev
Prompt: Create a staking system called "Iceberg Growing" where token holders can stake their tokens and earn rewards over time, inspired by the Pingu token's staking mechanism.
Generated: DETERMINISTIC_80984c414742fdaa
Batch ID: 20250612_150604
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title IcebergGrowing Staking Contract
 * @dev Allows token holders to stake their tokens and earn rewards over time.
 */
contract IcebergGrowing {
    using SafeMath for uint256;

    // Token interface
    IERC20 public token;

    // Staker information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping of staker addresses to their data
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per second (adjust as needed, e.g., 1 token per second)
    uint256 public rewardRate = 1e18; // 1 token reward per second per staked token

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ClaimedRewards(address indexed user, uint256 reward);

    /**
     * @param _token Address of the ERC20 token to be staked.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "You must stake a positive amount");
        require(token.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];
        
        // Update staker's information
        staker.rewardDebt = calculateRewards(msg.sender).add(staker.rewardDebt);
        staker.amountStaked = staker.amountStaked.add(_amount);
        staker.lastStakedTime = block.timestamp;

        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake previously staked tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "You must unstake a positive amount");
        require(staker.amountStaked >= _amount, "Insufficient staked balance");

        // Update rewards and staker's information
        staker.rewardDebt = calculateRewards(msg.sender).add(staker.rewardDebt);
        staker.amountStaked = staker.amountStaked.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens back to the staker
        require(token.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards earned from staking.
     */
    function claimRewards() external {
        uint256 reward = calculateRewards(msg.sender).add(stakers[msg.sender].rewardDebt);
        require(reward > 0, "No rewards to claim");

        // Reset reward debt to zero after claiming
        stakers[msg.sender].rewardDebt = 0;
        require(token.transfer(msg.sender, reward), "Transfer failed");

        emit ClaimedRewards(msg.sender, reward);
    }

    /**
     * @dev Calculate the total rewards of a staker based on their staked amount and time.
     * @param _staker Address of the staker.
     * @return Total rewards earned.
     */
    function calculateRewards(address _staker) internal view returns (uint256) {
        Staker memory staker = stakers[_staker];
        return staker.amountStaked.mul(rewardRate).mul(block.timestamp.sub(staker.lastStakedTime)).div(1e18);
    }

    /**
     * @dev Returns the staker's current balance of staked tokens.
     * @param _staker Address of the staker.
     * @return Amount of tokens staked.
     */
    function stakedBalance(address _staker) external view returns (uint256) {
        return stakers[_staker].amountStaked;
    }
}
```
