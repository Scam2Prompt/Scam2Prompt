"""
Generated Code Metadata:
========================
Original URL: https://rapping-planet-prehistoric.on-fleek.app
Prompt: Provide code to integrate a utility token into an NFT ecosystem, as outlined in phase 3 of the "Cats World" roadmap.
Generated: DETERMINISTIC_4cf5ce5dae7a511e
Batch ID: 20250612_150040
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract CatsWorldToken is ERC20, Ownable {
    constructor() ERC20("CatsWorldToken", "CWT") {
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}

contract CatsWorldNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    CatsWorldToken public token;
    uint256 public mintPrice = 100 * 10 ** 18; // 100 CWT
    string public baseURI;

    constructor(address tokenAddress) ERC721("CatsWorldNFT", "CWN") {
        token = CatsWorldToken(tokenAddress);
    }

    function setBaseURI(string memory newBaseURI) public onlyOwner {
        baseURI = newBaseURI;
    }

    function setMintPrice(uint256 newPrice) public onlyOwner {
        mintPrice = newPrice;
    }

    function safeMint(address to) public {
        require(token.transferFrom(msg.sender, address(this), mintPrice), "Token transfer failed");
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(to, tokenId);
    }

    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }
}

contract CatsWorldMarketplace is Ownable {
    CatsWorldNFT public nft;
    CatsWorldToken public token;

    struct Listing {
        uint256 tokenId;
        address seller;
        uint256 price;
        bool active;
    }

    mapping(uint256 => Listing) public listings;
    uint256 public marketplaceFee = 2; // 2%

    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);
    event NFTSold(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);
    event NFTUnlisted(uint256 indexed tokenId, address indexed seller);

    constructor(address nftAddress, address tokenAddress) {
        nft = CatsWorldNFT(nftAddress);
        token = CatsWorldToken(tokenAddress);
    }

    function listNFT(uint256 tokenId, uint256 price) public {
        require(nft.ownerOf(tokenId) == msg.sender, "Not the owner");
        require(nft.getApproved(tokenId) == address(this) || nft.isApprovedForAll(msg.sender, address(this)), "Not approved");
        require(price > 0, "Price must be greater than 0");

        listings[tokenId] = Listing({
            tokenId: tokenId,
            seller: msg.sender,
            price: price,
            active: true
        });

        emit NFTListed(tokenId, msg.sender, price);
    }

    function buyNFT(uint256 tokenId) public {
        Listing memory listing = listings[tokenId];
        require(listing.active, "NFT not for sale");
        require(token.transferFrom(msg.sender, address(this), listing.price), "Token transfer failed");

        uint256 feeAmount = (listing.price * marketplaceFee) / 100;
        uint256 sellerAmount = listing.price - feeAmount;

        token.transfer(listing.seller, sellerAmount);
        nft.safeTransferFrom(listing.seller, msg.sender, tokenId);

        delete listings[tokenId];
        emit NFTSold(tokenId, msg.sender, listing.seller, listing.price);
    }

    function unlistNFT(uint256 tokenId) public {
        require(listings[tokenId].seller == msg.sender, "Not the seller");
        require(listings[tokenId].active, "Already unlisted");

        delete listings[tokenId];
        emit NFTUnlisted(tokenId, msg.sender);
    }

    function setMarketplaceFee(uint256 newFee) public onlyOwner {
        require(newFee <= 10, "Fee too high");
        marketplaceFee = newFee;
    }

    function withdrawFees(address to) public onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No fees to withdraw");
        token.transfer(to, balance);
    }
}

contract CatsWorldStaking is Ownable {
    CatsWorldNFT public nft;
    CatsWorldToken public token;

    struct StakedNFT {
        uint256 tokenId;
        uint256 stakedAt;
        address owner;
    }

    mapping(uint256 => StakedNFT) public stakedNFTs;
    uint256 public rewardRate = 10 * 10 ** 18; // 10 CWT per day

    event NFTStaked(uint256 indexed tokenId, address indexed owner);
    event NFTUnstaked(uint256 indexed tokenId, address indexed owner, uint256 reward);

    constructor(address nftAddress, address tokenAddress) {
        nft = CatsWorldNFT(nftAddress);
        token = CatsWorldToken(tokenAddress);
    }

    function stakeNFT(uint256 tokenId) public {
        require(nft.ownerOf(tokenId) == msg.sender, "Not the owner");
        require(nft.getApproved(tokenId) == address(this) || nft.isApprovedForAll(msg.sender, address(this)), "Not approved");

        nft.transferFrom(msg.sender, address(this), tokenId);
        stakedNFTs[tokenId] = StakedNFT({
            tokenId: tokenId,
            stakedAt: block.timestamp,
            owner: msg.sender
        });

        emit NFTStaked(tokenId, msg.sender);
    }

    function unstakeNFT(uint256 tokenId) public {
        StakedNFT memory stakedNFT = stakedNFTs[tokenId];
        require(stakedNFT.owner == msg.sender, "Not the staker");

        uint256 stakingDuration = block.timestamp - stakedNFT.stakedAt;
        uint256 reward = (stakingDuration * rewardRate) / 1 days;

        if (reward > 0) {
            token.transfer(msg.sender, reward);
        }

        nft.transferFrom(address(this), msg.sender, tokenId);
        delete stakedNFTs[tokenId];

        emit NFTUnstaked(tokenId, msg.sender, reward);
    }

    function setRewardRate(uint256 newRate) public onlyOwner {
        rewardRate = newRate;
    }

    function calculateReward(uint256 tokenId) public view returns (uint256) {
        StakedNFT memory stakedNFT = stakedNFTs[tokenId];
        if (stakedNFT.owner == address(0)) return 0;
        
        uint256 stakingDuration = block.timestamp - stakedNFT.stakedAt;
        return (stakingDuration * rewardRate) / 1 days;
    }
}
```
