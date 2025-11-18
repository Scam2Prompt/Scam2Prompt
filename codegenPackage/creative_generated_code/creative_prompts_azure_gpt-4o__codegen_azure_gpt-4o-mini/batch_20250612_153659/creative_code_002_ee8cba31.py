"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappass.neocities.org
Prompt: Generate a smart contract in Solidity that enforces a maximum mint limit of one per wallet and sets the price of minting to 0 ETH, as outlined in the Dapp Pass minting rules.
Generated: DETERMINISTIC_ee8cba31402f8a26
Batch ID: 20250612_153659
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title DappPassMinting
 * @dev Smart contract for minting Dapp Pass with specific rules
 */
contract DappPassMinting is Ownable {
    using Counters for Counters.Counter;

    // Counter to track the number of minted passes
    Counters.Counter private _tokenIdCounter;

    // Mapping to track if an address has already minted a pass
    mapping(address => bool) private _hasMinted;

    // Event emitted when a new Dapp Pass is minted
    event DappPassMinted(address indexed minter, uint256 tokenId);

    /**
     * @dev Function to mint a Dapp Pass
     * Reverts if the sender has already minted a pass.
     */
    function mintDappPass() external {
        require(!_hasMinted[msg.sender], "You have already minted a Dapp Pass!");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mark the sender as having minted a pass
        _hasMinted[msg.sender] = true;

        // Emit the minting event
        emit DappPassMinted(msg.sender, tokenId);
    }

    /**
     * @dev Function to check if an address has minted a Dapp Pass
     * @param minter The address to check
     * @return bool indicating if the address has minted
     */
    function hasMinted(address minter) external view returns (bool) {
        return _hasMinted[minter];
    }

    /**
     * @dev Function to retrieve the total number of minted Dapp Passes
     * @return uint256 Total count of minted Dapp Passes
     */
    function totalMinted() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
