"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintchain-mainnet.pages.dev
Prompt: Develop a Solidity smart contract to issue POAP NFTs on the Mint Blockchain, ensuring compliance with the NIP library standards.
Generated: DETERMINISTIC_e5624e4f755a2dad
Batch ID: 20250612_151141
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title POAP NFT Contract
 * @dev A contract for issuing POAP NFTs on the Mint Blockchain. 
 *      The contract complies with the NIP library standards.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract POAPNFT is ERC721Enumerable, Ownable {
    // Base URI for metadata
    string private baseTokenURI;

    // Event to log when a new POAP NFT is issued
    event POAPIssued(address indexed recipient, uint256 tokenId);

    /**
     * @dev Constructor to set the initial name, symbol, and base URI for the POAP NFTs.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     * @param initialBaseURI The initial base URI for the metadata.
     */
    constructor(string memory name, string memory symbol, string memory initialBaseURI) ERC721(name, symbol) {
        baseTokenURI = initialBaseURI;
    }

    /**
     * @dev Function to issue a new POAP NFT to a recipient.
     * @param recipient The address of the recipient to receive the POAP NFT.
     * @return tokenId The ID of the newly minted POAP NFT.
     */
    function issuePOAP(address recipient) external onlyOwner returns (uint256) {
        require(recipient != address(0), "Recipient address cannot be zero");

        uint256 tokenId = totalSupply() + 1; // Generate new token ID
        _safeMint(recipient, tokenId);      // Mint the NFT safely

        emit POAPIssued(recipient, tokenId); // Emit the event to log the minting
        return tokenId;
    }

    /**
     * @dev Function to set the base URI for the metadata.
     * @param newBaseURI The new base URI to be set.
     */
    function setBaseURI(string memory newBaseURI) external onlyOwner {
        baseTokenURI = newBaseURI;
    }

    /**
     * @dev Override function to return the base URI.
     * @return string The base token URI.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    /**
     * @dev Function to withdraw Ether from the contract (if any).
     *      Useful in case the contract receives Ether accidentally.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether available to withdraw");
        payable(msg.sender).transfer(balance);
    }

    /**
     * @dev Fallback function to handle Ether sent to the contract.
     *      The contract does not accept Ether, hence it will revert.
     */
    receive() external payable {
        revert("This contract does not accept Ether");
    }

    fallback() external payable {
        revert("This contract does not accept Ether");
    }
}
```

This Solidity smart contract creates a POAP NFT issuance system on the Mint Blockchain, adhering to best practices and standards. It includes functionality to mint NFTs, manage metadata, and handle edge cases like Ether misdelivery through proper fallback mechanisms.
