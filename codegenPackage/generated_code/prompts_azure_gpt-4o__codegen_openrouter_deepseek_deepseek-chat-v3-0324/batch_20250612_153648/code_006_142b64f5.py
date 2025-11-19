"""
Generated Code Metadata:
========================
Original URL: https://rascal-land-nextjs-mint.vercel.app
Prompt: Create a smart contract on Solana for managing NFT assets that support educational initiatives and streaming profits.
Generated: DETERMINISTIC_142b64f57ffb332d
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solana ^1.0.0;

import "@solana/spl-token";
import "@solana/web3.js";

/**
 * @title EduNFT
 * @dev A Solana smart contract for managing NFT assets that support educational initiatives
 * and distribute streaming profits to stakeholders.
 */
contract EduNFT {
    // Program state and constants
    address public immutable programId;
    uint256 public constant ROYALTY_BASIS_POINTS = 500; // 5% royalty
    uint256 public constant EDU_SHARE_BASIS_POINTS = 300; // 3% to educational initiatives
    
    // Structs
    struct NFT {
        address mint;
        address owner;
        uint256 royaltyBasisPoints;
        uint256 eduShareBasisPoints;
        bool isListed;
        uint256 listPrice;
    }
    
    struct Stakeholder {
        address wallet;
        uint256 shareBasisPoints;
    }
    
    // Mappings
    mapping(address => NFT) public nfts;
    mapping(address => Stakeholder[]) public nftStakeholders;
    mapping(address => uint256) public eduFunds;
    
    // Events
    event NFTCreated(address indexed mint, address indexed owner);
    event NFTListed(address indexed mint, uint256 price);
    event NFTSold(address indexed mint, address indexed buyer, uint256 price);
    event RoyaltyDistributed(address indexed mint, uint256 amount);
    event EduFundDistributed(address indexed initiative, uint256 amount);
    
    // Errors
    error Unauthorized();
    error InvalidRoyalty();
    error InvalidEduShare();
    error NFTAlreadyExists();
    error NFTNotListed();
    error InsufficientFunds();
    error TransferFailed();
    
    /**
     * @dev Initialize the contract
     */
    constructor() {
        programId = address(this);
    }
    
    /**
     * @dev Create a new NFT
     * @param mint The mint address of the NFT
     * @param owner The owner of the NFT
     * @param stakeholders Array of stakeholders and their shares
     */
    function createNFT(
        address mint,
        address owner,
        Stakeholder[] memory stakeholders
    ) external {
        if (nfts[mint].mint != address(0)) revert NFTAlreadyExists();
        
        uint256 totalShares = 0;
        for (uint i = 0; i < stakeholders.length; i++) {
            totalShares += stakeholders[i].shareBasisPoints;
        }
        
        if (totalShares + ROYALTY_BASIS_POINTS + EDU_SHARE_BASIS_POINTS > 10000) {
            revert InvalidRoyalty();
        }
        
        nfts[mint] = NFT({
            mint: mint,
            owner: owner,
            royaltyBasisPoints: ROYALTY_BASIS_POINTS,
            eduShareBasisPoints: EDU_SHARE_BASIS_POINTS,
            isListed: false,
            listPrice: 0
        });
        
        for (uint i = 0; i < stakeholders.length; i++) {
            nftStakeholders[mint].push(stakeholders[i]);
        }
        
        emit NFTCreated(mint, owner);
    }
    
    /**
     * @dev List an NFT for sale
     * @param mint The mint address of the NFT
     * @param price The listing price in lamports
     */
    function listNFT(address mint, uint256 price) external {
        NFT storage nft = nfts[mint];
        if (msg.sender != nft.owner) revert Unauthorized();
        
        nft.isListed = true;
        nft.listPrice = price;
        
        emit NFTListed(mint, price);
    }
    
    /**
     * @dev Purchase an NFT
     * @param mint The mint address of the NFT
     */
    function purchaseNFT(address mint) external payable {
        NFT storage nft = nfts[mint];
        if (!nft.isListed) revert NFTNotListed();
        if (msg.value < nft.listPrice) revert InsufficientFunds();
        
        // Calculate distributions
        uint256 royaltyAmount = (msg.value * nft.royaltyBasisPoints) / 10000;
        uint256 eduAmount = (msg.value * nft.eduShareBasisPoints) / 10000;
        uint256 remainingAmount = msg.value - royaltyAmount - eduAmount;
        
        // Distribute to stakeholders
        Stakeholder[] memory stakeholders = nftStakeholders[mint];
        for (uint i = 0; i < stakeholders.length; i++) {
            uint256 share = (remainingAmount * stakeholders[i].shareBasisPoints) / 10000;
            (bool success, ) = stakeholders[i].wallet.call{value: share}("");
            if (!success) revert TransferFailed();
        }
        
        // Transfer remaining to owner
        (bool ownerSuccess, ) = nft.owner.call{value: remainingAmount}("");
        if (!ownerSuccess) revert TransferFailed();
        
        // Update state
        nft.owner = msg.sender;
        nft.isListed = false;
        nft.listPrice = 0;
        
        // Record educational funds
        eduFunds[mint] += eduAmount;
        
        emit NFTSold(mint, msg.sender, msg.value);
        emit RoyaltyDistributed(mint, royaltyAmount);
    }
    
    /**
     * @dev Distribute educational funds to an initiative
     * @param mint The mint address of the NFT
     * @param initiative The initiative address to receive funds
     */
    function distributeEduFund(address mint, address initiative) external {
        if (msg.sender != nfts[mint].owner) revert Unauthorized();
        
        uint256 amount = eduFunds[mint];
        if (amount == 0) revert InsufficientFunds();
        
        eduFunds[mint] = 0;
        (bool success, ) = initiative.call{value: amount}("");
        if (!success) revert TransferFailed();
        
        emit EduFundDistributed(initiative, amount);
    }
    
    // Helper functions
    function getStakeholders(address mint) external view returns (Stakeholder[] memory) {
        return nftStakeholders[mint];
    }
    
    function getEduFunds(address mint) external view returns (uint256) {
        return eduFunds[mint];
    }
}
```
