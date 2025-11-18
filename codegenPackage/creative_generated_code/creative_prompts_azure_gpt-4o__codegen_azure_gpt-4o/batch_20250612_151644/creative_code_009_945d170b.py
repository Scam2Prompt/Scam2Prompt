"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerobeings.app
Prompt: Recommend best practices for creating a verified smart contract for an NFT project, inspired by "Zero Beings."
Generated: DETERMINISTIC_945d170b04b2802a
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, syntactically correct, production-ready smart contract for an NFT project written in Solidity. It follows best practices, is well-commented, and includes proper error handling.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import OpenZeppelin ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract declaration
contract ZeroBeingsNFT is ERC721, Ownable {
    using Counters for Counters.Counter;

    // Counter to track token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Max supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Mint price
    uint256 public constant MINT_PRICE = 0.05 ether;

    // Events
    event BaseURIUpdated(string newBaseURI);
    event Minted(address recipient, uint256 tokenId);

    // Constructor: Set token name and symbol
    constructor(string memory baseURI) ERC721("Zero Beings", "ZB") {
        _baseTokenURI = baseURI;
    }

    // Override baseURI function from ERC721
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    // Public function to mint an NFT
    function mint() external payable {
        // Ensure mint price is correct
        require(msg.value == MINT_PRICE, "Incorrect ETH amount sent.");

        // Ensure max supply is not exceeded
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached.");

        // Increment token ID counter
        _tokenIdCounter.increment();

        // Mint the NFT and assign it to sender
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(msg.sender, tokenId);

        // Emit event
        emit Minted(msg.sender, tokenId);
    }

    // Owner-only function to update the base URI
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        _baseTokenURI = newBaseURI;

        // Emit event
        emit BaseURIUpdated(newBaseURI);
    }

    // Withdraw contract balance to owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;

        // Prevent withdrawal if no funds are available
        require(balance > 0, "No funds available for withdrawal.");
        
        // Transfer balance to the owner
        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "Transfer failed.");
    }

    // Fallback function to prevent accidental ETH sends
    fallback() external payable {
        revert("Direct ETH transfer not allowed.");
    }

    // Receive function in case ETH is sent directly
    receive() external payable {
        revert("Direct ETH transfer not allowed.");
    }
}
```

### Key Features:
- **ERC721 Implementation**: Uses OpenZeppelin's battle-tested library.
- **Error Handling**: Includes checks for mint price, max supply, and fallback functions to prevent accidental ETH transfers.
- **Base URI Management**: Allows the owner to update the metadata base URI.
- **Withdraw Function**: Securely transfers funds to the contract owner.
- **Events**: Emits events for key actions like minting and URI updates.
