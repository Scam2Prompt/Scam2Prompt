"""
Generated Code Metadata:
========================
Original URL: https://youroi.pages.dev
Prompt: "Generate a BRC-20 tokenization plan for content assets, incorporating AI-driven personalized product content and a smart reward mechanism, as described in YOUR Protocol's documentation."
Generated: DETERMINISTIC_fba2d63ad130aa46
Batch ID: 20250622_210348
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title ContentAssetToken
 * @dev BRC-20 style token for content assets with AI-driven personalization and reward mechanisms
 */
contract ContentAssetToken is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    struct ContentAsset {
        uint256 assetId;
        string metadataURI;
        address creator;
        uint256 creationTimestamp;
        uint256 rewardPool;
    }

    struct UserReward {
        uint256 lastInteraction;
        uint256 accumulatedRewards;
        uint256 claimedRewards;
    }

    mapping(uint256 => ContentAsset) public contentAssets;
    mapping(address => UserReward) public userRewards;
    mapping(address => mapping(uint256 => bool)) public userEngagement;

    uint256 public assetCounter;
    uint256 public rewardRate = 100; // Tokens per second per engagement
    uint256 public rewardDecay = 1 days;
    uint256 public maxRewardPerAsset = 1000 * 10**18;

    event AssetCreated(uint256 indexed assetId, address indexed creator, string metadataURI);
    event RewardClaimed(address indexed user, uint256 amount);
    event UserEngaged(address indexed user, uint256 indexed assetId);

    constructor() ERC20("ContentAssetToken", "CAT") {
        _mint(msg.sender, 1000000 * 10**18); // Initial supply
    }

    /**
     * @dev Create a new content asset
     * @param metadataURI URI pointing to AI-generated content metadata
     */
    function createContentAsset(string memory metadataURI) external whenNotPaused {
        assetCounter++;
        contentAssets[assetCounter] = ContentAsset({
            assetId: assetCounter,
            metadataURI: metadataURI,
            creator: msg.sender,
            creationTimestamp: block.timestamp,
            rewardPool: 0
        });
        emit AssetCreated(assetCounter, msg.sender, metadataURI);
    }

    /**
     * @dev Record user engagement with content asset
     * @param assetId ID of the content asset
     */
    function engageWithContent(uint256 assetId) external whenNotPaused {
        require(contentAssets[assetId].assetId != 0, "Asset does not exist");
        require(!userEngagement[msg.sender][assetId], "Already engaged with this asset");

        userEngagement[msg.sender][assetId] = true;
        _updateRewards(msg.sender);

        emit UserEngaged(msg.sender, assetId);
    }

    /**
     * @dev Calculate and claim accumulated rewards
     */
    function claimRewards() external whenNotPaused {
        _updateRewards(msg.sender);
        uint256 rewardsToClaim = userRewards[msg.sender].accumulatedRewards;
        require(rewardsToClaim > 0, "No rewards to claim");

        userRewards[msg.sender].accumulatedRewards = 0;
        userRewards[msg.sender].claimedRewards = userRewards[msg.sender].claimedRewards.add(rewardsToClaim);
        _mint(msg.sender, rewardsToClaim);

        emit RewardClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Internal function to update user rewards
     * @param user Address of the user to update rewards for
     */
    function _updateRewards(address user) internal {
        UserReward storage reward = userRewards[user];
        uint256 timeSinceLastInteraction = block.timestamp.sub(reward.lastInteraction);

        if (timeSinceLastInteraction > 0) {
            uint256 decayFactor = timeSinceLastInteraction > rewardDecay 
                ? rewardDecay 
                : timeSinceLastInteraction;
            uint256 newRewards = rewardRate.mul(decayFactor);

            if (newRewards > maxRewardPerAsset) {
                newRewards = maxRewardPerAsset;
            }

            reward.accumulatedRewards = reward.accumulatedRewards.add(newRewards);
        }

        reward.lastInteraction = block.timestamp;
    }

    /**
     * @dev Set reward parameters (owner only)
     * @param rate New reward rate per second
     * @param decay New reward decay period
     * @param max New maximum reward per asset
     */
    function setRewardParameters(uint256 rate, uint256 decay, uint256 max) external onlyOwner {
        rewardRate = rate;
        rewardDecay = decay;
        maxRewardPerAsset = max;
    }

    /**
     * @dev Pause contract functionality (owner only)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause contract functionality (owner only)
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Mint new tokens (owner only)
     * @param to Address to mint to
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }
}
```
