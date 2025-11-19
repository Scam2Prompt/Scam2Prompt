"""
Generated Code Metadata:
========================
Original URL: https://zora-7pj.pages.dev
Prompt: Write a smart contract that facilitates minting commemorative NFTs for Reveel Campaigns, ensuring rewards are unlocked for holders.
Generated: DETERMINISTIC_10ad46fe43beb0b6
Batch ID: 20250612_151117
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

contract ReveelCommemorativeNFT is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct Reward {
        bool isUnlocked;
        string rewardURI;
    }

    mapping(uint256 => Reward) private _tokenRewards;
    mapping(address => bool) private _authorizedMinters;
    string private _baseTokenURI;
    bool public mintingEnabled = false;

    event NFTMinted(address indexed recipient, uint256 tokenId);
    event RewardUnlocked(uint256 indexed tokenId, string rewardURI);
    event MinterAdded(address indexed minter);
    event MinterRemoved(address indexed minter);

    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    modifier onlyMinter() {
        require(_authorizedMinters[msg.sender] || msg.sender == owner(), "Not authorized");
        _;
    }

    modifier whenMintingEnabled() {
        require(mintingEnabled, "Minting is disabled");
        _;
    }

    function addMinter(address minter) external onlyOwner {
        require(minter != address(0), "Invalid address");
        _authorizedMinters[minter] = true;
        emit MinterAdded(minter);
    }

    function removeMinter(address minter) external onlyOwner {
        require(_authorizedMinters[minter], "Not a minter");
        _authorizedMinters[minter] = false;
        emit MinterRemoved(minter);
    }

    function toggleMinting() external onlyOwner {
        mintingEnabled = !mintingEnabled;
    }

    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    function mintNFT(address recipient) external onlyMinter whenMintingEnabled nonReentrant returns (uint256) {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(recipient, tokenId);
        
        _tokenRewards[tokenId] = Reward({
            isUnlocked: false,
            rewardURI: ""
        });

        emit NFTMinted(recipient, tokenId);
        return tokenId;
    }

    function unlockReward(uint256 tokenId, string memory rewardURI) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        require(!_tokenRewards[tokenId].isUnlocked, "Reward already unlocked");

        _tokenRewards[tokenId].isUnlocked = true;
        _tokenRewards[tokenId].rewardURI = rewardURI;

        emit RewardUnlocked(tokenId, rewardURI);
    }

    function getRewardInfo(uint256 tokenId) external view returns (bool isUnlocked, string memory rewardURI) {
        require(_exists(tokenId), "Token does not exist");
        Reward memory reward = _tokenRewards[tokenId];
        return (reward.isUnlocked, reward.rewardURI);
    }

    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    function isMinter(address account) external view returns (bool) {
        return _authorizedMinters[account];
    }
}
```
