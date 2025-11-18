"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge2014sale.pages.dev
Prompt: Write a smart contract in Solidity that facilitates staking for Doge2014 tokens, allowing users to earn rewards based on the staking allocation described in the Doge2014 tokenomics. Ensure compatibility with Ethereum wallets like MetaMask.
Generated: DETERMINISTIC_f53b9bac96e9909c
Batch ID: 20250612_152240
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
 * @title Doge2014 Staking Contract
 * @dev This contract enables users to stake Doge2014 tokens and earn rewards based on the tokenomics.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract Doge2014Staking {
    IERC20 public immutable doge2014Token; // Doge2014 token contract
    address public owner; // Contract owner
    uint256 public rewardRate; // Reward rate in percentage (e.g., 5 for 5%)

    struct Stake {
        uint256 amount; // Staked amount
        uint256 timestamp; // Time of staking
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes
    mapping(address => uint256) public rewards; // Mapping of user addresses to their rewards

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardWithdrawn(address indexed user, uint256 reward);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor that initializes the contract.
     * @param _doge2014Token Address of the Doge2014 token contract.
     * @param _rewardRate Reward rate in percentage.
     */
    constructor(IERC20 _doge2014Token, uint256 _rewardRate) {
        require(address(_doge2014Token) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        doge2014Token = _doge2014Token;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to stake Doge2014 tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(doge2014Token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Calculate and store pending rewards
        if (stakes[msg.sender].amount > 0) {
            rewards[msg.sender] += calculateReward(msg.sender);
        }

        // Update staked amount and timestamp
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to unstake their Doge2014 tokens.
     */
    function unstake() external {
        uint256 stakedAmount = stakes[msg.sender].amount;
        require(stakedAmount > 0, "No tokens to unstake");

        // Calculate and store pending rewards
        rewards[msg.sender] += calculateReward(msg.sender);

        // Reset stake info
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        require(doge2014Token.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Allows a user to withdraw their accumulated rewards.
     */
    function withdrawReward() external {
        uint256 reward = rewards[msg.sender] + calculateReward(msg.sender);
        require(reward > 0, "No rewards to withdraw");

        rewards[msg.sender] = 0;
        stakes[msg.sender].timestamp = block.timestamp;

        require(doge2014Token.transfer(msg.sender, reward), "Token transfer failed");

        emit RewardWithdrawn(msg.sender, reward);
    }

    /**
     * @dev Calculates the rewards for a user based on their staking duration.
     * @param _user Address of the user.
     * @return Calculated reward amount.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.timestamp; // Duration in seconds
        uint256 reward = (userStake.amount * rewardRate * stakingDuration) / (100 * 365 days); // Annual reward formula
        return reward;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRewardRate New reward rate in percentage.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract.
     * @param _amount Amount to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(doge2014Token.transfer(owner, _amount), "Token transfer failed");
    }
}
```
