"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icoprotolcol.com
Prompt: Provide an example of a smart contract for staking tokens that aligns with the features mentioned on the Guildhall platform.
Generated: DETERMINISTIC_648a40dd9fd12b3e
Batch ID: 20250612_162711
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

// Importing necessary libraries and interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for a token
contract TokenStaking is Ownable {
    // State variables
    IERC20 public stakingToken; // Token to be staked
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per staked token
    uint256 public lastUpdateTime; // Last update time for rewards
    mapping(address => uint256) public balances; // User's staking balance
    mapping(address => uint256) public rewards; // User's earned rewards
    mapping(address => uint256) public userRewardPerTokenPaid; // User's reward per token paid

    // Event for staking
    event Staked(address indexed user, uint256 amount);
    // Event for withdrawal
    event Withdrawn(address indexed user, uint256 amount);
    // Event for reward claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    // Modifier to update rewards
    modifier updateReward(address account) {
        rewards[account] = earned(account);
        userRewardPerTokenPaid[account] = rewardPerToken();
        _;
    }

    // Function to calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return 0;
        }
        return ((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / totalStaked;
    }

    // Function to calculate earned rewards
    function earned(address account) public view returns (uint256) {
        return (balances[account] * (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18 + rewards[account];
    }

    // Function to stake tokens
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        stakingToken.transferFrom(msg.sender, address(this), amount);
        totalStaked += amount;
        balances[msg.sender] += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to recover tokens sent to the contract by mistake
    function recoverTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != stakingToken, "Cannot recover staked tokens");
        token.transfer(msg.sender, amount);
    }
}
```
