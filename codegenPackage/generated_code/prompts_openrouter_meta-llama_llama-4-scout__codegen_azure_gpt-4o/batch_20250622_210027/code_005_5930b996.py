"""
Generated Code Metadata:
========================
Original URL: https://prism-61a.pages.dev
Prompt: Create a smart contract function to handle DUEL token staking and rewards distribution on a blockchain platform.
Generated: DETERMINISTIC_5930b9966a1b699a
Batch ID: 20250622_210027
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
 * @title DUEL Token Staking Contract
 * @dev This contract allows users to stake DUEL tokens and earn rewards over time.
 */
contract DuelTokenStaking {
    // State variables
    address public owner; // Contract owner
    IERC20 public duelToken; // DUEL token contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total tokens staked in the contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 lastUpdated; // Timestamp of the last reward calculation
        uint256 rewards; // Accumulated rewards
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _duelToken, uint256 _rewardRate) {
        owner = msg.sender;
        duelToken = IERC20(_duelToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake DUEL tokens to earn rewards.
     * @param _amount The amount of DUEL tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update rewards for the user before modifying their stake
        _updateRewards(msg.sender);

        // Transfer DUEL tokens from the user to the contract
        require(duelToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake DUEL tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Update rewards for the user before unstaking
        _updateRewards(msg.sender);

        uint256 amountToUnstake = userStake.amount;
        uint256 rewardsToClaim = userStake.rewards;

        // Reset user's stake
        userStake.amount = 0;
        userStake.rewards = 0;
        userStake.lastUpdated = block.timestamp;

        // Update total staked amount
        totalStaked -= amountToUnstake;

        // Transfer staked tokens and rewards to the user
        require(duelToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");
        if (rewardsToClaim > 0) {
            require(duelToken.transfer(msg.sender, rewardsToClaim), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, amountToUnstake);
        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Claim accumulated rewards without unstaking.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 rewardsToClaim = stakes[msg.sender].rewards;
        require(rewardsToClaim > 0, "No rewards to claim");

        // Reset user's rewards
        stakes[msg.sender].rewards = 0;

        // Transfer rewards to the user
        require(duelToken.transfer(msg.sender, rewardsToClaim), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Update rewards for a user based on their stake and elapsed time.
     * @param _user The address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
            uint256 newRewards = (userStake.amount * rewardRate * timeElapsed) / 1e18; // Assuming rewardRate is scaled
            userStake.rewards += newRewards;
            userStake.lastUpdated = block.timestamp;
        }
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param _newRewardRate The new reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Emergency withdrawal of tokens from the contract. Only callable by the owner.
     * @param _amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(duelToken.transfer(owner, _amount), "Token transfer failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
