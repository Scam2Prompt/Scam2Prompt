"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Create a function in Solidity that calculates the number of tokens a user receives based on their ETH contribution, using the rate of 0.1 ETH = 99,500 tokens as described in the presale.
Generated: DETERMINISTIC_b7817c223e278e04
Batch ID: 20250612_152235
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

contract TokenSale {
    // Define constants for the token rate
    uint256 public constant ETH_TO_TOKENS_RATE = 99500; // Tokens per 0.1 ETH
    uint256 public constant ETH_CONTRIBUTION_UNIT = 0.1 ether; // 0.1 ETH unit

    // Event to log token allocation
    event TokensAllocated(address indexed user, uint256 tokensAmount);

    /**
     * @dev Calculate the number of tokens a user will receive based on their ETH contribution.
     * @param ethAmount The amount of ETH contributed by the user.
     * @return The number of tokens the user will receive.
     */
    function calculateTokens(uint256 ethAmount) external pure returns (uint256) {
        // Ensure the ETH amount is a multiple of the contribution unit
        require(ethAmount % ETH_CONTRIBUTION_UNIT == 0, "ETH amount must be a multiple of 0.1 ETH");

        // Calculate the number of tokens to be issued
        uint256 tokensAmount = (ethAmount / ETH_CONTRIBUTION_UNIT) * ETH_TO_TOKENS_RATE;
        return tokensAmount;
    }

    /**
     * @dev Allocate tokens to a user based on their ETH contribution.
     * @param ethAmount The amount of ETH contributed by the user.
     */
    function allocateTokens(uint256 ethAmount) external payable {
        // Ensure the correct amount of ETH is sent
        require(msg.value == ethAmount, "Incorrect ETH amount sent");

        // Calculate the number of tokens
        uint256 tokensAmount = calculateTokens(ethAmount);

        // Emit an event to log the token allocation
        emit TokensAllocated(msg.sender, tokensAmount);
    }

    // Fallback function to prevent sending ETH directly to the contract
    receive() external payable {
        revert("Direct ETH transfers are not allowed, please use the allocateTokens function.");
    }
}
```
