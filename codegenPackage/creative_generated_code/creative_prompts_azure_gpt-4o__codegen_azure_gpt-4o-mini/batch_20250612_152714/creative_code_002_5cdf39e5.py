"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://move-e87.pages.dev
Prompt: Generate a smart contract in Solidity that allows users to claim tokens or NFTs after verifying their wallet address, similar to the MoveDrop Claim process.
Generated: DETERMINISTIC_5cdf39e54ddf374c
Batch ID: 20250612_152714
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TokenClaim
 * @dev This contract allows users to claim tokens or NFTs after verifying their wallet address.
 */
contract TokenClaim is Ownable {
    // Mapping of addresses that have claimed tokens
    mapping(address => bool) public hasClaimed;

    // ERC20 token that users can claim
    IERC20 public token;
    
    // ERC721 contract for NFTs that users can claim
    IERC721 public nft;

    // Event emitted when a claim is successful
    event Claimed(address indexed claimant, uint256 amount);

    /**
     * @dev Constructor to initialize the token and NFT contracts.
     * @param _tokenAddress The address of the ERC20 token contract.
     * @param _nftAddress The address of the ERC721 contract for NFTs.
     */
    constructor(address _tokenAddress, address _nftAddress) {
        token = IERC20(_tokenAddress);
        nft = IERC721(_nftAddress);
    }

    /**
     * @dev Allows the owner to set the token and NFT contracts.
     * @param _tokenAddress The address of the ERC20 token contract.
     * @param _nftAddress The address of the ERC721 contract for NFTs.
     */
    function setContracts(address _tokenAddress, address _nftAddress) external onlyOwner {
        token = IERC20(_tokenAddress);
        nft = IERC721(_nftAddress);
    }

    /**
     * @dev Users can claim their tokens if they have not already claimed.
     * @param amount The amount of tokens to claim.
     */
    function claimTokens(uint256 amount) external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(address(this)) >= amount, "Insufficient tokens in contract");

        // Mark the address as having claimed
        hasClaimed[msg.sender] = true;
        
        // Transfer tokens to the user
        token.transfer(msg.sender, amount);
        
        emit Claimed(msg.sender, amount);
    }

    /**
     * @dev Users can claim an NFT if they have not already claimed.
     * @param tokenId The ID of the NFT to claim.
     */
    function claimNFT(uint256 tokenId) external {
        require(!hasClaimed[msg.sender], "NFT already claimed");
        
        // Ensure the NFT exists and is owned by the contract
        require(nft.ownerOf(tokenId) == address(this), "NFT not owned by contract");

        // Mark the address as having claimed
        hasClaimed[msg.sender] = true;
        
        // Transfer NFT to the user
        nft.transferFrom(address(this), msg.sender, tokenId);
        
        emit Claimed(msg.sender, tokenId);
    }

    /**
     * @dev Withdraws any ERC20 tokens stuck in the contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        token.transfer(msg.sender, amount);
    }

    /**
     * @dev Withdraws any ERC721 NFTs stuck in the contract.
     * @param tokenId The ID of the NFT to withdraw.
     */
    function withdrawNFT(uint256 tokenId) external onlyOwner {
        require(nft.ownerOf(tokenId) == address(this), "NFT not owned by contract");
        nft.transferFrom(address(this), msg.sender, tokenId);
    }
}
```
