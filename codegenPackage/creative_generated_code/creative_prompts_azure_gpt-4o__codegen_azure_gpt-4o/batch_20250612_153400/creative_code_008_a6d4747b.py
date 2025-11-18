"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogepreneur-io.pages.dev
Prompt: Write a smart contract to handle token staking and passive income distribution for DogePreneur token holders, following the platform’s outlined process.
Generated: DETERMINISTIC_a6d4747b71546b10
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
 * @title DogePreneur Staking Contract
 * @dev Smart contract to enable token staking and passive income distribution
 * for DogePreneur token holders.
 */
contract DogePreneurStaking {
    // State variables
    address public owner; // Contract owner
    IERC20 public token; // DogePreneur token interface
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total tokens staked in the contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Time when staking started
        uint256 rewardsClaimed; // Total rewards claimed by the user
    }

    mapping(address => Stake) public stakes; // Mapping of user address to their staking info

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);
    event RewardsClaimed(address indexed user, uint256 amount, uint256 timestamp);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier hasStake(address user) {
        require(stakes[user].amount > 0, "No active stake found for the user");
        _;
    }

    constructor(IERC20 _token, uint256 _rewardRate) {
        owner = msg.sender;
        token = _token;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows a user to stake DogePreneur tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the sender to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Allows a user to unstake their tokens and withdraw rewards.
     */
    function unstake() external hasStake(msg.sender) {
        Stake memory userStake = stakes[msg.sender];

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Reset user stake
        uint256 stakedAmount = userStake.amount;
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;
        stakes[msg.sender].rewardsClaimed += rewards;

        // Update total staked
        totalStaked -= stakedAmount;

        // Transfer staked tokens and rewards to the user
        require(token.transfer(msg.sender, stakedAmount + rewards), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount, block.timestamp);
        emit RewardsClaimed(msg.sender, rewards, block.timestamp);
    }

    /**
     * @dev Allows a user to claim their accrued rewards without unstaking.
     */
    function claimRewards() external hasStake(msg.sender) {
        uint256 rewards = calculateRewards(msg.sender);

        require(rewards > 0, "No rewards available to claim");

        stakes[msg.sender].timestamp = block.timestamp; // Reset timestamp
        stakes[msg.sender].rewardsClaimed += rewards; // Update claimed rewards

        // Transfer rewards to the user
        require(token.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewards, block.timestamp);
    }

    /**
     * @dev Calculates the rewards for a given user based on their stake and time staked.
     * @param user Address of the user.
     * @return reward Amount of rewards earned by the user.
     */
    function calculateRewards(address user) public view returns (uint256 reward) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Calculate rewards based on staking duration
        uint256 duration = block.timestamp - userStake.timestamp;
        reward = (userStake.amount * rewardRate * duration) / 1e18;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRate;
    }

    /**
     * @dev Emergency function to withdraw all tokens from the contract.
     * Can only be called by the owner.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner, balance), "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
