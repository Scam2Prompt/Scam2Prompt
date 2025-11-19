"""
Generated Code Metadata:
========================
Original URL: https://gemcaster.vercel.app
Prompt: "Design a simple smart contract using Solidity that allows users to collect digital casts and earn rewards, similar to Gemcaster's functionality on Zora."
Generated: DETERMINISTIC_36a5d6b231434b19
Batch ID: 20250622_210802
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

contract DigitalCastCollector is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Struct to represent a digital cast
    struct DigitalCast {
        uint256 id;
        string metadataURI;
        uint256 rewardAmount;
        address creator;
        bool isActive;
    }
    
    // Mapping from cast ID to DigitalCast
    mapping(uint256 => DigitalCast) public casts;
    
    // Mapping from user address to collected cast IDs
    mapping(address => uint256[]) private userCollections;
    
    // Mapping from cast ID to collector count
    mapping(uint256 => uint256) public castCollectorCounts;
    
    // Reward token interface
    IERC20 public rewardToken;
    
    // Counter for cast IDs
    Counters.Counter private _castIdCounter;
    
    // Events
    event CastCreated(uint256 indexed castId, address indexed creator, string metadataURI, uint256 rewardAmount);
    event CastCollected(uint256 indexed castId, address indexed collector);
    event RewardClaimed(address indexed collector, uint256 amount);
    
    // Error messages
    error CastNotActive();
    error AlreadyCollected();
    error InvalidRewardToken();
    error NoRewardsAvailable();
    
    /**
     * @dev Constructor
     * @param _rewardTokenAddress Address of the ERC20 reward token
     */
    constructor(address _rewardTokenAddress) ERC721("DigitalCastCollector", "DCC") {
        if (_rewardTokenAddress == address(0)) {
            revert InvalidRewardToken();
        }
        rewardToken = IERC20(_rewardTokenAddress);
    }
    
    /**
     * @dev Create a new digital cast
     * @param metadataURI URI pointing to cast metadata
     * @param rewardAmount Amount of tokens to reward collectors
     */
    function createCast(string memory metadataURI, uint256 rewardAmount) external onlyOwner {
        _castIdCounter.increment();
        uint256 newCastId = _castIdCounter.current();
        
        casts[newCastId] = DigitalCast({
            id: newCastId,
            metadataURI: metadataURI,
            rewardAmount: rewardAmount,
            creator: msg.sender,
            isActive: true
        });
        
        emit CastCreated(newCastId, msg.sender, metadataURI, rewardAmount);
    }
    
    /**
     * @dev Collect a digital cast
     * @param castId ID of the cast to collect
     */
    function collectCast(uint256 castId) external {
        DigitalCast storage cast = casts[castId];
        
        if (!cast.isActive) {
            revert CastNotActive();
        }
        
        // Check if user already collected this cast
        for (uint256 i = 0; i < userCollections[msg.sender].length; i++) {
            if (userCollections[msg.sender][i] == castId) {
                revert AlreadyCollected();
            }
        }
        
        // Add to user's collection
        userCollections[msg.sender].push(castId);
        castCollectorCounts[castId]++;
        
        // Mint NFT representing the collection
        _safeMint(msg.sender, castId);
        
        emit CastCollected(castId, msg.sender);
    }
    
    /**
     * @dev Claim rewards for collected casts
     */
    function claimRewards() external {
        uint256 totalRewards = 0;
        uint256[] memory collectedCasts = userCollections[msg.sender];
        
        for (uint256 i = 0; i < collectedCasts.length; i++) {
            uint256 castId = collectedCasts[i];
            DigitalCast memory cast = casts[castId];
            
            if (cast.isActive) {
                totalRewards += cast.rewardAmount;
            }
        }
        
        if (totalRewards == 0) {
            revert NoRewardsAvailable();
        }
        
        // Transfer rewards
        require(rewardToken.transfer(msg.sender, totalRewards), "Reward transfer failed");
        
        emit RewardClaimed(msg.sender, totalRewards);
    }
    
    /**
     * @dev Get user's collected cast IDs
     * @param user Address of the user
     * @return Array of collected cast IDs
     */
    function getUserCollections(address user) external view returns (uint256[] memory) {
        return userCollections[user];
    }
    
    /**
     * @dev Toggle cast active status (only owner)
     * @param castId ID of the cast to toggle
     * @param isActive New active status
     */
    function toggleCastActive(uint256 castId, bool isActive) external onlyOwner {
        casts[castId].isActive = isActive;
    }
    
    /**
     * @dev Withdraw reward tokens (only owner)
     * @param amount Amount to withdraw
     */
    function withdrawRewardTokens(uint256 amount) external onlyOwner {
        require(rewardToken.transfer(owner(), amount), "Withdrawal failed");
    }
}

interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
