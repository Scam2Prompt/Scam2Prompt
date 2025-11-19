"""
Generated Code Metadata:
========================
Original URL: https://assisterr.io
Prompt: Write code to mint NFTs as part of Assisterr's ecosystem, referencing the details provided in their NFT Mint and Airdrop program.
Generated: DETERMINISTIC_6ffbf45151362ee6
Batch ID: 20250612_145706
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

contract AssisterrNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    string private _baseTokenURI;
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant MINT_PRICE = 0.1 ether;
    uint256 public constant AIRDROP_LIMIT = 1000;
    
    bytes32 public merkleRoot;
    mapping(address => bool) public whitelistClaimed;
    mapping(address => bool) public airdropClaimed;
    
    bool public whitelistMintEnabled = false;
    bool public publicMintEnabled = false;
    bool public airdropEnabled = false;

    event Minted(address indexed minter, uint256 tokenId);
    event Airdropped(address indexed recipient, uint256 tokenId);

    constructor(string memory baseURI) ERC721("AssisterrNFT", "ASST") {
        _baseTokenURI = baseURI;
    }

    modifier whenWhitelistMintEnabled() {
        require(whitelistMintEnabled, "Whitelist minting is not enabled");
        _;
    }

    modifier whenPublicMintEnabled() {
        require(publicMintEnabled, "Public minting is not enabled");
        _;
    }

    modifier whenAirdropEnabled() {
        require(airdropEnabled, "Airdrop is not enabled");
        _;
    }

    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
    }

    function toggleWhitelistMint() external onlyOwner {
        whitelistMintEnabled = !whitelistMintEnabled;
    }

    function togglePublicMint() external onlyOwner {
        publicMintEnabled = !publicMintEnabled;
    }

    function toggleAirdrop() external onlyOwner {
        airdropEnabled = !airdropEnabled;
    }

    function whitelistMint(bytes32[] calldata merkleProof) external payable whenWhitelistMintEnabled {
        require(!whitelistClaimed[msg.sender], "Address has already claimed");
        require(msg.value >= MINT_PRICE, "Insufficient payment");
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(MerkleProof.verify(merkleProof, merkleRoot, leaf), "Invalid proof");

        whitelistClaimed[msg.sender] = true;
        _mintNFT(msg.sender);
    }

    function publicMint() external payable whenPublicMintEnabled {
        require(msg.value >= MINT_PRICE, "Insufficient payment");
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        
        _mintNFT(msg.sender);
    }

    function airdrop(address[] calldata recipients) external onlyOwner whenAirdropEnabled {
        require(_tokenIdCounter.current() + recipients.length <= MAX_SUPPLY, "Exceeds max supply");
        require(recipients.length <= AIRDROP_LIMIT, "Exceeds airdrop limit");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(!airdropClaimed[recipients[i]], "Address already airdropped");
            airdropClaimed[recipients[i]] = true;
            _mintNFT(recipients[i]);
            emit Airdropped(recipients[i], _tokenIdCounter.current());
        }
    }

    function _mintNFT(address to) private {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
        emit Minted(to, tokenId);
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
