"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: Generate a code snippet for a smart contract that manages a presale with a cap of 1000 BASE for the $JESSE token.
Generated: DETERMINISTIC_9804bdf54911001c
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Presale Contract for $JESSE Token
 * @dev This contract manages a presale for the $JESSE token with a cap.
 */
contract JessePresale is Ownable {
    IERC20 public jesseToken; // The $JESSE token contract
    uint256 public constant PRESALE_CAP = 1000 * 10**18; // Presale cap in token units
    uint256 public totalRaised; // Total amount raised in the presale
    mapping(address => uint256) public contributions; // Contributions by address

    event Purchase(address indexed purchaser, uint256 amount);
    event Withdrawal(address indexed owner, uint256 amount);

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _jesseToken The address of the $JESSE token contract.
     */
    constructor(IERC20 _jesseToken) {
        require(address(_jesseToken) != address(0), "Invalid token address");
        jesseToken = _jesseToken;
    }

    /**
     * @dev Purchases tokens during the presale.
     * @param amount The amount of $JESSE tokens to purchase.
     */
    function purchase(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(totalRaised + amount <= PRESALE_CAP, "Presale cap exceeded");

        // Update total raised and individual contribution
        totalRaised += amount;
        contributions[msg.sender] += amount;

        // Transfer the tokens from the contract
        jesseToken.transfer(msg.sender, amount);

        emit Purchase(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw funds from the contract.
     * @param amount The amount of funds to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");

        // Transfer Ether to the owner
        payable(owner()).transfer(amount);
        emit Withdrawal(owner(), amount);
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to check the presale status.
     * @return totalTokensSold The total amount of tokens sold.
     * @return presaleCap The presale cap.
     */
    function presaleStatus() external view returns (uint256 totalTokensSold, uint256 presaleCap) {
        return (totalRaised, PRESALE_CAP);
    }
}
```
