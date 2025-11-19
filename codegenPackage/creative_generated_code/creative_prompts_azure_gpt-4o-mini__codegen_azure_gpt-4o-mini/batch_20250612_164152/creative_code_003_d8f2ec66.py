"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc-wl.web.app
Prompt: Generate code for a smart contract that allows a limited number of free mints for token holders, inspired by the USDC Whitelist Mint model.
Generated: DETERMINISTIC_d8f2ec66768ff3c6
Batch ID: 20250612_164152
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

/**
 * @title LimitedMintNFT
 * @dev This smart contract allows token holders to mint a limited number of NFTs for free.
 */
contract LimitedMintNFT is ERC721Enumerable, Ownable {
    using Strings for uint256;

    // Mapping to track the number of mints per address
    mapping(address => uint256) public mintsPerAddress;

    // Maximum number of free mints allowed per address
    uint256 public constant MAX_FREE_MINTS = 1;

    // Total supply cap for the NFTs
    uint256 public constant MAX_SUPPLY = 10000;

    // Counter for the total minted NFTs
    uint256 private _tokenIdCounter;

    // Base URI for metadata
    string private _baseTokenURI;

    /**
     * @dev Event emitted when a new NFT is minted.
     */
    event Minted(address indexed to, uint256 tokenId);

    /**
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     * @param baseURI The base URI for NFT metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseURI)
        ERC721(name, symbol)
    {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Mint a new NFT. This function can only be called by a token holder.
     */
    function mint() external {
        require(mintsPerAddress[msg.sender] < MAX_FREE_MINTS, "Limit reached for free mints");
        require(_tokenIdCounter < MAX_SUPPLY, "Max supply reached");

        // Increment the mint count for the sender
        mintsPerAddress[msg.sender]++;

        // Mint the NFT
        uint256 newTokenId = _tokenIdCounter;
        _safeMint(msg.sender, newTokenId);
        _tokenIdCounter++;

        emit Minted(msg.sender, newTokenId);
    }

    /**
     * @dev Retrieve the base URI for the NFT metadata.
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Update the base URI. Only callable by the owner.
     * @param baseURI The new base URI for NFT metadata.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Withdraw contract balance to the owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Direct deposits not allowed");
    }
}
```
