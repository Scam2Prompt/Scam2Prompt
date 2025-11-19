"""
Generated Code Metadata:
========================
Original URL: https://dogeversehub.pages.dev
Prompt: Analyze the security measures implemented in the Dogeverse presale smart contract, and suggest additional security features to protect users' funds.
Generated: DETERMINISTIC_652419f0a4f71fab
Batch ID: 20250622_205836
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title DogeversePresale
 * @dev A smart contract for managing a presale of Dogeverse tokens.
 * This contract includes security measures to protect users' funds.
 */
contract DogeversePresale is Ownable, ReentrancyGuard {
    // State variables
    IERC20 public token; // The token being sold
    uint256 public presaleEndTime; // End time of the presale
    uint256 public tokenPrice; // Price of one token in wei
    mapping(address => uint256) public contributions; // User contributions

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();

    // Modifiers
    modifier onlyBeforePresaleEnd() {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        _;
    }

    modifier onlyAfterPresaleEnd() {
        require(block.timestamp >= presaleEndTime, "Presale is still ongoing");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token The address of the token being sold.
     * @param _presaleDuration Duration of the presale in seconds.
     * @param _tokenPrice Price of the token in wei.
     */
    constructor(IERC20 _token, uint256 _presaleDuration, uint256 _tokenPrice) {
        token = _token;
        presaleEndTime = block.timestamp + _presaleDuration;
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param amount The amount of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable onlyBeforePresaleEnd nonReentrant {
        require(msg.value == amount * tokenPrice, "Incorrect Ether value sent");
        require(amount > 0, "Amount must be greater than zero");

        contributions[msg.sender] += amount;

        emit TokensPurchased(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw funds after the presale ends.
     * Only callable by the owner of the contract.
     */
    function withdrawFunds() external onlyOwner onlyAfterPresaleEnd {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Function to end the presale and transfer remaining tokens to the owner.
     * Only callable by the owner of the contract.
     */
    function endPresale() external onlyOwner onlyAfterPresaleEnd {
        uint256 remainingTokens = token.balanceOf(address(this));
        require(remainingTokens > 0, "No tokens to withdraw");
        token.transfer(owner(), remainingTokens);
        emit PresaleEnded();
    }

    /**
     * @dev Function to allow the owner to withdraw tokens mistakenly sent to the contract.
     * @param _token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 _token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        _token.transfer(owner(), amount);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to the contract.
     */
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
