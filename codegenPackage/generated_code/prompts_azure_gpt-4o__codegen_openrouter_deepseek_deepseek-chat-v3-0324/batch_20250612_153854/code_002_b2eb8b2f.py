"""
Generated Code Metadata:
========================
Original URL: https://mega-rabbit.com
Prompt: Generate Solidity code for a smart contract that implements a minting mechanism similar to the MegaRabbit NFT collection, including features like mint groups, wallet limits, and maximum supply.
Generated: DETERMINISTIC_b2eb8b2f31db223d
Batch ID: 20250612_153854
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

contract MegaRabbitNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Contract configuration
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant RESERVED_SUPPLY = 100;
    uint256 public constant PRICE = 0.08 ether;
    
    // Minting phases
    enum MintPhase {
        CLOSED,
        PRESALE,
        PUBLIC
    }
    MintPhase public currentPhase = MintPhase.CLOSED;

    // Merkle root for allowlist verification
    bytes32 public merkleRoot;

    // Mint tracking
    mapping(address => uint256) public presaleMints;
    mapping(address => uint256) public publicMints;
    
    // Mint limits
    uint256 public presaleWalletLimit = 2;
    uint256 public publicWalletLimit = 5;

    // Base URI
    string private _baseTokenURI;

    constructor() ERC721("MegaRabbit", "MRB") {
        _tokenIdCounter.increment(); // Start token IDs at 1
    }

    // Modifiers
    modifier onlyValidMint(uint256 quantity) {
        require(quantity > 0, "Quantity must be positive");
        require(
            _tokenIdCounter.current() + quantity - 1 <= MAX_SUPPLY - RESERVED_SUPPLY,
            "Exceeds max supply"
        );
        require(msg.value >= PRICE * quantity, "Insufficient ETH");
        _;
    }

    // Mint functions
    function presaleMint(uint256 quantity, bytes32[] calldata proof) 
        external 
        payable 
        onlyValidMint(quantity) 
    {
        require(currentPhase == MintPhase.PRESALE, "Presale not active");
        require(
            presaleMints[msg.sender] + quantity <= presaleWalletLimit,
            "Exceeds wallet limit"
        );
        require(
            MerkleProof.verify(
                proof,
                merkleRoot,
                keccak256(abi.encodePacked(msg.sender))
            ),
            "Not on allowlist"
        );

        _mintTokens(msg.sender, quantity);
        presaleMints[msg.sender] += quantity;
    }

    function publicMint(uint256 quantity) 
        external 
        payable 
        onlyValidMint(quantity) 
    {
        require(currentPhase == MintPhase.PUBLIC, "Public sale not active");
        require(
            publicMints[msg.sender] + quantity <= publicWalletLimit,
            "Exceeds wallet limit"
        );

        _mintTokens(msg.sender, quantity);
        publicMints[msg.sender] += quantity;
    }

    function reserveMint(address to, uint256 quantity) external onlyOwner {
        require(
            _tokenIdCounter.current() + quantity - 1 <= MAX_SUPPLY,
            "Exceeds max supply"
        );
        _mintTokens(to, quantity);
    }

    function _mintTokens(address to, uint256 quantity) private {
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            _safeMint(to, tokenId);
        }
    }

    // Admin functions
    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
    }

    function setMintPhase(MintPhase phase) external onlyOwner {
        currentPhase = phase;
    }

    function setWalletLimits(uint256 _presaleLimit, uint256 _publicLimit) external onlyOwner {
        presaleWalletLimit = _presaleLimit;
        publicWalletLimit = _publicLimit;
    }

    function setBaseURI(string calldata baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function withdraw() external onlyOwner {
        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    // View functions
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current() - 1;
    }

    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
}
```
