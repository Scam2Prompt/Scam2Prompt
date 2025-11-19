"""
Generated Code Metadata:
========================
Original URL: https://puffmypanda.pages.dev
Prompt: Create a staking protocol in Solidity for Puff Puff Pandas NFTs that allows holders to lock their NFTs and earn yield in $PUFFS tokens, as outlined in the Puff Like A Panda ecosystem.
Generated: DETERMINISTIC_cf5199279853e068
Batch ID: 20250612_152235
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for Puff Puff Pandas NFTs
contract PuffPuffPandasStaking is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 tokenId;
        uint256 timestamp;
    }

    // Mapping from user address to their stakes
    mapping(address => Stake[]) public stakes;

    // ERC721 NFT contract
    IERC721 public nftContract;
    // ERC20 token contract for $PUFFS
    IERC20 public rewardsToken;

    // Reward rate per second
    uint256 public rewardRate = 1e18; // 1 $PUFFS per second per NFT

    // Event emitted when an NFT is staked
    event Staked(address indexed user, uint256 indexed tokenId);
    // Event emitted when an NFT is unstaked
    event Unstaked(address indexed user, uint256 indexed tokenId);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the NFT and rewards token contracts
    constructor(IERC721 _nftContract, IERC20 _rewardsToken) {
        nftContract = _nftContract;
        rewardsToken = _rewardsToken;
    }

    // Function to stake an NFT
    function stake(uint256 tokenId) external {
        // Ensure the caller owns the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        // Transfer the NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);
        
        // Record the stake
        stakes[msg.sender].push(Stake(tokenId, block.timestamp));
        
        emit Staked(msg.sender, tokenId);
    }

    // Function to unstake an NFT
    function unstake(uint256 tokenId) external {
        // Ensure the user has staked this NFT
        require(isStaked(msg.sender, tokenId), "This NFT is not staked by you");
        
        // Calculate and distribute rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        if (rewards > 0) {
            rewardsToken.transfer(msg.sender, rewards);
            emit RewardsClaimed(msg.sender, rewards);
        }

        // Remove the stake
        removeStake(msg.sender, tokenId);
        // Transfer the NFT back to the user
        nftContract.transferFrom(address(this), msg.sender, tokenId);
        
        emit Unstaked(msg.sender, tokenId);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 totalRewards = 0;
        for (uint256 i = 0; i < stakes[user].length; i++) {
            Stake memory stakeInfo = stakes[user][i];
            uint256 stakedDuration = block.timestamp - stakeInfo.timestamp;
            totalRewards += stakedDuration * rewardRate;
        }
        return totalRewards;
    }

    // Function to check if a specific NFT is staked by a user
    function isStaked(address user, uint256 tokenId) internal view returns (bool) {
        for (uint256 i = 0; i < stakes[user].length; i++) {
            if (stakes[user][i].tokenId == tokenId) {
                return true;
            }
        }
        return false;
    }

    // Function to remove a stake from the user's stakes
    function removeStake(address user, uint256 tokenId) internal {
        uint256 length = stakes[user].length;
        for (uint256 i = 0; i < length; i++) {
            if (stakes[user][i].tokenId == tokenId) {
                stakes[user][i] = stakes[user][length - 1]; // Move the last stake to the current position
                stakes[user].pop(); // Remove the last stake
                break;
            }
        }
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
