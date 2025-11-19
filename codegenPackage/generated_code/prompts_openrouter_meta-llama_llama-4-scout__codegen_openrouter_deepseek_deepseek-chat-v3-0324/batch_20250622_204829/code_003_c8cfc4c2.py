"""
Generated Code Metadata:
========================
Original URL: https://paraxweb3dapp.pages.dev
Prompt: Develop a smart contract function to enable NFT token staking on ParaX, using Chainlink as the oracle for floor price calculations and supporting multiple NFT collections.
Generated: DETERMINISTIC_c8cfc4c2be7a7a33
Batch ID: 20250622_204829
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract ParaXNFTStaking is ReentrancyGuard, Ownable {
    // Struct to store staking information
    struct StakedNFT {
        address owner;
        uint256 tokenId;
        uint256 stakedAt;
        address collection;
    }

    // Mapping from collection to Chainlink price feed
    mapping(address => address) public collectionPriceFeeds;

    // Mapping from token ID to staking details
    mapping(uint256 => StakedNFT) public stakedNFTs;

    // Mapping from collection to staking rewards rate (per second)
    mapping(address => uint256) public rewardRates;

    // Mapping from user to total staked value
    mapping(address => uint256) public userStakedValue;

    // Events
    event NFTStaked(address indexed owner, address indexed collection, uint256 tokenId, uint256 timestamp);
    event NFTUnstaked(address indexed owner, address indexed collection, uint256 tokenId, uint256 reward, uint256 timestamp);
    event RewardClaimed(address indexed owner, uint256 amount, uint256 timestamp);
    event CollectionAdded(address indexed collection, address priceFeed, uint256 rewardRate);
    event CollectionRemoved(address indexed collection);

    constructor() {}

    /**
     * @dev Add a new NFT collection for staking
     * @param collection Address of the NFT collection
     * @param priceFeed Chainlink price feed address for floor price
     * @param rewardRate Reward rate per second (in wei)
     */
    function addCollection(address collection, address priceFeed, uint256 rewardRate) external onlyOwner {
        require(collection != address(0), "Invalid collection address");
        require(priceFeed != address(0), "Invalid price feed address");
        require(rewardRate > 0, "Reward rate must be positive");

        collectionPriceFeeds[collection] = priceFeed;
        rewardRates[collection] = rewardRate;

        emit CollectionAdded(collection, priceFeed, rewardRate);
    }

    /**
     * @dev Remove an NFT collection from staking
     * @param collection Address of the NFT collection to remove
     */
    function removeCollection(address collection) external onlyOwner {
        require(collectionPriceFeeds[collection] != address(0), "Collection not found");

        delete collectionPriceFeeds[collection];
        delete rewardRates[collection];

        emit CollectionRemoved(collection);
    }

    /**
     * @dev Stake an NFT
     * @param collection Address of the NFT collection
     * @param tokenId ID of the NFT to stake
     */
    function stakeNFT(address collection, uint256 tokenId) external nonReentrant {
        require(collectionPriceFeeds[collection] != address(0), "Collection not supported");
        
        IERC721 nft = IERC721(collection);
        require(nft.ownerOf(tokenId) == msg.sender, "Not the owner");
        
        nft.transferFrom(msg.sender, address(this), tokenId);

        uint256 floorPrice = getFloorPrice(collection);
        require(floorPrice > 0, "Invalid floor price");

        stakedNFTs[tokenId] = StakedNFT({
            owner: msg.sender,
            tokenId: tokenId,
            stakedAt: block.timestamp,
            collection: collection
        });

        userStakedValue[msg.sender] += floorPrice;

        emit NFTStaked(msg.sender, collection, tokenId, block.timestamp);
    }

    /**
     * @dev Unstake an NFT and claim rewards
     * @param tokenId ID of the NFT to unstake
     */
    function unstakeNFT(uint256 tokenId) external nonReentrant {
        StakedNFT memory stakedNFT = stakedNFTs[tokenId];
        require(stakedNFT.owner == msg.sender, "Not the staker");

        uint256 floorPrice = getFloorPrice(stakedNFT.collection);
        uint256 stakingDuration = block.timestamp - stakedNFT.stakedAt;
        uint256 reward = stakingDuration * rewardRates[stakedNFT.collection];

        IERC721(stakedNFT.collection).transferFrom(address(this), msg.sender, tokenId);

        userStakedValue[msg.sender] -= floorPrice;
        delete stakedNFTs[tokenId];

        // In a production environment, you would transfer the reward tokens here
        // For simplicity, we're just emitting the reward amount
        emit NFTUnstaked(msg.sender, stakedNFT.collection, tokenId, reward, block.timestamp);
    }

    /**
     * @dev Get the current floor price of an NFT collection from Chainlink
     * @param collection Address of the NFT collection
     * @return floorPrice Current floor price in wei
     */
    function getFloorPrice(address collection) public view returns (uint256) {
        address priceFeed = collectionPriceFeeds[collection];
        require(priceFeed != address(0), "Price feed not found");

        AggregatorV3Interface aggregator = AggregatorV3Interface(priceFeed);
        (, int256 price,,,) = aggregator.latestRoundData();
        require(price > 0, "Invalid price");

        return uint256(price);
    }

    /**
     * @dev Calculate pending rewards for a staked NFT
     * @param tokenId ID of the staked NFT
     * @return reward Pending reward amount in wei
     */
    function calculateReward(uint256 tokenId) public view returns (uint256) {
        StakedNFT memory stakedNFT = stakedNFTs[tokenId];
        if (stakedNFT.owner == address(0)) return 0;

        uint256 stakingDuration = block.timestamp - stakedNFT.stakedAt;
        return stakingDuration * rewardRates[stakedNFT.collection];
    }

    /**
     * @dev Calculate total pending rewards for a user
     * @param user Address of the user
     * @return totalReward Total pending reward amount in wei
     */
    function calculateTotalRewards(address user) external view returns (uint256 totalReward) {
        // In a production implementation, you would iterate through all staked NFTs
        // For simplicity, we're returning the total staked value multiplied by a base rate
        // This is a placeholder implementation
        return userStakedValue[user] * 1e16; // 1% reward rate for demonstration
    }
}
```
