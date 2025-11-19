"""
Generated Code Metadata:
========================
Original URL: https://etfswap-in.pages.dev
Prompt: Generate a smart contract code for staking ETFS tokens and earning rewards from the 5% sell tax on the ETFSwap platform.
Generated: DETERMINISTIC_812f24439acf2609
Batch ID: 20250622_210802
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
 * @title ETFS Staking Smart Contract
 * @dev This contract allows users to stake ETFS tokens and earn rewards from the 5% sell tax on the ETFSwap platform.
 */
contract ETFSStaking {
    // Token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    IERC20 public etfsToken; // ETFS token contract
    address public owner; // Contract owner
    uint256 public totalStaked; // Total staked tokens
    uint256 public rewardPool; // Reward pool from the 5% sell tax
    uint256 public constant REWARD_RATE = 5; // Reward rate (5% sell tax)

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already claimed
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardAdded(uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No stake found for user");
        _;
    }

    // Constructor
    constructor(address _etfsToken) {
        etfsToken = IERC20(_etfsToken);
        owner = msg.sender;
    }

    /**
     * @dev Stake ETFS tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from user to contract
        require(etfsToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].rewardDebt += calculateReward(msg.sender);

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake ETFS tokens from the contract.
     */
    function unstake() external hasStake(msg.sender) {
        uint256 stakedAmount = stakes[msg.sender].amount;

        // Transfer staked tokens back to user
        require(etfsToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Update total staked
        totalStaked -= stakedAmount;

        // Reset user stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].rewardDebt = 0;

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Claim rewards from the reward pool.
     */
    function claimReward() external hasStake(msg.sender) {
        uint256 reward = calculateReward(msg.sender);

        require(reward > 0, "No rewards available");
        require(reward <= rewardPool, "Insufficient reward pool");

        // Transfer reward to user
        require(etfsToken.transfer(msg.sender, reward), "Reward transfer failed");

        // Update reward pool
        rewardPool -= reward;

        // Update user reward debt
        stakes[msg.sender].rewardDebt += reward;

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Add rewards to the reward pool (called by ETFSwap platform).
     * @param _amount Amount of rewards to add.
     */
    function addReward(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Reward amount must be greater than zero");

        // Transfer rewards to the contract
        require(etfsToken.transferFrom(msg.sender, address(this), _amount), "Reward transfer failed");

        // Update reward pool
        rewardPool += _amount;

        emit RewardAdded(_amount);
    }

    /**
     * @dev Calculate the reward for a user based on their stake.
     * @param _user Address of the user.
     * @return Reward amount.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        // Calculate reward based on user's stake proportion
        uint256 userReward = (userStake.amount * rewardPool) / totalStaked;
        return userReward - userStake.rewardDebt;
    }

    /**
     * @dev Emergency withdraw function for the owner to recover tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= etfsToken.balanceOf(address(this)), "Insufficient contract balance");
        require(etfsToken.transfer(owner, _amount), "Token transfer failed");
    }
}
```
