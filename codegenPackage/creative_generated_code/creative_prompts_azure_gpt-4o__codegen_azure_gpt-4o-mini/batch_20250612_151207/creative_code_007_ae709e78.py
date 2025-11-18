"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-wat0x63.pages.dev
Prompt: Write a Solidity contract that pays homage to Matt Furie's creative works by including metadata or references to "Night Riders" in the token's description or functionality.
Generated: DETERMINISTIC_ae709e7894c8acd2
Batch ID: 20250612_151207
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

// Importing OpenZeppelin ERC721 implementation for Non-Fungible Tokens
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title NightRidersToken
 * @dev ERC721 token that pays homage to Matt Furie's creative works, particularly "Night Riders".
 */
contract NightRidersToken is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event emitted when a new token is minted
    event TokenMinted(address indexed to, uint256 indexed tokenId);

    /**
     * @dev Sets the values for {name} and {symbol} of the token.
     * Initializes base URI for token metadata.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param baseURI The base URI for the token metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mints a new token to the specified address.
     * @param to Address of the recipient.
     * Emits a {TokenMinted} event.
     */
    function mintToken(address to) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");

        // Increment the token ID counter and assign it to a new token
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        
        _mint(to, tokenId);
        
        emit TokenMinted(to, tokenId);
    }

    /**
     * @dev Returns the base URI for token metadata.
     * @return The base URI string.
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Allows the owner to update the base URI for token metadata.
     * @param baseURI The new base URI for the token metadata.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Returns specific token metadata including homage to "Night Riders".
     * @param tokenId The ID of the token.
     * @return A string representing the token's metadata.
     */
    function getTokenMetadata(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        
        return string(abi.encodePacked("This token pays homage to Matt Furie's 'Night Riders'. Token ID: ", uint2str(tokenId)));
    }

    /**
     * @dev Converts a uint256 to its string representation.
     * @param _i The uint256 number to convert.
     * @return The string representation of the number.
     */
    function uint2str(uint256 _i) internal pure returns (string memory) {
        if (_i == 0) {
            return "0";
        }
        uint256 j = _i;
        uint256 len;
        while (j != 0) {
            len++;
            j /= 10;
        }
        bytes memory bstr = new bytes(len);
        uint256 k = len;
        while (_i != 0) {
            bstr[--k] = bytes1(uint8(48 + _i % 10));
            _i /= 10;
        }
        return string(bstr);
    }
}
```
