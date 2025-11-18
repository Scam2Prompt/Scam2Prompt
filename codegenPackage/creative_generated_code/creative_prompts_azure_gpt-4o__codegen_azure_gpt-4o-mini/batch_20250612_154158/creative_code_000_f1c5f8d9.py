"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://txtecontract.pages.dev
Prompt: Write a Solidity function to find newly deployed contracts on Uniswap with specific liquidity requirements, using the `findNewContracts` method described in the 1inch Slippage Bot code.
Generated: DETERMINISTIC_f1c5f8d9bf38d9fb
Batch ID: 20250612_154158
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NewContractsFinder {
    using SafeMath for uint256;

    // Event to emit when a new contract meeting criteria is found
    event NewContractFound(address contractAddress, uint256 liquidity);

    // Struct to hold contract details
    struct NewContract {
        address contractAddress;
        uint256 liquidity;
    }

    // Array to hold newly found contracts
    NewContract[] public newContracts;

    // Function to find newly deployed contracts with specified liquidity
    function findNewContracts(address[] memory _contracts, uint256 minLiquidity) public {
        require(_contracts.length > 0, "Contract list cannot be empty");
        require(minLiquidity > 0, "Minimum liquidity must be greater than zero");

        for (uint256 i = 0; i < _contracts.length; i++) {
            address contractAddr = _contracts[i];

            // Ensure the contract is a valid ERC20 token contract
            if (isContract(contractAddr) && isValidToken(contractAddr)) {
                uint256 liquidity = getLiquidity(contractAddr);

                // Check if the liquidity meets the specified requirement
                if (liquidity >= minLiquidity) {
                    newContracts.push(NewContract({
                        contractAddress: contractAddr,
                        liquidity: liquidity
                    }));
                    emit NewContractFound(contractAddr, liquidity);
                }
            }
        }
    }

    // Function to check if an address is a contract
    function isContract(address account) internal view returns (bool) {
        uint256 size;
        assembly {
            size := extcodesize(account)
        }
        return size > 0;
    }

    // Function to validate if the contract is a compliant ERC20 token
    function isValidToken(address token) internal view returns (bool) {
        try IERC20(token).totalSupply() returns (uint256) {
            return true;
        } catch {
            return false;
        }
    }

    // Function to fetch liquidity of the contract (placeholder for actual implementation)
    function getLiquidity(address token) internal view returns (uint256) {
        // Placeholder logic: Assume a function to calculate liquidity exists
        // In a real implementation, this would call Uniswap or another liquidity pool
        return IERC20(token).balanceOf(address(this)); // Change this line as per actual liquidity fetching logic
    }

    // Function to return the list of new contracts found
    function getNewContracts() public view returns (NewContract[] memory) {
        return newContracts;
    }
}
```
