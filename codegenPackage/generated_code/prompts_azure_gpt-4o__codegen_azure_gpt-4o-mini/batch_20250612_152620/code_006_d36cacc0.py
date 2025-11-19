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
 * @dev Implementation of the Bitcoin Dogs token with a burning mechanism for unsold tokens.
 */
contract BitcoinDogsToken is ERC20, Ownable {
    // State variable to track if the presale has ended
    bool public presaleEnded = false;

    // Event to log the burning of tokens
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Bitcoin Dogs", "BTCDOG") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    /**
     * @dev Function to end the presale and burn unsold tokens.
     * Can only be called by the contract owner.
     */
    function endPresale() external onlyOwner {
        require(!presaleEnded, "Presale has already ended");
        
        // Mark presale as ended
        presaleEnded = true;

        // Calculate unsold tokens (assuming the total supply is known)
        uint256 unsoldTokens = balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to burn");

        // Burn the unsold tokens
        _burn(address(this), unsoldTokens);
        emit TokensBurned(address(this), unsoldTokens);
    }

    /**
     * @dev Override the transfer function to prevent transfers during presale.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(presaleEnded, "Transfers are not allowed until presale ends");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Override the transferFrom function to prevent transfers during presale.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(presaleEnded, "Transfers are not allowed until presale ends");
        return super.transferFrom(sender, recipient, amount);
    }
}
```
