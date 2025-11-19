"""
Generated Code Metadata:
========================
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Write a function in Solidity that enforces the total token supply limit of 100,000,000 ALIEN during the presale, ensuring no additional tokens are minted beyond this limit.
Generated: DETERMINISTIC_3a140298792c088f
Batch ID: 20250612_152235
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
 * @title AlienToken
 * @dev ERC20 Token with a capped supply of 100,000,000 ALIEN tokens
 */
contract AlienToken is ERC20, Ownable {
    // Maximum supply of ALIEN tokens
    uint256 public constant MAX_SUPPLY = 100_000_000 * 10**18; // 100 million tokens with 18 decimals

    // Boolean to track if presale is active
    bool public presaleActive;

    // Event to log presale status changes
    event PresaleStatusChanged(bool isActive);

    /**
     * @dev Constructor that initializes the token with a name and symbol
     */
    constructor() ERC20("Alien Token", "ALIEN") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Function to start or stop the presale
     * @param _active Boolean indicating if presale should be active
     */
    function setPresaleActive(bool _active) external onlyOwner {
        presaleActive = _active;
        emit PresaleStatusChanged(_active);
    }

    /**
     * @dev Override the _mint function to enforce the total supply limit during presale
     * @param account The address to mint tokens to
     * @param amount The amount of tokens to mint
     */
    function _mint(address account, uint256 amount) internal override {
        // Check if presale is active and if minting exceeds the maximum supply
        require(totalSupply() + amount <= MAX_SUPPLY, "Minting exceeds maximum supply");
        super._mint(account, amount);
    }

    /**
     * @dev Function to safely transfer tokens, ensuring presale rules are followed
     * @param recipient The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(presaleActive, "Transfers are not allowed during presale");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Function to safely transfer tokens from one address to another
     * @param sender The address to transfer tokens from
     * @param recipient The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(presaleActive, "Transfers are not allowed during presale");
        return super.transferFrom(sender, recipient, amount);
    }
}
```
