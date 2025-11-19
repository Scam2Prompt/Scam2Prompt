"""
Generated Code Metadata:
========================
Original URL: https://simpsontrump.pages.dev
Prompt: Generate a smart contract in Solidity for minting AI-generated NFTs, aligning with the Simpson Trump ($TRUMP) project's roadmap.
Generated: DETERMINISTIC_b655e95848c6c270
Batch ID: 20250612_150226
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
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract SimpsonTrumpNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;
    
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;
    
    // Mint price
    uint256 public mintPrice = 0.1 ether;
    
    // Whitelist merkle root
    bytes32 public merkleRoot;
    
    // Minting phases
    enum MintPhase {
        CLOSED,
        WHITELIST,
        PUBLIC
    }
    
    MintPhase public currentPhase = MintPhase.CLOSED;
    
    // Mapping to track minted tokens per address
    mapping(address => uint256) public mintedPerAddress;
    
    // Mapping to track whitelist mints
    mapping(address => bool) public whitelistMinted;
    
    // Events
    event Minted(address indexed minter, uint256 tokenId);
    event BaseURIUpdated(string newBaseURI);
    event MintPhaseChanged(MintPhase newPhase);
    event MintPriceUpdated(uint256 newPrice);
    event MerkleRootUpdated(bytes32 newRoot);

    constructor(
        string memory name,
        string memory symbol,
        string memory baseURI
    ) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    // Modifier to check mint phase
    modifier isMintPhase(MintPhase phase) {
        require(currentPhase == phase, "Minting not allowed in current phase");
        _;
    }

    // Modifier to check payment
    modifier correctPayment(uint256 quantity) {
        require(msg.value >= mintPrice * quantity, "Incorrect ETH amount");
        _;
    }

    // Modifier to check supply
    modifier withinSupply(uint256 quantity) {
        require(_tokenIdCounter.current() + quantity <= MAX_SUPPLY, "Exceeds max supply");
        _;
    }

    // Whitelist mint function
    function whitelistMint(
        uint256 quantity,
        bytes32[] calldata merkleProof
    ) 
        external 
        payable 
        isMintPhase(MintPhase.WHITELIST)
        correctPayment(quantity)
        withinSupply(quantity)
    {
        require(!whitelistMinted[msg.sender], "Already minted in whitelist");
        require(verifyWhitelist(msg.sender, merkleProof), "Not whitelisted");
        
        whitelistMinted[msg.sender] = true;
        _mintNFTs(msg.sender, quantity);
    }

    // Public mint function
    function publicMint(uint256 quantity) 
        external 
        payable 
        isMintPhase(MintPhase.PUBLIC)
        correctPayment(quantity)
        withinSupply(quantity)
    {
        _mintNFTs(msg.sender, quantity);
    }

    // Owner mint function
    function ownerMint(address to, uint256 quantity) 
        external 
        onlyOwner 
        withinSupply(quantity)
    {
        _mintNFTs(to, quantity);
    }

    // Internal mint function
    function _mintNFTs(address to, uint256 quantity) internal {
        for (uint256 i = 0; i < quantity; i++) {
            _tokenIdCounter.increment();
            uint256 tokenId = _tokenIdCounter.current();
            _safeMint(to, tokenId);
            emit Minted(to, tokenId);
        }
    }

    // Verify whitelist status
    function verifyWhitelist(address account, bytes32[] calldata merkleProof) 
        public 
        view 
        returns (bool) 
    {
        bytes32 leaf = keccak256(abi.encodePacked(account));
        return MerkleProof.verify(merkleProof, merkleRoot, leaf);
    }

    // Set base URI
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
        emit BaseURIUpdated(baseURI);
    }

    // Set mint price
    function setMintPrice(uint256 price) external onlyOwner {
        mintPrice = price;
        emit MintPriceUpdated(price);
    }

    // Set merkle root
    function setMerkleRoot(bytes32 root) external onlyOwner {
        merkleRoot = root;
        emit MerkleRootUpdated(root);
    }

    // Set mint phase
    function setMintPhase(MintPhase phase) external onlyOwner {
        currentPhase = phase;
        emit MintPhaseChanged(phase);
    }

    // Withdraw funds
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        payable(owner()).transfer(balance);
    }

    // Override tokenURI
    function tokenURI(uint256 tokenId) 
        public 
        view 
        override 
        returns (string memory) 
    {
        require(_exists(tokenId), "Token does not exist");
        return string(abi.encodePacked(_baseTokenURI, tokenId.toString(), ".json"));
    }

    // Get total minted count
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
