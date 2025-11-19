"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://t1-32y.pages.dev
Prompt: Provide an example of a smart contract function that enforces a maximum of 1 mint per wallet for the Blaze NFT collection.
Generated: DETERMINISTIC_524bccfa984b3279
Batch ID: 20250612_162404
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

contract BlazeNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for keeping track of the current token ID
    Counters.Counter private _tokenIdCounter;

    // Mapping to track if a wallet has already minted
    mapping(address => bool) private _hasMinted;

    // Maximum NFTs that can be minted per wallet
    uint256 public constant MAX_MINT_PER_WALLET = 1;

    // Event emitted when a new NFT is minted
    event Minted(address indexed owner, uint256 indexed tokenId);

    // Constructor to set the name and symbol of the NFT collection
    constructor() ERC721("Blaze NFT", "BLZ") {}

    /**
     * @dev Function to mint a new NFT.
     * Reverts if the caller has already minted or if the mint is not allowed.
     */
    function mint() external {
        // Check if the caller has already minted
        require(!_hasMinted[msg.sender], "You have already minted an NFT.");

        // Ensure that minting is limited to one per wallet
        require(balanceOf(msg.sender) < MAX_MINT_PER_WALLET, "Maximum mint limit reached for this wallet.");

        // Increment the token ID counter and mint the new NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _hasMinted[msg.sender] = true; // Mark the wallet as having minted

        // Mint the NFT to the caller
        _safeMint(msg.sender, tokenId);

        // Emit the mint event
        emit Minted(msg.sender, tokenId);
    }

    /**
     * @dev Function to check if an address has minted an NFT.
     * @param wallet The address of the wallet to check.
     * @return bool indicating whether the wallet has minted.
     */
    function hasMinted(address wallet) external view returns (bool) {
        return _hasMinted[wallet];
    }
}
```
