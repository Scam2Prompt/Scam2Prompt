"""
Generated Code Metadata:
========================
Original URL: https://faint-vr-immense.on-fleek.app
Prompt: Develop a smart contract function in Solidity to implement the buyback and burn model for deflationary tokens like MCADE, referencing the Metacade token utility benefits.
Generated: DETERMINISTIC_094ad487b908393d
Batch ID: 20250612_150040
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MetacadeToken
 * @author [Your Name]
 * @notice Implementation of the Metacade token with buyback and burn functionality.
 */
contract MetacadeToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of addresses to their respective buyback fees
    mapping(address => uint256) public buybackFees;

    // Address of the token owner
    address public owner;

    // Event emitted when a buyback and burn transaction occurs
    event BuybackAndBurn(address indexed sender, uint256 amount);

    /**
     * @notice Constructor for the MetacadeToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        // Mint the initial supply to the contract owner
        _mint(msg.sender, initialSupply);
        owner = msg.sender;
    }

    /**
     * @notice Sets the buyback fee for a specific address.
     * @param account The address to set the buyback fee for.
     * @param fee The buyback fee as a percentage (in basis points, e.g., 100 = 1%).
     */
    function setBuybackFee(address account, uint256 fee) public onlyOwner {
        require(fee <= 10000, "Buyback fee must not exceed 100%");
        buybackFees[account] = fee;
    }

    /**
     * @notice Buys back and burns tokens from the sender.
     * @param amount The amount of tokens to buy back and burn.
     */
    function buybackAndBurn(uint256 amount) public nonReentrant {
        // Check if the sender has sufficient balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Calculate the buyback fee
        uint256 fee = (amount * buybackFees[msg.sender]) / 10000;
        uint256 netAmount = amount - fee;

        // Burn the tokens
        _burn(msg.sender, amount);

        // Transfer the buyback fee to the owner
        if (fee > 0) {
            _transfer(msg.sender, owner, fee);
        }

        // Emit the BuybackAndBurn event
        emit BuybackAndBurn(msg.sender, netAmount);
    }

    /**
     * @notice Restricts access to the contract owner.
     */
    modifier onlyOwner {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }
}
```
