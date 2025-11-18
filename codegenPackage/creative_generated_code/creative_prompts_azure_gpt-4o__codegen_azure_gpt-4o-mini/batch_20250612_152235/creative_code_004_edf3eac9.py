"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mallconomy-claimreward.pages.dev
Prompt: Develop a smart contract for staking MallCard NFTs to unlock faster rewards in Mallconomy's Rewards Hub.
Generated: DETERMINISTIC_edf3eac975cf9ed3
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

// Interface for the ERC721 NFT standard
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function balanceOf(address owner) external view returns (uint256);
}

// Interface for the Rewards Hub to handle reward distribution
interface IRewardsHub {
    function distributeRewards(address user, uint256 amount) external;
}

contract MallCardStaking {
    // State variables
    IERC721 public mallCardNFT;
    IRewardsHub public rewardsHub;
    
    // Mapping to track staked NFTs
    mapping(address => uint256[]) public stakedNFTs;
    
    // Event emitted when an NFT is staked
    event NFTStaked(address indexed user, uint256 indexed tokenId);
    
    // Event emitted when an NFT is unstaked
    event NFTUnstaked(address indexed user, uint256 indexed tokenId);
    
    // Modifier to check if the caller is the NFT owner
    modifier onlyNFTOwner(uint256 tokenId) {
        require(mallCardNFT.ownerOf(tokenId) == msg.sender, "Not the NFT owner");
        _;
    }
    
    // Constructor to initialize the contract
    constructor(address _mallCardNFT, address _rewardsHub) {
        mallCardNFT = IERC721(_mallCardNFT);
        rewardsHub = IRewardsHub(_rewardsHub);
    }
    
    // Function to stake an NFT
    function stakeNFT(uint256 tokenId) external onlyNFTOwner(tokenId {
        // Transfer the NFT to this contract
        // (Assumes the NFT adheres to the ERC721 transfer mechanism)
        mallCardNFT.transferFrom(msg.sender, address(this), tokenId);
        
        // Record the staked NFT
        stakedNFTs[msg.sender].push(tokenId);
        
        // Emit the staking event
        emit NFTStaked(msg.sender, tokenId);
    }

    // Function to unstake an NFT
    function unstakeNFT(uint256 tokenId) external {
        // Check if the sender has staked this NFT
        require(isNFTStaked(msg.sender, tokenId), "NFT is not staked by you");
        
        // Find and remove the tokenId from the staked array
        _removeStakedNFT(msg.sender, tokenId);
        
        // Transfer the NFT back to the owner
        mallCardNFT.transferFrom(address(this), msg.sender, tokenId);
        
        // Emit the unstaking event
        emit NFTUnstaked(msg.sender, tokenId);
    }
    
    // Internal function to remove NFT from staked array
    function _removeStakedNFT(address user, uint256 tokenId) internal {
        uint256[] storage staked = stakedNFTs[user];
        for (uint256 i = 0; i < staked.length; i++) {
            if (staked[i] == tokenId) {
                // Replace the tokenId to be removed with the last one and pop
                staked[i] = staked[staked.length - 1];
                staked.pop();
                return;
            }
        }
    }
    
    // Function to check if an NFT is staked by a user
    function isNFTStaked(address user, uint256 tokenId) public view returns (bool) {
        uint256[] memory staked = stakedNFTs[user];
        for (uint256 i = 0; i < staked.length; i++) {
            if (staked[i] == tokenId) {
                return true;
            }
        }
        return false;
    }

    // Function to distribute rewards based on the number of staked NFTs
    function distributeRewards() external {
        uint256 rewardAmount = calculateReward(msg.sender);
        require(rewardAmount > 0, "No rewards to distribute");
        
        // Call the Rewards Hub to distribute the rewards
        rewardsHub.distributeRewards(msg.sender, rewardAmount);
    }
    
    // Function to calculate rewards based on staked NFTs
    function calculateReward(address user) internal view returns (uint256) {
        return stakedNFTs[user].length * 10; // Example: 10 units of reward per NFT staked
    }
}
```
