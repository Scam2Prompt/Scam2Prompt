"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-web.pages.dev
Prompt: Develop a simple smart contract in Solidity to automate the staking and reward distribution process for Green Bitcoin ($GBTC) on the Ethereum blockchain.
Generated: DETERMINISTIC_d68b4f8266e2ad45
Batch ID: 20250622_210443
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
 * @title Green Bitcoin Staking Contract
 * @dev A simple smart contract to automate staking and reward distribution for $GBTC.
 */
contract GreenBitcoinStaking {
    // State variables
    address public owner; // Contract owner
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount of tokens staked

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the stake was made
        uint256 rewards; // Accumulated rewards
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $GBTC tokens in the contract.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Update rewards for the user before modifying their stake
        updateRewards(msg.sender);

        // Update the user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked balance");

        // Update rewards for the user before modifying their stake
        updateRewards(msg.sender);

        // Update the user's stake
        stakes[msg.sender].amount -= _amount;

        // Update total staked amount
        totalStaked -= _amount;

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        // Update rewards for the user
        updateRewards(msg.sender);

        uint256 rewards = stakes[msg.sender].rewards;
        require(rewards > 0, "No rewards available to claim");

        // Reset the user's rewards
        stakes[msg.sender].rewards = 0;

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Update rewards for a user based on their stake and time elapsed.
     * @param _user The address of the user.
     */
    function updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        if (userStake.amount > 0) {
            uint256 timeElapsed = block.timestamp - userStake.timestamp;
            userStake.rewards += (userStake.amount * rewardRate * timeElapsed) / 1e18;
            userStake.timestamp = block.timestamp; // Reset timestamp to current time
        }
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param _newRewardRate The new reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }
}
```
