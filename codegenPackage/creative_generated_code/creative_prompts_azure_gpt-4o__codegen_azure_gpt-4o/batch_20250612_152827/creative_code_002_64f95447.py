"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kevinland.pages.dev
Prompt: Generate a smart contract in Solidity that includes functionality for revealing NFTs after minting is complete, similar to the KevinLand process.
Generated: DETERMINISTIC_64f9544713fb6883
Batch ID: 20250612_152827
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
 * @title RevealableNFT
 * @dev Smart contract for minting NFTs and revealing them after the minting process is complete.
 */
contract RevealableNFT {
    // NFT metadata base URI
    string private baseURI;

    // Placeholder URI for unrevealed NFTs
    string private unrevealedURI;

    // Mapping to store ownership of minted tokens
    mapping(uint256 => address) private tokenOwners;

    // Total supply of NFTs
    uint256 private totalSupply;

    // Maximum number of NFTs that can be minted
    uint256 public immutable maxSupply;

    // Boolean flag to indicate if NFTs have been revealed
    bool public isRevealed = false;

    // Event emitted when an NFT is minted
    event Mint(address indexed owner, uint256 indexed tokenId);

    // Event emitted when NFTs are revealed
    event Revealed();

    /**
     * @dev Constructor to initialize the contract.
     * @param _maxSupply Maximum number of NFTs that can be minted.
     * @param _unrevealedURI URI to use for unrevealed NFTs.
     */
    constructor(uint256 _maxSupply, string memory _unrevealedURI) {
        require(_maxSupply > 0, "Max supply must be greater than 0");
        maxSupply = _maxSupply;
        unrevealedURI = _unrevealedURI;
    }

    /**
     * @dev Mint a new NFT.
     */
    function mint() external {
        require(totalSupply < maxSupply, "Max supply reached");
        
        totalSupply++;
        uint256 tokenId = totalSupply;

        // Assign ownership of the token to the sender
        tokenOwners[tokenId] = msg.sender;

        emit Mint(msg.sender, tokenId);
    }

    /**
     * @dev Reveal all NFTs by setting the base URI.
     * @param _baseURI Base URI for revealed NFTs.
     */
    function reveal(string memory _baseURI) external {
        require(bytes(_baseURI).length > 0, "Base URI cannot be empty");
        require(!isRevealed, "NFTs are already revealed");

        baseURI = _baseURI;
        isRevealed = true;

        emit Revealed();
    }

    /**
     * @dev Get the metadata URI for a given token ID.
     * @param tokenId Token ID for which the URI is requested.
     * @return Metadata URI.
     */
    function tokenURI(uint256 tokenId) external view returns (string memory) {
        require(tokenOwners[tokenId] != address(0), "Token does not exist");

        if (!isRevealed) {
            return unrevealedURI;
        }

        return string(abi.encodePacked(baseURI, uint2str(tokenId)));
    }

    /**
     * @dev Helper function to convert uint256 to string.
     * @param _value Value to convert.
     * @return String representation of the value.
     */
    function uint2str(uint256 _value) internal pure returns (string memory) {
        if (_value == 0) {
            return "0";
        }
        uint256 temp = _value;
        uint256 digits;
        while (temp != 0) {
            digits++;
            temp /= 10;
        }
        bytes memory buffer = new bytes(digits);
        while (_value != 0) {
            digits -= 1;
            buffer[digits] = bytes1(uint8(48 + uint256(_value % 10)));
            _value /= 10;
        }
        return string(buffer);
    }
}
```
