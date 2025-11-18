"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mike-token-web-olj7orfr7-percenal-miketoken.vercel.app
Prompt: Generate Solidity code for creating a farming pool contract that aligns with Mike Token's roadmap goals for staking and compounding rewards.
Generated: DETERMINISTIC_ac1d4c0ccd1cee9c
Batch ID: 20250612_154216
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

// Importing SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ERC20 token (Mike Token)
interface IMikeToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// FarmingPool contract for staking and compounding rewards
contract FarmingPool is Ownable {
    using SafeMath for uint256;

    // Struct to represent a user's stake
    struct Stake {
        uint256 amount;       // Amount staked
        uint256 lastRewarded; // Timestamp of last reward calculation
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Token used for rewards
    IMikeToken public rewardToken;

    // Events for staking and rewards
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IMikeToken _rewardToken, uint256 _rewardRate) {
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Calculate and pay any rewards before staking
        _calculateReward(msg.sender);

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].lastRewarded = block.timestamp;
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to un-stake tokens and claim rewards
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Calculate and pay any rewards before unstaking
        _calculateReward(msg.sender);

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        totalStaked = totalStaked.sub(amount);
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Internal function to calculate and pay rewards
    function _calculateReward(address user) internal {
        Stake storage userStake = stakes[user];
        
        // Calculate the time since the last reward
        uint256 timeElapsed = block.timestamp.sub(userStake.lastRewarded);
        if (timeElapsed > 0 && userStake.amount > 0) {
            // Calculate reward
            uint256 reward = userStake.amount.mul(rewardRate).mul(timeElapsed).div(1e18);
            // Update the last rewarded time
            userStake.lastRewarded = block.timestamp;

            // Mint and transfer the reward to the user
            rewardToken.mint(user, reward);
            emit RewardPaid(user, reward);
        }
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw any tokens sent directly to the contract (only owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        IERC20(token).transfer(owner(), amount);
    }

    // Function to get the user's staked amount and pending rewards
    function getUserInfo(address user) external view returns (uint256 stakedAmount, uint256 pendingReward) {
        Stake memory userStake = stakes[user];
        stakedAmount = userStake.amount;

        // Calculate pending rewards
        uint256 timeElapsed = block.timestamp.sub(userStake.lastRewarded);
        if (timeElapsed > 0 && userStake.amount > 0) {
            pendingReward = userStake.amount.mul(rewardRate).mul(timeElapsed).div(1e18);
        } else {
            pendingReward = 0;
        }
    }
}
```
