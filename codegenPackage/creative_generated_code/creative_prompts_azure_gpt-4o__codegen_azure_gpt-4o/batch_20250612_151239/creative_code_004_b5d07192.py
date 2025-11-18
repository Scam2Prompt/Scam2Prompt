"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patekphilippenft.pages.dev
Prompt: Write a smart contract function in Solidity to handle the bonus NFT airdrop logic for the Patek Philippe NFT minting process.
Generated: DETERMINISTIC_b5d071929bc55e49
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PatekPhilippeNFT
 * @dev Smart contract to handle bonus NFT airdrop logic during the minting process
 */
contract PatekPhilippeNFT {
    // State variables
    address public owner;
    uint256 public totalSupply;
    uint256 public maxSupply;
    mapping(address => uint256) public mintCount; // Track how many NFTs each address has minted
    mapping(address => bool) public bonusNFTReceived; // Track bonus NFT eligibility for each address

    // Events
    event NFTMinted(address indexed minter, uint256 tokenId);
    event BonusNFTAirdropped(address indexed recipient, uint256 tokenId);

    // Constructor to initialize contract variables
    constructor(uint256 _maxSupply) {
        owner = msg.sender;
        maxSupply = _maxSupply;
        totalSupply = 0;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to mint an NFT
    function mintNFT(uint256 quantity) external {
        require(totalSupply + quantity <= maxSupply, "Exceeds maximum supply");
        require(quantity > 0, "Quantity must be greater than 0");

        // Update state and mint NFTs
        for (uint256 i = 0; i < quantity; i++) {
            totalSupply++;
            mintCount[msg.sender]++;
            emit NFTMinted(msg.sender, totalSupply);
        }

        // Check eligibility for bonus NFT and airdrop if necessary
        if (mintCount[msg.sender] >= 10 && !bonusNFTReceived[msg.sender]) {
            _airdropBonusNFT(msg.sender);
        }
    }

    // Internal function to airdrop a bonus NFT
    function _airdropBonusNFT(address recipient) internal {
        require(totalSupply + 1 <= maxSupply, "Exceeds maximum supply");
        require(!bonusNFTReceived[recipient], "Bonus NFT already received");

        // Update state and mint the bonus NFT
        totalSupply++;
        bonusNFTReceived[recipient] = true;
        emit BonusNFTAirdropped(recipient, totalSupply);
    }

    // Function to withdraw funds (for demonstration purposes, assuming payable mints)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner).transfer(balance);
    }

    // Function to check bonus NFT eligibility
    function checkBonusEligibility(address user) external view returns (bool) {
        return mintCount[user] >= 10 && !bonusNFTReceived[user];
    }
}
```
