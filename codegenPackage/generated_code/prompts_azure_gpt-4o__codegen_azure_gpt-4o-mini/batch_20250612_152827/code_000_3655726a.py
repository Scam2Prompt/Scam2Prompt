"""
Generated Code Metadata:
========================
Original URL: https://gameswap-org.web.app
Prompt: Write a smart contract in Solidity to mint and bridge in-game assets into Ethereum-compatible NFTs using ERC721 or ERC1155 standards, as described on GameSwap's platform.
Generated: DETERMINISTIC_3655726aa37dde8e
Batch ID: 20250612_152827
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

// Importing the ERC721 and ERC1155 interfaces from OpenZeppelin
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for minting and bridging in-game assets as NFTs
contract GameSwapNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to asset metadata
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event Minted(uint256 indexed tokenId, address indexed owner, string tokenURI);

    // Constructor to initialize the ERC721 contract with a name and symbol
    constructor() ERC721("GameSwapNFT", "GSNFT") {}

    // Function to mint a new NFT
    function mint(string memory tokenURI) external onlyOwner {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the caller
        _mint(msg.sender, tokenId);
        
        // Set the token URI for the newly minted NFT
        _setTokenURI(tokenId, tokenURI);

        // Emit the Minted event
        emit Minted(tokenId, msg.sender, tokenURI);
    }

    // Internal function to set the token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "ERC721Metadata: URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    // Function to retrieve the token URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    // Function to bridge the NFT to another platform (placeholder for actual bridging logic)
    function bridgeNFT(uint256 tokenId, address targetPlatform) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this token");
        require(_exists(tokenId), "Token does not exist");

        // Placeholder for bridging logic
        // This could involve calling a function on the target platform's contract

        // Burn the NFT after bridging
        _burn(tokenId);
    }
}

// Smart contract for minting and bridging in-game assets as ERC1155 NFTs
contract GameSwapERC1155 is ERC1155, Ownable {
    using Counters for Counters.Counter;

    // Counter for tracking token IDs
    Counters.Counter private _tokenIdCounter;

    // Event emitted when a new ERC1155 token is minted
    event Minted(uint256 indexed tokenId, address indexed owner, uint256 amount);

    // Constructor to initialize the ERC1155 contract with a URI
    constructor(string memory uri) ERC1155(uri) {}

    // Function to mint a new ERC1155 token
    function mint(uint256 amount) external onlyOwner {
        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the specified amount of tokens to the caller
        _mint(msg.sender, tokenId, amount, "");

        // Emit the Minted event
        emit Minted(tokenId, msg.sender, amount);
    }

    // Function to bridge the ERC1155 token to another platform (placeholder for actual bridging logic)
    function bridgeERC1155(uint256 tokenId, uint256 amount, address targetPlatform) external {
        require(balanceOf(msg.sender, tokenId) >= amount, "Insufficient token balance");
        
        // Placeholder for bridging logic
        // This could involve calling a function on the target platform's contract

        // Burn the tokens after bridging
        _burn(msg.sender, tokenId, amount);
    }
}
```
