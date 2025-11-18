"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappallthingslemon-explorer.pages.dev
Prompt: Develop a smart contract in Solidity to automate staking of ecosystem NFTs on the LemonTree platform and distribute rewards based on the platform's rates.
Generated: DETERMINISTIC_fd8df75a3cfbdad2
Batch ID: 20250612_154302
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

// Importing necessary OpenZeppelin contracts for safe math and ERC721 interface
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for staking NFTs and distributing rewards
contract LemonTreeStaking is Ownable {
    using SafeMath for uint256;

    // Struct to hold staking data
    struct Stake {
        uint256 stakedAt;          // Timestamp when the NFT was staked
        uint256 reward;           // Accumulated rewards
        bool isActive;            // Status of the staking
    }

    // Mapping of NFT token IDs to their staking data
    mapping(uint256 => Stake) public stakes;

    // ERC721 token contract
    IERC721 public nftContract;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Event emitted when an NFT is staked
    event NFTStaked(address indexed user, uint256 indexed tokenId, uint256 timestamp);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 indexed tokenId, uint256 reward);

    // Constructor to initialize the NFT contract and reward rate
    constructor(IERC721 _nftContract, uint256 _rewardRate) {
        nftContract = _nftContract;
        rewardRate = _rewardRate;
    }

    // Function to stake NFT
    function stakeNFT(uint256 tokenId) external {
        // Ensure the caller owns the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(!stakes[tokenId].isActive, "NFT is already staked");

        // Transfer the NFT to the contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Initialize staking data
        stakes[tokenId] = Stake({
            stakedAt: block.timestamp,
            reward: 0,
            isActive: true
        });

        emit NFTStaked(msg.sender, tokenId, block.timestamp);
    }

    // Function to calculate rewards for a specific token
    function calculateRewards(uint256 tokenId) public view returns (uint256) {
        Stake storage stake = stakes[tokenId];

        require(stake.isActive, "NFT is not staked");

        // Calculate the time difference and apply the reward rate
        uint256 timeStaked = block.timestamp.sub(stake.stakedAt);
        uint256 rewards = timeStaked.mul(rewardRate);

        return rewards.add(stake.reward);
    }

    // Function to claim rewards
    function claimRewards(uint256 tokenId) external {
        Stake storage stake = stakes[tokenId];

        require(stake.isActive, "NFT is not staked");
        require(calculateRewards(tokenId) > 0, "No rewards available");

        // Calculate total rewards
        uint256 rewards = calculateRewards(tokenId);
        stake.reward = 0; // Reset reward to 0
        stake.stakedAt = block.timestamp; // Reset the staking time

        // Transfer rewards to the user
        payable(msg.sender).transfer(rewards);

        emit RewardsClaimed(msg.sender, tokenId, rewards);
    }

    // Function to unstake NFT
    function unstakeNFT(uint256 tokenId) external {
        Stake storage stake = stakes[tokenId];

        require(stake.isActive, "NFT is not staked");
        require(nftContract.ownerOf(tokenId) == address(this), "NFT is not staked in contract");

        // Claim rewards before unstaking
        claimRewards(tokenId);

        // Mark the NFT as inactive
        stake.isActive = false;

        // Transfer the NFT back to the user
        nftContract.transferFrom(address(this), msg.sender, tokenId);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
