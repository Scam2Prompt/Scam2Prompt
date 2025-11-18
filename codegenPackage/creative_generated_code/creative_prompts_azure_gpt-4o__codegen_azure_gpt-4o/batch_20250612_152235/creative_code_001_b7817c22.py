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
pragma solidity ^0.8.7;

/**
 * @title TokenPresale
 * @dev Contract to calculate token allocation based on ETH contribution during presale.
 */
contract TokenPresale {
    // Constants
    uint256 public constant RATE = 99500; // Number of tokens per 0.1 ETH (99,500 tokens)
    uint256 public constant ETH_UNIT = 0.1 ether; // 0.1 ETH in wei

    /**
     * @dev Calculates the number of tokens a user receives based on their ETH contribution.
     * @param ethAmount The amount of ETH contributed in wei.
     * @return tokens The number of tokens allocated to the user.
     */
    function calculateTokens(uint256 ethAmount) public pure returns (uint256 tokens) {
        require(ethAmount > 0, "ETH contribution must be greater than zero");

        // Calculate number of tokens based on the rate
        // (ethAmount / ETH_UNIT) * RATE
        tokens = (ethAmount * RATE) / ETH_UNIT;
    }
}
```
