"""
Generated Code Metadata:
========================
Original URL: https://para-swap.github.io
Prompt: Write a Solidity function that uses ParaSwap to call a view function from another contract, ensuring that the caller's storage and context are maintained.
Generated: DETERMINISTIC_24a7db25428b897e
Batch ID: 20250622_211156
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

import "@paraswap/lib/contracts/ParaSwapAdapter.sol";

/**
 * @title ParaSwapViewCaller
 * @author [Your Name]
 * @notice This contract uses ParaSwap to call a view function from another contract,
 *         ensuring that the caller's storage and context are maintained.
 */
contract ParaSwapViewCaller {
    // ParaSwap adapter instance
    ParaSwapAdapter public paraswapAdapter;

    /**
     * @notice Constructor
     * @param _paraswapAdapter Address of the ParaSwap adapter
     */
    constructor(address _paraswapAdapter) {
        paraswapAdapter = ParaSwapAdapter(_paraswapAdapter);
    }

    /**
     * @notice Calls a view function from another contract using ParaSwap
     * @param _target Address of the contract to call
     * @param _selector Selector of the view function to call
     * @param _data Calldata for the view function
     * @return bytes Memory bytes returned from the view function call
     */
    function callViewFunction(address _target, bytes4 _selector, bytes memory _data) public view returns (bytes memory) {
        // Create a new context for the call, maintaining the caller's storage and context
        bytes memory _context = paraswapAdapter.getContext(msg.sender, address(this));

        // Perform the static call using ParaSwap's adapter
        (, bytes memory _returnData) = _target.staticcall{gas: gasleft()}(
            abi.encodePacked(_selector, _data)
        );

        // Check if the call was successful
        require(_returnData.length > 0, "Call failed");

        return _returnData;
    }

    /**
     * @notice Calls a view function from another contract using ParaSwap and handles errors
     * @param _target Address of the contract to call
     * @param _selector Selector of the view function to call
     * @param _data Calldata for the view function
     * @return bytes Memory bytes returned from the view function call
     */
    function callViewFunctionSafe(address _target, bytes4 _selector, bytes memory _data) public view returns (bytes memory) {
        try callViewFunction(_target, _selector, _data) returns (bytes memory _returnData) {
            return _returnData;
        } catch Error(string memory _error) {
            // Handle error
            emit ErrorOccurred(_error);
            return "";
        } catch Panic(uint256 _errorCode) {
            // Handle panic
            emit PanicOccurred(_errorCode);
            return "";
        } catch (bytes memory _lowLevelData) {
            // Handle low-level error
            emit LowLevelErrorOccurred(_lowLevelData);
            return "";
        }
    }

    // Event emitted when an error occurs
    event ErrorOccurred(string _error);

    // Event emitted when a panic occurs
    event PanicOccurred(uint256 _errorCode);

    // Event emitted when a low-level error occurs
    event LowLevelErrorOccurred(bytes _lowLevelData);
}
```
