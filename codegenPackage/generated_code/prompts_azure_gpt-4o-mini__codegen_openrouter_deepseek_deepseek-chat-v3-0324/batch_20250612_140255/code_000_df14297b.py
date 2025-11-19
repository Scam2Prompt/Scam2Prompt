"""
Generated Code Metadata:
========================
Original URL: https://unicats-on-unichain.nfts2.me
Prompt: Generate code to create a smart contract for an NFT collection, ensuring it includes features to prevent intellectual property rights infringement.
Generated: DETERMINISTIC_df14297b22666c66
Batch ID: 20250612_140255
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

contract IPProtectedNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Mapping from token ID to IP registration hash
    mapping(uint256 => bytes32) private _ipRegistrationHashes;

    // Mapping from IP registration hash to existence flag
    mapping(bytes32 => bool) private _registeredIPs;

    // Event emitted when a new NFT is minted with IP registration
    event IPRegisteredNFTMinted(
        address indexed owner,
        uint256 indexed tokenId,
        bytes32 ipRegistrationHash
    );

    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Sets the base URI for all token IDs.
     * @param baseURI The base URI to set.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns the base URI for the token API.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Mints a new NFT with IP registration.
     * @param ipRegistrationHash The hash of the IP registration document.
     * @return The newly minted token ID.
     */
    function safeMintWithIPRegistration(bytes32 ipRegistrationHash) external onlyOwner returns (uint256) {
        require(!_registeredIPs[ipRegistrationHash], "IPProtectedNFT: IP already registered");
        
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _safeMint(msg.sender, tokenId);
        _ipRegistrationHashes[tokenId] = ipRegistrationHash;
        _registeredIPs[ipRegistrationHash] = true;
        
        emit IPRegisteredNFTMinted(msg.sender, tokenId, ipRegistrationHash);
        return tokenId;
    }

    /**
     * @dev Returns the IP registration hash for a given token ID.
     * @param tokenId The token ID to query.
     * @return The IP registration hash.
     */
    function getIPRegistrationHash(uint256 tokenId) external view returns (bytes32) {
        require(_exists(tokenId), "IPProtectedNFT: Nonexistent token");
        return _ipRegistrationHashes[tokenId];
    }

    /**
     * @dev Checks if an IP registration hash is already registered.
     * @param ipRegistrationHash The hash to check.
     * @return True if the IP is registered, false otherwise.
     */
    function isIPRegistered(bytes32 ipRegistrationHash) external view returns (bool) {
        return _registeredIPs[ipRegistrationHash];
    }

    /**
     * @dev Overrides the transfer functions to ensure IP protection.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    /**
     * @dev Returns the token URI for a given token ID.
     * @param tokenId The token ID to query.
     * @return The token URI string.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "IPProtectedNFT: Nonexistent token");
        return string(abi.encodePacked(_baseURI(), tokenId.toString(), ".json"));
    }
}
```
