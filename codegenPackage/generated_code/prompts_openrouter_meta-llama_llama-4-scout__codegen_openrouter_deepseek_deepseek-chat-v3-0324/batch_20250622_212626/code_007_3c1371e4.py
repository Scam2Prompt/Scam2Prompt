"""
Generated Code Metadata:
========================
Original URL: https://sophan.xyz
Prompt: Develop a smart contract using Solidity that integrates with Sophon's distribution layer and loyalty program for rewarding users with exclusive experiences and digital collectibles.
Generated: DETERMINISTIC_3c1371e4d521c71e
Batch ID: 20250622_212626
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title SophonLoyaltyProgram
 * @dev Smart contract for Sophon's loyalty program that rewards users with
 * exclusive experiences and digital collectibles (NFTs).
 */
contract SophonLoyaltyProgram is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct Reward {
        uint256 id;
        string name;
        string description;
        uint256 pointsRequired;
        uint256 totalSupply;
        uint256 mintedCount;
        string tokenURI;
        bool isActive;
    }

    mapping(uint256 => Reward) public rewards;
    mapping(address => uint256) public userPoints;
    mapping(address => mapping(uint256 => bool)) public userRewardsClaimed;
    mapping(uint256 => string) private _tokenURIs;

    event PointsAdded(address indexed user, uint256 amount);
    event PointsSubtracted(address indexed user, uint256 amount);
    event RewardCreated(uint256 rewardId, string name, uint256 pointsRequired);
    event RewardClaimed(address indexed user, uint256 rewardId, uint256 tokenId);

    constructor() ERC721("SophonLoyaltyNFT", "SLNFT") {}

    /**
     * @dev Creates a new reward type
     */
    function createReward(
        string memory name,
        string memory description,
        uint256 pointsRequired,
        uint256 totalSupply,
        string memory tokenURI
    ) external onlyOwner {
        uint256 rewardId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        rewards[rewardId] = Reward({
            id: rewardId,
            name: name,
            description: description,
            pointsRequired: pointsRequired,
            totalSupply: totalSupply,
            mintedCount: 0,
            tokenURI: tokenURI,
            isActive: true
        });

        emit RewardCreated(rewardId, name, pointsRequired);
    }

    /**
     * @dev Toggles reward active status
     */
    function toggleRewardActive(uint256 rewardId) external onlyOwner {
        Reward storage reward = rewards[rewardId];
        reward.isActive = !reward.isActive;
    }

    /**
     * @dev Adds points to user's balance
     */
    function addPoints(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(amount > 0, "Amount must be positive");

        userPoints[user] += amount;
        emit PointsAdded(user, amount);
    }

    /**
     * @dev Subtracts points from user's balance
     */
    function subtractPoints(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(amount > 0, "Amount must be positive");
        require(userPoints[user] >= amount, "Insufficient points");

        userPoints[user] -= amount;
        emit PointsSubtracted(user, amount);
    }

    /**
     * @dev Allows user to claim a reward
     */
    function claimReward(uint256 rewardId) external nonReentrant {
        Reward storage reward = rewards[rewardId];
        require(reward.isActive, "Reward is not active");
        require(userPoints[msg.sender] >= reward.pointsRequired, "Insufficient points");
        require(!userRewardsClaimed[msg.sender][rewardId], "Reward already claimed");
        require(reward.mintedCount < reward.totalSupply, "Reward supply exhausted");

        userPoints[msg.sender] -= reward.pointsRequired;
        userRewardsClaimed[msg.sender][rewardId] = true;

        uint256 newTokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, reward.tokenURI);

        reward.mintedCount += 1;

        emit RewardClaimed(msg.sender, rewardId, newTokenId);
    }

    /**
     * @dev Returns the token URI for a given token ID
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Sets the token URI for a given token ID
     */
    function _setTokenURI(uint256 tokenId, string memory _tokenURI) internal virtual {
        require(_exists(tokenId), "ERC721Metadata: URI set of nonexistent token");
        _tokenURIs[tokenId] = _tokenURI;
    }

    /**
     * @dev Returns user's point balance
     */
    function getPointsBalance(address user) external view returns (uint256) {
        return userPoints[user];
    }

    /**
     * @dev Returns reward details
     */
    function getRewardDetails(uint256 rewardId) external view returns (Reward memory) {
        return rewards[rewardId];
    }

    /**
     * @dev Checks if user has claimed a specific reward
     */
    function hasUserClaimedReward(address user, uint256 rewardId) external view returns (bool) {
        return userRewardsClaimed[user][rewardId];
    }
}
```
