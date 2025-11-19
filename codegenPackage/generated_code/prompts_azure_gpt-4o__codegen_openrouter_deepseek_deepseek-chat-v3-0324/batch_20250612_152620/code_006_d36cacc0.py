"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogsclub.web.app
Prompt: Write a Solidity smart contract to implement the token burning mechanism described in the Bitcoin Dogs tokenomics, where unsold tokens are removed after the presale ends.
Generated: DETERMINISTIC_d36cacc0f2a92785
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BitcoinDogsToken
 * @dev ERC20 token with presale functionality and token burning mechanism
 */
contract BitcoinDogsToken is ERC20, Ownable {
    uint256 public constant MAX_SUPPLY = 1000000000 * 10**18; // 1 billion tokens
    uint256 public constant PRESALE_SUPPLY = 500000000 * 10**18; // 500 million for presale
    uint256 public constant PRESALE_END_TIMESTAMP = 1735689600; // Jan 1, 2025 00:00:00 UTC
    
    bool private _presaleEnded = false;
    bool private _burned = false;

    /**
     * @dev Constructor that mints initial supply to contract owner
     */
    constructor() ERC20("Bitcoin Dogs Token", "0DOG") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Modifier to check if presale has ended
     */
    modifier onlyAfterPresale() {
        require(block.timestamp >= PRESALE_END_TIMESTAMP, "Presale has not ended yet");
        _;
    }

    /**
     * @dev Function to end presale and burn unsold tokens
     * Can only be called once after presale ends
     */
    function endPresaleAndBurn() external onlyOwner onlyAfterPresale {
        require(!_presaleEnded, "Presale already ended");
        require(!_burned, "Tokens already burned");
        
        _presaleEnded = true;
        
        uint256 currentBalance = balanceOf(msg.sender);
        uint256 unsoldTokens = currentBalance - (MAX_SUPPLY - PRESALE_SUPPLY);
        
        if (unsoldTokens > 0) {
            _burn(msg.sender, unsoldTokens);
            _burned = true;
        }
    }

    /**
     * @dev Returns whether presale has ended
     */
    function presaleEnded() external view returns (bool) {
        return _presaleEnded || block.timestamp >= PRESALE_END_TIMESTAMP;
    }

    /**
     * @dev Returns whether unsold tokens have been burned
     */
    function tokensBurned() external view returns (bool) {
        return _burned;
    }
}
```
