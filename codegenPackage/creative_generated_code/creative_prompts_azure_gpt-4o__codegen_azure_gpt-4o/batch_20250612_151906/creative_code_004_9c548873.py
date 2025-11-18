"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oldmallowswap.pages.dev
Prompt: Develop a smart contract to manage liquidity pools on MallowSwap, specifically for staking Mallow-ETH LP tokens.
Generated: DETERMINISTIC_9c548873bad36a56
Batch ID: 20250612_151906
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
 * @title MallowSwap Liquidity Pool Staking Contract
 * @dev This contract allows users to stake Mallow-ETH LP tokens and earn rewards.
 */
contract MallowSwapLiquidityPool {
    // Struct to represent the staking details for a user
    struct Stake {
        uint256 amount; // Amount of LP tokens staked
        uint256 rewardDebt; // Reward debt accumulated
        uint256 lastUpdated; // Timestamp of last update
    }

    // State variables
    address public owner; // Owner of the contract
    address public lpToken; // Address of the Mallow-ETH LP token
    uint256 public totalStaked; // Total amount of LP tokens staked in the contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public constant REWARD_PRECISION = 1e18; // Precision for rewards calculation

    mapping(address => Stake) public stakes; // Mapping to store user stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(address _lpToken, uint256 _rewardRate) {
        require(_lpToken != address(0), "LP token address cannot be zero");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        owner = msg.sender;
        lpToken = _lpToken;
        rewardRate = _rewardRate;
    }

    // Modifier to restrict access to owner functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Stake LP tokens in the contract.
     * @param _amount Amount of LP tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer LP tokens from user to the contract
        require(
            IERC20(lpToken).transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        _updateReward(msg.sender);

        userStake.amount += _amount;
        userStake.lastUpdated = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked LP tokens from the contract.
     * @param _amount Amount of LP tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked balance");

        _updateReward(msg.sender);

        userStake.amount -= _amount;
        userStake.lastUpdated = block.timestamp;

        totalStaked -= _amount;

        // Transfer LP tokens back to the user
        require(IERC20(lpToken).transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards accumulated from staking.
     */
    function claimReward() external {
        _updateReward(msg.sender);

        Stake storage userStake = stakes[msg.sender];
        uint256 reward = userStake.rewardDebt;

        require(reward > 0, "No rewards to claim");

        userStake.rewardDebt = 0;

        // Transfer reward tokens (assumed to be ETH or ERC20 tokens) to the user
        payable(msg.sender).transfer(reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Update the reward for a user.
     * @param _user Address of the user.
     */
    function _updateReward(address _user) internal {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            uint256 pendingReward = ((block.timestamp - userStake.lastUpdated) *
                userStake.amount *
                rewardRate) / REWARD_PRECISION;

            userStake.rewardDebt += pendingReward;
        }
        userStake.lastUpdated = block.timestamp;
    }

    /**
     * @dev Allow the owner to set a new reward rate.
     * @param _newRewardRate New reward rate per second.
     */
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Emergency withdrawal of staked LP tokens without rewards.
     */
    function emergencyWithdraw() external {
        Stake storage userStake = stakes[msg.sender];
        uint256 amount = userStake.amount;

        require(amount > 0, "No staked tokens to withdraw");

        userStake.amount = 0;
        userStake.rewardDebt = 0;
        userStake.lastUpdated = block.timestamp;

        totalStaked -= amount;

        // Transfer LP tokens back to the user
        require(IERC20(lpToken).transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }
}

/**
 * @dev Interface for ERC20 token interactions.
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
