"""
Generated Code Metadata:
========================
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Generate a smart contract in Solidity for an NFT project similar to Prime Ape Planet, including functionalities for minting, exclusive events, and charity donations.
Generated: DETERMINISTIC_c31c7bb43bcaaa8e
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready Solidity smart contract for an NFT project with minting, exclusive events, and charity donation functionalities:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PrimeApePlanet is ERC721, Ownable, ReentrancyGuard {
    using SafeMath for uint256;
    using Counters for Counters.Counter;

    // Token counter
    Counters.Counter private _tokenIdCounter;

    // Contract configuration
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant MINT_PRICE = 0.08 ether;
    uint256 public constant MAX_MINT_PER_TX = 5;
    uint256 public constant CHARITY_PERCENTAGE = 10; // 10% of mint price goes to charity

    // Charity address
    address public charityAddress;

    // Sale state
    bool public publicSaleActive = false;
    bool public whitelistSaleActive = false;

    // Base URI for metadata
    string private _baseTokenURI;

    // Whitelist mapping
    mapping(address => bool) private whitelist;

    // Events
    event Minted(address indexed owner, uint256 tokenId);
    event CharityDonated(address indexed donor, uint256 amount);
    event WhitelistUpdated(address indexed account, bool status);
    event SaleStateChanged(bool publicSale, bool whitelistSale);

    constructor(
        string memory name,
        string memory symbol,
        string memory baseURI,
        address _charityAddress
    ) ERC721(name, symbol) {
        require(_charityAddress != address(0), "Invalid charity address");
        _baseTokenURI = baseURI;
        charityAddress = _charityAddress;
    }

    /**
     * @dev Mint NFTs during public sale
     * @param quantity Number of NFTs to mint
     */
    function mint(uint256 quantity) external payable nonReentrant {
        require(publicSaleActive, "Public sale is not active");
        require(quantity > 0 && quantity <= MAX_MINT_PER_TX, "Invalid mint quantity");
        require(_tokenIdCounter.current().add(quantity) <= MAX_SUPPLY, "Exceeds max supply");
        require(msg.value >= MINT_PRICE.mul(quantity), "Insufficient ETH sent");

        _mintNFTs(msg.sender, quantity);
    }

    /**
     * @dev Mint NFTs during whitelist sale
     * @param quantity Number of NFTs to mint
     */
    function whitelistMint(uint256 quantity) external payable nonReentrant {
        require(whitelistSaleActive, "Whitelist sale is not active");
        require(whitelist[msg.sender], "Not whitelisted");
        require(quantity > 0 && quantity <= MAX_MINT_PER_TX, "Invalid mint quantity");
        require(_tokenIdCounter.current().add(quantity) <= MAX_SUPPLY, "Exceeds max supply");
        require(msg.value >= MINT_PRICE.mul(quantity), "Insufficient ETH sent");

        _mintNFTs(msg.sender, quantity);
        whitelist[msg.sender] = false; // Remove from whitelist after minting
    }

    /**
     * @dev Internal function to handle NFT minting
     */
    function _mintNFTs(address to, uint256 quantity) private {
        uint256 charityAmount = msg.value.mul(CHARITY_PERCENTAGE).div(100);
        (bool charitySuccess, ) = charityAddress.call{value: charityAmount}("");
        require(charitySuccess, "Charity transfer failed");

        for (uint256 i = 0; i < quantity; i++) {
            _tokenIdCounter.increment();
            uint256 tokenId = _tokenIdCounter.current();
            _safeMint(to, tokenId);
            emit Minted(to, tokenId);
        }

        emit CharityDonated(msg.sender, charityAmount);
    }

    /**
     * @dev Admin function to mint reserved NFTs
     */
    function adminMint(address to, uint256 quantity) external onlyOwner {
        require(_tokenIdCounter.current().add(quantity) <= MAX_SUPPLY, "Exceeds max supply");
        _mintNFTs(to, quantity);
    }

    /**
     * @dev Set base URI for token metadata
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Get base URI
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Toggle public sale state
     */
    function togglePublicSale() external onlyOwner {
        publicSaleActive = !publicSaleActive;
        emit SaleStateChanged(publicSaleActive, whitelistSaleActive);
    }

    /**
     * @dev Toggle whitelist sale state
     */
    function toggleWhitelistSale() external onlyOwner {
        whitelistSaleActive = !whitelistSaleActive;
        emit SaleStateChanged(publicSaleActive, whitelistSaleActive);
    }

    /**
     * @dev Add addresses to whitelist
     */
    function addToWhitelist(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = true;
            emit WhitelistUpdated(addresses[i], true);
        }
    }

    /**
     * @dev Remove addresses from whitelist
     */
    function removeFromWhitelist(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = false;
            emit WhitelistUpdated(addresses[i], false);
        }
    }

    /**
     * @dev Check if address is whitelisted
     */
    function isWhitelisted(address account) external view returns (bool) {
        return whitelist[account];
    }

    /**
     * @dev Withdraw contract balance (minus charity portion)
     */
    function withdraw() external onlyOwner nonReentrant {
        uint256 balance = address(this).balance;
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Update charity address
     */
    function setCharityAddress(address _charityAddress) external onlyOwner {
        require(_charityAddress != address(0), "Invalid charity address");
        charityAddress = _charityAddress;
    }

    /**
     * @dev Get total supply
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
