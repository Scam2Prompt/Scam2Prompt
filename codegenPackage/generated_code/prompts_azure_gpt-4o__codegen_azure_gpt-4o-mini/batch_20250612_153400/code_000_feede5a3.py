"""
Generated Code Metadata:
========================
Original URL: https://presale-jessecoinorg.pages.dev
Prompt: Write a smart contract in Solidity for a cryptocurrency presale with a cap of 1000 BASE and an exchange rate of 0.1 BASE for 99,500 JESSE tokens.
Generated: DETERMINISTIC_feede5a3b79f16d7
Batch ID: 20250612_153400
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

// Importing the ERC20 interface for the JESSE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PresaleContract
 * @dev A smart contract for conducting a cryptocurrency presale
 */
contract PresaleContract is Ownable {
    // State variables
    IERC20 public jesseToken; // The JESSE token contract
    uint256 public constant CAP = 1000 * 10**18; // Presale cap in BASE (adjusted for decimals)
    uint256 public constant EXCHANGE_RATE = 99500; // Number of JESSE tokens per 0.1 BASE
    uint256 public totalRaised; // Total amount raised in BASE
    mapping(address => uint256) public contributions; // Track contributions by address

    // Events
    event TokensPurchased(address indexed buyer, uint256 amountInBase, uint256 amountInJesse);
    event PresaleFinalized(uint256 totalRaised);

    // Modifier to check if the presale cap is reached
    modifier capNotReached(uint256 amount) {
        require(totalRaised + amount <= CAP, "Presale cap reached");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract
     * @param _jesseToken Address of the JESSE token contract
     */
    constructor(IERC20 _jesseToken) {
        jesseToken = _jesseToken;
    }

    /**
     * @dev Function to purchase JESSE tokens with BASE
     * @param amountInBase Amount of BASE to spend
     */
    function buyTokens(uint256 amountInBase) external capNotReached(amountInBase) {
        require(amountInBase > 0, "Amount must be greater than 0");
        
        // Calculate the amount of JESSE tokens to be purchased
        uint256 amountInJesse = (amountInBase * EXCHANGE_RATE) / 1e18; // Adjust for BASE decimals

        // Update state
        totalRaised += amountInBase;
        contributions[msg.sender] += amountInBase;

        // Transfer JESSE tokens to the buyer
        require(jesseToken.transfer(msg.sender, amountInJesse), "Token transfer failed");

        emit TokensPurchased(msg.sender, amountInBase, amountInJesse);
    }

    /**
     * @dev Function to finalize the presale and withdraw funds
     */
    function finalizePresale() external onlyOwner {
        require(totalRaised > 0, "No funds to withdraw");
        
        // Transfer the total raised BASE to the owner
        payable(owner()).transfer(totalRaised);
        
        emit PresaleFinalized(totalRaised);
    }

    /**
     * @dev Fallback function to accept BASE payments
     */
    receive() external payable {
        buyTokens(msg.value);
    }

    /**
     * @dev Function to withdraw any ERC20 tokens accidentally sent to the contract
     * @param token Address of the ERC20 token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != jesseToken, "Cannot withdraw JESSE tokens");
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");
        
        require(token.transfer(owner(), amount), "Token transfer failed");
    }
}
```
