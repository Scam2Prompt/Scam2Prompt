"""
Generated Code Metadata:
========================
Original URL: https://mileimoneda.pages.dev
Prompt: Recommend blockchain-based solutions for implementing exclusive NFT rewards and gamification features, inspired by the $MEDA ecosystem described on the Milei Moneda site.
Generated: DETERMINISTIC_84d70918d450a2d7
Batch ID: 20250612_153401
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MileiMonedaNFT
 * @dev NFT contract for exclusive rewards and gamification features
 * Inspired by $MEDA ecosystem with tiered rewards and staking mechanics
 */
contract MileiMonedaNFT is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using SafeMath for uint256;

    Counters.Counter private _tokenIdCounter;

    // NFT Tier structure
    struct Tier {
        string name;
        uint256 price;
        uint256 maxSupply;
        uint256 currentSupply;
        string baseURI;
    }

    // User staking information
    struct StakingInfo {
        uint256 tokenId;
        uint256 stakedAt;
        uint256 lastClaimed;
    }

    // Reward rates per tier (per second)
    mapping(uint256 => uint256) public tierRewardRates;
    mapping(address => StakingInfo[]) public userStakes;
    mapping(uint256 => uint256) public tokenTier;

    Tier[] public tiers;
    string private _baseTokenURI;

    // Events
    event NFTMinted(address indexed owner, uint256 tokenId, uint256 tier);
    event Staked(address indexed user, uint256 tokenId);
    event Unstaked(address indexed user, uint256 tokenId);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        string memory baseURI
    ) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
        
        // Initialize default tiers (can be modified by owner)
        tiers.push(Tier("Bronze", 0.1 ether, 1000, 0, ""));
        tiers.push(Tier("Silver", 0.3 ether, 500, 0, ""));
        tiers.push(Tier("Gold", 1 ether, 100, 0, ""));
        
        // Set reward rates (per second)
        tierRewardRates[0] = 5787037; // ~0.5 MEDA per day for Bronze
        tierRewardRates[1] = 11574074; // ~1 MEDA per day for Silver
        tierRewardRates[2] = 57870370; // ~5 MEDA per day for Gold
    }

    /**
     * @dev Mint NFT of specified tier
     * @param tierIndex Index of the tier to mint
     */
    function mintNFT(uint256 tierIndex) external payable nonReentrant {
        require(tierIndex < tiers.length, "Invalid tier");
        Tier storage tier = tiers[tierIndex];
        
        require(msg.value >= tier.price, "Insufficient payment");
        require(tier.currentSupply < tier.maxSupply, "Tier sold out");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        tier.currentSupply++;
        
        _safeMint(msg.sender, tokenId);
        tokenTier[tokenId] = tierIndex;
        
        emit NFTMinted(msg.sender, tokenId, tierIndex);
    }

    /**
     * @dev Stake NFT to start earning rewards
     * @param tokenId ID of the NFT to stake
     */
    function stakeNFT(uint256 tokenId) external nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Not NFT owner");
        
        userStakes[msg.sender].push(StakingInfo({
            tokenId: tokenId,
            stakedAt: block.timestamp,
            lastClaimed: block.timestamp
        }));
        
        _transfer(msg.sender, address(this), tokenId);
        emit Staked(msg.sender, tokenId);
    }

    /**
     * @dev Unstake NFT and claim pending rewards
     * @param stakeIndex Index of the stake in user's stakes array
     */
    function unstakeNFT(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        
        StakingInfo memory stake = userStakes[msg.sender][stakeIndex];
        uint256 rewards = calculateRewards(msg.sender, stakeIndex);
        
        if (rewards > 0) {
            // In a real implementation, transfer MEDA tokens here
            emit RewardClaimed(msg.sender, rewards);
        }
        
        _transfer(address(this), msg.sender, stake.tokenId);
        
        // Remove stake from array
        userStakes[msg.sender][stakeIndex] = userStakes[msg.sender][userStakes[msg.sender].length - 1];
        userStakes[msg.sender].pop();
        
        emit Unstaked(msg.sender, stake.tokenId);
    }

    /**
     * @dev Claim rewards without unstaking
     * @param stakeIndex Index of the stake in user's stakes array
     */
    function claimRewards(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < userStakes[msg.sender].length, "Invalid stake index");
        
        StakingInfo storage stake = userStakes[msg.sender][stakeIndex];
        uint256 rewards = calculateRewards(msg.sender, stakeIndex);
        
        require(rewards > 0, "No rewards to claim");
        
        // In a real implementation, transfer MEDA tokens here
        stake.lastClaimed = block.timestamp;
        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate pending rewards for a stake
     * @param user Address of the staker
     * @param stakeIndex Index of the stake in user's stakes array
     * @return rewards Calculated reward amount
     */
    function calculateRewards(address user, uint256 stakeIndex) public view returns (uint256 rewards) {
        require(stakeIndex < userStakes[user].length, "Invalid stake index");
        
        StakingInfo memory stake = userStakes[user][stakeIndex];
        uint256 tier = tokenTier[stake.tokenId];
        uint256 timeStaked = block.timestamp.sub(stake.lastClaimed);
        
        rewards = timeStaked.mul(tierRewardRates[tier]);
        return rewards;
    }

    /**
     * @dev Add new tier (owner only)
     * @param name Tier name
     * @param price Mint price
     * @param maxSupply Maximum supply
     * @param baseURI Base metadata URI
     */
    function addTier(
        string memory name,
        uint256 price,
        uint256 maxSupply,
        string memory baseURI
    ) external onlyOwner {
        tiers.push(Tier(name, price, maxSupply, 0, baseURI));
        tierRewardRates[tiers.length - 1] = 0; // Owner must set reward rate separately
    }

    /**
     * @dev Set reward rate for tier (owner only)
     * @param tierIndex Tier index
     * @param rate Reward rate per second
     */
    function setRewardRate(uint256 tierIndex, uint256 rate) external onlyOwner {
        require(tierIndex < tiers.length, "Invalid tier");
        tierRewardRates[tierIndex] = rate;
    }

    /**
     * @dev Withdraw contract balance (owner only)
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Override base URI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Get all stakes for a user
     * @param user User address
     * @return Array of StakingInfo
     */
    function getUserStakes(address user) external view returns (StakingInfo[] memory) {
        return userStakes[user];
    }

    /**
     * @dev Get all tiers
     * @return Array of Tier structs
     */
    function getAllTiers() external view returns (Tier[] memory) {
        return tiers;
    }
}

/**
 * @title MockMEDAToken
 * @dev Mock token for testing rewards distribution
 */
contract MockMEDAToken {
    function transfer(address to, uint256 amount) public returns (bool) {
        // Implementation would transfer MEDA tokens
        return true;
    }
}
```
