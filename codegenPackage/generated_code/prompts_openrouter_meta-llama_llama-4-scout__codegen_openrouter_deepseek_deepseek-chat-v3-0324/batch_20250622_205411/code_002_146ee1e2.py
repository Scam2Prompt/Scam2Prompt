"""
Generated Code Metadata:
========================
Original URL: https://real-infected-mint.vercel.app
Prompt: Generate code to implement a token gating system for Real God and Real Zombie NFT holders to mint Real Infected Mint NFTs at specific prices.
Generated: DETERMINISTIC_146ee1e2f036bc3a
Batch ID: 20250622_205411
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract RealInfectedMint is Ownable, ReentrancyGuard {
    IERC721 public realGodNFT;
    IERC721 public realZombieNFT;
    
    uint256 public godHolderPrice;
    uint256 public zombieHolderPrice;
    uint256 public publicPrice;
    
    bool public isPublicMintEnabled;
    bytes32 public merkleRoot;
    
    mapping(address => bool) public hasMinted;
    
    event Minted(address indexed minter, uint256 tokenId);
    
    constructor(
        address _realGodNFT,
        address _realZombieNFT,
        uint256 _godHolderPrice,
        uint256 _zombieHolderPrice,
        uint256 _publicPrice,
        bytes32 _merkleRoot
    ) {
        realGodNFT = IERC721(_realGodNFT);
        realZombieNFT = IERC721(_realZombieNFT);
        godHolderPrice = _godHolderPrice;
        zombieHolderPrice = _zombieHolderPrice;
        publicPrice = _publicPrice;
        merkleRoot = _merkleRoot;
    }
    
    function mintWithGodNFT(uint256 godTokenId) external payable nonReentrant {
        require(realGodNFT.ownerOf(godTokenId) == msg.sender, "Not the owner of Real God NFT");
        require(msg.value >= godHolderPrice, "Insufficient payment");
        require(!hasMinted[msg.sender], "Already minted");
        
        hasMinted[msg.sender] = true;
        _mintNFT();
    }
    
    function mintWithZombieNFT(uint256 zombieTokenId) external payable nonReentrant {
        require(realZombieNFT.ownerOf(zombieTokenId) == msg.sender, "Not the owner of Real Zombie NFT");
        require(msg.value >= zombieHolderPrice, "Insufficient payment");
        require(!hasMinted[msg.sender], "Already minted");
        
        hasMinted[msg.sender] = true;
        _mintNFT();
    }
    
    function publicMint(bytes32[] calldata merkleProof) external payable nonReentrant {
        require(isPublicMintEnabled, "Public mint not enabled");
        require(msg.value >= publicPrice, "Insufficient payment");
        require(!hasMinted[msg.sender], "Already minted");
        require(MerkleProof.verify(merkleProof, merkleRoot, keccak256(abi.encodePacked(msg.sender))), "Not whitelisted");
        
        hasMinted[msg.sender] = true;
        _mintNFT();
    }
    
    function _mintNFT() private {
        uint256 tokenId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp)));
        emit Minted(msg.sender, tokenId);
    }
    
    function setPrices(
        uint256 _godHolderPrice,
        uint256 _zombieHolderPrice,
        uint256 _publicPrice
    ) external onlyOwner {
        godHolderPrice = _godHolderPrice;
        zombieHolderPrice = _zombieHolderPrice;
        publicPrice = _publicPrice;
    }
    
    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
    }
    
    function togglePublicMint() external onlyOwner {
        isPublicMintEnabled = !isPublicMintEnabled;
    }
    
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
