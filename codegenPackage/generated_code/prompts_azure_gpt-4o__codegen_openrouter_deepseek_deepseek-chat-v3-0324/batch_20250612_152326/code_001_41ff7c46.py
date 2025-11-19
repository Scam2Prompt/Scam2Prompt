"""
Generated Code Metadata:
========================
Original URL: https://mainnet-nobody.pages.dev
Prompt: Create a smart contract in Solidity for an NFT minting process that includes features like raffles, airdrops, and refund mechanisms, as described in the "Nobody NFT" project.
Generated: DETERMINISTIC_41ff7c46d730b67c
Batch ID: 20250612_152326
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

contract NobodyNFT is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Contract configuration
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant PRICE = 0.08 ether;
    uint256 public constant MAX_PER_WALLET = 5;
    uint256 public constant RAFFLE_TICKET_PRICE = 0.01 ether;
    uint256 public constant RAFFLE_DURATION = 7 days;

    // Sale phases
    enum SalePhase {
        Closed,
        Presale,
        Public
    }
    SalePhase public currentPhase = SalePhase.Closed;

    // Raffle state
    struct Raffle {
        uint256 endTime;
        uint256 prizePool;
        address[] participants;
        bool isActive;
        address winner;
    }
    Raffle public currentRaffle;

    // Merkle root for allowlist verification
    bytes32 public merkleRoot;

    // Token metadata
    string private _baseTokenURI;

    // Tracking
    mapping(address => uint256) public mintedPerWallet;
    mapping(address => uint256) public raffleTicketsPurchased;
    mapping(address => bool) public hasClaimedAirdrop;

    // Events
    event Minted(address indexed minter, uint256 tokenId);
    event RaffleStarted(uint256 endTime, uint256 prizePool);
    event RaffleTicketPurchased(address indexed participant, uint256 tickets);
    event RaffleWinner(address indexed winner, uint256 prize);
    event AirdropClaimed(address indexed recipient, uint256 tokenId);
    event RefundIssued(address indexed recipient, uint256 amount);

    constructor(string memory baseURI) ERC721("NobodyNFT", "NOBODY") {
        _baseTokenURI = baseURI;
    }

    // Modifiers
    modifier onlyDuringSale() {
        require(currentPhase != SalePhase.Closed, "Sale is not active");
        _;
    }

    modifier onlyPresale() {
        require(currentPhase == SalePhase.Presale, "Presale is not active");
        _;
    }

    modifier onlyPublicSale() {
        require(currentPhase == SalePhase.Public, "Public sale is not active");
        _;
    }

    // Minting functions
    function presaleMint(uint256 quantity, bytes32[] calldata proof) external payable onlyPresale nonReentrant {
        require(isAllowlisted(msg.sender, proof), "Not on allowlist");
        _mintNFTs(quantity);
    }

    function publicMint(uint256 quantity) external payable onlyPublicSale nonReentrant {
        _mintNFTs(quantity);
    }

    function _mintNFTs(uint256 quantity) private {
        require(quantity > 0, "Quantity must be positive");
        require(totalSupply() + quantity <= MAX_SUPPLY, "Exceeds max supply");
        require(mintedPerWallet[msg.sender] + quantity <= MAX_PER_WALLET, "Exceeds max per wallet");
        require(msg.value >= PRICE * quantity, "Insufficient payment");

        mintedPerWallet[msg.sender] += quantity;

        for (uint256 i = 0; i < quantity; i++) {
            _tokenIdCounter.increment();
            uint256 tokenId = _tokenIdCounter.current();
            _safeMint(msg.sender, tokenId);
            emit Minted(msg.sender, tokenId);
        }
    }

    // Raffle functions
    function startRaffle() external onlyOwner {
        require(!currentRaffle.isActive, "Raffle already active");
        currentRaffle = Raffle({
            endTime: block.timestamp + RAFFLE_DURATION,
            prizePool: 0,
            participants: new address[](0),
            isActive: true,
            winner: address(0)
        });
        emit RaffleStarted(currentRaffle.endTime, currentRaffle.prizePool);
    }

    function buyRaffleTickets(uint256 tickets) external payable nonReentrant {
        require(currentRaffle.isActive, "Raffle not active");
        require(block.timestamp < currentRaffle.endTime, "Raffle ended");
        require(tickets > 0, "Must buy at least 1 ticket");
        require(msg.value >= RAFFLE_TICKET_PRICE * tickets, "Insufficient payment");

        currentRaffle.prizePool += msg.value;
        raffleTicketsPurchased[msg.sender] += tickets;

        for (uint256 i = 0; i < tickets; i++) {
            currentRaffle.participants.push(msg.sender);
        }

        emit RaffleTicketPurchased(msg.sender, tickets);
    }

    function drawRaffleWinner() external onlyOwner {
        require(currentRaffle.isActive, "Raffle not active");
        require(block.timestamp >= currentRaffle.endTime, "Raffle not ended");
        require(currentRaffle.participants.length > 0, "No participants");

        uint256 winnerIndex = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty))) % currentRaffle.participants.length;
        currentRaffle.winner = currentRaffle.participants[winnerIndex];
        currentRaffle.isActive = false;

        (bool success, ) = currentRaffle.winner.call{value: currentRaffle.prizePool}("");
        require(success, "Prize transfer failed");

        emit RaffleWinner(currentRaffle.winner, currentRaffle.prizePool);
    }

    // Airdrop functions
    function claimAirdrop(bytes32[] calldata proof) external nonReentrant {
        require(isAirdropEligible(msg.sender, proof), "Not eligible for airdrop");
        require(!hasClaimedAirdrop[msg.sender], "Already claimed airdrop");
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");

        hasClaimedAirdrop[msg.sender] = true;
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(msg.sender, tokenId);

        emit AirdropClaimed(msg.sender, tokenId);
    }

    // Refund functions
    function requestRefund(uint256 tokenId) external nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Not token owner");
        require(currentPhase == SalePhase.Closed, "Refunds only when sale is closed");

        _burn(tokenId);
        (bool success, ) = msg.sender.call{value: PRICE}("");
        require(success, "Refund failed");

        emit RefundIssued(msg.sender, PRICE);
    }

    // Utility functions
    function isAllowlisted(address account, bytes32[] calldata proof) public view returns (bool) {
        bytes32 leaf = keccak256(abi.encodePacked(account));
        return MerkleProof.verify(proof, merkleRoot, leaf);
    }

    function isAirdropEligible(address account, bytes32[] calldata proof) public view returns (bool) {
        bytes32 leaf = keccak256(abi.encodePacked(account));
        return MerkleProof.verify(proof, merkleRoot, leaf);
    }

    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Admin functions
    function setSalePhase(SalePhase phase) external onlyOwner {
        currentPhase = phase;
    }

    function setMerkleRoot(bytes32 root) external onlyOwner {
        merkleRoot = root;
    }

    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function withdraw() external onlyOwner nonReentrant {
        uint256 balance = address(this).balance;
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Overrides
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
}
```
