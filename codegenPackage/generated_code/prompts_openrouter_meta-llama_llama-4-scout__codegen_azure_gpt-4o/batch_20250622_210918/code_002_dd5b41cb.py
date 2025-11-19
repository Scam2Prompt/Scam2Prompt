"""
Generated Code Metadata:
========================
Original URL: https://presales-99bitcoin.pages.dev
Prompt: Develop a simple staking function for 99Bitcoins tokens using Solidity, considering a dynamic rewards rate based on the staking pool percentage.
Generated: DETERMINISTIC_dd5b41cb6f42f7fb
Batch ID: 20250622_210918
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
 * @dev A simple staking contract for 99Bitcoins tokens with dynamic rewards based on staking pool percentage.
 */
contract StakingContract {
    // ERC20 token interface
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    IERC20 public token; // 99Bitcoins token contract
    uint256 public totalStaked; // Total tokens staked in the contract
    uint256 public rewardPool; // Total reward pool available for distribution
    uint256 public constant REWARD_RATE_BASE = 1000; // Base reward rate (percentage multiplier)

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the stake was made
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _token Address of the 99Bitcoins token contract.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking data
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards based on staking pool percentage
        uint256 stakingPercentage = (userStake.amount * 100) / totalStaked;
        uint256 rewardRate = (stakingPercentage * REWARD_RATE_BASE) / 100;
        uint256 reward = (userStake.amount * rewardRate) / 100;

        // Ensure reward pool has enough tokens
        require(reward <= rewardPool, "Insufficient reward pool");

        // Update state
        totalStaked -= userStake.amount;
        rewardPool -= reward;

        // Transfer staked tokens and rewards to the user
        require(token.transfer(msg.sender, userStake.amount + reward), "Token transfer failed");

        // Reset user stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Add tokens to the reward pool.
     * @param _amount Amount of tokens to add to the reward pool.
     */
    function addRewardPool(uint256 _amount) external {
        require(_amount > 0, "Reward pool amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        rewardPool += _amount;
    }

    /**
     * @dev Get the staking details of a user.
     * @param _user Address of the user.
     * @return amount Staked amount.
     * @return timestamp Timestamp of the stake.
     */
    function getStakeDetails(address _user) external view returns (uint256 amount, uint256 timestamp) {
        Stake storage userStake = stakes[_user];
        return (userStake.amount, userStake.timestamp);
    }
}
```
