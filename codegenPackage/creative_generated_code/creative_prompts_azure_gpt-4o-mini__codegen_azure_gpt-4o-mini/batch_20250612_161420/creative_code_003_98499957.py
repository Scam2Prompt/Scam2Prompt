"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pablo-defi.web.app
Prompt: Develop a smart contract for staking $PABLO tokens that aligns with the revenue-sharing model detailed in the Pablo ecosystem.
Generated: DETERMINISTIC_98499957cb711ede
Batch ID: 20250612_161420
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @dev A smart contract for staking $PABLO tokens with revenue sharing.
 */
contract StakingContract is Ownable {
    using SafeMath for uint256;

    IERC20 public token; // Reference to the $PABLO token
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Rate of reward distribution per token staked
    uint256 public lastUpdateTime; // Last time rewards were calculated

    struct Staker {
        uint256 stakedAmount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt of the user
    }

    mapping(address => Staker) public stakers; // Mapping of stakers

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the token and reward rate.
     * @param _token Address of the $PABLO token contract.
     * @param _rewardRate Reward rate for staking.
     */
    constructor(IERC20 _token, uint256 _rewardRate) {
        token = _token;
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Update the staker's rewards based on their staked amount and the current time.
     * @param user The address of the user to update.
     */
    function updateRewards(address user) internal {
        Staker storage staker = stakers[user];
        uint256 accumulatedReward = staker.stakedAmount.mul(rewardRate).mul(block.timestamp.sub(lastUpdateTime)).div(1e18);
        staker.rewardDebt = staker.rewardDebt.add(accumulatedReward);
    }

    /**
     * @dev Stake $PABLO tokens into the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        updateRewards(msg.sender);
        
        // Transfer $PABLO tokens from the user to the contract
        token.transferFrom(msg.sender, address(this), amount);
        
        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.add(amount);
        totalStaked = totalStaked.add(amount);
        lastUpdateTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $PABLO tokens from the contract.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount >= amount, "Insufficient staked amount");

        updateRewards(msg.sender);

        // Transfer $PABLO tokens back to the user
        staker.stakedAmount = staker.stakedAmount.sub(amount);
        totalStaked = totalStaked.sub(amount);
        token.transfer(msg.sender, amount);
        lastUpdateTime = block.timestamp;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim the accumulated rewards for the caller.
     */
    function claimRewards() external {
        updateRewards(msg.sender);
        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.rewardDebt;

        require(reward > 0, "No rewards available");

        // Reset the user's reward debt after claiming
        staker.rewardDebt = 0;

        // Transfer the reward to the user
        token.transfer(msg.sender, reward);
        
        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Set a new reward rate. Only callable by the owner.
     * @param newRewardRate The new reward rate.
     */
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    /**
     * @dev Get the total staked amount in the contract.
     * @return Total amount of staked tokens.
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    /**
     * @dev Get the staked amount and reward debt for a user.
     * @param user The address of the user.
     * @return stakedAmount Amount of tokens staked by the user.
     * @return rewardDebt Amount of rewards accrued by the user.
     */
    function getUserInfo(address user) external view returns (uint256 stakedAmount, uint256 rewardDebt) {
        Staker storage staker = stakers[user];
        return (staker.stakedAmount, staker.rewardDebt);
    }
}
```
