"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flockerz-site.web.app
Prompt: Write a smart contract in Solidity for a staking system that mimics Flockerz's token breeding mechanism, allowing users to stake $FLOCK and earn rewards proportional to their holdings.
Generated: DETERMINISTIC_88eaa245e4bd6d5a
Batch ID: 20250612_145223
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
 * @title FlockerStaking
 * @dev A staking smart contract allowing users to stake $FLOCK tokens
 *      and earn rewards proportional to their holdings in a "breeding-like" mechanism.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FlockerStaking is Ownable {
    IERC20 public flockToken; // The $FLOCK token contract
    uint256 public rewardRate; // Reward rate (in tokens per second per staked token)
    uint256 public totalStaked; // Total $FLOCK tokens staked in the contract

    struct Staker {
        uint256 balance; // Amount of $FLOCK tokens staked by the user
        uint256 rewardDebt; // Reward debt to track pending rewards
        uint256 lastUpdated; // Last time the user's rewards were calculated
    }

    mapping(address => Staker) public stakers; // Mapping of user address to staking details

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(address _flockToken, uint256 _rewardRate) {
        require(_flockToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        flockToken = IERC20(_flockToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stakes $FLOCK tokens into the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        Staker storage staker = stakers[msg.sender];

        _updateRewards(msg.sender);

        // Transfer $FLOCK tokens to the contract
        require(flockToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        staker.balance += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraws staked $FLOCK tokens from the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(staker.balance >= amount, "Insufficient staked balance");

        _updateRewards(msg.sender);

        staker.balance -= amount;
        totalStaked -= amount;

        // Transfer $FLOCK tokens back to the user
        require(flockToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claims pending rewards earned by the user.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];

        _updateRewards(msg.sender);

        uint256 pendingRewards = staker.rewardDebt;
        require(pendingRewards > 0, "No rewards to claim");

        staker.rewardDebt = 0;
        // Transfer rewards to the user (assuming rewards come from the contract balance)
        require(flockToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Internal function to update the user's rewards.
     * @param user The address of the user to update rewards for.
     */
    function _updateRewards(address user) internal {
        Staker storage staker = stakers[user];

        if (staker.balance > 0) {
            uint256 timeElapsed = block.timestamp - staker.lastUpdated;
            uint256 rewards = (staker.balance * rewardRate * timeElapsed) / 1e18; // Reward calculation

            staker.rewardDebt += rewards;
        }

        staker.lastUpdated = block.timestamp;
    }

    /**
     * @dev Updates the reward rate. Only the contract owner can call this.
     * @param _rewardRate The new reward rate.
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }

    /**
     * @dev Emergency function to allow the owner to withdraw $FLOCK tokens in case of issues.
     * @param amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Cannot withdraw 0 tokens");
        flockToken.transfer(owner(), amount);
    }
}
```
