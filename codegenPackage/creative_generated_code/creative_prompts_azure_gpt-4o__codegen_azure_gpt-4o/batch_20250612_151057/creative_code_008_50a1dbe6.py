"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roost-cys.pages.dev
Prompt: Provide code to implement a staking mechanism for $ROOST tokens using Solidity, allowing users to earn rewards based on their contributions to the Base ecosystem.
Generated: DETERMINISTIC_50a1dbe6da6f8af3
Batch ID: 20250612_151057
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
 * @title ROOST Token Staking Contract
 * @dev This contract allows users to stake ROOST tokens and earn rewards based on their contributions.
 */
contract RoostStaking {
    // ERC20 token interface for staking
    IERC20 public immutable roostToken;

    // Mapping from user address to staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping from user address to reward balances
    mapping(address => uint256) public rewardBalances;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward rate per second (customizable based on ecosystem design)
    uint256 public rewardRate = 1; // 1 token per second for simplicity

    // Mapping to store last update time per user
    mapping(address => uint256) private lastUpdateTime;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor sets the ROOST token address.
     * @param _roostTokenAddress Address of the ROOST token contract.
     */
    constructor(address _roostTokenAddress) {
        require(_roostTokenAddress != address(0), "Invalid token address");
        roostToken = IERC20(_roostTokenAddress);
    }

    /**
     * @dev Stake ROOST tokens in the contract.
     * @param _amount Number of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");
        updateRewards(msg.sender);

        // Transfer tokens from user to the contract
        require(
            roostToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param _amount Number of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(
            stakedBalances[msg.sender] >= _amount,
            "Insufficient staked balance"
        );
        updateRewards(msg.sender);

        // Update staked balances and total staked amount
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(
            roostToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim reward tokens earned through staking.
     */
    function claimRewards() external {
        updateRewards(msg.sender);
        uint256 reward = rewardBalances[msg.sender];
        require(reward > 0, "No rewards available to claim");

        // Reset reward balance
        rewardBalances[msg.sender] = 0;

        // Transfer rewards to user
        require(
            roostToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Updates user rewards based on staking duration.
     * @param _user Address of the user to update rewards for.
     */
    function updateRewards(address _user) internal {
        uint256 timeElapsed = block.timestamp - lastUpdateTime[_user];
        rewardBalances[_user] += stakedBalances[_user] * rewardRate * timeElapsed;
        lastUpdateTime[_user] = block.timestamp;
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param _user Address of the user to calculate rewards for.
     * @return Pending reward amount.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdateTime[_user];
        uint256 pending = stakedBalances[_user] * rewardRate * timeElapsed;
        return rewardBalances[_user] + pending;
    }
}

/**
 * @dev Minimal ERC20 token interface.
 * Used for interacting with ROOST token contract.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount)
        external
        returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
