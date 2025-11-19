"""
Generated Code Metadata:
========================
Original URL: https://metarebelz-rust.vercel.app
Prompt: Generate code to implement a staking mechanism for an NFT collection, where holders can stake their NFTs to receive rewards in the form of airdropped NFTs or other benefits.
Generated: DETERMINISTIC_d8adfb7ba100e868
Batch ID: 20250622_210216
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
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title NFT Staking Mechanism
 * @author [Your Name]
 * @notice This contract allows NFT holders to stake their NFTs to receive rewards.
 */
contract NFTStaking is Ownable, ReentrancyGuard {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Mapping of NFT contracts to their respective staking data
    mapping(address => StakingData) public stakingData;

    // Event emitted when an NFT is staked
    event NFTStaked(address indexed nftContract, uint256 indexed tokenId, address indexed staker);

    // Event emitted when an NFT is unstaked
    event NFTUnstaked(address indexed nftContract, uint256 indexed tokenId, address indexed staker);

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed nftContract, uint256 indexed tokenId, address indexed staker);

    /**
     * @dev Struct to store staking data for an NFT contract
     */
    struct StakingData {
        // Mapping of staked NFTs to their stakers
        mapping(uint256 => address) stakers;
        // Mapping of stakers to their staked NFTs
        mapping(address => EnumerableSet.UintSet) stakerTokens;
        // Reward NFT contract address
        address rewardNftContract;
        // Reward NFT ID
        uint256 rewardNftId;
    }

    /**
     * @dev Function to stake an NFT
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the NFT to stake
     */
    function stakeNFT(address nftContract, uint256 tokenId) public nonReentrant {
        // Check if the NFT contract has staking data initialized
        require(stakingData[nftContract].rewardNftContract != address(0), "Staking not initialized for this NFT contract");

        // Check if the NFT is owned by the staker
        IERC721 nft = IERC721(nftContract);
        require(nft.ownerOf(tokenId) == msg.sender, "You do not own this NFT");

        // Check if the NFT is already staked
        require(stakingData[nftContract].stakers[tokenId] == address(0), "NFT is already staked");

        // Transfer the NFT to the staking contract
        nft.safeTransferFrom(msg.sender, address(this), tokenId);

        // Update staking data
        stakingData[nftContract].stakers[tokenId] = msg.sender;
        stakingData[nftContract].stakerTokens[msg.sender].add(tokenId);

        emit NFTStaked(nftContract, tokenId, msg.sender);
    }

    /**
     * @dev Function to unstake an NFT
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the NFT to unstake
     */
    function unstakeNFT(address nftContract, uint256 tokenId) public nonReentrant {
        // Check if the NFT is staked
        require(stakingData[nftContract].stakers[tokenId] == msg.sender, "You do not have permission to unstake this NFT");

        // Transfer the NFT back to the staker
        IERC721 nft = IERC721(nftContract);
        nft.safeTransferFrom(address(this), msg.sender, tokenId);

        // Update staking data
        stakingData[nftContract].stakers[tokenId] = address(0);
        stakingData[nftContract].stakerTokens[msg.sender].remove(tokenId);

        emit NFTUnstaked(nftContract, tokenId, msg.sender);
    }

    /**
     * @dev Function to claim a reward
     * @param nftContract Address of the NFT contract
     * @param tokenId ID of the staked NFT
     */
    function claimReward(address nftContract, uint256 tokenId) public nonReentrant {
        // Check if the NFT is staked
        require(stakingData[nftContract].stakers[tokenId] == msg.sender, "You do not have permission to claim a reward for this NFT");

        // Transfer the reward NFT to the staker
        IERC721 rewardNft = IERC721(stakingData[nftContract].rewardNftContract);
        rewardNft.safeTransferFrom(address(this), msg.sender, stakingData[nftContract].rewardNftId);

        emit RewardClaimed(nftContract, tokenId, msg.sender);
    }

    /**
     * @dev Function to initialize staking for an NFT contract
     * @param nftContract Address of the NFT contract
     * @param rewardNftContract Address of the reward NFT contract
     * @param rewardNftId ID of the reward NFT
     */
    function initializeStaking(address nftContract, address rewardNftContract, uint256 rewardNftId) public onlyOwner {
        require(stakingData[nftContract].rewardNftContract == address(0), "Staking already initialized for this NFT contract");

        stakingData[nftContract].rewardNftContract = rewardNftContract;
        stakingData[nftContract].rewardNftId = rewardNftId;
    }

    /**
     * @dev Function to set a new reward NFT
     * @param nftContract Address of the NFT contract
     * @param newRewardNftContract Address of the new reward NFT contract
     * @param newRewardNftId ID of the new reward NFT
     */
    function setNewRewardNft(address nftContract, address newRewardNftContract, uint256 newRewardNftId) public onlyOwner {
        stakingData[nftContract].rewardNftContract = newRewardNftContract;
        stakingData[nftContract].rewardNftId = newRewardNftId;
    }
}
```
