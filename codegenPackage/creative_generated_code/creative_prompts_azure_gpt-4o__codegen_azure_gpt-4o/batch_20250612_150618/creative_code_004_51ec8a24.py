"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aurora-eth.pages.dev
Prompt: Create a smart contract for staking on the Aurora blockchain that supports Bitcoin NFTs.
Generated: DETERMINISTIC_51ec8a242a3857b5
Batch ID: 20250612_150618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a staking smart contract that supports Bitcoin NFTs on Aurora blockchain using Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Staking Contract for Bitcoin NFTs on Aurora
 * @dev This contract allows users to stake their Bitcoin NFTs and earn rewards.
 *      It follows best practices for security and code clarity.
 */
contract BitcoinNFTStaking {
    // Struct to store staking information
    struct Stake {
        address owner;          // Owner of the NFT
        uint256 tokenId;        // ID of the staked NFT
        uint256 stakedAt;       // Timestamp when the NFT was staked
    }

    // Mapping from token ID to staking information
    mapping(uint256 => Stake) public stakes;

    // Reward rate (e.g., 10 tokens per day)
    uint256 public constant REWARD_RATE = 10;
    
    // Address of the Bitcoin NFT contract
    address public nftContract;

    // Event emitted when an NFT is staked
    event NFTStaked(address indexed owner, uint256 indexed tokenId, uint256 timestamp);

    // Event emitted when an NFT is unstaked
    event NFTUnstaked(address indexed owner, uint256 indexed tokenId, uint256 timestamp);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed owner, uint256 indexed tokenId, uint256 amount);

    // Modifier to ensure only the owner of the NFT can perform certain actions
    modifier onlyOwner(uint256 tokenId) {
        require(stakes[tokenId].owner == msg.sender, "Not the owner of this NFT");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract
     * @param _nftContract Address of the Bitcoin NFT contract
     */
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = _nftContract;
    }

    /**
     * @dev Stake an NFT by transferring it to the contract
     * @param tokenId ID of the NFT to stake
     */
    function stakeNFT(uint256 tokenId) external {
        require(stakes[tokenId].owner == address(0), "NFT already staked");

        // Transfer NFT to this contract
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Record staking information
        stakes[tokenId] = Stake({
            owner: msg.sender,
            tokenId: tokenId,
            stakedAt: block.timestamp
        });

        emit NFTStaked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @dev Unstake an NFT and transfer it back to the owner
     * @param tokenId ID of the NFT to unstake
     */
    function unstakeNFT(uint256 tokenId) external onlyOwner(tokenId) {
        // Claim rewards before unstaking
        claimRewards(tokenId);

        // Remove staking information
        delete stakes[tokenId];

        // Transfer NFT back to the owner
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        emit NFTUnstaked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @dev Claim rewards for staking an NFT
     * @param tokenId ID of the NFT to claim rewards for
     */
    function claimRewards(uint256 tokenId) public onlyOwner(tokenId) {
        Stake memory stakeData = stakes[tokenId];
        require(stakeData.stakedAt > 0, "NFT not staked");

        // Calculate the number of days staked
        uint256 stakingDuration = block.timestamp - stakeData.stakedAt;
        uint256 daysStaked = stakingDuration / 1 days;

        // Calculate reward amount
        uint256 rewardAmount = daysStaked * REWARD_RATE;

        require(rewardAmount > 0, "No rewards available");

        // Update staking timestamp
        stakes[tokenId].stakedAt = block.timestamp;

        // Transfer reward to the owner (replace with actual reward logic)
        // Example: Mint reward tokens or transfer tokens from a pool
        // For simplicity, we emit an event
        emit RewardsClaimed(msg.sender, tokenId, rewardAmount);
    }

    /**
     * @dev Get staking information for an NFT
     * @param tokenId ID of the NFT to query
     * @return Stake struct containing staking details
     */
    function getStake(uint256 tokenId) external view returns (Stake memory) {
        return stakes[tokenId];
    }
}

// Interface for the ERC721 standard
interface IERC721 {
    function transferFrom(address from, address to, uint256 tokenId) external;
}
```

This smart contract allows users to stake their Bitcoin NFTs, earn rewards based on staking duration, and unstake their NFTs when desired. It assumes that the Aurora blockchain supports Ethereum-compatible Solidity smart contracts and that the Bitcoin NFTs follow the ERC721 standard.
