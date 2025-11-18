"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pigc.pages.dev
Prompt: Create a function in Solidity to retrieve Pigcoin token metadata from its contract on the Polygon blockchain.
Generated: DETERMINISTIC_7cac69746fd32799
Batch ID: 20250612_152109
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
 * @title PigcoinMetadataRetriever
 * @dev A contract to retrieve Pigcoin token metadata from its contract on the Polygon blockchain.
 */
contract PigcoinMetadataRetriever {
    // Address of the Pigcoin token contract.
    address public pigcoinContractAddress;

    /**
     * @dev Constructor to initialize the Pigcoin contract address.
     * @param _pigcoinContractAddress The address of the Pigcoin token contract.
     */
    constructor(address _pigcoinContractAddress) {
        require(_pigcoinContractAddress != address(0), "Invalid contract address");
        pigcoinContractAddress = _pigcoinContractAddress;
    }

    /**
     * @dev Interface to interact with the Pigcoin ERC-721 contract.
     */
    interface PigcoinContract {
        function name() external view returns (string memory);
        function symbol() external view returns (string memory);
        function tokenURI(uint256 tokenId) external view returns (string memory);
    }

    /**
     * @dev Function to retrieve the name of the Pigcoin token.
     * @return The name of the Pigcoin token.
     */
    function getTokenName() external view returns (string memory) {
        PigcoinContract pigcoin = PigcoinContract(pigcoinContractAddress);
        return pigcoin.name();
    }

    /**
     * @dev Function to retrieve the symbol of the Pigcoin token.
     * @return The symbol of the Pigcoin token.
     */
    function getTokenSymbol() external view returns (string memory) {
        PigcoinContract pigcoin = PigcoinContract(pigcoinContractAddress);
        return pigcoin.symbol();
    }

    /**
     * @dev Function to retrieve the token URI for a specific token ID.
     * @param tokenId The ID of the token whose URI is to be retrieved.
     * @return The metadata URI of the token.
     */
    function getTokenURI(uint256 tokenId) external view returns (string memory) {
        PigcoinContract pigcoin = PigcoinContract(pigcoinContractAddress);
        return pigcoin.tokenURI(tokenId);
    }
}
```
