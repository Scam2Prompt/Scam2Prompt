"""
Generated Code Metadata:
========================
Original URL: https://dioneprotocol-app.pages.dev
Prompt: Write a Solidity contract for an NFT collection inspired by celestial narratives, similar to the Elysium88 collection on Odyssey Chain. Include features for storyline integration and staking boosts.
Generated: DETERMINISTIC_bdc5055f62a252d6
Batch ID: 20250612_153527
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract CelestialNarratives is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Storyline data structure
    struct Chapter {
        string title;
        string contentURI;
        uint256 unlockTimestamp;
    }

    // Staking data structure
    struct StakedToken {
        uint256 tokenId;
        uint256 stakedAt;
        address owner;
    }

    // Constants
    uint256 public constant STAKING_BOOST_BASE = 10; // 10% base boost
    uint256 public constant STAKING_BOOST_PER_DAY = 1; // 1% per day
    uint256 public constant MAX_STAKING_DAYS = 90; // Max 90 days (100% max boost)

    // Variables
    string private _baseTokenURI;
    uint256 public maxSupply;
    uint256 public mintPrice;
    bool public mintingEnabled;
    Chapter[] public chapters;
    mapping(uint256 => StakedToken) public stakedTokens;
    mapping(address => uint256[]) public stakedTokensByOwner;

    // Events
    event ChapterAdded(uint256 chapterId, string title, uint256 unlockTimestamp);
    event Minted(address indexed to, uint256 tokenId);
    event Staked(address indexed owner, uint256 tokenId);
    event Unstaked(address indexed owner, uint256 tokenId, uint256 boostEarned);
    event StorylineUnlocked(uint256 tokenId, uint256 chapterId);

    constructor(
        string memory name,
        string memory symbol,
        string memory baseURI,
        uint256 _maxSupply,
        uint256 _mintPrice
    ) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
        mintingEnabled = false;
    }

    // Modifiers
    modifier onlyTokenOwner(uint256 tokenId) {
        require(ownerOf(tokenId) == msg.sender, "Not token owner");
        _;
    }

    modifier whenMintingEnabled() {
        require(mintingEnabled, "Minting disabled");
        _;
    }

    // Minting functions
    function toggleMinting() external onlyOwner {
        mintingEnabled = !mintingEnabled;
    }

    function mint(address to) external payable whenMintingEnabled nonReentrant {
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");
        require(msg.value >= mintPrice, "Insufficient payment");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);

        emit Minted(to, tokenId);
    }

    // Storyline functions
    function addChapter(
        string memory title,
        string memory contentURI,
        uint256 unlockTimestamp
    ) external onlyOwner {
        chapters.push(Chapter(title, contentURI, unlockTimestamp));
        emit ChapterAdded(chapters.length - 1, title, unlockTimestamp);
    }

    function unlockStoryline(uint256 tokenId, uint256 chapterId)
        external
        onlyTokenOwner(tokenId)
    {
        require(chapterId < chapters.length, "Invalid chapter");
        require(
            block.timestamp >= chapters[chapterId].unlockTimestamp,
            "Chapter locked"
        );

        emit StorylineUnlocked(tokenId, chapterId);
    }

    // Staking functions
    function stake(uint256 tokenId) external onlyTokenOwner(tokenId) {
        require(stakedTokens[tokenId].stakedAt == 0, "Already staked");

        stakedTokens[tokenId] = StakedToken({
            tokenId: tokenId,
            stakedAt: block.timestamp,
            owner: msg.sender
        });

        stakedTokensByOwner[msg.sender].push(tokenId);
        emit Staked(msg.sender, tokenId);
    }

    function unstake(uint256 tokenId) external nonReentrant {
        require(stakedTokens[tokenId].owner == msg.sender, "Not staker");
        require(stakedTokens[tokenId].stakedAt > 0, "Not staked");

        uint256 stakedAt = stakedTokens[tokenId].stakedAt;
        uint256 stakingDuration = (block.timestamp - stakedAt) / 1 days;
        uint256 boost = calculateBoost(stakingDuration);

        delete stakedTokens[tokenId];
        removeStakedToken(msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId, boost);
    }

    function calculateBoost(uint256 stakingDays) public pure returns (uint256) {
        if (stakingDays > MAX_STAKING_DAYS) {
            stakingDays = MAX_STAKING_DAYS;
        }
        return STAKING_BOOST_BASE + (stakingDays * STAKING_BOOST_PER_DAY);
    }

    // Utility functions
    function removeStakedToken(address owner, uint256 tokenId) private {
        uint256[] storage staked = stakedTokensByOwner[owner];
        for (uint256 i = 0; i < staked.length; i++) {
            if (staked[i] == tokenId) {
                staked[i] = staked[staked.length - 1];
                staked.pop();
                break;
            }
        }
    }

    function getStakedTokens(address owner) external view returns (uint256[] memory) {
        return stakedTokensByOwner[owner];
    }

    function getStakingInfo(uint256 tokenId) external view returns (StakedToken memory) {
        return stakedTokens[tokenId];
    }

    function totalChapters() external view returns (uint256) {
        return chapters.length;
    }

    // Overrides
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    // Withdraw funds
    function withdraw() external onlyOwner nonReentrant {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }
}
```
