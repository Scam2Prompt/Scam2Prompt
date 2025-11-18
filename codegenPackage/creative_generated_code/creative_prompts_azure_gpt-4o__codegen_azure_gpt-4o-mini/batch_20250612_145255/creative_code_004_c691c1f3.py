"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-nakamigos.vercel.app
Prompt: Create a smart contract in Solidity that limits NFT minting to a maximum of 1 set per wallet, as described on the Mint Nakamigos site.
Generated: DETERMINISTIC_c691c1f3b227e416
Batch ID: 20250612_145255
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

/**
 * @title LimitedMintNFT
 * @dev A smart contract for minting NFTs with a limit of one set per wallet.
 */
contract LimitedMintNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping to keep track of which wallets have minted
    mapping(address => bool) private _hasMinted;

    // Base URI for the metadata
    string private _baseTokenURI;

    // Event to emit when a new token is minted
    event TokenMinted(address indexed minter, uint256 tokenId);
    
    /**
     * @dev Constructor to set the name and symbol of the NFT collection.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     * @param baseURI The base URI for token metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mint a new NFT. Allows only one mint per wallet.
     */
    function mint() public {
        // Ensure the wallet has not minted before
        require(!_hasMinted[msg.sender], "You have already minted an NFT.");

        // Mint the NFT
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _hasMinted[msg.sender] = true;

        _safeMint(msg.sender, tokenId);
        emit TokenMinted(msg.sender, tokenId);
    }

    /**
     * @dev Returns the base URI for the token metadata.
     * @return The base URI as a string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Update the base URI for the token metadata (only owner can call).
     * @param newBaseURI The new base URI as a string.
     */
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;
    }

    /**
     * @dev Check if a wallet has minted an NFT.
     * @param wallet The address of the wallet to check.
     * @return True if the wallet has minted; otherwise, false.
     */
    function hasMinted(address wallet) external view returns (bool) {
        return _hasMinted[wallet];
    }
}
```
