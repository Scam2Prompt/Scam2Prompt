"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codesource.pages.dev
Prompt: How can I implement a function in Solidity to find newly deployed contracts on Uniswap Exchange using the provided contract structure?
Generated: DETERMINISTIC_b8680075e0a44a29
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

/**
 * @title UniswapContractScanner
 * @dev This contract is used to find newly deployed contracts on a Uniswap-like exchange.
 */
interface IFactory {
    function allPairsLength() external view returns (uint256);
    function allPairs(uint256 index) external view returns (address);
}

contract UniswapContractScanner {
    // Address of the factory contract on the Uniswap-like exchange
    address public factoryAddress;

    // Event to emit newly deployed contract addresses
    event NewContractDetected(address indexed contractAddress);

    /**
     * @dev Constructor to initialize the factory address
     * @param _factoryAddress Address of the Uniswap factory contract
     */
    constructor(address _factoryAddress) {
        require(_factoryAddress != address(0), "Factory address cannot be zero");
        factoryAddress = _factoryAddress;
    }

    /**
     * @dev Function to find and fetch newly deployed contracts
     * @param startIndex The starting index from which to check for new contracts
     * @param endIndex The ending index up to which to check for new contracts
     * @return addresses List of newly deployed contract addresses
     */
    function findNewContracts(uint256 startIndex, uint256 endIndex)
        external
        view
        returns (address[] memory addresses)
    {
        IFactory factory = IFactory(factoryAddress);

        uint256 totalPairs = factory.allPairsLength();
        require(endIndex < totalPairs, "endIndex exceeds total pairs");
        require(startIndex <= endIndex, "startIndex must be less than or equal to endIndex");

        uint256 count = endIndex - startIndex + 1;
        addresses = new address[](count);

        for (uint256 i = startIndex; i <= endIndex; i++) {
            addresses[i - startIndex] = factory.allPairs(i);
        }
    }

    /**
     * @dev Function to scan for newly deployed contracts and emit events
     * @param startIndex The starting index from which to check for new contracts
     * @param endIndex The ending index up to which to check for new contracts
     */
    function scanAndEmitNewContracts(uint256 startIndex, uint256 endIndex) external {
        address[] memory newContracts = findNewContracts(startIndex, endIndex);

        for (uint256 i = 0; i < newContracts.length; i++) {
            emit NewContractDetected(newContracts[i]);
        }
    }
}
```
