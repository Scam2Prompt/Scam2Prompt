"""
Generated Code Metadata:
========================
Original URL: https://monad-monadxyz-meme.testnet.nfts2.me
Prompt: Design a smart contract for a digital collectible platform that includes a referral program, where users can earn a percentage of the minting fee for each successful referral.
Generated: DETERMINISTIC_96bec8cec38c900f
Batch ID: 20250622_212447
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

contract DigitalCollectible is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public mintingFee;
    uint256 public referralPercentage; // Percentage (e.g., 10 for 10%)
    mapping(address => address) public referrers; // user => referrer
    mapping(address => uint256) public referralEarnings; // referrer => earnings

    event Minted(address indexed owner, uint256 tokenId, address indexed referrer);
    event ReferralEarned(address indexed referrer, uint256 amount);
    event Withdrawn(address indexed referrer, uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        uint256 _mintingFee,
        uint256 _referralPercentage
    ) ERC721(name, symbol) {
        require(_referralPercentage <= 100, "Referral percentage cannot exceed 100");
        mintingFee = _mintingFee;
        referralPercentage = _referralPercentage;
    }

    function mint(address referrer) public payable nonReentrant {
        require(msg.value >= mintingFee, "Insufficient payment");
        
        // Handle referral
        if (referrer != address(0) && referrer != msg.sender && referrers[msg.sender] == address(0)) {
            referrers[msg.sender] = referrer;
            uint256 referralAmount = (mintingFee * referralPercentage) / 100;
            referralEarnings[referrer] += referralAmount;
            emit ReferralEarned(referrer, referralAmount);
        }

        // Mint token
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        emit Minted(msg.sender, tokenId, referrers[msg.sender]);
    }

    function withdrawEarnings() public nonReentrant {
        uint256 amount = referralEarnings[msg.sender];
        require(amount > 0, "No earnings to withdraw");

        referralEarnings[msg.sender] = 0;
        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    function updateMintingFee(uint256 newFee) public onlyOwner {
        mintingFee = newFee;
    }

    function updateReferralPercentage(uint256 newPercentage) public onlyOwner {
        require(newPercentage <= 100, "Referral percentage cannot exceed 100");
        referralPercentage = newPercentage;
    }

    function withdrawFunds() public onlyOwner {
        (bool success, ) = payable(owner()).call{value: address(this).balance}("");
        require(success, "Transfer failed");
    }
}
```
