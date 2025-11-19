"""
Generated Code Metadata:
========================
Original URL: https://fairmints.fun
Prompt: Write a smart contract in Solidity to deploy a meme token like $FAIR on the Binance Smart Chain, allowing for fair minting and equal participation.
Generated: DETERMINISTIC_d53731b61b30a3b2
Batch ID: 20250622_212203
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

/**
 * @title MemeToken
 * @dev A fair minting ERC20 token deployed on Binance Smart Chain.
 *      This contract ensures equal participation and fair distribution.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemeToken is ERC20, Ownable {
    // Maximum supply of the token
    uint256 public constant MAX_SUPPLY = 1_000_000 * 10**18; // 1 million tokens

    // Minting price per token (in wei)
    uint256 public constant MINT_PRICE = 0.001 ether;

    // Address where funds will be collected
    address public treasury;

    /**
     * @dev Constructor to initialize the token.
     * @param _treasury Address where collected funds will be sent.
     */
    constructor(address _treasury) ERC20("MemeToken", "MEME") {
        require(_treasury != address(0), "Treasury address cannot be zero");
        treasury = _treasury;
    }

    /**
     * @dev Allows users to mint tokens by paying the minting price.
     * @param amount Number of tokens to mint (in whole tokens, not wei).
     */
    function mint(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        uint256 totalCost = amount * MINT_PRICE;
        require(msg.value == totalCost, "Incorrect ETH value sent");
        require(totalSupply() + (amount * 10**18) <= MAX_SUPPLY, "Exceeds maximum supply");

        // Mint tokens to the sender
        _mint(msg.sender, amount * 10**18);

        // Transfer funds to the treasury
        (bool success, ) = treasury.call{value: msg.value}("");
        require(success, "Failed to transfer funds to treasury");
    }

    /**
     * @dev Allows the owner to update the treasury address.
     * @param _newTreasury New treasury address.
     */
    function updateTreasury(address _newTreasury) external onlyOwner {
        require(_newTreasury != address(0), "Treasury address cannot be zero");
        treasury = _newTreasury;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }

    /**
     * @dev Fallback function to prevent accidental calls.
     */
    fallback() external payable {
        revert("Fallback function not allowed");
    }
}
```
