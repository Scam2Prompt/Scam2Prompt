"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-de.web.app
Prompt: Generate a code snippet for a smart contract that facilitates the buying and selling of $MGLS tokens on the Ethereum network.
Generated: DETERMINISTIC_68fdfc796f82884a
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

// Importing OpenZeppelin's ERC20 implementation for secure token management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MGLSToken
 * @dev ERC20 Token with buying and selling functionality
 */
contract MGLSToken is ERC20, Ownable {
    // Event to log token purchases
    event TokensPurchased(address indexed buyer, uint256 amount);
    
    // Event to log token sales
    event TokensSold(address indexed seller, uint256 amount);

    // Price of one MGLS token in wei
    uint256 public tokenPrice;

    /**
     * @dev Constructor to initialize the token with a name, symbol, and initial supply.
     * Sets the token price to a defined value.
     * @param initialSupply The initial supply of tokens.
     * @param _tokenPrice The price of a token in wei.
     */
    constructor(uint256 initialSupply, uint256 _tokenPrice) ERC20("MGLS Token", "MGLS") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        tokenPrice = _tokenPrice;
    }

    /**
     * @dev Function for users to buy tokens.
     * Accepts ETH and mints tokens to the buyer's address.
     */
    function buyTokens(uint256 numberOfTokens) external payable {
        // Calculate the cost of the tokens in wei
        uint256 cost = numberOfTokens * tokenPrice;

        // Ensure the buyer has sent enough ETH
        require(msg.value >= cost, "Insufficient ETH sent.");

        // Ensure the contract has enough tokens available for purchase
        require(balanceOf(owner()) >= numberOfTokens, "Not enough tokens available.");

        // Transfer tokens to the buyer
        _transfer(owner(), msg.sender, numberOfTokens);

        // Emit an event to log the purchase
        emit TokensPurchased(msg.sender, numberOfTokens);

        // Refund excess ETH, if any
        uint256 refund = msg.value - cost;
        if (refund > 0) {
            payable(msg.sender).transfer(refund);
        }
    }

    /**
     * @dev Function for users to sell tokens back to the contract.
     * The contract buys tokens from the seller and transfers ETH.
     */
    function sellTokens(uint256 numberOfTokens) external {
        // Ensure the seller has enough tokens to sell
        require(balanceOf(msg.sender) >= numberOfTokens, "Insufficient tokens to sell.");

        // Calculate the amount of ETH to send back to the seller
        uint256 etherAmount = numberOfTokens * tokenPrice;

        // Check if the contract has enough ETH to buy the tokens
        require(address(this).balance >= etherAmount, "Not enough ETH in contract.");

        // Transfer tokens from the seller to the contract
        _transfer(msg.sender, owner(), numberOfTokens);

        // Transfer ETH to the seller
        payable(msg.sender).transfer(etherAmount);

        // Emit an event to log the sale
        emit TokensSold(msg.sender, numberOfTokens);
    }

    /**
     * @dev Function to withdraw contract's accumulated ETH.
     * Only the owner can call this function.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;

        // Ensure there is ETH to withdraw
        require(balance > 0, "No ETH to withdraw.");

        // Transfer the ETH to the owner's address
        payable(owner()).transfer(balance);
    }
}
```
