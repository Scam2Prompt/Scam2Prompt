"""
Generated Code Metadata:
========================
Original URL: https://phantom237.com
Prompt: Develop a smart contract in Solidity for a meme coin similar to PHANTOM237 ($PHTM), including functionality for tracking holders and limiting max supply.
Generated: DETERMINISTIC_6f6eec2e21bdd980
Batch ID: 20250612_155057
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

contract Phantom237 is ERC20, Ownable {
    uint256 private constant MAX_SUPPLY = 237000000000 * 10**18; // 237 billion tokens
    uint256 private _totalMinted = 0;
    
    // Mapping to track token holders
    mapping(address => bool) private _holders;
    address[] private _holderAddresses;

    event HolderAdded(address indexed account);
    event HolderRemoved(address indexed account);

    constructor() ERC20("Phantom237", "PHTM") {
        // Mint initial supply to contract deployer
        _mint(msg.sender, MAX_SUPPLY);
        _totalMinted = MAX_SUPPLY;
        _addHolder(msg.sender);
    }

    // Override transfer to track holders
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        super._transfer(sender, recipient, amount);
        
        // Add recipient to holders if they receive tokens and aren't already tracked
        if (balanceOf(recipient) > 0 && !_holders[recipient]) {
            _addHolder(recipient);
        }
        
        // Remove sender from holders if they've sent all their tokens
        if (balanceOf(sender) == 0 && _holders[sender]) {
            _removeHolder(sender);
        }
    }

    // Add a new holder to tracking
    function _addHolder(address account) private {
        if (!_holders[account]) {
            _holders[account] = true;
            _holderAddresses.push(account);
            emit HolderAdded(account);
        }
    }

    // Remove a holder from tracking
    function _removeHolder(address account) private {
        if (_holders[account]) {
            _holders[account] = false;
            
            // Remove from holderAddresses array
            for (uint256 i = 0; i < _holderAddresses.length; i++) {
                if (_holderAddresses[i] == account) {
                    _holderAddresses[i] = _holderAddresses[_holderAddresses.length - 1];
                    _holderAddresses.pop();
                    break;
                }
            }
            
            emit HolderRemoved(account);
        }
    }

    // Get total number of holders
    function getHolderCount() public view returns (uint256) {
        return _holderAddresses.length;
    }

    // Check if an address is a holder
    function isHolder(address account) public view returns (bool) {
        return _holders[account];
    }

    // Get holder by index (for enumeration)
    function getHolderByIndex(uint256 index) public view returns (address) {
        require(index < _holderAddresses.length, "Index out of bounds");
        return _holderAddresses[index];
    }

    // Prevent any additional minting beyond constructor
    function mint(address /*to*/, uint256 /*amount*/) public pure {
        revert("Minting is disabled after initial supply");
    }

    // Get max supply
    function maxSupply() public pure returns (uint256) {
        return MAX_SUPPLY;
    }

    // Get total minted tokens
    function totalMinted() public view returns (uint256) {
        return _totalMinted;
    }
}
```
