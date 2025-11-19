"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartdappsnodes.pages.dev
Prompt: Provide an example of how to set up NFT staking on the Smart Dapps platform.
Generated: DETERMINISTIC_96b42622967fec24
Batch ID: 20250612_164152
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the NFT contract
interface INFT is IERC721 {
    function mint(address to, uint256 tokenId) external;
    function burn(uint256 tokenId) external;
}

// Staking contract for NFTs
contract NFTStaking is ERC721Holder, Ownable {
    // Struct to hold staking information
    struct StakingInfo {
        uint256 tokenId;
        uint256 stakedAt;
    }

    // Mapping from user address to their staking info
    mapping(address => StakingInfo) public stakes;
    
    // The NFT contract interface
    INFT public nftContract;

    // Event emitted when an NFT is staked
    event NFTStaked(address indexed user, uint256 tokenId);

    // Event emitted when an NFT is unstaked
    event NFTUnstaked(address indexed user, uint256 tokenId);

    // Constructor to set the NFT contract
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = INFT(_nftContract);
    }

    // Stake an NFT by tokenId
    function stake(uint256 tokenId) external {
        // Ensure the user owns the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        
        // Transfer the NFT to the staking contract
        nftContract.safeTransferFrom(msg.sender, address(this), tokenId);

        // Update staking info
        stakes[msg.sender] = StakingInfo({
            tokenId: tokenId,
            stakedAt: block.timestamp
        });

        emit NFTStaked(msg.sender, tokenId);
    }

    // Unstake the NFT
    function unstake() external {
        // Ensure the user has staked an NFT
        StakingInfo memory stakingInfo = stakes[msg.sender];
        require(stakingInfo.tokenId != 0, "No NFT staked");

        // Transfer the NFT back to the user
        nftContract.safeTransferFrom(address(this), msg.sender, stakingInfo.tokenId);

        // Clear the staking info
        delete stakes[msg.sender];

        emit NFTUnstaked(msg.sender, stakingInfo.tokenId);
    }

    // Function to retrieve the staked tokenId of the caller
    function getStakedTokenId() external view returns (uint256) {
        StakingInfo memory stakingInfo = stakes[msg.sender];
        require(stakingInfo.tokenId != 0, "No NFT staked");
        return stakingInfo.tokenId;
    }

    // Function to recover ERC20 tokens accidentally sent to this contract
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(nftContract), "Cannot recover NFTs");
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
