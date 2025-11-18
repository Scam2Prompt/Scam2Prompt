"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btceftoken.pages.dev
Prompt: Write a smart contract in Solidity for staking BTCETF tokens, where rewards are dynamically calculated based on the total amount of tokens staked by the community, as described in the Bitcoin ETF Token documentation.
Generated: DETERMINISTIC_fbf2fd333b63cd1a
Batch ID: 20250612_145625
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
 * @title BTCETF Staking Contract
 * @dev A smart contract for staking BTCETF tokens and dynamically distributing rewards
 * based on the total staked amount in the system.
 */
interface IBTCETF {
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BTCETFStaking {
    // State variables
    IBTCETF public btcETFToken; // Interface to interact with the BTCETF token
    address public owner; // Contract owner
    uint256 public totalStaked; // Total tokens staked in the contract
    uint256 public rewardPool; // Total rewards available for distribution

    // Mapping to track user stakes
    mapping(address => uint256) public stakedBalances;

    // Mapping to track rewards for users
    mapping(address => uint256) public rewards;

    // Events for logging key actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardPoolUpdated(uint256 newRewardPool);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor
    constructor(address _btcETFTokenAddress) {
        btcETFToken = IBTCETF(_btcETFTokenAddress);
        owner = msg.sender;
    }

    /**
     * @notice Stake BTCETF tokens into the contract.
     * @param _amount Amount of BTCETF tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(btcETFToken.transferFrom(msg.sender, address(this), _amount), "Stake transfer failed");

        // Update user and global staking balances
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Withdraw staked BTCETF tokens.
     * @param _amount Amount of BTCETF tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update user and global staking balances
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(btcETFToken.transfer(msg.sender, _amount), "Withdraw transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards for staking.
     */
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available to claim");

        // Update rewards mapping and transfer reward to user
        rewards[msg.sender] = 0;
        require(btcETFToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Update the reward pool (only owner can call this).
     * @param _amount Amount of BTCETF tokens to add to the reward pool.
     */
    function updateRewardPool(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Reward pool amount must be greater than zero");
        require(btcETFToken.transferFrom(msg.sender, address(this), _amount), "Reward pool transfer failed");

        rewardPool += _amount;

        emit RewardPoolUpdated(rewardPool);
    }

    /**
     * @notice Calculate the rewards for a user based on their stake.
     * @param _user Address of the user to calculate rewards for.
     * @return reward The calculated reward.
     */
    function calculateReward(address _user) public view returns (uint256 reward) {
        if (totalStaked == 0) {
            return 0; // Avoid division by zero
        }
        // User's proportion of total staked multiplied by the reward pool
        reward = (stakedBalances[_user] * rewardPool) / totalStaked;
        return reward;
    }

    /**
     * @notice Emergency function for the owner to recover tokens.
     * @param _token Address of the token to recover.
     * @param _amount Amount of tokens to recover.
     */
    function recoverTokens(address _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Recover amount must be greater than zero");
        IBTCETF(_token).transfer(owner, _amount);
    }
}
```
