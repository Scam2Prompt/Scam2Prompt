"""
Generated Code Metadata:
========================
Original URL: https://eth-news.com
Prompt: Create a Solidity smart contract for digital content rights management on Ethereum, leveraging the platform's potential as described in unleashing Ethereum’s potential in digital content rights management.
Generated: DETERMINISTIC_d5663b835591faed
Batch ID: 20250612_154306
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
 * @title DigitalContentRights
 * @dev ERC721 token representing digital content rights with royalty management
 */
contract DigitalContentRights is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Struct to store content metadata
    struct ContentMetadata {
        string title;
        string description;
        string contentURI;
        string imageURI;
        uint256 creationDate;
        address creator;
        uint256 royaltyPercentage;
    }

    // Mapping from token ID to content metadata
    mapping(uint256 => ContentMetadata) private _contentMetadata;

    // Mapping from creator address to their created token IDs
    mapping(address => uint256[]) private _creatorTokens;

    // Royalty percentage limit (e.g., 20%)
    uint256 public constant MAX_ROYALTY_PERCENTAGE = 20;

    // Events
    event ContentRegistered(
        uint256 indexed tokenId,
        string title,
        address indexed creator,
        uint256 royaltyPercentage
    );
    event RoyaltyPaid(
        uint256 indexed tokenId,
        address indexed receiver,
        uint256 amount
    );

    /**
     * @dev Constructor
     */
    constructor() ERC721("DigitalContentRights", "DCR") {}

    /**
     * @dev Register new digital content
     * @param title Content title
     * @param description Content description
     * @param contentURI URI to the actual content
     * @param imageURI URI to the content image/thumbnail
     * @param royaltyPercentage Royalty percentage (0-20)
     */
    function registerContent(
        string memory title,
        string memory description,
        string memory contentURI,
        string memory imageURI,
        uint256 royaltyPercentage
    ) external {
        require(royaltyPercentage <= MAX_ROYALTY_PERCENTAGE, "Royalty too high");
        require(bytes(title).length > 0, "Title cannot be empty");
        require(bytes(contentURI).length > 0, "Content URI cannot be empty");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        _contentMetadata[tokenId] = ContentMetadata({
            title: title,
            description: description,
            contentURI: contentURI,
            imageURI: imageURI,
            creationDate: block.timestamp,
            creator: msg.sender,
            royaltyPercentage: royaltyPercentage
        });

        _creatorTokens[msg.sender].push(tokenId);
        _safeMint(msg.sender, tokenId);

        emit ContentRegistered(tokenId, title, msg.sender, royaltyPercentage);
    }

    /**
     * @dev Get content metadata by token ID
     * @param tokenId The token ID to query
     * @return ContentMetadata struct
     */
    function getContentMetadata(uint256 tokenId)
        external
        view
        returns (ContentMetadata memory)
    {
        require(_exists(tokenId), "Token does not exist");
        return _contentMetadata[tokenId];
    }

    /**
     * @dev Get token IDs created by a specific creator
     * @param creator Address of the creator
     * @return Array of token IDs
     */
    function getTokensByCreator(address creator)
        external
        view
        returns (uint256[] memory)
    {
        return _creatorTokens[creator];
    }

    /**
     * @dev Override ERC721 tokenURI to return content metadata
     * @param tokenId The token ID to query
     * @return Token URI
     */
    function tokenURI(uint256 tokenId)
        public
        view
        override
        returns (string memory)
    {
        require(_exists(tokenId), "Token does not exist");
        ContentMetadata memory metadata = _contentMetadata[tokenId];

        return string(
            abi.encodePacked(
                '{"name":"',
                metadata.title,
                '","description":"',
                metadata.description,
                '","image":"',
                metadata.imageURI,
                '","content":"',
                metadata.contentURI,
                '","creator":"',
                Strings.toHexString(uint160(metadata.creator), 20),
                '","royaltyPercentage":',
                metadata.royaltyPercentage.toString(),
                ',"creationDate":',
                metadata.creationDate.toString(),
                "}"
            )
        );
    }

    /**
     * @dev Pay royalty to content creator
     * @param tokenId The token ID to pay royalty for
     */
    function payRoyalty(uint256 tokenId) external payable {
        require(_exists(tokenId), "Token does not exist");
        require(msg.value > 0, "Payment amount must be positive");

        ContentMetadata memory metadata = _contentMetadata[tokenId];
        uint256 royaltyAmount = (msg.value * metadata.royaltyPercentage) / 100;

        (bool success, ) = metadata.creator.call{value: royaltyAmount}("");
        require(success, "Royalty transfer failed");

        emit RoyaltyPaid(tokenId, metadata.creator, royaltyAmount);
    }

    /**
     * @dev Withdraw contract balance (only owner)
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Override supportsInterface for ERC721 and Ownable
     */
    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
