"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mega-rabbit.com
Prompt: Generate code for a staking mechanism in Solidity that allows users to stake their MegaRabbit NFTs and earn rewards.
Generated: DETERMINISTIC_f62d3ca7bd1bf9bb
Batch ID: 20250612_153854
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

// Importing ERC721 interface for the MegaRabbit NFTs
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MegaRabbitStaking is Ownable {
    // Struct to hold staking information for each NFT
    struct Stake {
        uint256 tokenId;
        address owner;
        uint256 timestamp;
    }

    // Mapping from token ID to its stake details
    mapping(uint256 => Stake) public stakes;

    // Mapping from owner address to an array of staked token IDs
    mapping(address => uint256[]) private ownerToStakedTokens;

    // Address of the MegaRabbit NFT contract
    IERC721 public megaRabbitNFT;

    // Reward rate per second for staked tokens
    uint256 public rewardRate;

    // Events to log staking and unstaking
    event Staked(address indexed owner, uint256 indexed tokenId, uint256 timestamp);
    event Unstaked(address indexed owner, uint256 indexed tokenId, uint256 reward);

    // Constructor to set the NFT contract address and reward rate
    constructor(IERC721 _megaRabbitNFT, uint256 _rewardRate) {
        megaRabbitNFT = _megaRabbitNFT;
        rewardRate = _rewardRate;
    }

    // Function to stake a MegaRabbit NFT
    function stake(uint256 tokenId) external {
        // Ensure the caller owns the token and it is approved for staking
        require(megaRabbitNFT.ownerOf(tokenId) == msg.sender, "You do not own this token.");
        require(megaRabbitNFT.getApproved(tokenId) == address(this) || megaRabbitNFT.isApprovedForAll(msg.sender, address(this)), "NFT not approved for staking.");

        // Stake the token
        stakes[tokenId] = Stake({
            tokenId: tokenId,
            owner: msg.sender,
            timestamp: block.timestamp
        });

        // Add the token to the owner's staked tokens
        ownerToStakedTokens[msg.sender].push(tokenId);

        // Transfer the NFT to the staking contract
        megaRabbitNFT.transferFrom(msg.sender, address(this), tokenId);

        emit Staked(msg.sender, tokenId, block.timestamp);
    }

    // Function to unstake a MegaRabbit NFT and claim rewards
    function unstake(uint256 tokenId) external {
        // Ensure the caller is the owner of the staked token
        require(stakes[tokenId].owner == msg.sender, "You do not own this staked token.");

        // Calculate rewards
        uint256 rewards = calculateRewards(tokenId);

        // Remove the stake from the mapping
        delete stakes[tokenId];

        // Remove the token from the owner's staked tokens
        uint256 index = findTokenIndex(msg.sender, tokenId);
        require(index < ownerToStakedTokens[msg.sender].length, "Token not found in staked tokens.");
        ownerToStakedTokens[msg.sender][index] = ownerToStakedTokens[msg.sender][ownerToStakedTokens[msg.sender].length - 1];
        ownerToStakedTokens[msg.sender].pop();

        // Transfer the NFT back to the owner
        megaRabbitNFT.transferFrom(address(this), msg.sender, tokenId);

        // Transfer rewards to the owner (Replace with actual reward distribution logic)
        // Example: payable(msg.sender).transfer(rewards); // Uncomment if using Ether as rewards

        emit Unstaked(msg.sender, tokenId, rewards);
    }

    // Function to calculate rewards for a given token ID
    function calculateRewards(uint256 tokenId) public view returns (uint256) {
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.owner != address(0), "Stake does not exist.");

        uint256 stakingDuration = block.timestamp - stakeInfo.timestamp;
        return stakingDuration * rewardRate; // Adjust reward calculation as needed
    }

    // Internal function to find the index of a token in the owner's staked tokens
    function findTokenIndex(address owner, uint256 tokenId) internal view returns (uint256) {
        uint256[] memory stakedTokens = ownerToStakedTokens[owner];
        for (uint256 i = 0; i < stakedTokens.length; i++) {
            if (stakedTokens[i] == tokenId) {
                return i;
            }
        }
        revert("Token not found in owner's staked tokens.");
    }

    // Function to change the reward rate (only owner can change)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }
    
    // Function to get staked tokens of an owner
    function getStakedTokens(address owner) external view returns (uint256[] memory) {
        return ownerToStakedTokens[owner];
    }
}
```
