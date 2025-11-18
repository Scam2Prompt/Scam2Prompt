"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchainedclaimxyz.pages.dev
Prompt: Develop a smart contract to enable staking rewards distribution for $PEPU tokens on Pepe Unchained, ensuring compliance with the tokenomics allocation.
Generated: DETERMINISTIC_fb508676e7e5f977
Batch ID: 20250612_151255
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

// Import OpenZeppelin contracts for security and standardization
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The PepuStaking contract allows users to stake $PEPU tokens and earn rewards
contract PepuStaking is Ownable {
    // State variables
    IERC20 public pepuToken; // Reference to the $PEPU token contract
    uint256 public totalStaked; // Total amount of $PEPU tokens staked
    uint256 public rewardRate; // Reward rate per token per block
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards earned by each user
    mapping(address => uint256) public lastUpdate; // Last update block for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set the token and initial reward rate
    constructor(IERC20 _pepuToken, uint256 _rewardRate) {
        pepuToken = _pepuToken;
        rewardRate = _rewardRate;
    }

    // Modifier to update rewards before any staking or un-staking actions
    modifier updateReward(address account) {
        if (account != address(0)) {
            rewards[account] += earned(account);
            lastUpdate[account] = block.number;
        }
        _;
    }

    // Function to stake $PEPU tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        pepuToken.transferFrom(msg.sender, address(this), amount);
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to unstake $PEPU tokens
    function unstake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        pepuToken.transfer(msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        pepuToken.transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    // Function to calculate earned rewards for a user
    function earned(address account) public view returns (uint256) {
        return (stakedAmount[account] * rewardRate * (block.number - lastUpdate[account])) / 1e18;
    }

    // Function to set the reward rate (only owner can change it)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to get total staked tokens
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }

    // Function to get staked amount for a user
    function getStakedAmount(address account) external view returns (uint256) {
        return stakedAmount[account];
    }

    // Function to get the rewards of a user
    function getRewards(address account) external view returns (uint256) {
        return rewards[account] + earned(account);
    }
}
```
