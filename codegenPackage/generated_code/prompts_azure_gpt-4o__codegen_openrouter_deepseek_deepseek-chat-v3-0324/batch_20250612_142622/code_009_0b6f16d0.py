"""
Generated Code Metadata:
========================
Original URL: https://mint.fuckopensea.art
Prompt: Develop a smart contract feature that prevents the use of OpenSea for trading NFTs, while allowing other marketplaces like Blur or Looks Rare, as discussed on the "Fuck OpenSea" website.
Generated: DETERMINISTIC_0b6f16d0e14691e3
Batch ID: 20250612_142622
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract AntiOpenSeaNFT is ERC721, Ownable {
    // Mapping to store operator approvals
    mapping(address => bool) private _blockedOperators;

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        // Block OpenSea's Seaport contract by default
        _blockedOperators[0x00000000006c3852cbEf3e08E8dF289169EdE581] = true;
    }

    /**
     * @dev Override isApprovedForAll to block OpenSea's operator
     */
    function isApprovedForAll(address owner, address operator) 
        public 
        view 
        virtual 
        override 
        returns (bool) 
    {
        if (_blockedOperators[operator]) {
            return false;
        }
        return super.isApprovedForAll(owner, operator);
    }

    /**
     * @dev Add or remove operators from the blocked list
     * @param operator Address of the operator to modify
     * @param blocked Whether to block or unblock the operator
     */
    function setOperatorStatus(address operator, bool blocked) external onlyOwner {
        _blockedOperators[operator] = blocked;
    }

    /**
     * @dev Check if an operator is blocked
     * @param operator Address to check
     */
    function isOperatorBlocked(address operator) external view returns (bool) {
        return _blockedOperators[operator];
    }
}
```
