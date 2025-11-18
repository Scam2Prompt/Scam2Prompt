"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token2049.vercel.app
Prompt: Generate a Solidity smart contract for staking functionality in the 2049 NFT marketplace, ensuring compatibility with the platform's native stacking features.
Generated: DETERMINISTIC_d6b776700135b523
Batch ID: 20250612_152006
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

// Importing the required interfaces and standard libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingContract allows users to stake their NFTs and earn rewards
contract StakingContract is Ownable {
    
    // Structure to hold staking information for each user
    struct Stake {
        uint256 tokenId;
        uint256 stakedAt;
    }

    // Mapping to track staked NFTs of each user
    mapping(address => Stake[]) public stakes;

    // The NFT contract address
    IERC721 public nftContract;
    
    // Token to reward users for staking
    IERC20 public rewardToken;

    // Reward rate per second for staking
    uint256 public rewardRate;

    // Event to emit when a user stakes an NFT
    event Staked(address indexed user, uint256 tokenId, uint256 timestamp);

    // Event to emit when a user unstakes an NFT
    event Unstaked(address indexed user, uint256 tokenId, uint256 timestamp);

    // Constructor to initialize the contract with NFT and reward token addresses
    constructor(IERC721 _nftContract, IERC20 _rewardToken, uint256 _rewardRate) {
        nftContract = _nftContract;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate; // Set reward rate (tokens per second)
    }

    // Function to stake an NFT
    function stake(uint256 tokenId) external {
        // Ensure the caller owns the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        
        // Transfer the NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);
        
        // Save the stake information
        stakes[msg.sender].push(Stake({
            tokenId: tokenId,
            stakedAt: block.timestamp
        }));

        emit Staked(msg.sender, tokenId, block.timestamp);
    }

    // Function to unstake an NFT
    function unstake(uint256 tokenId) external {
        // Find the stake
        Stake[] storage userStakes = stakes[msg.sender];
        uint256 index = findStakeIndex(userStakes, tokenId);
        
        // Remove the stake from the array
        userStakes[index] = userStakes[userStakes.length - 1];
        userStakes.pop();

        // Transfer the NFT back to the user
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId, block.timestamp);

        // Distribute rewards
        distributeRewards(msg.sender);
    }

    // Internal function to find the index of a stake
    function findStakeIndex(Stake[] storage userStakes, uint256 tokenId) internal view returns (uint256) {
        for (uint256 i = 0; i < userStakes.length; i++) {
            if (userStakes[i].tokenId == tokenId) {
                return i;
            }
        }
        revert("Stake not found");
    }

    // Function to calculate and distribute rewards
    function distributeRewards(address user) internal {
        uint256 totalReward = calculateRewards(user);
        if (totalReward > 0) {
            require(rewardToken.balanceOf(address(this)) >= totalReward, "Insufficient reward balance");
            rewardToken.transfer(user, totalReward);
        }
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        uint256 totalReward = 0;
        Stake[] storage userStakes = stakes[user];
        
        for (uint256 i = 0; i < userStakes.length; i++) {
            Stake memory stakeInfo = userStakes[i];
            uint256 stakedDuration = block.timestamp - stakeInfo.stakedAt;
            totalReward += stakedDuration * rewardRate;
        }
        
        return totalReward;
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to withdraw any staked NFTs in case of emergency
    function emergencyWithdrawNFT(uint256 tokenId) external onlyOwner {
        nftContract.transferFrom(address(this), msg.sender, tokenId);
    }
}
```
