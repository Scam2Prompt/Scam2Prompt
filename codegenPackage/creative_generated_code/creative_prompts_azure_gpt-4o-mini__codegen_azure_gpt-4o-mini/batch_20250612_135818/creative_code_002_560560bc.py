"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patekphilippenft.pages.dev
Prompt: Generate code for a limited minting function for NFTs that includes bonus airdrops, as seen in the Patek Philippe NFT offering.
Generated: DETERMINISTIC_560560bc492a7498
Batch ID: 20250612_135818
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract LimitedMintingNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Maximum number of NFTs that can be minted
    uint256 public constant MAX_SUPPLY = 1000;

    // Mapping to track if an address has claimed airdrop
    mapping(address => bool) private _airdropClaimed;

    // Event to emit when an NFT is minted
    event NFTMinted(address to, uint256 tokenId);
    
    // Event to emit when an airdrop is claimed
    event AirdropClaimed(address to);

    // Constructor to set NFT name and symbol
    constructor() ERC721("LimitedMintingNFT", "LMNFT") {}

    // Function to mint a new NFT
    function mint() external onlyOwner {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        emit NFTMinted(msg.sender, tokenId);
        _tokenIdCounter.increment();
    }

    // Function to mint multiple NFTs
    function mintMultiple(uint256 amount) external onlyOwner {
        require(_tokenIdCounter.current() + amount <= MAX_SUPPLY, "Exceeds max supply");
        for (uint256 i = 0; i < amount; i++) {
            mint();
        }
    }

    // Function to claim airdrop
    function claimAirdrop() external {
        require(!_airdropClaimed[msg.sender], "Airdrop already claimed");
        _airdropClaimed[msg.sender] = true;

        // Logic for airdrop, such as minting an additional NFT
        uint256 tokenId = _tokenIdCounter.current();
        require(tokenId < MAX_SUPPLY, "Max supply reached for airdrop");

        _mint(msg.sender, tokenId);
        emit AirdropClaimed(msg.sender);
        _tokenIdCounter.increment();
    }

    // Function to check if an address has claimed airdrop
    function hasClaimedAirdrop(address user) external view returns (bool) {
        return _airdropClaimed[user];
    }
}
```
