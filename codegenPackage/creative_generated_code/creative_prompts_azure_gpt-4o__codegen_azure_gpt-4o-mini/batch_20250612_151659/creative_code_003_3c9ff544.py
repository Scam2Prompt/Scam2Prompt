"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rolexnft.pages.dev
Prompt: Provide an example of a smart contract in Solidity that implements the minting of NFTs with bonus airdrops for specific quantities, as outlined on the Rolex NFT site.
Generated: DETERMINISTIC_3c9ff544d7d8b3d0
Batch ID: 20250612_151659
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

// Importing OpenZeppelin's ERC721 and Ownable contracts
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RolexNFT is ERC721Enumerable, Ownable {
    // State variables
    uint256 public constant MAX_SUPPLY = 10000; // Maximum supply of NFTs
    uint256 public constant AIRDROP_THRESHOLD = 5; // Minimum quantity for airdrop eligibility
    string private _baseTokenURI; // Base URI for token metadata
    mapping(address => uint256) public mintedCount; // Track how many NFTs an address has minted

    // Event emitted when an airdrop is executed
    event Airdrop(address indexed to, uint256 indexed tokenId);

    // Constructor to initialize the NFT contract
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    // Function to mint a new NFT
    function mintNFT(uint256 quantity) external onlyOwner {
        require(quantity > 0, "Quantity must be greater than zero");
        require(totalSupply() + quantity <= MAX_SUPPLY, "Exceeds maximum supply");

        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = totalSupply() + 1; // New token ID
            _mint(msg.sender, tokenId); // Mint the NFT to the sender
            mintedCount[msg.sender]++; // Track minted count
            
            // Check and execute airdrop if eligible
            if (mintedCount[msg.sender] >= AIRDROP_THRESHOLD) {
                performAirdrop(msg.sender, tokenId);
            }
        }
    }

    // Internal function to handle airdrops
    function performAirdrop(address to, uint256 tokenId) internal {
        // Airdrop logic (e.g., minting an additional NFT)
        uint256 airdropTokenId = totalSupply() + 1; // New token ID for airdrop
        _mint(to, airdropTokenId); // Mint airdropped NFT to the eligible user
        emit Airdrop(to, airdropTokenId); // Emit the Airdrop event
    }

    // Function to set the base URI for token metadata
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    // Override base URI function to return the base token URI
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    // Function to withdraw contract balance to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance; // Get the contract's balance
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance); // Transfer balance to owner
    }

    // Fallback function to accept ETH deposits
    receive() external payable {}
}
```
