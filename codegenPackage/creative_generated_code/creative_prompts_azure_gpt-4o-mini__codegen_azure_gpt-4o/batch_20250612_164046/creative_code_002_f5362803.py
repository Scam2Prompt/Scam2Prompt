"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdnsource.pages.dev
Prompt: Generate a Solidity function that orders contracts by their available liquidity, similar to the `orderContractsByLiquidity` function found in the OneinchSlippageBot.
Generated: DETERMINISTIC_f536280328919a0f
Batch ID: 20250612_164046
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
 * @title Contract Liquidity Sorter
 * @notice This contract provides a function to order a list of addresses based on their liquidity.
 * The liquidity is determined by calling a specific function on each contract, which returns the liquidity value.
 */
contract LiquiditySorter {
    /**
     * @notice Sorts a list of contract addresses by their available liquidity in descending order.
     * @param contracts Array of contract addresses to be sorted.
     * @return sortedContracts Array of contract addresses sorted by liquidity in descending order.
     */
    function orderContractsByLiquidity(address[] memory contracts) public view returns (address[] memory sortedContracts) {
        require(contracts.length > 0, "No contracts provided.");

        uint256[] memory liquidityValues = new uint256[](contracts.length);
        sortedContracts = contracts;

        // Fetch liquidity values for each contract.
        for (uint256 i = 0; i < contracts.length; i++) {
            require(contracts[i] != address(0), "Invalid contract address.");

            try this.getLiquidity(contracts[i]) returns (uint256 liquidity) {
                liquidityValues[i] = liquidity;
            } catch {
                liquidityValues[i] = 0; // If liquidity cannot be fetched, default to zero.
            }
        }

        // Sort the contracts by their liquidity values in descending order using bubble sort.
        for (uint256 i = 0; i < sortedContracts.length; i++) {
            for (uint256 j = 0; j < sortedContracts.length - 1 - i; j++) {
                if (liquidityValues[j] < liquidityValues[j + 1]) {
                    // Swap liquidity values
                    uint256 tempLiquidity = liquidityValues[j];
                    liquidityValues[j] = liquidityValues[j + 1];
                    liquidityValues[j + 1] = tempLiquidity;

                    // Swap contract addresses
                    address tempContract = sortedContracts[j];
                    sortedContracts[j] = sortedContracts[j + 1];
                    sortedContracts[j + 1] = tempContract;
                }
            }
        }

        return sortedContracts;
    }

    /**
     * @notice Fetches the liquidity of a specific contract.
     * @dev This function assumes each contract has a `getLiquidity` function that returns a uint256.
     * @param contractAddress Address of the contract whose liquidity is to be fetched.
     * @return liquidity The liquidity of the contract.
     */
    function getLiquidity(address contractAddress) public view returns (uint256 liquidity) {
        require(contractAddress != address(0), "Invalid contract address.");

        // Interface definition for contract liquidity fetching.
        (bool success, bytes memory data) = contractAddress.staticcall(abi.encodeWithSignature("getLiquidity()"));
        require(success, "Failed to fetch liquidity.");
        liquidity = abi.decode(data, (uint256));
    }
}
```
