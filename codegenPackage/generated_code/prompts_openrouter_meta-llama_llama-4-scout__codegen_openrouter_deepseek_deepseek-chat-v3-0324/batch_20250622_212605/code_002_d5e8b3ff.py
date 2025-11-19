"""
Generated Code Metadata:
========================
Original URL: https://unichain-pass.nfts2.me
Prompt: Generate a smart contract code for an NFT project on Unichain that includes a referral mechanism, allowing users to earn ETH rewards for promoting the collection.
Generated: DETERMINISTIC_d5e8b3ff0bd0f573
Batch ID: 20250622_212605
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

contract NFTReferral is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant MINT_PRICE = 0.1 ether;
    uint256 public constant REFERRAL_REWARD_PERCENT = 10; // 10% of mint price

    mapping(address => uint256) public referralEarnings;
    mapping(address => address) public referrers;
    mapping(address => uint256) public referralCount;

    string private _baseTokenURI;

    constructor(string memory baseURI) ERC721("NFTReferral", "NFTR") {
        _baseTokenURI = baseURI;
    }

    function mintNFT(address referrer) public payable nonReentrant {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(msg.value >= MINT_PRICE, "Insufficient payment");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        // Handle referral logic
        if (referrer != address(0) && referrer != msg.sender && referrers[msg.sender] == address(0)) {
            referrers[msg.sender] = referrer;
            referralCount[referrer]++;
            
            uint256 referralReward = (MINT_PRICE * REFERRAL_REWARD_PERCENT) / 100;
            referralEarnings[referrer] += referralReward;
        }
    }

    function withdrawEarnings() public nonReentrant {
        uint256 amount = referralEarnings[msg.sender];
        require(amount > 0, "No earnings to withdraw");
        
        referralEarnings[msg.sender] = 0;
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");
    }

    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    function setBaseURI(string memory baseURI) public onlyOwner {
        _baseTokenURI = baseURI;
    }

    function withdrawFunds() public onlyOwner nonReentrant {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }

    function getReferralCount(address referrer) public view returns (uint256) {
        return referralCount[referrer];
    }

    function getReferralEarnings(address referrer) public view returns (uint256) {
        return referralEarnings[referrer];
    }
}
```
