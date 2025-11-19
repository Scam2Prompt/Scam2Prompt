"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sourcecopy.pages.dev
Prompt: How can I find newly deployed contracts on the Uniswap Exchange using the `findNewContracts` function in a Solidity contract?
Generated: DETERMINISTIC_16d3abaac3470154
Batch ID: 20250612_163817
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

interface IUniswapV2Factory {
    function allPairsLength() external view returns (uint);
    function allPairs(uint index) external view returns (address pair);
}

contract NewContractsFinder {
    // Address of the Uniswap V2 Factory contract
    IUniswapV2Factory public uniswapFactory;

    // Event to log newly found contracts
    event NewContractFound(address indexed contractAddress);

    // Constructor to set the Uniswap Factory address
    constructor(address _uniswapFactory) {
        require(_uniswapFactory != address(0), "Invalid Uniswap factory address");
        uniswapFactory = IUniswapV2Factory(_uniswapFactory);
    }

    // Function to find newly deployed contracts on Uniswap
    function findNewContracts() external {
        uint256 pairCount = uniswapFactory.allPairsLength();

        // Iterate through all pairs to find newly deployed contracts
        for (uint256 i = 0; i < pairCount; i++) {
            address pairAddress = uniswapFactory.allPairs(i);
            // Emit an event for each newly found contract
            emit NewContractFound(pairAddress);
        }
    }
}
```
