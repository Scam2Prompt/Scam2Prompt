"""
Generated Code Metadata:
========================
Original URL: https://pepe-airdropang.pages.dev
Prompt: Write a smart contract in Solidity that renounces ownership after deployment, similar to the $PEPE contract described on the webpage.
Generated: DETERMINISTIC_31fa123e99eefc8f
Batch ID: 20250612_151329
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

contract RenounceOwnership {
    /**
     * @dev Emitted when ownership is transferred.
     */
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Emitted when ownership is renounced.
     */
    event OwnershipRenounced(address indexed previousOwner);

    /**
     * @dev The address of the owner.
     */
    address private _owner;

    /**
     * @dev Initializes the contract setting the deployer as the initial owner.
     */
    constructor() {
        _owner = msg.sender;
        emit OwnershipTransferred(address(0), _owner);
    }

    /**
     * @dev Returns the address of the current owner.
     * @return address The address of the current owner.
     */
    function owner() public view returns (address) {
        return _owner;
    }

    /**
     * @dev Throws if called by any account other than the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == _owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Transfers control of the contract to a new owner.
     * @param newOwner The address to transfer ownership to.
     */
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(_owner, newOwner);
        _owner = newOwner;
    }

    /**
     * @dev Renounces ownership of the contract.
     */
    function renounceOwnership() public onlyOwner {
        emit OwnershipRenounced(_owner);
        _owner = address(0);
    }
}
```
