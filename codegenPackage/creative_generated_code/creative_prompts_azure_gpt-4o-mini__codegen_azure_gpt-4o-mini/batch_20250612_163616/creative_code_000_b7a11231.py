"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Generate a smart contract for a decentralized betting platform that allows users to stake $BCB tokens and receive rewards in stable coins.
Generated: DETERMINISTIC_b7a11231a0d2b817
Batch ID: 20250612_163616
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

// Importing OpenZeppelin Contracts for safe token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Decentralized Betting Platform
 * @dev This contract allows users to stake $BCB tokens and receive rewards in stable coins.
 */
contract DecentralizedBettingPlatform is Ownable {
    // State variables
    IERC20 public bcbToken;         // The staking token ($BCB)
    IERC20 public stableCoin;       // The reward token (stable coins)
    
    struct UserInfo {
        uint256 amountStaked;       // Amount of $BCB tokens staked by the user
        uint256 rewardDebt;          // User's reward debt to prevent double counting of rewards
    }
    
    mapping(address => UserInfo) public userInfo;  // Information about each user

    uint256 public totalStaked;                    // Total amount of $BCB tokens staked in the contract
    uint256 public accRewardPerShare;              // Accumulated rewards per share

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with token addresses
    constructor(address _bcbToken, address _stableCoin) {
        bcbToken = IERC20(_bcbToken);
        stableCoin = IERC20(_stableCoin);
    }

    /**
     * @dev Stakes $BCB tokens into the contract.
     * @param amount The amount of $BCB tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(bcbToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        UserInfo storage user = userInfo[msg.sender];
        user.amountStaked += amount;
        totalStaked += amount;

        // Update user's reward debt
        user.rewardDebt = (user.amountStaked * accRewardPerShare) / 1e12;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstakes $BCB tokens and claims rewards.
     * @param amount The amount of $BCB tokens to unstake.
     */
    function unstake(uint256 amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amountStaked >= amount, "Insufficient staked amount");

        // Calculate rewards before unstaking
        uint256 pendingRewards = ((user.amountStaked * accRewardPerShare) / 1e12) - user.rewardDebt;
        if (pendingRewards > 0) {
            // Transfer rewards to the user
            require(stableCoin.transfer(msg.sender, pendingRewards), "Reward transfer failed");
            emit RewardsClaimed(msg.sender, pendingRewards);
        }

        user.amountStaked -= amount;
        totalStaked -= amount;

        require(bcbToken.transfer(msg.sender, amount), "Unstake transfer failed");

        // Update user's reward debt
        user.rewardDebt = (user.amountStaked * accRewardPerShare) / 1e12;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Updates the reward variables. Should be called regularly.
     * @param addedReward The amount of stable coins to add as rewards.
     */
    function updateRewards(uint256 addedReward) external onlyOwner {
        require(totalStaked > 0, "No staked tokens");

        // Transfer the added reward to the contract
        require(stableCoin.transferFrom(msg.sender, address(this), addedReward), "Reward transfer failed");

        // Update accumulated rewards per share
        accRewardPerShare += (addedReward * 1e12) / totalStaked; // Use 1e12 to maintain precision
    }

    /**
     * @dev Returns the pending rewards for a user.
     * @param userAddress The address of the user to query.
     * @return The amount of pending rewards in stable coins.
     */
    function pendingRewards(address userAddress) external view returns (uint256) {
        UserInfo storage user = userInfo[userAddress];
        uint256 accReward = accRewardPerShare; // Snapshot of accumulated rewards per share
        if (totalStaked > 0) {
            return ((user.amountStaked * accReward) / 1e12) - user.rewardDebt;
        } else {
            return 0;
        }
    }
}
```
