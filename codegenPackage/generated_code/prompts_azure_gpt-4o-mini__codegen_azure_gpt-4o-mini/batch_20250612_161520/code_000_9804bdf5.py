"""
Generated Code Metadata:
========================
Original URL: https://jessecom.pages.dev
Prompt: Generate a code snippet for a smart contract that manages a presale with a cap of 1000 BASE for the $JESSE token.
Generated: DETERMINISTIC_9804bdf54911001c
Batch ID: 20250612_161520
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title JesseTokenPresale
 * @dev A smart contract for managing a presale of the $JESSE token with a cap.
 */
contract JesseTokenPresale is Ownable {
    // The token being sold
    IERC20 public jesseToken;

    // Presale cap in BASE (1000 BASE)
    uint256 public constant PRESALE_CAP = 1000 * 10**18; // Assuming BASE has 18 decimals

    // Total amount raised in the presale
    uint256 public totalRaised;

    // Mapping to track contributions of each address
    mapping(address => uint256) public contributions;

    // Event to log contributions
    event Contribution(address indexed contributor, uint256 amount);

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _jesseToken Address of the $JESSE token contract.
     */
    constructor(IERC20 _jesseToken) {
        jesseToken = _jesseToken;
    }

    /**
     * @dev Function to contribute to the presale.
     * @param amount Amount of BASE to contribute.
     */
    function contribute(uint256 amount) external {
        require(amount > 0, "Contribution must be greater than 0");
        require(totalRaised + amount <= PRESALE_CAP, "Presale cap reached");

        // Update total raised and contributions
        totalRaised += amount;
        contributions[msg.sender] += amount;

        // Emit contribution event
        emit Contribution(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw funds from the presale.
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Function to finalize the presale.
     * Only the owner can call this function.
     */
    function finalizePresale() external onlyOwner {
        require(totalRaised >= PRESALE_CAP, "Presale cap not reached");

        // Transfer remaining tokens to the owner
        uint256 remainingTokens = jesseToken.balanceOf(address(this));
        require(remainingTokens > 0, "No tokens to transfer");

        jesseToken.transfer(owner(), remainingTokens);
    }

    /**
     * @dev Fallback function to accept ETH contributions.
     */
    receive() external payable {
        contribute(msg.value);
    }
}
```
