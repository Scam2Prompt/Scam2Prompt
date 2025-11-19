"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealyi.github.io
Prompt: Generate a Solidity smart contract for staking ORB tokens on the Zealy platform, ensuring it includes reward distribution logic.
Generated: DETERMINISTIC_a49c5e07759eb499
Batch ID: 20250612_163135
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
 * @title ORB Token Staking Contract
 * @dev Allows users to stake ORB tokens and earn rewards. Includes reward distribution logic.
 */
contract ORBStaking {
    // State variables
    IERC20 public orbToken; // ORB Token contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total staked tokens

    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt to calculate pending rewards
        uint256 lastStakedTime; // Timestamp of the last stake
    }

    mapping(address => StakeInfo) public stakes; // Mapping of stakers to their stake info

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor
    constructor(IERC20 _orbToken, uint256 _rewardRate) {
        require(address(_orbToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        orbToken = _orbToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake ORB tokens to earn rewards.
     * @param _amount Amount of ORB tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");

        // Update user's rewards before modifying their staked balance
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(orbToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update stake info
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastStakedTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked ORB tokens.
     * @param _amount Amount of ORB tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Update user's rewards before modifying their staked balance
        _updateRewards(msg.sender);

        // Update stake info
        stakes[msg.sender].amount -= _amount;

        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(orbToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim earned rewards.
     */
    function claimRewards() external {
        // Update user's rewards
        _updateRewards(msg.sender);

        uint256 reward = stakes[msg.sender].rewardDebt;

        require(reward > 0, "No rewards available");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(orbToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a given user.
     * @param _user Address of the user to update rewards for.
     */
    function _updateRewards(address _user) internal {
        StakeInfo storage stake = stakes[_user];
        if (stake.amount > 0) {
            uint256 pendingReward = (block.timestamp - stake.lastStakedTime) * stake.amount * rewardRate / 1e18;
            stake.rewardDebt += pendingReward;
            stake.lastStakedTime = block.timestamp;
        }
    }

    /**
     * @dev Get the pending reward for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function getPendingRewards(address _user) external view returns (uint256) {
        StakeInfo storage stake = stakes[_user];
        if (stake.amount == 0) {
            return 0;
        }

        uint256 pendingReward = (block.timestamp - stake.lastStakedTime) * stake.amount * rewardRate / 1e18;
        return stake.rewardDebt + pendingReward;
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address from, address to, uint256 value) external returns (bool);
    function transfer(address to, uint256 value) external returns (bool);
}
```
