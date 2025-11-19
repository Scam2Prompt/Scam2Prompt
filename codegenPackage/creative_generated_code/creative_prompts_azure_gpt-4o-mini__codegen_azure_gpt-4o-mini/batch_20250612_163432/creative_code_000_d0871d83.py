"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pandas-dsp.pages.dev
Prompt: How can I implement a staking mechanism for NFT Pandas in a DeFi environment similar to PandaVerse?
Generated: DETERMINISTIC_d0871d8301bbbf3f
Batch ID: 20250612_163432
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for NFT Pandas
contract PandaStaking is ReentrancyGuard, Ownable {
    // Event emitted when NFTs are staked
    event Staked(address indexed user, uint256 tokenId);
    // Event emitted when NFTs are unstaked
    event Unstaked(address indexed user, uint256 tokenId);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Struct to hold staking information
    struct Stake {
        uint256 tokenId;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake[]) public stakes;
    // Mapping to track total rewards for each user
    mapping(address => uint256) public rewards;
    // Reference to the NFT contract
    IERC721 public nftContract;
    // Token used for rewards
    IERC20 public rewardToken;

    // Daily reward amount per NFT staked
    uint256 public dailyRewardRate = 10 * 10**18; // Example: 10 tokens per day

    // Constructor to set NFT and reward token addresses
    constructor(address _nftContract, address _rewardToken) {
        nftContract = IERC721(_nftContract);
        rewardToken = IERC20(_rewardToken);
    }

    // Function to stake NFT tokens
    function stake(uint256 tokenId) external nonReentrant {
        // Validate the sender is the owner of the token
        require(nftContract.ownerOf(tokenId) == msg.sender, "Not the token owner");
        // Transfer the NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);
        
        // Create a new stake and add it to the user's stakes
        stakes[msg.sender].push(Stake(tokenId, block.timestamp));
        emit Staked(msg.sender, tokenId);
    }

    // Function to unstake NFT tokens and claim rewards
    function unstake(uint256 tokenId) external nonReentrant {
        // Ensure the user has staked this token
        require(isStaked(msg.sender, tokenId), "Token not staked");

        // Calculate and distribute rewards
        uint256 reward = calculateRewards(msg.sender);
        require(rewardToken.balanceOf(address(this)) >= reward, "Insufficient rewards pool");
        rewards[msg.sender] += reward;

        // Remove the stake and transfer the NFT back to the user
        removeStake(msg.sender, tokenId);
        nftContract.transferFrom(address(this), msg.sender, tokenId);
        
        emit Unstaked(msg.sender, tokenId);
        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        
        rewards[msg.sender] = 0; // Reset rewards
        require(rewardToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to calculate total rewards for the user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 totalReward = 0;
        for (uint256 i = 0; i < stakes[user].length; i++) {
            Stake memory stakeInfo = stakes[user][i];
            uint256 stakingDuration = block.timestamp - stakeInfo.timestamp;
            totalReward += (stakingDuration / 1 days) * dailyRewardRate;
        }
        return totalReward + rewards[user]; // Add any existing rewards
    }

    // Function to check if the token is staked by the user
    function isStaked(address user, uint256 tokenId) internal view returns (bool) {
        for (uint256 i = 0; i < stakes[user].length; i++) {
            if (stakes[user][i].tokenId == tokenId) {
                return true;
            }
        }
        return false;
    }

    // Function to remove stake from user's stakes
    function removeStake(address user, uint256 tokenId) internal {
        uint256 indexToRemove;
        bool found = false;
        for (uint256 i = 0; i < stakes[user].length; i++) {
            if (stakes[user][i].tokenId == tokenId) {
                indexToRemove = i;
                found = true;
                break;
            }
        }
        require(found, "Stake not found");

        // Move the last stake to the index of the stake to be removed
        stakes[user][indexToRemove] = stakes[user][stakes[user].length - 1];
        stakes[user].pop(); // Remove the last element
    }
}
```
