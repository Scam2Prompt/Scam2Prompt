"""
Generated Code Metadata:
========================
Original URL: https://website-9v1.pages.dev
Prompt: Write a smart contract on the Binance Smart Chain for minting NFTs that represent cryptographically protected Private Label Rights (PLR) licenses, using the ERC20 token standard for integration with $PLRT.
Generated: DETERMINISTIC_f9b2f2ac026d6016
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract PLRLicenseNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    IERC20 public plrtToken;
    bytes32 public merkleRoot;
    string public baseURI;

    struct License {
        uint256 price;
        uint256 expiration;
        string metadataHash;
    }

    mapping(uint256 => License) public licenses;
    mapping(address => uint256[]) public userLicenses;

    event LicenseMinted(
        address indexed owner,
        uint256 indexed tokenId,
        uint256 price,
        uint256 expiration,
        string metadataHash
    );

    constructor(
        address _plrtToken,
        bytes32 _merkleRoot,
        string memory _baseURI
    ) ERC721("PLRLicenseNFT", "PLRNFT") {
        plrtToken = IERC20(_plrtToken);
        merkleRoot = _merkleRoot;
        baseURI = _baseURI;
    }

    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
    }

    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }

    function createLicense(
        uint256 price,
        uint256 expiration,
        string memory metadataHash
    ) external onlyOwner returns (uint256) {
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();

        licenses[tokenId] = License(price, expiration, metadataHash);
        return tokenId;
    }

    function mintLicense(
        uint256 tokenId,
        bytes32[] calldata merkleProof
    ) external {
        require(_exists(tokenId), "License does not exist");
        License memory license = licenses[tokenId];
        require(license.expiration > block.timestamp, "License has expired");

        // Verify Merkle proof if needed
        if (merkleRoot != bytes32(0)) {
            bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
            require(
                MerkleProof.verify(merkleProof, merkleRoot, leaf),
                "Invalid proof"
            );
        }

        // Transfer PLRT tokens
        require(
            plrtToken.transferFrom(msg.sender, address(this), license.price),
            "PLRT transfer failed"
        );

        _safeMint(msg.sender, tokenId);
        userLicenses[msg.sender].push(tokenId);

        emit LicenseMinted(
            msg.sender,
            tokenId,
            license.price,
            license.expiration,
            license.metadataHash
        );
    }

    function getUserLicenses(address user) external view returns (uint256[] memory) {
        return userLicenses[user];
    }

    function getLicenseDetails(uint256 tokenId) external view returns (License memory) {
        require(_exists(tokenId), "License does not exist");
        return licenses[tokenId];
    }

    function withdrawPLRT(address to) external onlyOwner {
        uint256 balance = plrtToken.balanceOf(address(this));
        require(balance > 0, "No PLRT to withdraw");
        require(plrtToken.transfer(to, balance), "Transfer failed");
    }

    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }
}
```
