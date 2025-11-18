"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfdbull.pages.dev
Prompt: Create a smart contract in Solidity that allows users to stake $BTFD tokens and earn rewards, as described in the staking section of the BTFD website.
Generated: DETERMINISTIC_cfc76429ed070250
Batch ID: 20250612_154236
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

// Importing the IERC20 interface to interact with the BTFD token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // Token being staked
    IERC20 public stakingToken;

    // User staking information
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }

    // Mapping from user address to their staking information
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;
    
    // Reward variables
    uint256 public rewardPerTokenAccumulated;
    uint256 public lastUpdateTime;

    // Emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the staking contract with the token address
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
        lastUpdateTime = block.timestamp;
    }

    // Modifier to update rewards before any action
    modifier updateReward(address account) {
        rewardPerTokenAccumulated = earnedRewardPerToken();
        if (account != address(0)) {
            stakes[account].rewardDebt = earnedRewards(account);
        }
        lastUpdateTime = block.timestamp;
        _;
    }

    // Function to calculate the reward per token accumulated
    function earnedRewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenAccumulated;
        }
        return rewardPerTokenAccumulated + ((block.timestamp - lastUpdateTime) * 1e18 / totalStaked);
    }

    // Function to calculate the earned rewards for a staker
    function earnedRewards(address account) public view returns (uint256) {
        Stake memory stake = stakes[account];
        return (stake.amount * (earnedRewardPerToken() - stake.rewardDebt)) / 1e18;
    }

    // Function for users to stake tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        // Transfer tokens from user to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake information
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function for users to withdraw their staked tokens
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function for users to claim their rewards
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = earnedRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update user's reward debt
        stakes[msg.sender].rewardDebt = earnedRewardPerToken();

        // Transfer rewards to user (assuming rewards are also in the stakingToken)
        stakingToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to rescue tokens sent to the contract by mistake
    function rescueTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(stakingToken), "Cannot rescue the staking token");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
