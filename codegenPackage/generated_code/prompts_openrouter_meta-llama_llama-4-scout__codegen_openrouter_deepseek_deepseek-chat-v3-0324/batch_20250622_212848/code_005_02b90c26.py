"""
Generated Code Metadata:
========================
Original URL: https://apygate.com
Prompt: Create a code example for a decentralized launchpad that allows users to buy NFTs, claim rewards, and participate in presales, using a variety of wallet options.
Generated: DETERMINISTIC_02b90c26c708377f
Batch ID: 20250622_212848
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

contract DecentralizedLaunchpad is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Struct to store presale information
    struct Presale {
        uint256 price;
        uint256 maxSupply;
        uint256 startTime;
        uint256 endTime;
        bytes32 merkleRoot;
        mapping(address => bool) claimed;
    }

    // Struct to store reward information
    struct Reward {
        uint256 amount;
        bool claimed;
    }

    // NFT properties
    string private _baseTokenURI;
    uint256 public maxSupply;
    uint256 public publicSalePrice;
    bool public publicSaleActive;

    // Presale information
    Presale public presale;
    
    // Rewards mapping
    mapping(uint256 => Reward) public rewards;
    mapping(address => uint256[]) public userRewards;

    // Events
    event NFTMinted(address indexed owner, uint256 tokenId);
    event PresalePurchased(address indexed buyer, uint256 tokenId);
    event RewardClaimed(address indexed user, uint256 rewardId, uint256 amount);
    event PublicSaleStateChanged(bool isActive);

    constructor(
        string memory name,
        string memory symbol,
        string memory baseURI,
        uint256 _maxSupply,
        uint256 _publicSalePrice
    ) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
        maxSupply = _maxSupply;
        publicSalePrice = _publicSalePrice;
    }

    // Modifier to check if public sale is active
    modifier isPublicSaleActive() {
        require(publicSaleActive, "Public sale is not active");
        _;
    }

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(
            block.timestamp >= presale.startTime && block.timestamp <= presale.endTime,
            "Presale is not active"
        );
        _;
    }

    // Function to set presale parameters
    function setPresale(
        uint256 price,
        uint256 _maxSupply,
        uint256 startTime,
        uint256 endTime,
        bytes32 merkleRoot
    ) external onlyOwner {
        presale.price = price;
        presale.maxSupply = _maxSupply;
        presale.startTime = startTime;
        presale.endTime = endTime;
        presale.merkleRoot = merkleRoot;
    }

    // Function to toggle public sale state
    function togglePublicSaleState() external onlyOwner {
        publicSaleActive = !publicSaleActive;
        emit PublicSaleStateChanged(publicSaleActive);
    }

    // Function to mint NFT during public sale
    function mintPublicSale() external payable isPublicSaleActive nonReentrant {
        require(msg.value == publicSalePrice, "Incorrect ETH amount");
        require(totalSupply() < maxSupply, "Max supply reached");
        
        _safeMint(msg.sender, _tokenIdCounter.current());
        emit NFTMinted(msg.sender, _tokenIdCounter.current());
        _tokenIdCounter.increment();
    }

    // Function to mint NFT during presale
    function mintPresale(bytes32[] calldata merkleProof) external payable isPresaleActive nonReentrant {
        require(!presale.claimed[msg.sender], "Already claimed presale");
        require(msg.value == presale.price, "Incorrect ETH amount");
        require(totalSupply() < presale.maxSupply, "Presale max supply reached");
        
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(MerkleProof.verify(merkleProof, presale.merkleRoot, leaf), "Invalid proof");
        
        presale.claimed[msg.sender] = true;
        _safeMint(msg.sender, _tokenIdCounter.current());
        emit PresalePurchased(msg.sender, _tokenIdCounter.current());
        _tokenIdCounter.increment();
    }

    // Function to add rewards for users
    function addReward(address user, uint256 amount) external onlyOwner {
        uint256 rewardId = _tokenIdCounter.current();
        rewards[rewardId] = Reward(amount, false);
        userRewards[user].push(rewardId);
        _tokenIdCounter.increment();
    }

    // Function to claim rewards
    function claimReward(uint256 rewardId) external nonReentrant {
        require(userHasReward(msg.sender, rewardId), "Reward not found");
        require(!rewards[rewardId].claimed, "Reward already claimed");
        
        rewards[rewardId].claimed = true;
        payable(msg.sender).transfer(rewards[rewardId].amount);
        emit RewardClaimed(msg.sender, rewardId, rewards[rewardId].amount);
    }

    // Helper function to check if user has a specific reward
    function userHasReward(address user, uint256 rewardId) public view returns (bool) {
        for (uint256 i = 0; i < userRewards[user].length; i++) {
            if (userRewards[user][i] == rewardId) {
                return true;
            }
        }
        return false;
    }

    // Function to get total supply
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    // Function to withdraw funds
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Override base URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to set base URI
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }
}
```
