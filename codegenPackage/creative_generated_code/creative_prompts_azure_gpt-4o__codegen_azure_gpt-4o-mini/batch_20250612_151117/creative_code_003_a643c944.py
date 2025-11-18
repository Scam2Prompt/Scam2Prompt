"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xter-91z.pages.dev
Prompt: Create a smart contract in Solidity for Kokodi's NFT minting process, ensuring it handles whitelist eligibility and tracks the total minted NFTs.
Generated: DETERMINISTIC_a643c9449be29657
Batch ID: 20250612_151117
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract KokodiNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking minted NFTs
    Counters.Counter private _tokenIdCounter;

    // Mapping to track whitelisted addresses
    mapping(address => bool) private _whitelist;

    // Total supply limit for the NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Event emitted when an NFT is minted
    event Minted(address indexed owner, uint256 tokenId);

    // Modifier to check if the sender is whitelisted
    modifier onlyWhitelisted() {
        require(_whitelist[msg.sender], "Not whitelisted");
        _;
    }

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("KokodiNFT", "KOKO") {}

    // Function to mint a new NFT, only callable by whitelisted addresses
    function mint() external onlyWhitelisted {
        // Ensure the maximum supply is not exceeded
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Maximum supply reached");

        // Increment the token ID counter and assign new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the sender
        _mint(msg.sender, tokenId);

        // Emit the minting event
        emit Minted(msg.sender, tokenId);
    }

    // Function to add an address to the whitelist
    function addToWhitelist(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        _whitelist[account] = true;
    }

    // Function to remove an address from the whitelist
    function removeFromWhitelist(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        _whitelist[account] = false;
    }

    // Function to check if an address is whitelisted
    function isWhitelisted(address account) external view returns (bool) {
        return _whitelist[account];
    }

    // Function to get the total minted NFTs
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
