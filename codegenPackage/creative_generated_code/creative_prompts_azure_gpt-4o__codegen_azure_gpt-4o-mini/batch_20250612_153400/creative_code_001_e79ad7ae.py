"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://merlion.pages.dev
Prompt: Generate a Solidity smart contract for staking NFTs in the Merlin ecosystem, incorporating features like reward distribution based on Star Points.
Generated: DETERMINISTIC_e79ad7ae4d019a71
Batch ID: 20250612_153400
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

interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function transferFrom(address from, address to, uint256 tokenId) external;
    function balanceOf(address owner) external view returns (uint256);
}

/**
 * @title MerlinNFTStaking
 * @dev A smart contract for staking NFTs in the Merlin ecosystem while distributing rewards based on Star Points.
 */
contract MerlinNFTStaking {
    struct Stake {
        uint256 tokenId;
        address owner;
        uint256 startTime;
    }

    IERC721 public nftContract;
    mapping(address => Stake[]) public stakedTokens;
    mapping(address => uint256) public starPoints;
    mapping(uint256 => uint256) public tokenStarPoints; // Token ID to Star Points mapping
    uint256 public rewardRate = 1; // Reward rate per staked NFT per day

    event Staked(address indexed user, uint256 indexed tokenId);
    event Unstaked(address indexed user, uint256 indexed tokenId, uint256 reward);
    event RewardDistributed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the NFT contract address.
     * @param _nftContract The address of the NFT contract.
     */
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = IERC721(_nftContract);
    }

    /**
     * @dev Stake an NFT by its tokenId.
     * @param tokenId The ID of the token to be staked.
     */
    function stake(uint256 tokenId) external {
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this token");
        
        // Transfer the NFT to the contract for staking
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Create a new stake
        stakedTokens[msg.sender].push(Stake(tokenId, msg.sender, block.timestamp));
        emit Staked(msg.sender, tokenId);
    }

    /**
     * @dev Unstake an NFT and claim rewards.
     * @param tokenId The ID of the token to be unstaked.
     */
    function unstake(uint256 tokenId) external {
        Stake[] storage stakes = stakedTokens[msg.sender];
        uint256 reward = 0;
        bool found = false;

        for (uint256 i = 0; i < stakes.length; i++) {
            if (stakes[i].tokenId == tokenId) {
                // Calculate the reward based on time staked
                reward = calculateReward(stakes[i].startTime);
                // Remove the stake
                stakes[i] = stakes[stakes.length - 1];
                stakes.pop();
                found = true;
                break;
            }
        }

        require(found, "Token not staked");

        // Transfer the NFT back to the user
        nftContract.transferFrom(address(this), msg.sender, tokenId);
        // Distribute the reward
        starPoints[msg.sender] += reward;
        emit Unstaked(msg.sender, tokenId, reward);
    }

    /**
     * @dev Calculate the reward based on the time staked.
     * @param startTime The timestamp when the NFT was staked.
     * @return The calculated reward amount.
     */
    function calculateReward(uint256 startTime) internal view returns (uint256) {
        uint256 duration = block.timestamp - startTime;
        return (duration / 1 days) * rewardRate;
    }

    /**
     * @dev Get the total Star Points of a user.
     * @param user The address of the user.
     * @return The total Star Points of the user.
     */
    function getStarPoints(address user) external view returns (uint256) {
        return starPoints[user];
    }

    /**
     * @dev Get the staked NFTs of a user.
     * @param user The address of the user.
     * @return An array of staked token IDs.
     */
    function getStakedTokens(address user) external view returns (uint256[] memory) {
        Stake[] memory stakes = stakedTokens[user];
        uint256[] memory tokenIds = new uint256[](stakes.length);
        
        for (uint256 i = 0; i < stakes.length; i++) {
            tokenIds[i] = stakes[i].tokenId;
        }
        return tokenIds;
    }
}
```
