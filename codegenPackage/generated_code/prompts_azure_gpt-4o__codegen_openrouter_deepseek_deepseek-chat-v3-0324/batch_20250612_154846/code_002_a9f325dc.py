"""
Generated Code Metadata:
========================
Original URL: https://nft-rewards.online
Prompt: Generate a smart contract in Solidity for distributing NFT-based rewards to users based on specific criteria, such as activity level or milestones.
Generated: DETERMINISTIC_a9f325dc2249652f
Batch ID: 20250612_154846
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

contract NFTRewardDistributor is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to store user activity data
    struct UserActivity {
        uint256 points;
        uint256 lastActivityTimestamp;
        bool isActive;
    }

    // Mapping from user address to activity data
    mapping(address => UserActivity) public userActivities;

    // Reward thresholds and corresponding token URIs
    mapping(uint256 => string) public rewardTiers;
    uint256[] public tierThresholds;

    // Events
    event ActivityRecorded(address indexed user, uint256 points);
    event RewardClaimed(address indexed user, uint256 tokenId, uint256 tier);

    constructor(
        string memory name,
        string memory symbol,
        uint256[] memory thresholds,
        string[] memory tokenURIs
    ) ERC721(name, symbol) {
        require(thresholds.length == tokenURIs.length, "Mismatched input lengths");
        
        // Initialize reward tiers
        for (uint256 i = 0; i < thresholds.length; i++) {
            rewardTiers[thresholds[i]] = tokenURIs[i];
            tierThresholds.push(thresholds[i]);
        }
    }

    /**
     * @dev Records user activity and updates their points
     * @param user Address of the user
     * @param points Points to add to the user's activity
     */
    function recordActivity(address user, uint256 points) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(points > 0, "Points must be positive");

        UserActivity storage activity = userActivities[user];
        activity.points += points;
        activity.lastActivityTimestamp = block.timestamp;
        activity.isActive = true;

        emit ActivityRecorded(user, points);
    }

    /**
     * @dev Allows a user to claim their NFT reward if they meet the criteria
     */
    function claimReward() external {
        address user = msg.sender;
        UserActivity storage activity = userActivities[user];
        require(activity.isActive, "User is not active");

        uint256 eligibleTier = 0;
        for (uint256 i = 0; i < tierThresholds.length; i++) {
            if (activity.points >= tierThresholds[i]) {
                eligibleTier = tierThresholds[i];
            } else {
                break;
            }
        }

        require(eligibleTier > 0, "No eligible reward tier");
        require(balanceOf(user) == 0, "Already claimed a reward");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(user, tokenId);
        _setTokenURI(tokenId, rewardTiers[eligibleTier]);

        emit RewardClaimed(user, tokenId, eligibleTier);
    }

    /**
     * @dev Sets the token URI for a specific tier
     * @param threshold The threshold for the tier
     * @param tokenURI The URI for the NFT metadata
     */
    function setRewardTier(uint256 threshold, string memory tokenURI) external onlyOwner {
        require(bytes(tokenURI).length > 0, "Empty token URI");
        rewardTiers[threshold] = tokenURI;
        
        // Add to thresholds if not already present
        bool exists = false;
        for (uint256 i = 0; i < tierThresholds.length; i++) {
            if (tierThresholds[i] == threshold) {
                exists = true;
                break;
            }
        }
        if (!exists) {
            tierThresholds.push(threshold);
            // Keep thresholds sorted
            for (uint256 i = tierThresholds.length - 1; i > 0; i--) {
                if (tierThresholds[i] < tierThresholds[i - 1]) {
                    (tierThresholds[i], tierThresholds[i - 1]) = (tierThresholds[i - 1], tierThresholds[i]);
                }
            }
        }
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId The ID of the token
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return super.tokenURI(tokenId);
    }

    /**
     * @dev Withdraws any ETH accidentally sent to the contract
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
