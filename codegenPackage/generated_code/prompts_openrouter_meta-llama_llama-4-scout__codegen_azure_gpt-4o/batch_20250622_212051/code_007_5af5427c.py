"""
Generated Code Metadata:
========================
Original URL: https://proposal-playmemoria.com
Prompt: Develop a simple smart contract for NFT staking on a blockchain platform like Avalanche.
Generated: DETERMINISTIC_5af5427ce52abcf4
Batch ID: 20250622_212051
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

/**
 * @title NFTStaking
 * @dev A simple smart contract for staking NFTs on a blockchain platform like Avalanche.
 */
contract NFTStaking {
    // Struct to store staking information
    struct Stake {
        address owner; // Address of the NFT owner
        uint256 tokenId; // ID of the staked NFT
        uint256 timestamp; // Timestamp when the NFT was staked
    }

    // Mapping from NFT ID to staking information
    mapping(uint256 => Stake) public stakes;

    // ERC721 token contract address
    address public nftContract;

    // Event emitted when an NFT is staked
    event NFTStaked(address indexed owner, uint256 indexed tokenId, uint256 timestamp);

    // Event emitted when an NFT is unstaked
    event NFTUnstaked(address indexed owner, uint256 indexed tokenId, uint256 timestamp);

    /**
     * @dev Constructor to set the NFT contract address.
     * @param _nftContract Address of the ERC721 token contract.
     */
    constructor(address _nftContract) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        nftContract = _nftContract;
    }

    /**
     * @dev Stake an NFT.
     * @param tokenId ID of the NFT to stake.
     */
    function stakeNFT(uint256 tokenId) external {
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "Caller is not the owner of the NFT");
        require(stakes[tokenId].owner == address(0), "NFT is already staked");

        // Transfer the NFT to the contract
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Record staking information
        stakes[tokenId] = Stake({
            owner: msg.sender,
            tokenId: tokenId,
            timestamp: block.timestamp
        });

        emit NFTStaked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @dev Unstake an NFT.
     * @param tokenId ID of the NFT to unstake.
     */
    function unstakeNFT(uint256 tokenId) external {
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.owner == msg.sender, "Caller is not the owner of the staked NFT");
        require(stakeInfo.owner != address(0), "NFT is not staked");

        // Remove staking information
        delete stakes[tokenId];

        // Transfer the NFT back to the owner
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        emit NFTUnstaked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @dev Get staking information for a specific NFT.
     * @param tokenId ID of the NFT.
     * @return Stake struct containing staking details.
     */
    function getStakeInfo(uint256 tokenId) external view returns (Stake memory) {
        return stakes[tokenId];
    }
}

// Interface for ERC721 token contract
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function transferFrom(address from, address to, uint256 tokenId) external;
}
```
