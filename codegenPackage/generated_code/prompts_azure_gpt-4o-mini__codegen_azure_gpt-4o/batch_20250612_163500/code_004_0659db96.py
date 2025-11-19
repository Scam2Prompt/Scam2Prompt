"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-is.pages.dev
Prompt: Provide an example of a Solidity contract that could be used to manage the presale and token distribution for WienerAI, incorporating the tokenomics outlined in the whitepaper.
Generated: DETERMINISTIC_0659db960ea42f00
Batch ID: 20250612_163500
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
 * @title WienerAI Presale and Token Distribution Contract
 * @dev This contract manages the presale and token distribution for WienerAI.
 * Tokenomics:
 * - Total supply: 1,000,000 tokens
 * - Presale allocation: 40% (400,000 tokens)
 * - Team allocation: 20% (200,000 tokens)
 * - Marketing allocation: 20% (200,000 tokens)
 * - Reserve allocation: 20% (200,000 tokens)
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract WienerAIToken is ERC20, Ownable {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18;

    // Token allocations
    uint256 public constant PRESALE_ALLOCATION = 400_000 * 10**18;
    uint256 public constant TEAM_ALLOCATION = 200_000 * 10**18;
    uint256 public constant MARKETING_ALLOCATION = 200_000 * 10**18;
    uint256 public constant RESERVE_ALLOCATION = 200_000 * 10**18;

    // Presale parameters
    uint256 public presalePrice = 0.01 ether; // Price per token in presale
    uint256 public presaleTokensSold;
    bool public presaleActive;

    // Events
    event PresaleStarted();
    event PresaleEnded();
    event TokensPurchased(address indexed buyer, uint256 amount);

    constructor() ERC20("WienerAI Token", "WAI") {
        // Mint total supply to the contract owner
        _mint(msg.sender, TOTAL_SUPPLY);

        // Allocate tokens to different categories
        _transfer(msg.sender, address(this), PRESALE_ALLOCATION); // Presale tokens
        _transfer(msg.sender, msg.sender, TEAM_ALLOCATION); // Team tokens
        _transfer(msg.sender, msg.sender, MARKETING_ALLOCATION); // Marketing tokens
        _transfer(msg.sender, msg.sender, RESERVE_ALLOCATION); // Reserve tokens
    }

    /**
     * @dev Start the presale.
     * Only the owner can start the presale.
     */
    function startPresale() external onlyOwner {
        require(!presaleActive, "Presale is already active");
        presaleActive = true;
        emit PresaleStarted();
    }

    /**
     * @dev End the presale.
     * Only the owner can end the presale.
     */
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is not active");
        presaleActive = false;
        emit PresaleEnded();
    }

    /**
     * @dev Purchase tokens during the presale.
     * Users can send Ether to purchase tokens at the presale price.
     */
    function purchaseTokens() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "Ether sent must be greater than zero");

        uint256 tokensToPurchase = (msg.value * 10**18) / presalePrice;
        require(tokensToPurchase > 0, "Insufficient Ether to purchase tokens");
        require(
            presaleTokensSold + tokensToPurchase <= PRESALE_ALLOCATION,
            "Not enough presale tokens remaining"
        );

        presaleTokensSold += tokensToPurchase;
        _transfer(address(this), msg.sender, tokensToPurchase);

        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @dev Withdraw Ether collected during the presale.
     * Only the owner can withdraw the funds.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("Use purchaseTokens() to buy tokens");
    }
}
```
