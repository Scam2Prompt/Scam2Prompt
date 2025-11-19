"""
Generated Code Metadata:
========================
Original URL: https://bafybeig2qxervlifeg5gur3hrsbgo6hrco4esjxaz2r6nixoqkc6nhhjbe.ipfs.dweb.link
Prompt: Design a system to integrate Pencils Protocol's community points system with a decentralized application (dApp) built on Scroll.
Generated: DETERMINISTIC_61483204ac3c7901
Batch ID: 20250622_205111
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PencilsCommunityPoints
 * @dev A contract to manage community points integration between Pencils Protocol and Scroll dApps
 */
contract PencilsCommunityPoints is Ownable, ReentrancyGuard {
    // The Pencils Protocol community points token
    IERC20 public pencilsToken;

    // Mapping to track user points in the dApp
    mapping(address => uint256) public userPoints;

    // Mapping to track claimed rewards
    mapping(address => mapping(uint256 => bool)) public hasClaimedReward;

    // Events
    event PointsEarned(address indexed user, uint256 amount);
    event PointsSpent(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 rewardId);
    event TokensDeposited(address indexed depositor, uint256 amount);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor
     * @param _pencilsTokenAddress The address of the Pencils Protocol token
     */
    constructor(address _pencilsTokenAddress) {
        require(_pencilsTokenAddress != address(0), "Invalid token address");
        pencilsToken = IERC20(_pencilsTokenAddress);
    }

    /**
     * @dev Deposit Pencils tokens to the contract
     * @param amount The amount of tokens to deposit
     */
    function depositTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(
            pencilsToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );
        emit TokensDeposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw Pencils tokens from the contract
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(
            pencilsToken.balanceOf(address(this)) >= amount,
            "Insufficient contract balance"
        );
        require(
            pencilsToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );
        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Award points to a user for dApp interactions
     * @param user The address of the user to award points to
     * @param amount The amount of points to award
     */
    function earnPoints(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than 0");
        
        userPoints[user] += amount;
        emit PointsEarned(user, amount);
    }

    /**
     * @dev Spend user points for dApp features
     * @param amount The amount of points to spend
     */
    function spendPoints(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(userPoints[msg.sender] >= amount, "Insufficient points");

        userPoints[msg.sender] -= amount;
        emit PointsSpent(msg.sender, amount);
    }

    /**
     * @dev Claim a reward by spending points
     * @param rewardId The ID of the reward to claim
     * @param pointsCost The points cost of the reward
     */
    function claimReward(uint256 rewardId, uint256 pointsCost) external nonReentrant {
        require(!hasClaimedReward[msg.sender][rewardId], "Reward already claimed");
        require(userPoints[msg.sender] >= pointsCost, "Insufficient points");

        userPoints[msg.sender] -= pointsCost;
        hasClaimedReward[msg.sender][rewardId] = true;

        emit RewardClaimed(msg.sender, rewardId);
    }

    /**
     * @dev Get a user's point balance
     * @param user The address of the user
     * @return The user's point balance
     */
    function getUserPoints(address user) external view returns (uint256) {
        return userPoints[user];
    }

    /**
     * @dev Check if a user has claimed a specific reward
     * @param user The address of the user
     * @param rewardId The ID of the reward
     * @return True if the user has claimed the reward, false otherwise
     */
    function hasUserClaimedReward(address user, uint256 rewardId) external view returns (bool) {
        return hasClaimedReward[user][rewardId];
    }

    /**
     * @dev Get the contract's Pencils token balance
     * @return The contract's token balance
     */
    function getContractTokenBalance() external view returns (uint256) {
        return pencilsToken.balanceOf(address(this));
    }
}
```
