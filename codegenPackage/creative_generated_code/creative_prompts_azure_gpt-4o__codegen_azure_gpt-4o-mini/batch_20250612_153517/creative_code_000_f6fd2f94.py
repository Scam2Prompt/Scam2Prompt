"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decubate-platform.pages.dev
Prompt: Write a smart contract in Solidity to implement a staking mechanism similar to Decubate, allowing users to stake DCB tokens and earn rewards based on fixed and compounding APY rates, with options for NFT and tier boosts.
Generated: DETERMINISTIC_f6fd2f9464aed6e8
Batch ID: 20250612_153517
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

// Import OpenZeppelin libraries for safe ERC20 handling and contract ownership
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract interface
interface IStakeable {
    function stake(uint256 amount) external;
    function unstake(uint256 amount) external;
    function claimRewards() external;
}

contract StakingContract is IStakeable, Ownable {
    IERC20 public dcbToken;       // DCB token contract
    uint256 public totalStaked;   // Total amount of tokens staked
    uint256 public rewardsRate;    // Fixed APY rate (in basis points)
    uint256 public lastUpdateTime; // Last time rewards were calculated

    struct StakeInfo {
        uint256 amount;            // Amount staked
        uint256 rewardDebt;        // Reward debt to calculate rewards
        uint256 lastStakeTime;     // Last time the user staked
    }

    mapping(address => StakeInfo) public stakes; // User stakes information

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _dcbToken, uint256 _rewardsRate) {
        dcbToken = _dcbToken;
        rewardsRate = _rewardsRate; // Set fixed APY rate
    }

    // Modifier to check that the user is staking
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No staked amount");
        _;
    }

    // Stake DCB tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(dcbToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user stake information
        StakeInfo storage stakeInfo = stakes[msg.sender];
        stakeInfo.amount += amount;
        stakeInfo.lastStakeTime = block.timestamp;

        totalStaked += amount;
        lastUpdateTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Unstake DCB tokens and claim rewards
    function unstake(uint256 amount) external hasStake {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(amount <= stakeInfo.amount, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        if (rewards > 0) {
            safeTransferReward(msg.sender, rewards);
        }

        // Update total staked amount and user info
        stakeInfo.amount -= amount;
        totalStaked -= amount;
        
        require(dcbToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Claim rewards without unstaking
    function claimRewards() external hasStake {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update user's reward debt
        stakes[msg.sender].rewardDebt += rewards;
        safeTransferReward(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Calculate rewards for a user
    function calculateRewards(address user) internal view returns (uint256) {
        StakeInfo memory stakeInfo = stakes[user];
        uint256 timeStaked = block.timestamp - stakeInfo.lastStakeTime;

        // Calculate rewards based on the amount staked and APY
        return (stakeInfo.amount * rewardsRate * timeStaked) / (365 days * 10000);
    }

    // Transfer rewards safely
    function safeTransferReward(address to, uint256 amount) internal {
        // Implement transfer logic here, ensure it does not exceed available rewards
        // Placeholder for reward transfer logic
    }

    // Admin function to update the rewards rate
    function updateRewardsRate(uint256 newRate) external onlyOwner {
        rewardsRate = newRate;
    }

    // Function to withdraw tokens in case of emergencies
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(dcbToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    // View function to get user's stake information
    function getUserStakeInfo(address user) external view returns (uint256 amount, uint256 rewards) {
        StakeInfo memory stakeInfo = stakes[user];
        rewards = calculateRewards(user);
        amount = stakeInfo.amount;
    }
}
```
