"""
Generated Code Metadata:
========================
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Create a function in Solidity that calculates the number of tokens a user receives based on their ETH contribution, using the rate of 0.1 ETH = 99,500 tokens as described in the presale.
Generated: DETERMINISTIC_b7817c223e278e04
Batch ID: 20250612_152235
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

contract TokenSale {
    // Rate of token allocation per ETH contribution
    uint256 public constant RATE = 99500; // 0.1 ETH = 99,500 tokens
    uint256 public constant ETH_CONVERSION = 0.1 ether; // 0.1 ETH in wei

    // Event to log token purchase
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 ethAmount);

    // Function to calculate the number of tokens based on ETH contribution
    // @param ethAmount: The amount of ETH contributed by the user
    // @return uint256: The number of tokens the user will receive
    function calculateTokens(uint256 ethAmount) public pure returns (uint256) {
        // Ensure the ETH amount is valid and greater than zero
        require(ethAmount > 0, "ETH amount must be greater than zero");
        
        // Ensure the ETH amount is a multiple of 0.1 ETH
        require(ethAmount % ETH_CONVERSION == 0, "ETH amount must be a multiple of 0.1 ETH");

        // Calculate the number of tokens based on the contribution
        uint256 tokens = (ethAmount * RATE) / ETH_CONVERSION;

        return tokens;
    }

    // Function to purchase tokens
    // @param ethAmount: The amount of ETH the user wants to contribute
    function buyTokens(uint256 ethAmount) external payable {
        // Check if the sent value matches the ethAmount
        require(msg.value == ethAmount, "Incorrect ETH amount sent");

        // Calculate the number of tokens to be issued
        uint256 tokens = calculateTokens(ethAmount);

        // Emit an event for the token purchase
        emit TokensPurchased(msg.sender, tokens, ethAmount);
        
        // Additional logic to handle token distribution would go here
        // For example, transferring tokens to the buyer's address
    }
}
```
