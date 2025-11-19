"""
Generated Code Metadata:
========================
Original URL: https://website-9v1.pages.dev
Prompt: Write a Solidity function to enforce cryptographic protection of PLR content during the NFT minting process, ensuring compliance with PLR license rules.
Generated: DETERMINISTIC_33608eedac160628
Batch ID: 20250612_154520
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
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ProtectedContentNFT is ERC721, Ownable {
    using ECDSA for bytes32;

    struct ContentLicense {
        string contentHash;
        uint256 expirationTimestamp;
        address licensee;
        bool isActive;
    }

    mapping(uint256 => ContentLicense) private _tokenLicenses;
    mapping(string => bool) private _usedHashes;
    address private _verifier;

    event ContentProtected(
        uint256 indexed tokenId,
        string contentHash,
        uint256 expirationTimestamp,
        address indexed licensee
    );

    constructor(address verifier) ERC721("ProtectedContentNFT", "PCNFT") {
        require(verifier != address(0), "Invalid verifier address");
        _verifier = verifier;
    }

    function mintWithLicense(
        address to,
        uint256 tokenId,
        string memory contentHash,
        uint256 expirationTimestamp,
        bytes memory signature
    ) external {
        require(!_exists(tokenId), "Token already minted");
        require(!_usedHashes[contentHash], "Content hash already used");
        require(expirationTimestamp > block.timestamp, "License already expired");

        bytes32 messageHash = keccak256(
            abi.encodePacked(
                to,
                tokenId,
                contentHash,
                expirationTimestamp
            )
        );

        address signer = messageHash.toEthSignedMessageHash().recover(signature);
        require(signer == _verifier, "Invalid license signature");

        _mint(to, tokenId);
        _tokenLicenses[tokenId] = ContentLicense(
            contentHash,
            expirationTimestamp,
            to,
            true
        );
        _usedHashes[contentHash] = true;

        emit ContentProtected(tokenId, contentHash, expirationTimestamp, to);
    }

    function verifyLicense(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        ContentLicense memory license = _tokenLicenses[tokenId];
        return license.isActive && license.expirationTimestamp > block.timestamp;
    }

    function getLicenseInfo(uint256 tokenId) external view returns (ContentLicense memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenLicenses[tokenId];
    }

    function revokeLicense(uint256 tokenId) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        _tokenLicenses[tokenId].isActive = false;
    }

    function updateVerifier(address newVerifier) external onlyOwner {
        require(newVerifier != address(0), "Invalid verifier address");
        _verifier = newVerifier;
    }
}
```
