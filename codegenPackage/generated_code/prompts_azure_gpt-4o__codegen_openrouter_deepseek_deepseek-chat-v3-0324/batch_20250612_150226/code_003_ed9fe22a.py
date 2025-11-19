"""
Generated Code Metadata:
========================
Original URL: https://rplanet-io.vercel.app
Prompt: Write a smart contract in Solidity to manage the creation and trading of Hero NFTs in the R-Planet Conquest game.
Generated: DETERMINISTIC_ed9fe22a7a4579c3
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract HeroNFT is ERC721, ERC721Enumerable, Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using Counters for Counters.Counter;

    Counters.Counter private _tokenIdCounter;

    // Hero attributes
    struct Hero {
        string name;
        uint256 strength;
        uint256 agility;
        uint256 intelligence;
        uint256 level;
        uint256 experience;
    }

    // Mapping from token ID to hero attributes
    mapping(uint256 => Hero) private _heroes;

    // Marketplace variables
    struct Listing {
        uint256 price;
        address seller;
    }

    mapping(uint256 => Listing) private _listings;
    uint256 public listingFee = 0.01 ether;
    uint256 public maxLevel = 100;
    uint256 public experienceToLevelUp = 1000;

    // Events
    event HeroMinted(uint256 indexed tokenId, address indexed owner, string name);
    event HeroListed(uint256 indexed tokenId, address indexed seller, uint256 price);
    event HeroUnlisted(uint256 indexed tokenId, address indexed seller);
    event HeroPurchased(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);
    event HeroLevelUp(uint256 indexed tokenId, uint256 newLevel);

    constructor() ERC721("R-Planet Hero", "RPH") {}

    // Modifiers
    modifier onlyTokenOwner(uint256 tokenId) {
        require(ownerOf(tokenId) == msg.sender, "Not the token owner");
        _;
    }

    modifier notListed(uint256 tokenId) {
        require(_listings[tokenId].seller == address(0), "Hero already listed");
        _;
    }

    modifier isListed(uint256 tokenId) {
        require(_listings[tokenId].seller != address(0), "Hero not listed");
        _;
    }

    // Mint a new hero
    function mintHero(
        string memory name,
        uint256 strength,
        uint256 agility,
        uint256 intelligence
    ) public payable nonReentrant {
        require(bytes(name).length > 0, "Name cannot be empty");
        require(strength > 0 && agility > 0 && intelligence > 0, "Stats must be positive");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _heroes[tokenId] = Hero({
            name: name,
            strength: strength,
            agility: agility,
            intelligence: intelligence,
            level: 1,
            experience: 0
        });

        _safeMint(msg.sender, tokenId);
        emit HeroMinted(tokenId, msg.sender, name);
    }

    // List hero for sale
    function listHero(uint256 tokenId, uint256 price) public payable onlyTokenOwner(tokenId) notListed(tokenId) {
        require(price > 0, "Price must be greater than 0");
        require(msg.value >= listingFee, "Insufficient listing fee");

        _listings[tokenId] = Listing({
            price: price,
            seller: msg.sender
        });

        emit HeroListed(tokenId, msg.sender, price);
    }

    // Unlist hero from sale
    function unlistHero(uint256 tokenId) public onlyTokenOwner(tokenId) isListed(tokenId) {
        delete _listings[tokenId];
        emit HeroUnlisted(tokenId, msg.sender);
    }

    // Purchase a listed hero
    function purchaseHero(uint256 tokenId) public payable nonReentrant isListed(tokenId) {
        Listing memory listing = _listings[tokenId];
        require(msg.value >= listing.price, "Insufficient funds");
        require(msg.sender != listing.seller, "Cannot buy your own hero");

        address seller = listing.seller;
        uint256 price = listing.price;
        uint256 fee = price.mul(5).div(100); // 5% fee
        uint256 sellerProceeds = price.sub(fee);

        delete _listings[tokenId];
        _transfer(seller, msg.sender, tokenId);

        payable(seller).transfer(sellerProceeds);
        payable(owner()).transfer(fee);

        emit HeroPurchased(tokenId, msg.sender, seller, price);
    }

    // Add experience to hero
    function addExperience(uint256 tokenId, uint256 experience) public onlyTokenOwner(tokenId) {
        Hero storage hero = _heroes[tokenId];
        hero.experience = hero.experience.add(experience);

        // Check for level up
        uint256 requiredExp = hero.level.mul(experienceToLevelUp);
        if (hero.experience >= requiredExp && hero.level < maxLevel) {
            hero.level = hero.level.add(1);
            hero.strength = hero.strength.add(10);
            hero.agility = hero.agility.add(10);
            hero.intelligence = hero.intelligence.add(10);
            emit HeroLevelUp(tokenId, hero.level);
        }
    }

    // Get hero details
    function getHero(uint256 tokenId) public view returns (
        string memory name,
        uint256 strength,
        uint256 agility,
        uint256 intelligence,
        uint256 level,
        uint256 experience
    ) {
        Hero memory hero = _heroes[tokenId];
        return (
            hero.name,
            hero.strength,
            hero.agility,
            hero.intelligence,
            hero.level,
            hero.experience
        );
    }

    // Get listing details
    function getListing(uint256 tokenId) public view returns (uint256 price, address seller) {
        Listing memory listing = _listings[tokenId];
        return (listing.price, listing.seller);
    }

    // Update listing fee (owner only)
    function setListingFee(uint256 fee) public onlyOwner {
        listingFee = fee;
    }

    // Withdraw contract balance (owner only)
    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Override required by Solidity
    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
