"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samoyedmint.web.app
Prompt: Generate a smart contract code for a whitelist minting process that allows token holders to mint for free, based on the Samoyed Coin model.
Generated: DETERMINISTIC_6523a10b3316addd
Batch ID: 20250612_160804
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
 * @title WhitelistMinting
 * @dev A smart contract for whitelist minting process based on a token (e.g., Samoyed Coin) model.
 * Token holders can mint for free if their wallet is whitelisted.
 */

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract WhitelistMinting is Ownable, ReentrancyGuard {
    // Address of the token (e.g., Samoyed Coin)
    IERC20 public token;

    // Mapping to track whitelisted addresses
    mapping(address => bool) public whitelist;

    // Mapping to track minting status (to ensure one-time minting per whitelisted address)
    mapping(address => bool) public hasMinted;

    // Minting event
    event Mint(address indexed minter);

    /**
     * @dev Constructor to initialize the token address.
     * @param _token Address of the token contract (e.g., Samoyed Coin).
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
    }

    /**
     * @dev Add addresses to the whitelist.
     * @param _addresses Array of addresses to be whitelisted.
     */
    function addToWhitelist(address[] calldata _addresses) external onlyOwner {
        for (uint256 i = 0; i < _addresses.length; i++) {
            whitelist[_addresses[i]] = true;
        }
    }

    /**
     * @dev Remove addresses from the whitelist.
     * @param _addresses Array of addresses to be removed from the whitelist.
     */
    function removeFromWhitelist(address[] calldata _addresses) external onlyOwner {
        for (uint256 i = 0; i < _addresses.length; i++) {
            whitelist[_addresses[i]] = false;
        }
    }

    /**
     * @dev Mint function that allows whitelisted addresses to mint for free.
     */
    function mint() external nonReentrant {
        require(whitelist[msg.sender], "Address not whitelisted");
        require(!hasMinted[msg.sender], "Address has already minted");

        // Mark the address as having minted
        hasMinted[msg.sender] = true;

        // Emit minting event
        emit Mint(msg.sender);

        // Business logic for minting can be added here
        // (e.g., transferring an NFT or performing some other minting action)
    }

    /**
     * @dev Check if an address is eligible to mint.
     * @param _address Address to check for eligibility.
     * @return bool True if eligible, false otherwise.
     */
    function isEligibleToMint(address _address) external view returns (bool) {
        return whitelist[_address] && !hasMinted[_address];
    }
}
```
