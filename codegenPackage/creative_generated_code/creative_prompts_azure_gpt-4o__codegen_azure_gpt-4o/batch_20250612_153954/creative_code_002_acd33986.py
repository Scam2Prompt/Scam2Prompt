"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldmobile-token.pages.dev
Prompt: Develop a smart contract in Solidity that facilitates staking WMTx tokens and calculates rewards based on network transactions.
Generated: DETERMINISTIC_acd33986d26a2abe
Batch ID: 20250612_153954
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
 * @title WMTx Staking Smart Contract
 * @dev This contract allows users to stake WMTx tokens and earn rewards based on network transactions.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract WMTxStaking {
    // Address of the WMTx token
    IERC20 public immutable wmtxToken;

    // Struct to store staking information
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Accumulated rewards already paid out
    }

    // Mapping of user address to staking information
    mapping(address => StakeInfo) public stakes;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Reward pool (tokens allocated for rewards)
    uint256 public rewardPool;

    // Last transaction count used to calculate rewards
    uint256 public lastTransactionCount;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the WMTx token address.
     * @param _wmtxToken Address of the WMTx token contract.
     */
    constructor(address _wmtxToken) {
        require(_wmtxToken != address(0), "Invalid token address");
        wmtxToken = IERC20(_wmtxToken);
    }

    /**
     * @dev Function to stake WMTx tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer WMTx tokens from user to contract
        require(
            wmtxToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update user stake information
        StakeInfo storage userStake = stakes[msg.sender];
        userStake.amount += _amount;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake WMTx tokens and withdraw rewards.
     */
    function unstake() external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate user rewards
        uint256 userReward = calculateReward(msg.sender);

        // Transfer staked tokens back to the user
        uint256 stakedAmount = userStake.amount;
        require(
            wmtxToken.transfer(msg.sender, stakedAmount),
            "Token transfer failed"
        );

        // Reset the user's stake
        totalStaked -= stakedAmount;
        userStake.amount = 0;
        userStake.rewardDebt = 0;

        // Transfer rewards to the user
        if (userReward > 0) {
            require(
                wmtxToken.transfer(msg.sender, userReward),
                "Reward transfer failed"
            );
            rewardPool -= userReward;
            emit RewardWithdrawn(msg.sender, userReward);
        }

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Function to add transaction-based rewards to the reward pool.
     * @param _transactionCount The current network transaction count.
     * @param _rewardAmount The reward amount added to the pool.
     */
    function addTransactionReward(uint256 _transactionCount, uint256 _rewardAmount) external {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        require(_transactionCount > lastTransactionCount, "Invalid transaction count");

        // Transfer reward tokens into the contract
        require(
            wmtxToken.transferFrom(msg.sender, address(this), _rewardAmount),
            "Reward transfer failed"
        );

        // Update the reward pool and transaction count
        rewardPool += _rewardAmount;
        lastTransactionCount = _transactionCount;
    }

    /**
     * @dev Internal function to calculate rewards for a user.
     * @param _user Address of the user.
     * @return Reward amount for the user.
     */
    function calculateReward(address _user) internal view returns (uint256) {
        StakeInfo storage userStake = stakes[_user];
        if (totalStaked == 0 || userStake.amount == 0 || rewardPool == 0) {
            return 0;
        }

        // Rewards are distributed proportionally based on the user's stake
        uint256 userShare = (userStake.amount * 1e18) / totalStaked;
        uint256 userReward = (userShare * rewardPool) / 1e18;
        return userReward - userStake.rewardDebt;
    }

    /**
     * @dev Function to view the pending reward for a user.
     * @param _user Address of the user.
     * @return Pending reward amount for the user.
     */
    function pendingReward(address _user) external view returns (uint256) {
        return calculateReward(_user);
    }
}
```
