"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claynosaurz-nft.web.app
Prompt: Generate a smart contract code snippet for minting NFTs for the Claynosaurz project, ensuring it includes wallet integration and whitelist functionality.
Generated: DETERMINISTIC_8bbfc818ff32aafe
Batch ID: 20250612_162346
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

/**
 * @title ClaynosaurzNFT
 * @dev A smart contract for minting NFTs with wallet integration and whitelist functionality.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ClaynosaurzNFT is ERC721Enumerable, Ownable {
    // Maximum number of NFTs that can be minted
    uint256 public constant MAX_SUPPLY = 10000;

    // Base URI for metadata
    string private _baseTokenURI;

    // Whitelist mapping for approved wallets
    mapping(address => bool) public whitelist;

    // Minting price per NFT (in wei)
    uint256 public mintPrice = 0.05 ether;

    // Track minted tokens
    uint256 private _currentTokenId;

    // Events
    event Mint(address indexed to, uint256 indexed tokenId);
    event BaseURIUpdated(string baseURI);
    event WalletWhitelisted(address indexed wallet, bool isWhitelisted);
    event MintPriceUpdated(uint256 newPrice);

    /**
     * @dev Constructor to initialize the NFT contract.
     * @param baseURI The initial base URI for metadata.
     */
    constructor(string memory baseURI) ERC721("ClaynosaurzNFT", "CLAY") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mint a new NFT.
     * @param to Address of the recipient.
     */
    function mint(address to) external payable {
        require(to != address(0), "Invalid address");
        require(whitelist[msg.sender], "Address not whitelisted");
        require(msg.value == mintPrice, "Incorrect mint price");
        require(_currentTokenId < MAX_SUPPLY, "Max supply reached");

        // Increment token ID
        _currentTokenId++;

        // Mint the NFT
        _safeMint(to, _currentTokenId);

        // Emit mint event
        emit Mint(to, _currentTokenId);
    }

    /**
     * @dev Set the base URI for metadata.
     * @param baseURI New base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
        emit BaseURIUpdated(baseURI);
    }

    /**
     * @dev Get the base URI for metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Add or remove an address from the whitelist.
     * @param wallet Address to add/remove.
     * @param isWhitelisted True to add, false to remove.
     */
    function updateWhitelist(address wallet, bool isWhitelisted) external onlyOwner {
        whitelist[wallet] = isWhitelisted;
        emit WalletWhitelisted(wallet, isWhitelisted);
    }

    /**
     * @dev Update the mint price for NFTs.
     * @param newPrice New mint price (in wei).
     */
    function setMintPrice(uint256 newPrice) external onlyOwner {
        mintPrice = newPrice;
        emit MintPriceUpdated(newPrice);
    }

    /**
     * @dev Withdraw contract balance to owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available");
        payable(owner()).transfer(balance);
    }
}
```
