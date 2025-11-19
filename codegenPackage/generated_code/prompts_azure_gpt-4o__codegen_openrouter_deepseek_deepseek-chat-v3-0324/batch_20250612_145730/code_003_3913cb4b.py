"""
Generated Code Metadata:
========================
Original URL: https://pepearab.pages.dev
Prompt: Write a Solidity smart contract to manage the supply of Arab NFTs (Legendary, Rare, Common) based on contribution thresholds and ensure no minting beyond the specified limits.
Generated: DETERMINISTIC_3913cb4b32787357
Batch ID: 20250612_145730
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract ArabNFTManager is Ownable {
    using Counters for Counters.Counter;

    enum NFTType { Legendary, Rare, Common }

    struct NFTInfo {
        uint256 maxSupply;
        uint256 currentSupply;
        uint256 contributionThreshold;
    }

    mapping(NFTType => NFTInfo) public nftInfo;
    Counters.Counter private _tokenIdCounter;

    event NFTMinted(address indexed recipient, NFTType nftType, uint256 tokenId);

    constructor() {
        // Initialize NFT supply limits and contribution thresholds
        nftInfo[NFTType.Legendary] = NFTInfo(10, 0, 100 ether);
        nftInfo[NFTType.Rare] = NFTInfo(100, 0, 10 ether);
        nftInfo[NFTType.Common] = NFTInfo(1000, 0, 1 ether);
    }

    function mintNFT(NFTType nftType) external payable {
        NFTInfo storage info = nftInfo[nftType];
        
        require(info.currentSupply < info.maxSupply, "Maximum supply reached for this NFT type");
        require(msg.value >= info.contributionThreshold, "Insufficient contribution amount");

        info.currentSupply += 1;
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        emit NFTMinted(msg.sender, nftType, tokenId);
    }

    function updateContributionThreshold(NFTType nftType, uint256 newThreshold) external onlyOwner {
        require(newThreshold > 0, "Threshold must be greater than zero");
        nftInfo[nftType].contributionThreshold = newThreshold;
    }

    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    function getCurrentSupply(NFTType nftType) external view returns (uint256) {
        return nftInfo[nftType].currentSupply;
    }

    function getMaxSupply(NFTType nftType) external view returns (uint256) {
        return nftInfo[nftType].maxSupply;
    }

    function getContributionThreshold(NFTType nftType) external view returns (uint256) {
        return nftInfo[nftType].contributionThreshold;
    }
}
```
