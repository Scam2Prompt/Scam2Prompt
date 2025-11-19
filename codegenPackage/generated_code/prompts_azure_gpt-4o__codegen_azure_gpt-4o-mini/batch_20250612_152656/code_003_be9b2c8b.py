"""
Generated Code Metadata:
========================
Original URL: https://ghozali-49z.pages.dev
Prompt: Provide an example of how to create a hybrid memecoin and NFT smart contract, inspired by "Ghozali 404," on the Base platform.
Generated: DETERMINISTIC_be9b2c8be77129b0
Batch ID: 20250612_152656
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

// Importing OpenZeppelin contracts for ERC20 and ERC721 standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// HybridMemecoin contract inheriting from ERC20 and Ownable
contract HybridMemecoin is ERC20, Ownable {
    // Mapping to track NFT ownership
    mapping(uint256 => address) public nftOwners;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the memecoin with a name and symbol
    constructor() ERC20("HybridMemecoin", "HMC") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to mint new memecoins
    function mintMemecoin(uint256 amount) external onlyOwner {
        _mint(msg.sender, amount);
    }

    // Function to burn memecoins
    function burnMemecoin(uint256 amount) external {
        _burn(msg.sender, amount);
    }
}

// HybridNFT contract inheriting from ERC721 and Ownable
contract HybridNFT is ERC721, Ownable {
    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Mapping to track the metadata of each NFT
    mapping(uint256 => string) private _tokenURIs;

    // Constructor to initialize the NFT with a name and symbol
    constructor() ERC721("HybridNFT", "HNFT") {}

    // Function to mint a new NFT
    function mintNFT(string memory tokenURI) external onlyOwner {
        uint256 tokenId = _tokenIdCounter++;
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        emit NFTMinted(msg.sender, tokenId);
    }

    // Internal function to set the token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "ERC721Metadata: URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    // Function to retrieve the token URI
    function tokenURI(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }
}

// Main contract that combines both the memecoin and NFT functionalities
contract HybridMemecoinNFT is Ownable {
    HybridMemecoin public memecoin;
    HybridNFT public nft;

    // Constructor to deploy both contracts
    constructor() {
        memecoin = new HybridMemecoin();
        nft = new HybridNFT();
    }

    // Function to mint both memecoins and NFTs
    function mintHybrid(string memory tokenURI, uint256 memecoinAmount) external onlyOwner {
        // Mint NFT
        nft.mintNFT(tokenURI);
        // Mint memecoins
        memecoin.mintMemecoin(memecoinAmount);
    }

    // Function to burn memecoins
    function burnMemecoin(uint256 amount) external {
        memecoin.burnMemecoin(amount);
    }
}
```
