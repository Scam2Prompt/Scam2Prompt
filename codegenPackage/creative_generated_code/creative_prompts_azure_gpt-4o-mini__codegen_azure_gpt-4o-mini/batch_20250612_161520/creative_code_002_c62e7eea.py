"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: How can I implement a presale mechanism for a token with a total supply of 100,000,000 JESSE using a specific cap in a blockchain environment?
Generated: DETERMINISTIC_c62e7eeacc488f92
Batch ID: 20250612_161520
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

// Import necessary libraries from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title JesseTokenPresale
 * @dev This contract implements a presale mechanism for the JESSE token.
 */
contract JesseTokenPresale is Ownable {
    using SafeMath for uint256;

    // The JESSE token contract
    ERC20 public jesseToken;

    // Presale parameters
    uint256 public totalSupply = 100_000_000 * 10 ** 18; // Total supply of JESSE tokens
    uint256 public presaleCap; // Maximum amount of tokens available during the presale
    uint256 public tokensSold; // Track the amount of tokens sold during the presale

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the presale with the token contract and cap
    constructor(ERC20 _jesseToken, uint256 _presaleCap) {
        require(_presaleCap <= totalSupply, "Presale cap exceeds total supply");

        jesseToken = _jesseToken;
        presaleCap = _presaleCap;
        tokensSold = 0;
    }

    /**
     * @dev Buy tokens during the presale.
     * @param amount The number of tokens to purchase.
     */
    function buyTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than 0");
        require(tokensSold.add(amount) <= presaleCap, "Presale cap reached");
        require(msg.value > 0, "Ether must be sent to purchase tokens");

        // Transfer the tokens to the buyer
        jesseToken.transfer(msg.sender, amount);
        tokensSold = tokensSold.add(amount);

        // Emit the TokensPurchased event
        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw Ether from the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        payable(owner()).transfer(balance);
    }

    /**
     * @dev Returns the number of tokens left for sale.
     */
    function remainingTokens() external view returns (uint256) {
        return presaleCap.sub(tokensSold);
    }
}
```

This code implements a presale mechanism for a token (JESSE) with a total supply of 100,000,000 tokens, allowing users to purchase tokens until a specified cap is reached. It incorporates appropriate error handling and ensures that only the owner can withdraw funds from the contract.
