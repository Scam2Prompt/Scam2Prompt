"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xipon.pages.dev
Prompt: Create a smart contract example for managing rewards distribution in the Xion DeFi ecosystem, ensuring compatibility with the BonusBlock protocol.
Generated: DETERMINISTIC_3c88ee3e2a81413c
Batch ID: 20250612_151947
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RewardsDistributor
 * @dev Smart contract for managing rewards distribution in the Xion DeFi ecosystem
 *      compatible with the BonusBlock protocol.
 */
contract RewardsDistributor is Ownable {
    IERC20 public rewardToken; // The token used for rewards
    uint256 public totalRewards; // Total rewards to be distributed
    mapping(address => uint256) public userRewards; // User rewards mapping
    mapping(address => bool) public hasClaimed; // Track if user has claimed rewards

    event RewardsDistributed(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the reward token address.
     * @param _rewardToken Address of the ERC20 token to be used for rewards.
     */
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    /**
     * @dev Distribute rewards to a list of users.
     * @param users List of user addresses to distribute rewards to.
     * @param amounts Corresponding reward amounts for each user.
     */
    function distributeRewards(address[] memory users, uint256[] memory amounts) external onlyOwner {
        require(users.length == amounts.length, "Mismatching users and amounts length");
        
        for (uint256 i = 0; i < users.length; i++) {
            require(amounts[i] > 0, "Amount must be greater than zero");
            totalRewards += amounts[i];
            userRewards[users[i]] += amounts[i];

            emit RewardsDistributed(users[i], amounts[i]);
        }
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimRewards() external {
        uint256 amount = userRewards[msg.sender];
        require(amount > 0, "No rewards to claim");
        require(!hasClaimed[msg.sender], "Rewards already claimed");

        hasClaimed[msg.sender] = true;
        userRewards[msg.sender] = 0; // Reset user rewards to zero

        // Transfer the reward tokens to the user
        require(rewardToken.transfer(msg.sender, amount), "Token transfer failed");

        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw accidentally sent tokens to the contract.
     * @param token Address of the token to withdraw.
     * @param amount Amount of the token to withdraw.
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(msg.sender, amount), "Token withdrawal failed");
    }

    /**
     * @dev Function to check the rewards of a specific user.
     * @param user Address of the user to check rewards for.
     * @return uint256 Amount of rewards available for the user.
     */
    function checkUserRewards(address user) external view returns (uint256) {
        return userRewards[user];
    }
}
```
