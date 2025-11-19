"""
Generated Code Metadata:
========================
Original URL: https://aria.fyi
Prompt: Develop a staking system for the Aria token, incorporating the information from the Arianee Protocol's FAQ and tokenomics.
Generated: DETERMINISTIC_bee5b929df2ce0ce
Batch ID: 20250622_212323
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
 * @title AriaTokenStaking
 * @dev A staking system for the Aria token based on the Arianee Protocol's tokenomics.
 * Users can stake their Aria tokens to earn rewards over time.
 */
contract AriaTokenStaking {
    // ERC20 interface for the Aria token
    IERC20 public ariaToken;

    // Struct to store staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        uint256 rewardDebt; // Rewards already paid out
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Reward rate per second (e.g., 0.0001 Aria tokens per second)
    uint256 public rewardRate;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _ariaToken Address of the Aria token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _ariaToken, uint256 _rewardRate) {
        require(address(_ariaToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        ariaToken = _ariaToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake Aria tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update rewards for the user before modifying their stake
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(ariaToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].startTime = block.timestamp;

        // Update total staked tokens
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake Aria tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Update rewards for the user before unstaking
        _updateRewards(msg.sender);

        uint256 amountToUnstake = userStake.amount;

        // Reset user's stake
        userStake.amount = 0;
        userStake.startTime = 0;

        // Update total staked tokens
        totalStaked -= amountToUnstake;

        // Transfer tokens back to the user
        require(ariaToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Claim staking rewards without unstaking.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 rewardsToClaim = stakes[msg.sender].rewardDebt;
        require(rewardsToClaim > 0, "No rewards to claim");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(ariaToken.transfer(msg.sender, rewardsToClaim), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            uint256 stakingDuration = block.timestamp - userStake.startTime;
            uint256 pendingRewards = (userStake.amount * rewardRate * stakingDuration) / 1e18;

            userStake.rewardDebt += pendingRewards;
            userStake.startTime = block.timestamp; // Reset start time for reward calculation
        }
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending rewards for the user.
     */
    function pendingRewards(address _user) external view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            uint256 stakingDuration = block.timestamp - userStake.startTime;
            uint256 pendingRewards = (userStake.amount * rewardRate * stakingDuration) / 1e18;
            return pendingRewards + userStake.rewardDebt;
        }
        return 0;
    }
}

/**
 * @dev Minimal ERC20 interface for interacting with the Aria token.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
