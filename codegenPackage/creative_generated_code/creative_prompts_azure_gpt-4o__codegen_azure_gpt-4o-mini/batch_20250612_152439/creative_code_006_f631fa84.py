"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinu-gateway.pages.dev
Prompt: Generate code for an NFT smart contract that supports composable interchain NFTs, as described in Any Inu's roadmap, ensuring compatibility with Cosmos EVM chains.
Generated: DETERMINISTIC_f631fa84a7779f86
Batch ID: 20250612_152439
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

// Importing OpenZeppelin's ERC721 contract and Ownable for security and convenience
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for interacting with other smart contracts
interface IComposableNFT {
    function mint(address to, uint256 tokenId) external;
    function transferFrom(address from, address to, uint256 tokenId) external;
}

// ComposableNFT contract for creating interchain NFTs
contract ComposableNFT is ERC721Enumerable, Ownable {
    // Mapping from token ID to metadata URI
    mapping(uint256 => string) private _tokenURIs;
    
    // Counter for the next mintable token ID
    uint256 private _nextTokenId;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Modifier to ensure that the token exists
    modifier tokenExists(uint256 tokenId) {
        require(_exists(tokenId), "Token does not exist");
        _;
    }

    // Constructor to initialize the ERC721 contract with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        _nextTokenId = 1; // Start token IDs from 1
    }

    // Function to mint a new NFT
    function mint(string memory tokenURI) external onlyOwner {
        uint256 tokenId = _nextTokenId;
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit NFTMinted(msg.sender, tokenId, tokenURI);
        
        _nextTokenId++;
    }

    // Function to set the token URI for a given token ID
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal tokenExists(tokenId) {
        _tokenURIs[tokenId] = tokenURI;
    }

    // Function to retrieve the token URI for a given token ID
    function tokenURI(uint256 tokenId) public view override tokenExists(tokenId) returns (string memory) {
        return _tokenURIs[tokenId];
    }

    // Function to transfer NFT ownership, with compatibility for interchain transfer
    function transferNFT(address to, uint256 tokenId) external tokenExists(tokenId) {
        require(ownerOf(tokenId) == msg.sender, "You do not own this token");
        safeTransferFrom(msg.sender, to, tokenId);
    }

    // Function to handle interchain composability (example placeholder)
    function composeNFT(uint256[] memory tokenIds) external {
        // Logic to compose NFTs across chains (implementation-dependent)
        // This could involve calling other contracts or emitting events
    }

    // Function to withdraw any Ether accidentally sent to the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
