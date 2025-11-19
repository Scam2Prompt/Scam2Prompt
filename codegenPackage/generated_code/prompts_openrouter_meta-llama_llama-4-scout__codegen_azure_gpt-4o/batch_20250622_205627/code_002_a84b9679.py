"""
Generated Code Metadata:
========================
Original URL: https://panz-3cy.pages.dev
Prompt: Generate a smart contract code in Solidity for creating a membership-based NFT collection, like Genesis PANZ, on the Ethereum blockchain.
Generated: DETERMINISTIC_a84b9679e8217034
Batch ID: 20250622_205627
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
 * @title MembershipNFT
 * @dev A smart contract for creating a membership-based NFT collection.
 *      This contract uses ERC721 standard and includes minting functionality.
 */

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MembershipNFT is ERC721Enumerable, Ownable {
    // Maximum number of NFTs that can be minted
    uint256 public maxSupply;

    // Base URI for metadata
    string private baseTokenURI;

    // Price per NFT
    uint256 public mintPrice;

    // Mapping to track membership status
    mapping(address => bool) public isMember;

    // Events
    event MembershipGranted(address indexed member);
    event MembershipRevoked(address indexed member);

    /**
     * @dev Constructor to initialize the contract.
     * @param _name Name of the NFT collection.
     * @param _symbol Symbol of the NFT collection.
     * @param _maxSupply Maximum number of NFTs that can be minted.
     * @param _mintPrice Price per NFT in wei.
     * @param _baseTokenURI Base URI for metadata.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _maxSupply,
        uint256 _mintPrice,
        string memory _baseTokenURI
    ) ERC721(_name, _symbol) {
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Function to mint a new NFT.
     * @notice Requires payment of `mintPrice` and ensures max supply is not exceeded.
     */
    function mint() external payable {
        require(totalSupply() < maxSupply, "Max supply reached");
        require(msg.value == mintPrice, "Incorrect payment amount");

        uint256 tokenId = totalSupply() + 1; // Token IDs start from 1
        _safeMint(msg.sender, tokenId);

        // Grant membership to the minter
        isMember[msg.sender] = true;
        emit MembershipGranted(msg.sender);
    }

    /**
     * @dev Function to revoke membership for a specific address.
     * @notice Only callable by the contract owner.
     * @param _member Address of the member to revoke.
     */
    function revokeMembership(address _member) external onlyOwner {
        require(isMember[_member], "Address is not a member");
        isMember[_member] = false;
        emit MembershipRevoked(_member);
    }

    /**
     * @dev Function to update the mint price.
     * @notice Only callable by the contract owner.
     * @param _newMintPrice New price per NFT in wei.
     */
    function updateMintPrice(uint256 _newMintPrice) external onlyOwner {
        mintPrice = _newMintPrice;
    }

    /**
     * @dev Function to update the base URI for metadata.
     * @notice Only callable by the contract owner.
     * @param _newBaseTokenURI New base URI for metadata.
     */
    function updateBaseURI(string memory _newBaseTokenURI) external onlyOwner {
        baseTokenURI = _newBaseTokenURI;
    }

    /**
     * @dev Override function to return the base URI for metadata.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    /**
     * @dev Function to withdraw contract balance.
     * @notice Only callable by the contract owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed");
    }
}
```
