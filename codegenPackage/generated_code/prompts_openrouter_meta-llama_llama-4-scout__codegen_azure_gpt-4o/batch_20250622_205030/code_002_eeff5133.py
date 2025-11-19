"""
Generated Code Metadata:
========================
Original URL: https://rapping-planet-prehistoric.on-fleek.app
Prompt: Generate a smart contract code in Solidity for an NFT collection with a utility token, allowing for fair launch, private marketplace, and merchandising release features.
Generated: DETERMINISTIC_eeff5133211bea97
Batch ID: 20250622_205030
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

/**
 * @title NFTCollectionWithUtilityToken
 * @dev A smart contract for an NFT collection with a utility token, private marketplace, and merchandising release features.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTCollectionWithUtilityToken is ERC721Enumerable, Ownable {
    // Utility token contract
    ERC20 public utilityToken;

    // NFT metadata base URI
    string private baseURI;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Price per NFT (in wei)
    uint256 public constant MINT_PRICE = 0.05 ether;

    // Private marketplace mapping (tokenId => price)
    mapping(uint256 => uint256) private marketplacePrices;

    // Merchandising release mapping (tokenId => merchandise details)
    mapping(uint256 => string) private merchandiseDetails;

    // Events
    event NFTMinted(address indexed minter, uint256 indexed tokenId);
    event NFTListed(uint256 indexed tokenId, uint256 price);
    event NFTPurchased(uint256 indexed tokenId, address indexed buyer);
    event MerchandiseReleased(uint256 indexed tokenId, string details);

    /**
     * @dev Constructor to initialize the NFT collection and utility token.
     * @param _name Name of the NFT collection.
     * @param _symbol Symbol of the NFT collection.
     * @param _utilityToken Address of the utility token contract.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        address _utilityToken
    ) ERC721(_name, _symbol) {
        utilityToken = ERC20(_utilityToken);
    }

    /**
     * @dev Set the base URI for NFT metadata.
     * @param _baseURI Base URI string.
     */
    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }

    /**
     * @dev Override the _baseURI function to return the custom base URI.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    /**
     * @dev Mint a new NFT.
     * @param _amount Number of NFTs to mint.
     */
    function mint(uint256 _amount) external payable {
        require(_amount > 0, "Amount must be greater than zero");
        require(totalSupply() + _amount <= MAX_SUPPLY, "Exceeds maximum supply");
        require(msg.value == MINT_PRICE * _amount, "Incorrect ETH value sent");

        for (uint256 i = 0; i < _amount; i++) {
            uint256 tokenId = totalSupply() + 1;
            _safeMint(msg.sender, tokenId);
            emit NFTMinted(msg.sender, tokenId);
        }
    }

    /**
     * @dev List an NFT for sale in the private marketplace.
     * @param _tokenId Token ID of the NFT.
     * @param _price Sale price in utility tokens.
     */
    function listNFT(uint256 _tokenId, uint256 _price) external {
        require(ownerOf(_tokenId) == msg.sender, "Not the owner of the NFT");
        require(_price > 0, "Price must be greater than zero");

        marketplacePrices[_tokenId] = _price;
        emit NFTListed(_tokenId, _price);
    }

    /**
     * @dev Purchase an NFT from the private marketplace.
     * @param _tokenId Token ID of the NFT.
     */
    function purchaseNFT(uint256 _tokenId) external {
        uint256 price = marketplacePrices[_tokenId];
        require(price > 0, "NFT not listed for sale");

        address seller = ownerOf(_tokenId);
        require(seller != msg.sender, "Cannot purchase your own NFT");

        // Transfer utility tokens from buyer to seller
        require(
            utilityToken.transferFrom(msg.sender, seller, price),
            "Utility token transfer failed"
        );

        // Transfer NFT ownership
        _transfer(seller, msg.sender, _tokenId);

        // Remove from marketplace
        marketplacePrices[_tokenId] = 0;

        emit NFTPurchased(_tokenId, msg.sender);
    }

    /**
     * @dev Release merchandise for a specific NFT.
     * @param _tokenId Token ID of the NFT.
     * @param _details Merchandise details (e.g., URL or description).
     */
    function releaseMerchandise(uint256 _tokenId, string memory _details)
        external
        onlyOwner
    {
        require(_exists(_tokenId), "NFT does not exist");

        merchandiseDetails[_tokenId] = _details;
        emit MerchandiseReleased(_tokenId, _details);
    }

    /**
     * @dev Get merchandise details for a specific NFT.
     * @param _tokenId Token ID of the NFT.
     * @return Merchandise details string.
     */
    function getMerchandiseDetails(uint256 _tokenId)
        external
        view
        returns (string memory)
    {
        require(_exists(_tokenId), "NFT does not exist");
        return merchandiseDetails[_tokenId];
    }

    /**
     * @dev Withdraw contract balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        payable(owner()).transfer(balance);
    }
}
```
