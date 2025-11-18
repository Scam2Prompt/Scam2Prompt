"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascalsnft.web.app
Prompt: Create a smart contract for staking Rascals NFTs to earn $Jelly tokens, ensuring compatibility with the Ethereum blockchain.
Generated: DETERMINISTIC_b56c7b62acbf063f
Batch ID: 20250612_152329
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

// Import the ERC721 interface for NFT interactions
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
// Import the Ownable contract for ownership management
import "@openzeppelin/contracts/access/Ownable.sol";
// Import the SafeERC20 for safe token transfers
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

// Interface for the Jelly Token
interface IJellyToken {
    function mint(address to, uint256 amount) external;
}

contract RascalsStaking is Ownable {
    using SafeERC20 for IERC20;

    // The address of the Jelly token contract
    IJellyToken public jellyToken;
    
    // Mapping to keep track of staked NFTs by user
    mapping(address => uint256[]) public stakedNFTs;
    // Mapping to track if an NFT is currently staked
    mapping(uint256 => address) public nftOwner;

    // Event emitted when an NFT is staked
    event NFTStaked(address indexed user, uint256 indexed tokenId);
    // Event emitted when an NFT is unstaked
    event NFTUnstaked(address indexed user, uint256 indexed tokenId);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the Jelly token address
    constructor(address _jellyToken) {
        require(_jellyToken != address(0), "Invalid token address");
        jellyToken = IJellyToken(_jellyToken);
    }

    // Function to stake an NFT
    function stakeNFT(address nftContract, uint256 tokenId) external {
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "Not the NFT owner");
        require(nftOwner[tokenId] == address(0), "NFT already staked");

        // Transfer the NFT to the contract for staking
        IERC721(nftContract).safeTransferFrom(msg.sender, address(this), tokenId);

        // Record the staked NFT
        stakedNFTs[msg.sender].push(tokenId);
        nftOwner[tokenId] = msg.sender;

        emit NFTStaked(msg.sender, tokenId);
    }

    // Function to unstake an NFT
    function unstakeNFT(address nftContract, uint256 tokenId) external {
        require(nftOwner[tokenId] == msg.sender, "Not the NFT staker");
        
        // Remove the NFT from the staked list
        _removeStake(msg.sender, tokenId);
        
        // Transfer the NFT back to the owner
        IERC721(nftContract).safeTransferFrom(address(this), msg.sender, tokenId);

        emit NFTUnstaked(msg.sender, tokenId);
    }

    // Internal function to remove a stake from the list of staked NFTs
    function _removeStake(address user, uint256 tokenId) internal {
        uint256[] storage userStakedNFTs = stakedNFTs[user];
        for (uint256 i = 0; i < userStakedNFTs.length; i++) {
            if (userStakedNFTs[i] == tokenId) {
                userStakedNFTs[i] = userStakedNFTs[userStakedNFTs.length - 1];
                userStakedNFTs.pop();
                break;
            }
        }
        delete nftOwner[tokenId];
    }

    // Function to claim rewards in Jelly tokens
    function claimRewards() external {
        uint256 rewardAmount = calculateRewards(msg.sender);
        require(rewardAmount > 0, "No rewards to claim");

        // Mint the Jelly tokens to the user
        jellyToken.mint(msg.sender, rewardAmount);

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Dummy function to calculate rewards (to be implemented with real logic)
    function calculateRewards(address user) internal view returns (uint256) {
        // Placeholder: Each staked NFT earns 10 Jelly tokens
        return stakedNFTs[user].length * 10;
    }
}
```
