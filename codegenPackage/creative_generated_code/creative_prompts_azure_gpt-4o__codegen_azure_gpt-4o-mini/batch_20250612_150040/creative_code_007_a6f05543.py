"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patch-monorepo-linea.vercel.app
Prompt: Create a smart contract function that allows users to mint `.linea` domains and directs proceeds to ecosystem funding and grants, as described on the Linea domains page.
Generated: DETERMINISTIC_a6f055438965908d
Batch ID: 20250612_150040
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title LineaDomain
 * @dev A smart contract for minting .linea domains
 */
contract LineaDomain is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIdCounter;
    string private _baseTokenURI;
    address payable public ecosystemFundAddress;

    // Event emitted when a new domain is minted
    event DomainMinted(address indexed owner, uint256 tokenId, string domainName);

    // Constructor to set the base URI and ecosystem fund address
    constructor(string memory baseTokenURI, address payable fundAddress) 
        ERC721("LineaDomain", ".linea") 
    {
        _baseTokenURI = baseTokenURI;
        ecosystemFundAddress = fundAddress;
    }

    /**
     * @notice Mint a new .linea domain
     * @param domainName The name of the domain to mint
     */
    function mintDomain(string memory domainName) external payable {
        require(msg.value > 0.01 ether, "Insufficient funds sent for minting");
        require(bytes(domainName).length > 0, "Domain name cannot be empty");

        // Increment token ID and mint the domain
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _tokenIdCounter.increment();

        // Emit event for the minted domain
        emit DomainMinted(msg.sender, tokenId, domainName);
        
        // Forward funds to the ecosystem funding address
        (bool success, ) = ecosystemFundAddress.call{value: msg.value}("");
        require(success, "Failed to transfer funds to the ecosystem fund");
    }

    /**
     * @notice Set a new ecosystem funding address
     * @param newFundAddress The address of the new funding address
     */
    function setEcosystemFundAddress(address payable newFundAddress) external onlyOwner {
        require(newFundAddress != address(0), "Invalid address");
        ecosystemFundAddress = newFundAddress;
    }

    /**
     * @notice Override the base URI for metadata
     * @return The base URI for the token metadata
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @notice Withdraw funds from the contract
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Failed to withdraw funds");
    }

    /**
     * @notice Fallback function to accept ether
     */
    receive() external payable {}
}
```
