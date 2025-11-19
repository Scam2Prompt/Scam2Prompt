"""
Generated Code Metadata:
========================
Original URL: https://hypurrnft.org
Prompt: Generate a smart contract in Solidity for minting NFTs, specifically for a Genesis Collection, and include terms and conditions handling as outlined on the Hypurr NFT Mint Portal.
Generated: DETERMINISTIC_89b37bd154fa5d47
Batch ID: 20250612_153854
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title GenesisCollection contract
 * @author [Your Name]
 * @notice A smart contract for minting NFTs for the Genesis Collection
 */
contract GenesisCollection is SafeERC721, Ownable {
    // Mapping of terms and conditions hashes to their status
    mapping(bytes32 => bool) public termsAndConditions;

    // Mapping of user addresses to their mint status
    mapping(address => bool) public mintedAddresses;

    // Total supply of NFTs
    uint256 public totalSupply;

    // Maximum supply of NFTs
    uint256 public maxSupply;

    // Base URI for NFTs
    string public baseURI;

    // Token name
    string public name;

    // Token symbol
    string public symbol;

    /**
     * @notice Event emitted when an NFT is minted
     * @param _to Address of the user who minted the NFT
     * @param _tokenId ID of the minted NFT
     */
    event Minted(address indexed _to, uint256 indexed _tokenId);

    /**
     * @notice Event emitted when terms and conditions are updated
     * @param _termsHash Hash of the terms and conditions
     * @param _status Status of the terms and conditions
     */
    event TermsAndConditionsUpdated(bytes32 indexed _termsHash, bool _status);

    /**
     * @notice Constructor for the GenesisCollection contract
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     * @param _maxSupply Maximum supply of NFTs
     * @param _baseURI Base URI for NFTs
     */
    constructor(string memory _name, string memory _symbol, uint256 _maxSupply, string memory _baseURI) public {
        name = _name;
        symbol = _symbol;
        maxSupply = _maxSupply;
        baseURI = _baseURI;
    }

    /**
     * @notice Function to set terms and conditions
     * @param _termsHash Hash of the terms and conditions
     * @param _status Status of the terms and conditions
     */
    function setTermsAndConditions(bytes32 _termsHash, bool _status) public onlyOwner {
        termsAndConditions[_termsHash] = _status;
        emit TermsAndConditionsUpdated(_termsHash, _status);
    }

    /**
     * @notice Function to mint an NFT
     * @param _to Address of the user who wants to mint an NFT
     * @param _termsHash Hash of the terms and conditions
     */
    function mint(address _to, bytes32 _termsHash) public onlyOwner {
        require(termsAndConditions[_termsHash], "Terms and conditions not accepted");
        require(totalSupply < maxSupply, "Maximum supply reached");
        require(!mintedAddresses[_to], "Address already minted");

        uint256 _tokenId = totalSupply + 1;
        _mint(_to, _tokenId);
        mintedAddresses[_to] = true;
        totalSupply++;

        emit Minted(_to, _tokenId);
    }

    /**
     * @notice Function to update the base URI
     * @param _newBaseURI New base URI for NFTs
     */
    function updateBaseURI(string memory _newBaseURI) public onlyOwner {
        baseURI = _newBaseURI;
    }

    /**
     * @notice Function to get the URI of an NFT
     * @param _tokenId ID of the NFT
     * @return URI of the NFT
     */
    function uri(uint256 _tokenId) public view returns (string memory) {
        return string(abi.encodePacked(baseURI, Strings.toString(_tokenId)));
    }

    /**
     * @notice Function to check if an address has minted an NFT
     * @param _owner Address of the user
     * @return bool indicating if the address has minted an NFT
     */
    function hasMinted(address _owner) public view returns (bool) {
        return mintedAddresses[_owner];
    }
}
```
