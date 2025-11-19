"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20.web.app
Prompt: Generate a Solidity smart contract that mimics the DOGE20 staking mechanism, distributing rewards to stakers over a specified period.
Generated: DETERMINISTIC_c692795b58a9adac
Batch ID: 20250612_161353
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
 * @title DOGE20 Staking Contract
 * @dev A staking contract that distributes rewards to stakers over a specified period.
 */
contract DOGE20Staking {
    // Struct to track user staking information
    struct Stake {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt to manage reward distribution
        uint256 lastUpdated;    // Timestamp of the last staking update
    }

    // ERC20 token interface
    IERC20 public immutable token;

    // Reward rate per second (in tokens)
    uint256 public rewardRate;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Mapping of user address to their staking info
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _token Address of the DOGE20 ERC20 token contract.
     * @param _rewardRate Reward rate per second (in tokens).
     */
    constructor(address _token, uint256 _rewardRate) {
        require(_token != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        token = IERC20(_token);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake tokens into the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        _updateReward(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        totalStaked += amount;

        // Transfer tokens to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their tokens from the contract.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked balance");

        _updateReward(msg.sender);

        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their pending rewards.
     */
    function claimReward() external {
        _updateReward(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 pendingReward = userStake.rewardDebt;

        require(pendingReward > 0, "No rewards available");

        userStake.rewardDebt = 0;

        // Transfer rewards to the user
        require(token.transfer(msg.sender, pendingReward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Internal function to update reward calculations for a user.
     * @param user Address of the user.
     */
    function _updateReward(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
            uint256 pendingReward = (userStake.amount * rewardRate * timeElapsed) / 1 ether;

            userStake.rewardDebt += pendingReward;
        }
        userStake.lastUpdated = block.timestamp;
    }

    /**
     * @dev Returns the pending rewards for a user.
     * @param user Address of the user.
     * @return Pending rewards in tokens.
     */
    function pendingReward(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
        uint256 pendingReward = (userStake.amount * rewardRate * timeElapsed) / 1 ether;

        return userStake.rewardDebt + pendingReward;
    }
}

/**
 * @dev Minimal ERC20 token interface for interacting with DOGE20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
