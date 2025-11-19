"""
Generated Code Metadata:
========================
Original URL: https://mega-rabbit.com
Prompt: Develop a code snippet in Solidity to implement a whitelist (WL) and allowlist (FCFS) system for minting NFTs in groups, similar to the MegaRabbit collection.
Generated: DETERMINISTIC_35d01a2f9b7bca21
Batch ID: 20250622_212626
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract NFTMintingGroups is Ownable {
    // Minting phases
    enum Phase {
        Closed,
        Whitelist,
        Allowlist,
        Public
    }

    Phase public currentPhase = Phase.Closed;

    // Whitelist merkle root
    bytes32 public whitelistMerkleRoot;
    // Allowlist merkle root
    bytes32 public allowlistMerkleRoot;

    // Group minting limits
    mapping(address => uint256) public whitelistMinted;
    mapping(address => uint256) public allowlistMinted;

    // Group limits
    uint256 public whitelistMaxPerWallet;
    uint256 public allowlistMaxPerWallet;

    // Total supply tracking
    uint256 public totalSupply;
    uint256 public maxSupply;

    // Events
    event Minted(address indexed minter, uint256 amount, Phase phase);

    constructor(
        uint256 _maxSupply,
        uint256 _whitelistMaxPerWallet,
        uint256 _allowlistMaxPerWallet
    ) {
        maxSupply = _maxSupply;
        whitelistMaxPerWallet = _whitelistMaxPerWallet;
        allowlistMaxPerWallet = _allowlistMaxPerWallet;
    }

    // Set merkle roots
    function setMerkleRoots(bytes32 _whitelistRoot, bytes32 _allowlistRoot) external onlyOwner {
        whitelistMerkleRoot = _whitelistRoot;
        allowlistMerkleRoot = _allowlistRoot;
    }

    // Set minting phase
    function setPhase(Phase _phase) external onlyOwner {
        currentPhase = _phase;
    }

    // Whitelist mint function
    function whitelistMint(uint256 amount, bytes32[] calldata proof) external {
        require(currentPhase == Phase.Whitelist, "Whitelist minting not active");
        require(totalSupply + amount <= maxSupply, "Exceeds max supply");
        require(
            whitelistMinted[msg.sender] + amount <= whitelistMaxPerWallet,
            "Exceeds whitelist limit"
        );

        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(
            MerkleProof.verify(proof, whitelistMerkleRoot, leaf),
            "Invalid proof"
        );

        whitelistMinted[msg.sender] += amount;
        totalSupply += amount;

        emit Minted(msg.sender, amount, Phase.Whitelist);
    }

    // Allowlist mint function
    function allowlistMint(uint256 amount, bytes32[] calldata proof) external {
        require(currentPhase == Phase.Allowlist, "Allowlist minting not active");
        require(totalSupply + amount <= maxSupply, "Exceeds max supply");
        require(
            allowlistMinted[msg.sender] + amount <= allowlistMaxPerWallet,
            "Exceeds allowlist limit"
        );

        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(
            MerkleProof.verify(proof, allowlistMerkleRoot, leaf),
            "Invalid proof"
        );

        allowlistMinted[msg.sender] += amount;
        totalSupply += amount;

        emit Minted(msg.sender, amount, Phase.Allowlist);
    }

    // Public mint function
    function publicMint(uint256 amount) external {
        require(currentPhase == Phase.Public, "Public minting not active");
        require(totalSupply + amount <= maxSupply, "Exceeds max supply");

        totalSupply += amount;

        emit Minted(msg.sender, amount, Phase.Public);
    }

    // Update minting limits
    function updateMintingLimits(
        uint256 _whitelistMaxPerWallet,
        uint256 _allowlistMaxPerWallet
    ) external onlyOwner {
        whitelistMaxPerWallet = _whitelistMaxPerWallet;
        allowlistMaxPerWallet = _allowlistMaxPerWallet;
    }
}
```
