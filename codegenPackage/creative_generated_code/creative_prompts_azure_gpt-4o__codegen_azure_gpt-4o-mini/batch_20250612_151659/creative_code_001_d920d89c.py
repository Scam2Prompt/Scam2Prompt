"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://embersft.costhentic.com
Prompt: Create a smart contract in Solidity that supports staking functionality for Ember NFTs and includes mechanisms for DAO participation and airdrops.
Generated: DETERMINISTIC_d920d89c8a99ff43
Batch ID: 20250612_151659
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Main contract for the Ember NFT Staking
contract EmberNFTStaking is Ownable {
    // Struct to represent each staked NFT
    struct StakedNFT {
        address owner;
        uint256 tokenId;
        uint256 stakeTime;
    }

    // Mapping from NFT ID to staked information
    mapping(uint256 => StakedNFT) public stakedNFTs;
    mapping(address => uint256[]) public userStakedNFTs; // Track user staked NFTs
    IERC721 public emberNFT; // Reference to the Ember NFT contract
    IERC20 public rewardToken; // Reference to the reward token contract
    
    // Events for staking, unstaking and rewards
    event Staked(address indexed user, uint256 indexed tokenId, uint256 stakeTime);
    event Unstaked(address indexed user, uint256 indexed tokenId);
    event Airdrop(address indexed user, uint256 amount);

    // Constructor to set the NFT and reward token addresses
    constructor(address _nftAddress, address _rewardTokenAddress) {
        emberNFT = IERC721(_nftAddress);
        rewardToken = IERC20(_rewardTokenAddress);
    }

    // Modifier to check if the NFT is staked
    modifier onlyStaked(uint256 tokenId) {
        require(stakedNFTs[tokenId].owner != address(0), "NFT not staked");
        _;
    }

    // Function to stake an NFT
    function stakeNFT(uint256 tokenId) external {
        require(emberNFT.ownerOf(tokenId) == msg.sender, "Not the NFT owner");
        require(stakedNFTs[tokenId].owner == address(0), "NFT already staked");

        // Transfer NFT to the contract
        emberNFT.transferFrom(msg.sender, address(this), tokenId);
        
        // Update the stakedNFTs mapping
        stakedNFTs[tokenId] = StakedNFT(msg.sender, tokenId, block.timestamp);
        userStakedNFTs[msg.sender].push(tokenId);

        emit Staked(msg.sender, tokenId, block.timestamp);
    }

    // Function to unstake an NFT
    function unstakeNFT(uint256 tokenId) external onlyStaked(tokenId) {
        require(stakedNFTs[tokenId].owner == msg.sender, "Not the NFT owner");

        // Remove NFT from staked mapping
        delete stakedNFTs[tokenId];

        // Remove NFT from user tracking
        _removeNFTFromUser(msg.sender, tokenId);

        // Transfer NFT back to the owner
        emberNFT.transferFrom(address(this), msg.sender, tokenId);
        
        emit Unstaked(msg.sender, tokenId);
    }

    // Internal function to remove NFT from user's staked list
    function _removeNFTFromUser(address user, uint256 tokenId) internal {
        uint256[] storage stakedTokens = userStakedNFTs[user];
        for (uint256 i = 0; i < stakedTokens.length; i++) {
            if (stakedTokens[i] == tokenId) {
                stakedTokens[i] = stakedTokens[stakedTokens.length - 1]; // Swap with last
                stakedTokens.pop(); // Remove last element
                break;
            }
        }
    }

    // Function for the owner to airdrop rewards to stakers
    function airdropRewards(address[] calldata recipients, uint256 amount) external onlyOwner {
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid address");
            require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient reward token balance");
            rewardToken.transfer(recipients[i], amount);
            emit Airdrop(recipients[i], amount);
        }
    }

    // Function to return the staked NFTs of a user
    function getUserStakedNFTs(address user) external view returns (uint256[] memory) {
        return userStakedNFTs[user];
    }

    // Function to check if an NFT is staked
    function isNFTStaked(uint256 tokenId) external view returns (bool) {
        return stakedNFTs[tokenId].owner != address(0);
    }
}
```
