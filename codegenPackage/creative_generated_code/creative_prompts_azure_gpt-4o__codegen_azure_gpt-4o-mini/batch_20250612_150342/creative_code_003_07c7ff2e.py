"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-ambassadors.org
Prompt: Generate a Solidity smart contract that aligns with Starknet's mission to empower communities and increase adoption of decentralized solutions.
Generated: DETERMINISTIC_07c7ff2e5a822ffa
Batch ID: 20250612_150342
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
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CommunityToken
 * @dev A simple ERC20 token contract that empowers communities by allowing them to mint, burn, and distribute community tokens.
 */
contract CommunityToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Event emitted when tokens are minted
    event TokensMinted(address indexed recipient, uint256 amount);

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @dev Constructor that initializes the token with a name and symbol
     * @param name The name of the token
     * @param symbol The symbol of the token
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Initial token supply can be set here if needed
    }

    /**
     * @dev Mint new tokens for a specific address
     * @param recipient The address that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid address: recipient is zero address");
        require(amount > 0, "Invalid amount: must mint more than zero");

        _mint(recipient, amount);
        emit TokensMinted(recipient, amount);
    }

    /**
     * @dev Burn tokens from the caller's balance
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Invalid amount: must burn more than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Distribute tokens to multiple addresses
     * @param recipients An array of addresses to receive tokens
     * @param amounts An array of amounts corresponding to each recipient
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Length mismatch: recipients and amounts arrays must be the same length");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid address: recipient is zero address");
            require(amounts[i] > 0, "Invalid amount: must distribute more than zero");

            _mint(recipients[i], amounts[i]);
            emit TokensMinted(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Override the transfer function to enforce certain rules if needed
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "Invalid address: sender is zero address");
        require(recipient != address(0), "Invalid address: recipient is zero address");
        require(amount > 0, "Invalid amount: must transfer more than zero");
        require(balanceOf(sender) >= amount, "Insufficient balance to transfer");

        super._transfer(sender, recipient, amount);
    }
}
```
