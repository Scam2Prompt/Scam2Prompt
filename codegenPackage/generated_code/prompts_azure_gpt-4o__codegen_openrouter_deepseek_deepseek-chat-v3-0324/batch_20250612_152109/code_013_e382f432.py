"""
Generated Code Metadata:
========================
Original URL: https://penguins-gainsassociates.pages.dev
Prompt: Develop a Solidity smart contract for distributing rewards in a multichain Web3 gaming ecosystem, similar to Kewl's features mentioned on the GAINS Associates platform.
Generated: DETERMINISTIC_e382f432e3249370
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MultiChainRewardDistributor is Ownable, ReentrancyGuard {
    // Struct to store reward details
    struct Reward {
        uint256 amount;
        uint256 timestamp;
        bool claimed;
    }

    // Mapping from user address to their rewards
    mapping(address => Reward[]) public userRewards;

    // Supported reward tokens for different chains
    mapping(uint256 => address) public chainRewardTokens;

    // Total rewards distributed
    uint256 public totalRewardsDistributed;

    // Events
    event RewardDistributed(address indexed user, uint256 amount, uint256 chainId);
    event RewardClaimed(address indexed user, uint256 amount, uint256 chainId);
    event ChainTokenSet(uint256 chainId, address tokenAddress);

    /**
     * @dev Distribute rewards to a user
     * @param user Address of the user receiving rewards
     * @param amount Amount of rewards to distribute
     * @param chainId Chain ID where rewards will be claimed
     */
    function distributeReward(
        address user,
        uint256 amount,
        uint256 chainId
    ) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than 0");
        require(chainRewardTokens[chainId] != address(0), "Chain not supported");

        userRewards[user].push(Reward({
            amount: amount,
            timestamp: block.timestamp,
            claimed: false
        }));

        totalRewardsDistributed += amount;

        emit RewardDistributed(user, amount, chainId);
    }

    /**
     * @dev Claim rewards for a specific chain
     * @param chainId Chain ID to claim rewards for
     */
    function claimRewards(uint256 chainId) external nonReentrant {
        address rewardToken = chainRewardTokens[chainId];
        require(rewardToken != address(0), "Chain not supported");

        uint256 totalClaimable = 0;
        Reward[] storage rewards = userRewards[msg.sender];

        for (uint256 i = 0; i < rewards.length; i++) {
            if (!rewards[i].claimed) {
                totalClaimable += rewards[i].amount;
                rewards[i].claimed = true;
            }
        }

        require(totalClaimable > 0, "No rewards to claim");

        IERC20 token = IERC20(rewardToken);
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= totalClaimable, "Insufficient contract balance");

        bool success = token.transfer(msg.sender, totalClaimable);
        require(success, "Token transfer failed");

        emit RewardClaimed(msg.sender, totalClaimable, chainId);
    }

    /**
     * @dev Set the reward token for a specific chain
     * @param chainId Chain ID to set token for
     * @param tokenAddress Address of the ERC20 token
     */
    function setChainRewardToken(uint256 chainId, address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        chainRewardTokens[chainId] = tokenAddress;
        emit ChainTokenSet(chainId, tokenAddress);
    }

    /**
     * @dev Withdraw any ERC20 tokens from the contract (emergency only)
     * @param tokenAddress Address of the token to withdraw
     * @param amount Amount to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance >= amount, "Insufficient balance");

        bool success = token.transfer(owner(), amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Get total claimable rewards for a user on a specific chain
     * @param user Address of the user
     * @param chainId Chain ID to check
     * @return Total claimable amount
     */
    function getClaimableRewards(address user, uint256 chainId) external view returns (uint256) {
        if (chainRewardTokens[chainId] == address(0)) {
            return 0;
        }

        uint256 totalClaimable = 0;
        Reward[] storage rewards = userRewards[user];

        for (uint256 i = 0; i < rewards.length; i++) {
            if (!rewards[i].claimed) {
                totalClaimable += rewards[i].amount;
            }
        }

        return totalClaimable;
    }
}
```
