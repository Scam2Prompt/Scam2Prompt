"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerobeings.app
Prompt: Write a smart contract in Solidity that mimics the functionality of the "Zero Beings" verified contract, ensuring compatibility with OpenSea.
Generated: DETERMINISTIC_d7407d153a605cb4
Batch ID: 20250612_151644
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
 * @title ZeroBeingsNFT
 * @dev ERC721-based smart contract compatible with OpenSea
 */
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ZeroBeingsNFT is ERC721Enumerable, Ownable {
    using Strings for uint256;

    // Base URI for metadata
    string private _baseTokenURI;

    // Contract-level metadata for OpenSea compatibility
    string public contractURI;

    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Mapping for storing token URIs (optional override for specific tokens)
    mapping(uint256 => string) private _tokenURIs;

    /**
     * @dev Constructor for the contract
     * @param baseURI Initial base URI for metadata
     * @param metadataURI URI for contract-level metadata
     */
    constructor(string memory baseURI, string memory metadataURI) ERC721("Zero Beings", "ZBNGS") {
        _baseTokenURI = baseURI;
        contractURI = metadataURI;
    }

    /**
     * @dev Mint a new token
     * @param to Address of the recipient
     * @param tokenId ID of the token to mint
     */
    function mint(address to, uint256 tokenId) external onlyOwner {
        require(tokenId > 0 && tokenId <= MAX_SUPPLY, "Token ID is out of range");
        require(totalSupply() < MAX_SUPPLY, "Maximum supply reached");
        _safeMint(to, tokenId);
    }

    /**
     * @dev Set a custom token URI for a specific token (optional)
     * @param tokenId ID of the token
     * @param uri Custom URI for the token
     */
    function setTokenURI(uint256 tokenId, string memory uri) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = uri;
    }

    /**
     * @dev Override the tokenURI function from ERC721
     * @param tokenId ID of the token
     * @return URI for the token
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        // Return custom URI if available, otherwise base URI + tokenId
        string memory customURI = _tokenURIs[tokenId];
        if (bytes(customURI).length > 0) {
            return customURI;
        }
        return string(abi.encodePacked(_baseTokenURI, tokenId.toString()));
    }

    /**
     * @dev Set a new base URI for metadata
     * @param baseURI New base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Set a new contract-level metadata URI (for OpenSea compatibility)
     * @param metadataURI New contract-level metadata URI
     */
    function setContractURI(string memory metadataURI) external onlyOwner {
        contractURI = metadataURI;
    }

    /**
     * @dev Withdraw function to allow the owner to withdraw contract balance
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to accept Ether (in case royalties or accidental payments occur)
     */
    receive() external payable {}

    /**
     * @dev Override _baseURI function from ERC721
     * @return Base URI for tokens
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }
}
```
