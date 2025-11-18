"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffmypanda.pages.dev
Prompt: Create a staking protocol in Solidity for Puff Puff Pandas NFTs that allows holders to lock their NFTs and earn yield in $PUFFS tokens, as outlined in the Puff Like A Panda ecosystem.
Generated: DETERMINISTIC_cf5199279853e068
Batch ID: 20250612_152235
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

// Interface for ERC721 (NFT) standard
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function transferFrom(address from, address to, uint256 tokenId) external;
}

// Interface for ERC20 (Token) standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract PuffPuffPandasStaking {
    // State variables
    IERC721 public nftContract; // Reference to the NFT contract
    IERC20 public tokenContract; // Reference to the $PUFFS token contract

    struct Stake {
        uint256 tokenId;
        uint256 stakingStart;
        address owner;
    }

    mapping(address => Stake[]) public stakes; // Maps user addresses to their stakes
    mapping(uint256 => address) public tokenIdToStaker; // Maps tokenId to staker address
    uint256 public constant REWARD_RATE = 1 ether; // Reward rate per NFT staked per day

    // Events
    event Staked(address indexed user, uint256 indexed tokenId);
    event Unstaked(address indexed user, uint256 indexed tokenId);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with NFT and Token addresses
    constructor(address _nftContract, address _tokenContract) {
        nftContract = IERC721(_nftContract);
        tokenContract = IERC20(_tokenContract);
    }

    // Function to stake an NFT
    function stake(uint256 tokenId) external {
        // Ensure the caller is the owner of the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT.");
        
        // Transfer the NFT to the staking contract
        nftContract.transferFrom(msg.sender, address(this), tokenId);

        // Record the stake
        stakes[msg.sender].push(Stake(tokenId, block.timestamp, msg.sender));
        tokenIdToStaker[tokenId] = msg.sender;

        emit Staked(msg.sender, tokenId);
    }

    // Function to unstake an NFT and claim rewards
    function unstake(uint256 tokenId) external {
        // Ensure the caller is the staker of the NFT
        require(tokenIdToStaker[tokenId] == msg.sender, "You did not stake this NFT.");

        // Calculate earned rewards
        uint256 earnedRewards = calculateRewards(msg.sender, tokenId);

        // Transfer the NFT back to the staker
        nftContract.transferFrom(address(this), msg.sender, tokenId);

        // Remove the stake
        _removeStake(msg.sender, tokenId);
        delete tokenIdToStaker[tokenId];

        // Transfer rewards
        require(tokenContract.transfer(msg.sender, earnedRewards), "Failed to transfer rewards.");

        emit Unstaked(msg.sender, tokenId);
        emit RewardsClaimed(msg.sender, earnedRewards);
    }

    // Function to calculate rewards for a given staker and tokenId
    function calculateRewards(address staker, uint256 tokenId) internal view returns (uint256) {
        // Find the stake
        for (uint256 i = 0; i < stakes[staker].length; i++) {
            if (stakes[staker][i].tokenId == tokenId) {
                uint256 stakedDuration = block.timestamp - stakes[staker][i].stakingStart;
                return (stakedDuration / 1 days) * REWARD_RATE; // Calculate rewards based on the duration staked
            }
        }
        return 0; // No rewards if stake not found
    }

    // Internal function to remove a stake
    function _removeStake(address staker, uint256 tokenId) internal {
        for (uint256 i = 0; i < stakes[staker].length; i++) {
            if (stakes[staker][i].tokenId == tokenId) {
                stakes[staker][i] = stakes[staker][stakes[staker].length - 1]; // Replace with the last stake
                stakes[staker].pop(); // Remove the last stake
                return;
            }
        }
    }

    // Function to retrieve stakes for an address
    function getStakes(address staker) external view returns (Stake[] memory) {
        return stakes[staker];
    }
}
```
