"""
Generated Code Metadata:
========================
Original URL: https://shibuya-git-website-redesign-landing-page-pleasrdevs.vercel.app
Prompt: How would you implement a secure and transparent NFT claiming process for users who have participated in a voting series, using blockchain technology and smart contracts, as seen in platforms like Shibuya?
Generated: DETERMINISTIC_f62db7bf4d19d285
Batch ID: 20250622_205335
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract VotingRewardNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    bytes32 public merkleRoot;
    string public baseURI;
    mapping(address => bool) public hasClaimed;

    event NFTClaimed(address indexed claimant, uint256 tokenId);

    constructor(
        string memory name,
        string memory symbol,
        bytes32 _merkleRoot,
        string memory _baseURI
    ) ERC721(name, symbol) {
        merkleRoot = _merkleRoot;
        baseURI = _baseURI;
    }

    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
    }

    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }

    function claimNFT(bytes32[] calldata merkleProof) external {
        require(!hasClaimed[msg.sender], "NFT already claimed");
        
        // Verify the merkle proof
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(
            MerkleProof.verify(merkleProof, merkleRoot, leaf),
            "Invalid proof"
        );

        hasClaimed[msg.sender] = true;
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(msg.sender, tokenId);

        emit NFTClaimed(msg.sender, tokenId);
    }

    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
