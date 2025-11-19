"""
Generated Code Metadata:
========================
Original URL: https://cem-seven.vercel.app
Prompt: Develop a smart contract template for creating co-editions or unique tokens with user-defined attributes, inspired by the Co-Edition platform.
Generated: DETERMINISTIC_0c430e3411c63a7a
Batch ID: 20250612_151752
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

/**
 * @title CoEditionToken
 * @dev A smart contract for creating co-editions or unique tokens with customizable attributes
 */
contract CoEditionToken is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Token metadata structure
    struct TokenAttributes {
        string name;
        string description;
        string imageURI;
        string externalURL;
        string[] attributes;
    }

    // Mapping from token ID to attributes
    mapping(uint256 => TokenAttributes) private _tokenAttributes;

    // Mapping from token ID to edition size (0 means unique)
    mapping(uint256 => uint256) private _editionSizes;

    // Mapping from token ID to current mint count
    mapping(uint256 => uint256) private _mintedCounts;

    // Mapping from token ID to price
    mapping(uint256 => uint256) private _tokenPrices;

    // Mapping from token ID to creator address
    mapping(uint256 => address) private _tokenCreators;

    // Base URI for token metadata
    string private _baseTokenURI;

    // Contract URI for marketplace metadata
    string private _contractURI;

    // Royalty percentage (basis points)
    uint256 private _royaltyPercentage;

    // Events
    event TokenCreated(
        uint256 indexed tokenId,
        address indexed creator,
        string name,
        uint256 editionSize,
        uint256 price
    );
    event TokenMinted(
        uint256 indexed tokenId,
        address indexed owner,
        uint256 editionNumber
    );
    event RoyaltiesUpdated(uint256 newPercentage);

    /**
     * @dev Constructor
     * @param name_ Token collection name
     * @param symbol_ Token collection symbol
     * @param baseTokenURI_ Base URI for token metadata
     * @param contractURI_ Contract metadata URI
     * @param royaltyPercentage_ Royalty percentage in basis points
     */
    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseTokenURI_,
        string memory contractURI_,
        uint256 royaltyPercentage_
    ) ERC721(name_, symbol_) {
        _baseTokenURI = baseTokenURI_;
        _contractURI = contractURI_;
        _royaltyPercentage = royaltyPercentage_;
    }

    /**
     * @dev Creates a new token or edition
     * @param name Token name
     * @param description Token description
     * @param imageURI Image URI
     * @param externalURL External URL
     * @param attributes Array of attributes
     * @param editionSize Edition size (0 for unique)
     * @param price Price per token in wei
     */
    function createToken(
        string memory name,
        string memory description,
        string memory imageURI,
        string memory externalURL,
        string[] memory attributes,
        uint256 editionSize,
        uint256 price
    ) external {
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _tokenAttributes[tokenId] = TokenAttributes({
            name: name,
            description: description,
            imageURI: imageURI,
            externalURL: externalURL,
            attributes: attributes
        });

        _editionSizes[tokenId] = editionSize;
        _tokenPrices[tokenId] = price;
        _tokenCreators[tokenId] = msg.sender;

        emit TokenCreated(tokenId, msg.sender, name, editionSize, price);
    }

    /**
     * @dev Mints a token or edition
     * @param tokenId ID of the token to mint
     */
    function mintToken(uint256 tokenId) external payable {
        require(_exists(tokenId), "Token does not exist");
        require(
            _editionSizes[tokenId] == 0 || _mintedCounts[tokenId] < _editionSizes[tokenId],
            "Edition is sold out"
        );
        require(msg.value >= _tokenPrices[tokenId], "Insufficient payment");

        uint256 editionNumber = _editionSizes[tokenId] == 0 ? 0 : _mintedCounts[tokenId] + 1;
        _mintedCounts[tokenId]++;

        uint256 newTokenId = tokenId;
        if (_editionSizes[tokenId] > 0) {
            newTokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            _tokenAttributes[newTokenId] = _tokenAttributes[tokenId];
        }

        _safeMint(msg.sender, newTokenId);
        emit TokenMinted(tokenId, msg.sender, editionNumber);

        // Distribute payment
        if (_tokenPrices[tokenId] > 0) {
            uint256 royaltyAmount = (_tokenPrices[tokenId] * _royaltyPercentage) / 10000;
            uint256 creatorAmount = _tokenPrices[tokenId] - royaltyAmount;

            payable(_tokenCreators[tokenId]).transfer(creatorAmount);
            if (royaltyAmount > 0) {
                payable(owner()).transfer(royaltyAmount);
            }
        }
    }

    /**
     * @dev Returns token attributes
     * @param tokenId ID of the token
     */
    function getTokenAttributes(uint256 tokenId)
        external
        view
        returns (
            string memory name,
            string memory description,
            string memory imageURI,
            string memory externalURL,
            string[] memory attributes,
            uint256 editionSize,
            uint256 mintedCount,
            uint256 price,
            address creator
        )
    {
        require(_exists(tokenId), "Token does not exist");
        TokenAttributes storage attr = _tokenAttributes[tokenId];
        return (
            attr.name,
            attr.description,
            attr.imageURI,
            attr.externalURL,
            attr.attributes,
            _editionSizes[tokenId],
            _mintedCounts[tokenId],
            _tokenPrices[tokenId],
            _tokenCreators[tokenId]
        );
    }

    /**
     * @dev Updates royalty percentage
     * @param newPercentage New royalty percentage in basis points
     */
    function updateRoyaltyPercentage(uint256 newPercentage) external onlyOwner {
        require(newPercentage <= 10000, "Royalty too high");
        _royaltyPercentage = newPercentage;
        emit RoyaltiesUpdated(newPercentage);
    }

    /**
     * @dev Updates contract URI
     * @param newContractURI New contract URI
     */
    function setContractURI(string memory newContractURI) external onlyOwner {
        _contractURI = newContractURI;
    }

    /**
     * @dev Returns contract URI
     */
    function contractURI() external view returns (string memory) {
        return _contractURI;
    }

    /**
     * @dev Returns base URI
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Returns token URI
     * @param tokenId ID of the token
     */
    function tokenURI(uint256 tokenId)
        public
        view
        override
        returns (string memory)
    {
        require(_exists(tokenId), "Token does not exist");
        return string(abi.encodePacked(_baseTokenURI, tokenId.toString()));
    }

    /**
     * @dev Withdraws contract balance to owner
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Checks if token exists
     * @param tokenId ID of the token
     */
    function _exists(uint256 tokenId) internal view returns (bool) {
        return tokenId < _tokenIdCounter.current();
    }
}
```
