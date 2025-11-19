"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecoin-1sa.pages.dev
Prompt: Generate a code snippet for a smart contract that manages a token presale with a cap of 1000 BASE and a total supply of 100,000,000 JESSE.
Generated: DETERMINISTIC_4eab0013497f2a31
Batch ID: 20250612_162203
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title JesseTokenPresale
 * @dev A smart contract for managing a token presale for JESSE tokens
 */
contract JesseTokenPresale is Ownable {
    ERC20 public jesseToken; // The JESSE token contract
    uint256 public constant PRESALE_CAP = 1000 * 10 ** 18; // Presale cap in BASE (adjust for decimals)
    uint256 public totalRaised; // Total amount raised in the presale
    mapping(address => uint256) public contributions; // Track contributions by address
    bool public presaleActive; // Status of the presale

    event ContributionReceived(address indexed contributor, uint256 amount);
    event PresaleStatusChanged(bool active);
    
    constructor(address _jesseTokenAddress) {
        jesseToken = ERC20(_jesseTokenAddress);
        presaleActive = false;
    }

    /**
     * @dev Start or stop the presale
     * @param _active - bool to indicate if presale should be active
     */
    function setPresaleStatus(bool _active) external onlyOwner {
        presaleActive = _active;
        emit PresaleStatusChanged(_active);
    }

    /**
     * @dev Contribute to the token presale
     * @param amount - amount of BASE to contribute
     */
    function contribute(uint256 amount) external {
        require(presaleActive, "Presale is not active");
        require(amount > 0, "Contribution must be greater than zero");
        require(totalRaised + amount <= PRESALE_CAP, "Presale cap reached");

        // Update state
        contributions[msg.sender] += amount;
        totalRaised += amount;

        // Emit event
        emit ContributionReceived(msg.sender, amount);
    }

    /**
     * @dev Withdraw collected funds by the owner
     */
    function withdrawFunds() external onlyOwner {
        // Transfer the contract's balance to the owner
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Allow the owner to finalize the presale and distribute tokens
     * @param recipient - address receiving JESSE tokens
     */
    function finalizeSale(address recipient) external onlyOwner {
        require(totalRaised > 0, "No funds raised");
        uint256 tokenAmount = totalRaised; // Define conversion rate as 1:1 for simplicity

        // Ensure the contract has enough tokens
        require(jesseToken.balanceOf(address(this)) >= tokenAmount, "Insufficient tokens in contract");

        // Transfer tokens to the recipient
        jesseToken.transfer(recipient, tokenAmount);
        totalRaised = 0; // Reset total raised after finalization
    }

    /**
     * @dev Fallback function to accept ETH contributions
     */
    receive() external payable {
        contribute(msg.value);
    }
}
```
