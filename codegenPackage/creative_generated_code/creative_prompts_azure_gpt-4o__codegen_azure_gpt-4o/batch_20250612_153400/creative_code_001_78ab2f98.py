"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinuairdrop.pages.dev
Prompt: Generate Solidity code for a staking smart contract that supports $POODL tokens, allowing users to lock their tokens and earn rewards at an annual rate of 79%.
Generated: DETERMINISTIC_78ab2f98085afc51
Batch ID: 20250612_153400
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
 * @title POODL Staking Contract
 * @dev Enables staking of $POODL tokens with a fixed annual reward rate of 79%.
 */
contract PoodlStaking {
    // ERC20 interface for interacting with the $POODL token
    IERC20 public immutable poodlToken;

    // Annual reward rate (79%)
    uint256 public constant ANNUAL_REWARD_RATE = 79;
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    // Data structure to track staker information
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 timestamp;    // Timestamp of when staking started
        uint256 rewardsEarned; // Total rewards earned by the staker
    }

    // Mapping of staker addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);
    event RewardsClaimed(address indexed user, uint256 rewards);

    /**
     * @dev Constructor to set the $POODL token address
     * @param _poodlToken Address of the $POODL token contract
     */
    constructor(IERC20 _poodlToken) {
        require(address(_poodlToken) != address(0), "Invalid token address");
        poodlToken = _poodlToken;
    }

    /**
     * @dev Allows users to stake $POODL tokens.
     * @param _amount Number of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update rewards for the user before modifying their stake
        _updateRewards(msg.sender);

        // Transfer $POODL tokens from the user to the contract
        require(
            poodlToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staker's information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their staked tokens along with rewards.
     */
    function unstake() external {
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount > 0, "No staked tokens to unstake");

        // Calculate and update rewards before unstaking
        _updateRewards(msg.sender);

        // Fetch staked amount and total rewards
        uint256 stakedAmount = stakeData.amount;
        uint256 totalRewards = stakeData.rewardsEarned;

        // Reset stake data
        stakeData.amount = 0;
        stakeData.timestamp = 0;
        stakeData.rewardsEarned = 0;

        // Transfer staked tokens and rewards back to the user
        require(
            poodlToken.transfer(msg.sender, stakedAmount + totalRewards),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, stakedAmount, totalRewards);
    }

    /**
     * @dev Allows users to claim their rewards without unstaking.
     */
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);

        // Fetch the rewards balance
        uint256 rewards = stakes[msg.sender].rewardsEarned;
        require(rewards > 0, "No rewards available to claim");

        // Reset rewards data
        stakes[msg.sender].rewardsEarned = 0;

        // Transfer rewards to the user
        require(
            poodlToken.transfer(msg.sender, rewards),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the staker
     */
    function _updateRewards(address _user) internal {
        Stake storage stakeData = stakes[_user];
        if (stakeData.amount == 0 || stakeData.timestamp == 0) {
            return;
        }

        // Calculate time elapsed since last update
        uint256 timeElapsed = block.timestamp - stakeData.timestamp;

        // Calculate rewards based on elapsed time and reward rate
        uint256 rewards = (stakeData.amount * ANNUAL_REWARD_RATE * timeElapsed) /
            (100 * SECONDS_IN_YEAR);

        // Update rewardsEarned and reset timestamp
        stakeData.rewardsEarned += rewards;
        stakeData.timestamp = block.timestamp;
    }
}

/**
 * @dev Interface for ERC20 token standard
 */
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
