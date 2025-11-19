"""
Generated Code Metadata:
========================
Original URL: https://presales99bitcoins.pages.dev
Prompt: Design a simple staking function for 99Bitcoins Token using Solidity, including a rewards calculation mechanism.
Generated: DETERMINISTIC_326c5f3ce82dbf98
Batch ID: 20250622_205836
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

/**
 * @title StakingContract
 * @dev A simple staking contract for 99Bitcoins Token with rewards calculation.
 */
contract StakingContract {
    // Token interface
    IERC20 public token;

    // Reward rate (e.g., 10% annual reward rate)
    uint256 public rewardRate = 10; // 10% annual reward
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    // Mapping to track staked balances and timestamps
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public stakingStartTime;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the token address.
     * @param _token Address of the 99Bitcoins Token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
    }

    /**
     * @dev Stake tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking balance and start time
        stakedBalances[msg.sender] += _amount;
        stakingStartTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked balance");

        // Calculate rewards
        uint256 stakingDuration = block.timestamp - stakingStartTime[msg.sender];
        uint256 reward = (stakedAmount * rewardRate * stakingDuration) / (100 * SECONDS_IN_YEAR);

        // Reset staking balance and start time
        stakedBalances[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;

        // Transfer staked tokens and rewards back to the user
        require(token.transfer(msg.sender, stakedAmount + reward), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Get the pending reward for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function pendingReward(address _user) external view returns (uint256) {
        uint256 stakedAmount = stakedBalances[_user];
        if (stakedAmount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - stakingStartTime[_user];
        uint256 reward = (stakedAmount * rewardRate * stakingDuration) / (100 * SECONDS_IN_YEAR);
        return reward;
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
