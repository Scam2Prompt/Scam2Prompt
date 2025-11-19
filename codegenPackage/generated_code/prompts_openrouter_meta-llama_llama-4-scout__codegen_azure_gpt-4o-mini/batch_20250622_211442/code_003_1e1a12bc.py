"""
Generated Code Metadata:
========================
Original URL: https://pandas-dsp.pages.dev
Prompt: "Generate a smart contract code for NFT staking and reward distribution, using a platform like Ethereum or Binance Smart Chain."
Generated: DETERMINISTIC_1e1a12bc94871554
Batch ID: 20250622_211442
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

// Importing OpenZeppelin contracts for ERC721 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the NFT contract
interface INFT is IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}

// Staking contract for NFT staking and reward distribution
contract NFTStaking is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 tokenId;
        uint256 timestamp;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake[]) public stakes;

    // Mapping to track total rewards for each user
    mapping(address => uint256) public rewards;

    // The NFT contract address
    INFT public nftContract;

    // Reward rate per second
    uint256 public rewardRate = 1e18; // 1 token per second

    // Event emitted when an NFT is staked
    event Staked(address indexed user, uint256 indexed tokenId, uint256 timestamp);

    // Event emitted when an NFT is unstaked
    event Unstaked(address indexed user, uint256 indexed tokenId, uint256 reward);

    // Constructor to set the NFT contract address
    constructor(address _nftContract) {
        nftContract = INFT(_nftContract);
    }

    // Function to stake an NFT
    function stake(uint256 tokenId) external {
        // Ensure the caller is the owner of the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        
        // Transfer the NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Record the stake
        stakes[msg.sender].push(Stake(tokenId, block.timestamp));

        // Emit the Staked event
        emit Staked(msg.sender, tokenId, block.timestamp);
    }

    // Function to unstake an NFT and claim rewards
    function unstake(uint256 tokenId) external {
        // Find the stake
        Stake[] storage userStakes = stakes[msg.sender];
        uint256 stakeIndex = findStakeIndex(userStakes, tokenId);
        
        // Ensure the stake exists
        require(stakeIndex < userStakes.length, "Stake not found");

        // Calculate rewards
        uint256 reward = calculateReward(userStakes[stakeIndex].timestamp);
        rewards[msg.sender] += reward;

        // Remove the stake
        userStakes[stakeIndex] = userStakes[userStakes.length - 1];
        userStakes.pop();

        // Transfer the NFT back to the user
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        // Emit the Unstaked event
        emit Unstaked(msg.sender, tokenId, reward);
    }

    // Function to calculate rewards based on the staking duration
    function calculateReward(uint256 stakeTimestamp) internal view returns (uint256) {
        return (block.timestamp - stakeTimestamp) * rewardRate;
    }

    // Function to find the index of a stake
    function findStakeIndex(Stake[] storage userStakes, uint256 tokenId) internal view returns (uint256) {
        for (uint256 i = 0; i < userStakes.length; i++) {
            if (userStakes[i].tokenId == tokenId) {
                return i;
            }
        }
        revert("Stake not found");
    }

    // Function to withdraw accumulated rewards
    function withdrawRewards() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to withdraw");

        // Reset the user's rewards
        rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        // Assuming the contract has a function to mint or transfer tokens
        // This part should be implemented based on the reward token logic
        // rewardToken.transfer(msg.sender, reward);
    }

    // Function to set the reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
