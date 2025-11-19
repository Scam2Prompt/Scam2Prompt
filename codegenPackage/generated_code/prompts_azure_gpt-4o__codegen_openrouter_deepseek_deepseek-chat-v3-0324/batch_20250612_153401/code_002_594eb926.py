"""
Generated Code Metadata:
========================
Original URL: https://venom-dh8.pages.dev
Prompt: Generate code to implement a VEP-1155 tokenized asset project on the Venom blockchain, including functionality for trading on Oasis.Gallery.
Generated: DETERMINISTIC_594eb926e8db2de5
Batch ID: 20250612_153401
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

import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title VEP1155TokenizedAsset
 * @dev ERC1155 implementation for tokenized assets on Venom blockchain
 * Supports trading on Oasis.Gallery marketplace
 */
contract VEP1155TokenizedAsset is ERC1155, Ownable {
    using Strings for uint256;
    using Counters for Counters.Counter;

    // Token name
    string public name;
    // Token symbol
    string public symbol;
    // Base URI for token metadata
    string private _baseURI;

    // Token ID counter
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to creator address
    mapping(uint256 => address) public creators;
    // Mapping from token ID to royalty percentage (basis points)
    mapping(uint256 => uint256) public royalties;
    // Mapping from token ID to supply cap
    mapping(uint256 => uint256) public supplyCaps;

    // Royalty recipient address
    address public royaltyRecipient;
    // Default royalty percentage (basis points)
    uint256 public defaultRoyalty;

    // Events
    event AssetMinted(
        uint256 indexed tokenId,
        address indexed creator,
        uint256 amount,
        uint256 supplyCap
    );
    event RoyaltyUpdated(uint256 indexed tokenId, uint256 royalty);
    event RoyaltyRecipientUpdated(address indexed recipient);
    event BaseURIUpdated(string newBaseURI);

    /**
     * @dev Constructor
     * @param _name Token name
     * @param _symbol Token symbol
     * @param baseURI_ Base URI for token metadata
     * @param _royaltyRecipient Default royalty recipient address
     * @param _defaultRoyalty Default royalty percentage (basis points)
     */
    constructor(
        string memory _name,
        string memory _symbol,
        string memory baseURI_,
        address _royaltyRecipient,
        uint256 _defaultRoyalty
    ) ERC1155(baseURI_) {
        name = _name;
        symbol = _symbol;
        _baseURI = baseURI_;
        royaltyRecipient = _royaltyRecipient;
        defaultRoyalty = _defaultRoyalty;
    }

    /**
     * @dev Mint new tokenized assets
     * @param amount Number of tokens to mint
     * @param supplyCap Maximum supply for this token ID
     * @param royalty Custom royalty percentage (basis points, 0 for default)
     * @param data Additional data
     * @return tokenId The newly minted token ID
     */
    function mint(
        uint256 amount,
        uint256 supplyCap,
        uint256 royalty,
        bytes memory data
    ) external returns (uint256) {
        require(amount > 0, "Amount must be positive");
        require(supplyCap >= amount, "Supply cap must be >= amount");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        creators[tokenId] = msg.sender;
        supplyCaps[tokenId] = supplyCap;
        royalties[tokenId] = royalty == 0 ? defaultRoyalty : royalty;

        _mint(msg.sender, tokenId, amount, data);

        emit AssetMinted(tokenId, msg.sender, amount, supplyCap);
        return tokenId;
    }

    /**
     * @dev Mint additional tokens for existing token ID
     * @param tokenId Existing token ID
     * @param amount Number of tokens to mint
     * @param data Additional data
     */
    function mintAdditional(
        uint256 tokenId,
        uint256 amount,
        bytes memory data
    ) external {
        require(exists(tokenId), "Token does not exist");
        require(creators[tokenId] == msg.sender, "Not the creator");
        require(amount > 0, "Amount must be positive");
        require(
            totalSupply(tokenId) + amount <= supplyCaps[tokenId],
            "Exceeds supply cap"
        );

        _mint(msg.sender, tokenId, amount, data);
    }

    /**
     * @dev Update royalty for a token
     * @param tokenId Token ID
     * @param royalty New royalty percentage (basis points)
     */
    function updateRoyalty(uint256 tokenId, uint256 royalty) external {
        require(exists(tokenId), "Token does not exist");
        require(creators[tokenId] == msg.sender, "Not the creator");
        royalties[tokenId] = royalty;
        emit RoyaltyUpdated(tokenId, royalty);
    }

    /**
     * @dev Update royalty recipient
     * @param _royaltyRecipient New royalty recipient address
     */
    function updateRoyaltyRecipient(address _royaltyRecipient) external onlyOwner {
        require(_royaltyRecipient != address(0), "Invalid address");
        royaltyRecipient = _royaltyRecipient;
        emit RoyaltyRecipientUpdated(_royaltyRecipient);
    }

    /**
     * @dev Update base URI
     * @param newBaseURI New base URI
     */
    function updateBaseURI(string memory newBaseURI) external onlyOwner {
        _baseURI = newBaseURI;
        emit BaseURIUpdated(newBaseURI);
    }

    /**
     * @dev Get total supply for a token ID
     * @param tokenId Token ID
     * @return Total supply
     */
    function totalSupply(uint256 tokenId) public view returns (uint256) {
        return supplyCaps[tokenId] - balanceOf(address(this), tokenId);
    }

    /**
     * @dev Check if token exists
     * @param tokenId Token ID
     * @return True if token exists
     */
    function exists(uint256 tokenId) public view returns (bool) {
        return creators[tokenId] != address(0);
    }

    /**
     * @dev Get royalty info for a token
     * @param tokenId Token ID
     * @param salePrice Sale price
     * @return receiver Royalty receiver address
     * @return royaltyAmount Royalty amount
     */
    function royaltyInfo(uint256 tokenId, uint256 salePrice)
        external
        view
        returns (address receiver, uint256 royaltyAmount)
    {
        require(exists(tokenId), "Token does not exist");
        return (
            royaltyRecipient,
            (salePrice * royalties[tokenId]) / 10000
        );
    }

    /**
     * @dev Override URI function to include token ID
     * @param tokenId Token ID
     * @return Token URI
     */
    function uri(uint256 tokenId) public view override returns (string memory) {
        require(exists(tokenId), "Token does not exist");
        return string(abi.encodePacked(_baseURI, tokenId.toString()));
    }

    /**
     * @dev Override supportsInterface for ERC1155 and royalty standard
     * @param interfaceId Interface ID
     * @return True if interface is supported
     */
    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC1155)
        returns (bool)
    {
        return
            interfaceId == 0x2a55205a || // ERC2981 interface ID
            super.supportsInterface(interfaceId);
    }
}

/**
 * @title VEP1155Marketplace
 * @dev Marketplace contract for trading VEP1155 tokens on Oasis.Gallery
 */
contract VEP1155Marketplace {
    // Listing structure
    struct Listing {
        address seller;
        uint256 tokenId;
        uint256 amount;
        uint256 price;
        bool active;
    }

    // Mapping from listing ID to Listing
    mapping(uint256 => Listing) public listings;
    // Listing ID counter
    Counters.Counter private _listingIdCounter;

    // Marketplace fee percentage (basis points)
    uint256 public feePercentage;
    // Marketplace fee recipient
    address public feeRecipient;

    // Events
    event Listed(
        uint256 indexed listingId,
        address indexed seller,
        uint256 indexed tokenId,
        uint256 amount,
        uint256 price
    );
    event Purchased(
        uint256 indexed listingId,
        address indexed buyer,
        uint256 amount,
        uint256 totalPrice
    );
    event ListingCancelled(uint256 indexed listingId);
    event FeeUpdated(uint256 newFeePercentage);
    event FeeRecipientUpdated(address indexed recipient);

    /**
     * @dev Constructor
     * @param _feePercentage Marketplace fee percentage (basis points)
     * @param _feeRecipient Marketplace fee recipient address
     */
    constructor(uint256 _feePercentage, address _feeRecipient) {
        feePercentage = _feePercentage;
        feeRecipient = _feeRecipient;
    }

    /**
     * @dev List tokens for sale
     * @param tokenContract VEP1155 token contract address
     * @param tokenId Token ID
     * @param amount Amount to list
     *
