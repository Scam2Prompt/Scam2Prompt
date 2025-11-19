"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://studio-git-scott-dashboard-update-metaplex.vercel.app
Prompt: Can you provide a code example for creating an NFT minting function in Truffle based on the "Test ABC" project?
Generated: DETERMINISTIC_f23030a6abac5065
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin's ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract TestABCNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new token is minted
    event NFTMinted(address indexed recipient, uint256 indexed tokenId);

    // Constructor to initialize the ERC721 token with name and symbol
    constructor(string memory baseURI) ERC721("Test ABC", "TABC") {
        _baseTokenURI = baseURI;
    }

    // Function to mint a new NFT
    function mintNFT(address recipient) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero.");

        // Increment the token ID counter
        _tokenIdCounter.increment();

        // Get the next token ID
        uint256 newTokenId = _tokenIdCounter.current();

        // Mint the token to the recipient address
        _safeMint(recipient, newTokenId);

        // Emit the mint event
        emit NFTMinted(recipient, newTokenId);
    }

    // Override the _baseURI function to return the base URI
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to update the base URI
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    // Retrieve the current token ID counter for external reference (optional)
    function getCurrentTokenId() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```

**Notes in code comments:**
- The contract uses OpenZeppelin's ERC721 implementation for NFTs.
- The `mintNFT` function is restricted to the contract owner using the `onlyOwner` modifier.
- Error handling ensures the recipient address is valid (`not zero`).
- The base URI is configurable via `setBaseURI` and used to fetch token metadata.
- Events are emitted for transparency and tracking when a new NFT is minted.
