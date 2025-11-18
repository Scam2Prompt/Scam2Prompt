"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dresale.pages.dev
Prompt: Write a smart contract in Solidity to manage the presale of a token named "DRE," ensuring a presale cap of 3,000,000 FTM and calculating token distribution based on the rate of 250 FTM = 99,500 DRE.
Generated: DETERMINISTIC_4963a4837fdeeb1c
Batch ID: 20250612_153401
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
 * @title DREPresale
 * @dev Smart contract for managing the presale of the DRE token
 */
contract DREPresale is Ownable {
    // The token being sold
    IERC20 public dreToken;

    // Presale parameters
    uint256 public constant PRESALE_CAP = 3000000 ether; // Presale cap in FTM
    uint256 public constant TOKEN_RATE = 99500 * 10 ** 18 / 250; // Token distribution rate (DRE per FTM)
    uint256 public totalRaised; // Total amount raised in FTM
    bool public presaleActive; // Status of presale

    // Events
    event TokensPurchased(address indexed purchaser, uint256 amountSpent, uint256 tokensPurchased);
    event PresaleStarted();
    event PresaleEnded();

    // Modifier to check if presale is active
    modifier whenPresaleActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract with the DRE token address
     * @param _dreToken Address of the DRE token contract
     */
    constructor(address _dreToken) {
        require(_dreToken != address(0), "Invalid token address");
        dreToken = IERC20(_dreToken);
    }

    /**
     * @dev Start the presale
     */
    function startPresale() external onlyOwner {
        require(!presaleActive, "Presale already active");
        presaleActive = true;
        emit PresaleStarted();
    }

    /**
     * @dev End the presale
     */
    function endPresale() external onlyOwner whenPresaleActive {
        presaleActive = false;
        emit PresaleEnded();
    }

    /**
     * @dev Purchase tokens during the presale
     * @param _amount Amount of FTM to spend
     */
    function buyTokens() external payable whenPresaleActive {
        require(msg.value > 0, "Must send FTM to purchase tokens");
        require(totalRaised + msg.value <= PRESALE_CAP, "Presale cap exceeded");

        // Calculate the number of tokens to be purchased
        uint256 tokensToPurchase = msg.value * TOKEN_RATE;

        // Update the total amount raised
        totalRaised += msg.value;

        // Transfer tokens to the purchaser
        require(dreToken.balanceOf(address(this)) >= tokensToPurchase, "Not enough tokens available");
        dreToken.transfer(msg.sender, tokensToPurchase);

        emit TokensPurchased(msg.sender, msg.value, tokensToPurchase);
    }

    /**
     * @dev Withdraw the FTM raised from the presale
     * Can only be called by the owner
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Allows the contract to receive FTM
     */
    receive() external payable {
        buyTokens();
    }
}
```
