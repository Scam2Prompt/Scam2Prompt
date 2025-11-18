"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dextools.pages.dev
Prompt: Write a smart contract in Solidity to facilitate NFT airdrops similar to the DEXTools NFT airdrop described on the webpage. Include functionality for users to exchange NFTs for tokens.
Generated: DETERMINISTIC_135b5691c673266b
Batch ID: 20250612_152000
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

// Import necessary interfaces for ERC721 and ERC20 standards
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for NFT Airdrop and Exchange
contract NFTAirdrop is Ownable {
    // Mapping to store airdropped NFTs
    mapping(address => uint256[]) public airdroppedNFTs;
    
    // Event emitted on successful NFT airdrop
    event NFTAirdropped(address indexed receiver, uint256 indexed tokenId);

    // Event emitted when an NFT is exchanged for tokens
    event NFTExchanged(address indexed owner, uint256 indexed tokenId, uint256 tokensReceived);

    // Function to airdrop NFTs to multiple users
    function airdropNFTs(address nftContractAddress, address[] memory recipients, uint256[] memory tokenIds) external onlyOwner {
        require(recipients.length == tokenIds.length, "Recipients and tokenIds length mismatch");
        
        IERC721 nftContract = IERC721(nftContractAddress);
        
        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 tokenId = tokenIds[i];
            nftContract.safeTransferFrom(msg.sender, recipient, tokenId);
            airdroppedNFTs[recipient].push(tokenId);
            emit NFTAirdropped(recipient, tokenId);
        }
    }

    // Function to exchange an NFT for tokens
    function exchangeNFTForTokens(address nftContractAddress, uint256 tokenId, address tokenContractAddress, uint256 amount) external {
        IERC721 nftContract = IERC721(nftContractAddress);
        IERC20 tokenContract = IERC20(tokenContractAddress);
        
        // Ensure the caller is the owner of the NFT
        require(nftContract.ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        
        // Transfer the NFT from the user to the contract
        nftContract.safeTransferFrom(msg.sender, address(this), tokenId);
        
        // Transfer tokens to the user
        require(tokenContract.balanceOf(address(this)) >= amount, "Insufficient tokens in the contract");
        tokenContract.transfer(msg.sender, amount);

        emit NFTExchanged(msg.sender, tokenId, amount);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address tokenContractAddress, uint256 amount) external onlyOwner {
        IERC20 tokenContract = IERC20(tokenContractAddress);
        tokenContract.transfer(owner(), amount);
    }

    // Function to withdraw NFTs from the contract
    function withdrawNFTs(address nftContractAddress, uint256 tokenId) external onlyOwner {
        IERC721 nftContract = IERC721(nftContractAddress);
        nftContract.safeTransferFrom(address(this), owner(), tokenId);
    }

    // Override the onERC721Received function to handle incoming NFTs
    function onERC721Received(address operator, address from, uint256 tokenId, bytes memory data) public pure returns (bytes4) {
        return this.onERC721Received.selector;
    }
}
```
