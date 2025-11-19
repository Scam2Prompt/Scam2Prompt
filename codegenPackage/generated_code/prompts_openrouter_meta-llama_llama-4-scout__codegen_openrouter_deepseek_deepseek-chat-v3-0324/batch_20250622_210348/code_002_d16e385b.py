"""
Generated Code Metadata:
========================
Original URL: https://riftscalingzea.pages.dev
Prompt: Generate a smart contract code for an NFT minting feature similar to the one described on the Rift Swap website.
Generated: DETERMINISTIC_d16e385b325ee7bb
Batch ID: 20250622_210348
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract RiftSwapNFT is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Minting parameters
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant PRICE = 0.08 ether;
    uint256 public constant MAX_PER_WALLET = 5;
    
    // Sale phases
    enum SalePhase {
        CLOSED,
        PRESALE,
        PUBLIC
    }
    SalePhase public currentPhase = SalePhase.CLOSED;

    // Merkle root for allowlist verification
    bytes32 public merkleRoot;

    // Metadata
    string public baseURI;
    string public contractURI;

    // Tracking
    mapping(address => uint256) public mintedPerWallet;

    // Events
    event Minted(address indexed minter, uint256 tokenId);
    event SalePhaseChanged(SalePhase newPhase);
    event BaseURIUpdated(string newBaseURI);
    event ContractURIUpdated(string newContractURI);

    constructor(
        string memory _name,
        string memory _symbol,
        string memory _initBaseURI,
        string memory _initContractURI
    ) ERC721(_name, _symbol) {
        baseURI = _initBaseURI;
        contractURI = _initContractURI;
    }

    // Modifiers
    modifier isCorrectPayment(uint256 quantity) {
        require(msg.value >= PRICE * quantity, "Insufficient payment");
        _;
    }

    modifier isWithinMaxSupply(uint256 quantity) {
        require(_tokenIdCounter.current() + quantity <= MAX_SUPPLY, "Exceeds max supply");
        _;
    }

    modifier isWithinWalletLimit(uint256 quantity) {
        require(
            mintedPerWallet[msg.sender] + quantity <= MAX_PER_WALLET,
            "Exceeds wallet limit"
        );
        _;
    }

    modifier isCorrectPhase(SalePhase requiredPhase) {
        require(currentPhase == requiredPhase, "Sale not active");
        _;
    }

    // Mint functions
    function presaleMint(
        uint256 quantity,
        bytes32[] calldata merkleProof
    )
        external
        payable
        nonReentrant
        isCorrectPayment(quantity)
        isWithinMaxSupply(quantity)
        isWithinWalletLimit(quantity)
        isCorrectPhase(SalePhase.PRESALE)
    {
        require(
            MerkleProof.verify(
                merkleProof,
                merkleRoot,
                keccak256(abi.encodePacked(msg.sender))
            ),
            "Not on allowlist"
        );

        _mintNFTs(msg.sender, quantity);
    }

    function publicMint(uint256 quantity)
        external
        payable
        nonReentrant
        isCorrectPayment(quantity)
        isWithinMaxSupply(quantity)
        isWithinWalletLimit(quantity)
        isCorrectPhase(SalePhase.PUBLIC)
    {
        _mintNFTs(msg.sender, quantity);
    }

    function _mintNFTs(address to, uint256 quantity) internal {
        for (uint256 i = 0; i < quantity; i++) {
            _tokenIdCounter.increment();
            uint256 tokenId = _tokenIdCounter.current();
            _safeMint(to, tokenId);
            emit Minted(to, tokenId);
        }
        mintedPerWallet[to] += quantity;
    }

    // Admin functions
    function setSalePhase(SalePhase newPhase) external onlyOwner {
        currentPhase = newPhase;
        emit SalePhaseChanged(newPhase);
    }

    function setMerkleRoot(bytes32 newMerkleRoot) external onlyOwner {
        merkleRoot = newMerkleRoot;
    }

    function setBaseURI(string memory newBaseURI) external onlyOwner {
        baseURI = newBaseURI;
        emit BaseURIUpdated(newBaseURI);
    }

    function setContractURI(string memory newContractURI) external onlyOwner {
        contractURI = newContractURI;
        emit ContractURIUpdated(newContractURI);
    }

    function withdraw() external onlyOwner nonReentrant {
        (bool success, ) = msg.sender.call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    // View functions
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }
}
```
