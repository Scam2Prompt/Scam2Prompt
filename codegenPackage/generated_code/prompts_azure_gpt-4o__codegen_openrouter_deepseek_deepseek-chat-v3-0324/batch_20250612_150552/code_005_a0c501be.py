"""
Generated Code Metadata:
========================
Original URL: https://llamanft.pages.dev
Prompt: Develop a Solidity smart contract for issuing NFTs with unique designs, ensuring security and testing mechanisms before public launch, as detailed in the Cyber Lama project.
Generated: DETERMINISTIC_a0c501be1b43abbb
Batch ID: 20250612_150552
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title CyberLamaNFT
 * @dev ERC721 token contract for Cyber Lama project with unique NFT designs
 */
contract CyberLamaNFT is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using Strings for uint256;

    // Token counter
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Mint price
    uint256 public mintPrice = 0.05 ether;

    // Minting status
    bool public mintingEnabled = false;

    // Mapping to track minted designs
    mapping(uint256 => string) private _designHashes;

    // Events
    event Minted(address indexed to, uint256 tokenId, string designHash);
    event BaseURIUpdated(string newBaseURI);
    event MintPriceUpdated(uint256 newPrice);
    event MintingStatusChanged(bool enabled);

    /**
     * @dev Constructor
     * @param baseURI Base URI for token metadata
     */
    constructor(string memory baseURI) ERC721("CyberLama", "CLAMA") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mint a new NFT with a unique design
     * @param designHash Unique hash representing the NFT design
     */
    function mint(string memory designHash) external payable nonReentrant {
        require(mintingEnabled, "Minting is not enabled");
        require(msg.value >= mintPrice, "Insufficient payment");
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        require(bytes(designHash).length > 0, "Design hash cannot be empty");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _designHashes[tokenId] = designHash;
        _safeMint(msg.sender, tokenId);

        emit Minted(msg.sender, tokenId, designHash);
    }

    /**
     * @dev Get the design hash for a token
     * @param tokenId Token ID to query
     * @return designHash The design hash for the token
     */
    function getDesignHash(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _designHashes[tokenId];
    }

    /**
     * @dev Set base URI for token metadata
     * @param baseURI New base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
        emit BaseURIUpdated(baseURI);
    }

    /**
     * @dev Set mint price
     * @param price New mint price in wei
     */
    function setMintPrice(uint256 price) external onlyOwner {
        mintPrice = price;
        emit MintPriceUpdated(price);
    }

    /**
     * @dev Toggle minting status
     * @param enabled Whether minting should be enabled
     */
    function setMintingEnabled(bool enabled) external onlyOwner {
        mintingEnabled = enabled;
        emit MintingStatusChanged(enabled);
    }

    /**
     * @dev Withdraw contract balance to owner
     */
    function withdraw() external onlyOwner nonReentrant {
        uint256 balance = address(this).balance;
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Get base URI
     * @return Base URI string
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Get token URI
     * @param tokenId Token ID to query
     * @return Token URI string
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return string(abi.encodePacked(_baseTokenURI, tokenId.toString()));
    }

    /**
     * @dev Get current token count
     * @return Current token count
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
