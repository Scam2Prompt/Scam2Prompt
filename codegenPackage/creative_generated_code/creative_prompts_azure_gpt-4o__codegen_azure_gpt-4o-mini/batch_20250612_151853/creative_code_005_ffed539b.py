"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-worldlibertfinancialcom.pages.dev
Prompt: Create a smart contract function to distribute tokens during a presale event, referencing the $WLFI Token Presale process where $10,000,000 $WLFI tokens are distributed.
Generated: DETERMINISTIC_ffed539b57f484ff
Batch ID: 20250612_151853
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title WLFI Presale Contract
 * @dev This contract manages the presale distribution of $WLFI tokens.
 */
contract WLFiPresale is Ownable {
    // Total amount of tokens to be distributed
    uint256 public constant TOTAL_TOKENS = 10_000_000 * 10**18; // $WLFI has 18 decimals
    // Address of the $WLFI token
    IERC20 public wlfiToken;
    // Total tokens sold in the presale
    uint256 public tokensSold;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed buyer, uint256 amount);

    /**
     * @dev Constructor to set the token address
     * @param _wlfiToken Address of the $WLFI token contract
     */
    constructor(IERC20 _wlfiToken) {
        wlfiToken = _wlfiToken;
    }

    /**
     * @dev Function to buy tokens during the presale
     * @param amount Amount of tokens to purchase
     */
    function buyTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than 0");
        require(tokensSold + amount <= TOTAL_TOKENS, "Exceeds total supply");
        require(msg.value >= calculateCost(amount), "Insufficient funds sent");

        // Update the total tokens sold
        tokensSold += amount;

        // Transfer tokens to the buyer
        require(wlfiToken.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensDistributed(msg.sender, amount);
    }

    /**
     * @dev Function to calculate the cost of tokens based on presale pricing
     * @param amount Amount of tokens to calculate cost for
     * @return uint256 Cost in wei
     */
    function calculateCost(uint256 amount) public pure returns (uint256) {
        // Assuming 1 $WLFI token is priced at 1 USD (for simplicity)
        return amount * 1 ether; // Using 1 ether to represent 1 USD
    }

    /**
     * @dev Function to withdraw funds from the contract
     * Only callable by the contract owner
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Function to withdraw unsold tokens after the presale
     * Only callable by the contract owner
     */
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = TOTAL_TOKENS - tokensSold;
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        // Transfer remaining unsold tokens back to the owner
        require(wlfiToken.transfer(owner(), unsoldTokens), "Token transfer failed");
    }

    /**
     * @dev Fallback function to accept ether payments
     */
    receive() external payable {}
}
```
