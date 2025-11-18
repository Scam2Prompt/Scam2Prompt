"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgcasino-app.pages.dev
Prompt: Create a smart contract in Solidity for staking $TGC tokens, incorporating TG.Casino's tokenomics (e.g., 20% liquidity pool, 40% presale allocation).
Generated: DETERMINISTIC_d7de26e01f7d464c
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

// Importing interfaces to interact with ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TGCStaking
 * @dev A smart contract for staking TGC tokens with built-in tokenomics features.
 */
contract TGCStaking is Ownable {
    IERC20 public tgcToken; // The TGC token contract
    uint256 public totalStaked; // Total amount of TGC tokens staked
    uint256 public rewardRate; // Rate of rewards per staked token
    mapping(address => uint256) public stakedBalances; // User's staked balances
    mapping(address => uint256) public rewardBalances; // User's reward balances
    mapping(address => uint256) public lastUpdated; // Timestamp of last update for rewards

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the TGC token contract address
     * @param _tgcToken The address of the TGC token contract
     */
    constructor(address _tgcToken) {
        tgcToken = IERC20(_tgcToken);
        rewardRate = 100; // Example: reward rate set to 100 (can be adjusted)
    }

    /**
     * @dev Function to stake TGC tokens
     * @param amount The amount of TGC tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(tgcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's rewards before staking
        updateReward(msg.sender);

        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake TGC tokens
     * @param amount The amount of TGC tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update user's rewards before unstaking
        updateReward(msg.sender);

        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;

        require(tgcToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to claim accrued rewards
     */
    function claimRewards() external {
        updateReward(msg.sender);
        
        uint256 reward = rewardBalances[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewardBalances[msg.sender] = 0;
        require(tgcToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a user
     * @param user The user's address
     */
    function updateReward(address user) internal {
        uint256 currentTime = block.timestamp;
        uint256 timeDiff = currentTime - lastUpdated[user];

        // Calculate the user reward based on staked balance and reward rate
        uint256 reward = (stakedBalances[user] * rewardRate * timeDiff) / 1 days;
        rewardBalances[user] += reward;
        lastUpdated[user] = currentTime;
    }

    /**
     * @dev Function to set a new reward rate (only owner can call)
     * @param newRate The new reward rate
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    /**
     * @dev Function to withdraw tokens from the contract (only owner can call)
     * @param amount The amount of TGC tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(tgcToken.transfer(msg.sender, amount), "Transfer failed");
    }

    /**
     * @dev Function to get the staked balance of a user
     * @param user The user's address
     * @return The staked balance of the user
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    /**
     * @dev Function to get the reward balance of a user
     * @param user The user's address
     * @return The reward balance of the user
     */
    function getRewardBalance(address user) external view returns (uint256) {
        return rewardBalances[user];
    }
}
```
