"""
Generated Code Metadata:
========================
Original URL: https://shibasaga-io.web.app
Prompt: Propose a set of NFT standards (e.g., ERC-721, ERC-1155) for a gaming metaverse like ShiaVerse, considering interoperability and scalability requirements.
Generated: DETERMINISTIC_9c6eb73b8c844eb7
Batch ID: 20250622_210348
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
 * @title ShiaVerseNFT Standards
 * @dev This contract implements both ERC-721 and ERC-1155 standards to support
 *      interoperability and scalability for a gaming metaverse like ShiaVerse.
 *      ERC-721 is used for unique assets (e.g., characters, rare items), while
 *      ERC-1155 is used for fungible and semi-fungible assets (e.g., consumables, skins).
 */

// Importing OpenZeppelin libraries for ERC-721 and ERC-1155 standards
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract ShiaVerseNFT is ERC721, ERC1155, Ownable {
    using Counters for Counters.Counter;

    // Counter for ERC-721 token IDs
    Counters.Counter private _erc721TokenIdCounter;

    // Base URI for ERC-721 tokens
    string private _erc721BaseURI;

    // Mapping for metadata URIs for ERC-1155 tokens
    mapping(uint256 => string) private _erc1155TokenURIs;

    /**
     * @dev Constructor initializes both ERC-721 and ERC-1155 standards.
     * @param erc721Name Name of the ERC-721 token collection.
     * @param erc721Symbol Symbol of the ERC-721 token collection.
     * @param erc1155BaseURI Base URI for ERC-1155 tokens.
     */
    constructor(
        string memory erc721Name,
        string memory erc721Symbol,
        string memory erc1155BaseURI
    ) ERC721(erc721Name, erc721Symbol) ERC1155(erc1155BaseURI) {
        _erc721BaseURI = erc1155BaseURI; // Default base URI for ERC-721 tokens
    }

    // ========================= ERC-721 Functions =========================

    /**
     * @dev Mint a new ERC-721 token.
     * @param to Address to receive the token.
     */
    function mintERC721(address to) external onlyOwner {
        uint256 tokenId = _erc721TokenIdCounter.current();
        _erc721TokenIdCounter.increment();
        _safeMint(to, tokenId);
    }

    /**
     * @dev Override base URI for ERC-721 tokens.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _erc721BaseURI;
    }

    /**
     * @dev Set a new base URI for ERC-721 tokens.
     * @param newBaseURI New base URI string.
     */
    function setERC721BaseURI(string memory newBaseURI) external onlyOwner {
        _erc721BaseURI = newBaseURI;
    }

    // ========================= ERC-1155 Functions =========================

    /**
     * @dev Mint new ERC-1155 tokens.
     * @param to Address to receive the tokens.
     * @param id Token ID to mint.
     * @param amount Number of tokens to mint.
     * @param data Additional data (if any).
     */
    function mintERC1155(
        address to,
        uint256 id,
        uint256 amount,
        bytes memory data
    ) external onlyOwner {
        _mint(to, id, amount, data);
    }

    /**
     * @dev Batch mint new ERC-1155 tokens.
     * @param to Address to receive the tokens.
     * @param ids Array of token IDs to mint.
     * @param amounts Array of token amounts to mint.
     * @param data Additional data (if any).
     */
    function mintBatchERC1155(
        address to,
        uint256[] memory ids,
        uint256[] memory amounts,
        bytes memory data
    ) external onlyOwner {
        _mintBatch(to, ids, amounts, data);
    }

    /**
     * @dev Set metadata URI for a specific ERC-1155 token ID.
     * @param id Token ID.
     * @param uri Metadata URI string.
     */
    function setERC1155TokenURI(uint256 id, string memory uri) external onlyOwner {
        _erc1155TokenURIs[id] = uri;
    }

    /**
     * @dev Override URI function for ERC-1155 tokens.
     * @param id Token ID.
     * @return Metadata URI string.
     */
    function uri(uint256 id) public view override returns (string memory) {
        return _erc1155TokenURIs[id];
    }

    // ========================= Interoperability =========================

    /**
     * @dev Fallback function to handle unexpected calls.
     */
    fallback() external payable {}

    /**
     * @dev Receive function to handle direct payments.
     */
    receive() external payable {}
}
```
