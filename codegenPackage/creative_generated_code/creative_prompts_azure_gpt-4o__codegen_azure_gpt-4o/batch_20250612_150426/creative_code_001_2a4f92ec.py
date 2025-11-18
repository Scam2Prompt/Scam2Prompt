"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsemex.com
Prompt: Generate Solidity code for a smart contract on PulseChain that implements a staking mechanism for $PLSX tokens with rewards in other PRC20 tokens.
Generated: DETERMINISTIC_2a4f92ecf32c1360
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title PLSXStaking
 * @dev A staking smart contract for PLSX tokens with rewards in other PRC20 tokens on PulseChain.
 */
contract PLSXStaking {
    // ---------------------------
    // Structs and State Variables
    // ---------------------------

    struct Stake {
        uint256 amount;          // Amount of staked PLSX tokens
        uint256 rewardDebt;      // Reward debt for the staker
        uint256 lastStakedTime;  // Timestamp of the last stake
    }

    address public immutable PLSX;            // Address of PLSX token contract
    address public immutable rewardToken;     // Address of reward PRC20 token contract
    uint256 public rewardRatePerSecond;       // Reward rate in tokens per second
    uint256 public totalStaked;               // Total amount of PLSX staked in the contract

    mapping(address => Stake) public stakes;  // Mapping of user addresses to Stake structs

    uint256 public lastRewardTime;            // Last time rewards were calculated
    uint256 public accRewardPerShare;         // Accumulated rewards per share (scaled by 1e18)

    address public owner;                     // Contract owner

    // ------------------
    // Events
    // ------------------

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);
    event RewardRateUpdated(uint256 newRate);

    // ------------------
    // Constructor
    // ------------------

    /**
     * @dev Initializes the contract with the token addresses and reward rate.
     * @param _PLSX Address of the PLSX token.
     * @param _rewardToken Address of the reward token.
     * @param _rewardRatePerSecond Reward rate in tokens per second.
     */
    constructor(address _PLSX, address _rewardToken, uint256 _rewardRatePerSecond) {
        require(_PLSX != address(0), "PLSX address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_rewardRatePerSecond > 0, "Reward rate must be greater than zero");

        PLSX = _PLSX;
        rewardToken = _rewardToken;
        rewardRatePerSecond = _rewardRatePerSecond;
        owner = msg.sender;
        lastRewardTime = block.timestamp;
    }

    // ------------------
    // Modifiers
    // ------------------

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // ------------------
    // Public Functions
    // ------------------

    /**
     * @dev Stake PLSX tokens to earn rewards.
     * @param _amount Amount of PLSX tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        updatePool();

        // Transfer PLSX tokens from user to contract
        bool success = IERC20(PLSX).transferFrom(msg.sender, address(this), _amount);
        require(success, "PLSX transfer failed");

        Stake storage userStake = stakes[msg.sender];

        // Calculate pending rewards and update user's rewardDebt
        if (userStake.amount > 0) {
            uint256 pending = (userStake.amount * accRewardPerShare / 1e18) - userStake.rewardDebt;
            safeRewardTransfer(msg.sender, pending);
        }

        // Update user's stake data
        userStake.amount += _amount;
        userStake.rewardDebt = userStake.amount * accRewardPerShare / 1e18;
        userStake.lastStakedTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake PLSX tokens and claim rewards.
     * @param _amount Amount of PLSX tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        updatePool();

        // Calculate pending rewards and update user's rewardDebt
        uint256 pending = (userStake.amount * accRewardPerShare / 1e18) - userStake.rewardDebt;
        safeRewardTransfer(msg.sender, pending);

        // Update user's stake data
        userStake.amount -= _amount;
        userStake.rewardDebt = userStake.amount * accRewardPerShare / 1e18;

        // Transfer PLSX tokens back to user
        bool success = IERC20(PLSX).transfer(msg.sender, _amount);
        require(success, "PLSX transfer failed");

        totalStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim pending rewards without unstaking.
     */
    function claimRewards() external {
        updatePool();

        Stake storage userStake = stakes[msg.sender];
        uint256 pending = (userStake.amount * accRewardPerShare / 1e18) - userStake.rewardDebt;

        require(pending > 0, "No rewards to claim");

        // Transfer pending rewards to user
        safeRewardTransfer(msg.sender, pending);

        // Update user's rewardDebt
        userStake.rewardDebt = userStake.amount * accRewardPerShare / 1e18;

        emit RewardsClaimed(msg.sender, pending);
    }

    // ------------------
    // Owner Functions
    // ------------------

    /**
     * @dev Updates the reward rate.
     * @param _newRate New reward rate in tokens per second.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than zero");

        updatePool();
        rewardRatePerSecond = _newRate;

        emit RewardRateUpdated(_newRate);
    }

    // ------------------
    // Internal Functions
    // ------------------

    /**
     * @dev Updates the reward pool, calculating accumulated rewards.
     */
    function updatePool() internal {
        if (block.timestamp <= lastRewardTime || totalStaked == 0) {
            lastRewardTime = block.timestamp;
            return;
        }

        uint256 timeElapsed = block.timestamp - lastRewardTime;
        uint256 reward = timeElapsed * rewardRatePerSecond;

        accRewardPerShare += (reward * 1e18) / totalStaked;
        lastRewardTime = block.timestamp;
    }

    /**
     * @dev Transfers reward tokens safely to a user.
     * @param _to Address of the user.
     * @param _amount Amount of reward tokens to transfer.
     */
    function safeRewardTransfer(address _to, uint256 _amount) internal {
        uint256 rewardBal = IERC20(rewardToken).balanceOf(address(this));
        if (_amount > rewardBal) {
            _amount = rewardBal;
        }
        if (_amount > 0) {
            bool success = IERC20(rewardToken).transfer(_to, _amount);
            require(success, "Reward transfer failed");
        }
    }
}

// ------------------
// Interface for PRC20
// ------------------

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
