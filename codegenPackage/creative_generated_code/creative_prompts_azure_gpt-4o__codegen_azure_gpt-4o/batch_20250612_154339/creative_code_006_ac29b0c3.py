"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcoin.world
Prompt: Write code in Solidity to implement a staking mechanism for God Token holders that integrates with the reward distribution system described on the website.
Generated: DETERMINISTIC_ac29b0c3360bf80e
Batch ID: 20250612_154339
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
 * @title StakingContract
 * @dev A staking mechanism for God Token holders with integrated reward distribution.
 * Holders can stake their tokens and claim periodic rewards based on their staked amount and duration.
 */
contract StakingContract {
    // Token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    IERC20 public godToken; // The God Token contract
    address public owner;   // Contract owner
    
    uint256 public rewardRate = 100; // Reward rate per second per token (adjustable)
    uint256 public totalStaked;     // Total tokens staked in the contract

    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardDebt;
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 oldRate, uint256 newRate);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier updateReward(address user) {
        if (stakes[user].amount > 0) {
            uint256 reward = calculateReward(user);
            stakes[user].rewardDebt += reward;
        }
        _;
    }

    constructor(address _tokenAddress) {
        godToken = IERC20(_tokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Stake God Tokens into the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");
        require(godToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake God Tokens and claim rewards.
     */
    function unstake() external updateReward(msg.sender) {
        uint256 stakedAmount = stakes[msg.sender].amount;
        require(stakedAmount > 0, "No tokens staked");

        uint256 reward = stakes[msg.sender].rewardDebt;
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].rewardDebt = 0;

        totalStaked -= stakedAmount;

        require(godToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        if (reward > 0) {
            require(godToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Claim accumulated rewards without unstaking.
     */
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards available");

        stakes[msg.sender].rewardDebt = 0;

        require(godToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the pending rewards for a user.
     * @param user Address of the user.
     * @return Pending reward amount.
     */
    function calculateReward(address user) public view returns (uint256) {
        Stake memory stakeData = stakes[user];
        if (stakeData.amount == 0) {
            return 0;
        }
        uint256 duration = block.timestamp - stakeData.startTime;
        uint256 reward = (stakeData.amount * rewardRate * duration) / 1e18;
        return reward;
    }

    /**
     * @dev Update the reward rate.
     * @param newRate New reward rate per second per token.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        emit RewardRateUpdated(rewardRate, newRate);
        rewardRate = newRate;
    }

    /**
     * @dev Withdraw tokens mistakenly sent to the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(owner, amount), "Token withdrawal failed");
    }
}
```
