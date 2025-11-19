"""
Generated Code Metadata:
========================
Original URL: https://op-enocean.github.io
Prompt: Generate an example of a library contract that uses Open Ocean to share reusable code securely across multiple consumer contracts.
Generated: DETERMINISTIC_8270317981648a90
Batch ID: 20250612_155554
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

import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Library Contract using OpenOcean
 * @author [Your Name]
 * @notice This contract demonstrates how to use OpenOcean to share reusable code securely across multiple consumer contracts.
 */
contract LibraryContract {
    using SafeMath for uint256;

    // Mapping of consumer contracts to their respective permissions
    mapping(address => bool) public authorizedConsumers;

    /**
     * @notice Initializes the library contract
     * @param _consumer The address of the consumer contract
     */
    constructor(address _consumer) public {
        // Authorize the consumer contract by default
        authorizedConsumers[_consumer] = true;
    }

    /**
     * @notice Authorizes a consumer contract to use the library
     * @param _consumer The address of the consumer contract
     */
    function authorizeConsumer(address _consumer) public onlyOwner {
        authorizedConsumers[_consumer] = true;
    }

    /**
     * @notice Revokes authorization for a consumer contract
     * @param _consumer The address of the consumer contract
     */
    function revokeConsumer(address _consumer) public onlyOwner {
        authorizedConsumers[_consumer] = false;
    }

    /**
     * @notice Reusable function to be used by consumer contracts
     * @param _x The first operand
     * @param _y The second operand
     * @return The sum of _x and _y
     */
    function add(uint256 _x, uint256 _y) public pure returns (uint256) {
        return _x.add(_y);
    }

    /**
     * @notice Modifier to restrict access to authorized consumers
     */
    modifier onlyAuthorizedConsumer() {
        require(authorizedConsumers[msg.sender], "Consumer not authorized");
        _;
    }

    /**
     * @notice Modifier to restrict access to the contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    /**
     * @notice Getter for the contract owner
     * @return The address of the contract owner
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}

// Example consumer contract
contract ConsumerContract {
    LibraryContract public library;

    /**
     * @notice Initializes the consumer contract
     * @param _library The address of the library contract
     */
    constructor(address _library) public {
        library = LibraryContract(_library);
    }

    /**
     * @notice Uses the reusable function from the library contract
     * @param _x The first operand
     * @param _y The second operand
     * @return The sum of _x and _y
     */
    function useLibraryFunction(uint256 _x, uint256 _y) public view returns (uint256) {
        // Call the library function
        return library.add(_x, _y);
    }
}
```
