"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesrc.pages.dev
Prompt: Generate a function in Solidity that finds new contracts on the Uniswap exchange, similar to the `findNewContracts` function in the OneinchSlippageBot example.
Generated: DETERMINISTIC_fd444413fe120eee
Batch ID: 20250612_163829
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

/**
 * @title UniswapNewContractsScanner
 * @dev This contract contains a function to scan for new contracts on the Uniswap Exchange.
 */
contract UniswapNewContractsScanner {
    // Address of the Uniswap Factory contract
    address public uniswapFactory;

    // Event emitted when a new contract is found
    event NewContractFound(address indexed newContract);

    /**
     * @dev Constructor to set the Uniswap Factory contract address.
     * @param _uniswapFactory The address of the Uniswap Factory contract.
     */
    constructor(address _uniswapFactory) {
        require(_uniswapFactory != address(0), "Invalid Uniswap Factory address");
        uniswapFactory = _uniswapFactory;
    }

    /**
     * @dev Function to find new contracts created on the Uniswap Exchange.
     * It queries the Uniswap Factory contract for all pairs and checks for new additions.
     * @param startIndex The starting index to scan from (useful for batching).
     * @param endIndex The ending index to scan to (useful for batching).
     * @return newContracts An array of addresses of newly found contracts.
     */
    function findNewContracts(uint256 startIndex, uint256 endIndex) external view returns (address[] memory newContracts) {
        require(startIndex < endIndex, "Invalid index range");
        
        uint256 pairCount = IUniswapFactory(uniswapFactory).allPairsLength();
        require(endIndex <= pairCount, "End index exceeds pair count");

        uint256 newContractsCount = 0;
        address[] memory tempContracts = new address[](endIndex - startIndex);

        for (uint256 i = startIndex; i < endIndex; i++) {
            address pairAddress = IUniswapFactory(uniswapFactory).allPairs(i);
            tempContracts[newContractsCount] = pairAddress;
            newContractsCount++;
        }

        // Resize the array to the actual number of new contracts found
        address[] memory resizedContracts = new address[](newContractsCount);
        for (uint256 j = 0; j < newContractsCount; j++) {
            resizedContracts[j] = tempContracts[j];
            emit NewContractFound(resizedContracts[j]);
        }

        return resizedContracts;
    }
}

/**
 * @dev Interface for the Uniswap Factory contract.
 */
interface IUniswapFactory {
    function allPairsLength() external view returns (uint256);
    function allPairs(uint256 index) external view returns (address);
}
```
