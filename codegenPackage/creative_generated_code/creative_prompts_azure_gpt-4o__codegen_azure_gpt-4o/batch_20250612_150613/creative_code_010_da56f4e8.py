"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://on-oeth.pages.dev
Prompt: Develop a Solidity contract that interacts with the Origin vault to execute the public allocate function and deploy smaller deposits to yield-earning strategies.
Generated: DETERMINISTIC_da56f4e8980f6083
Batch ID: 20250612_150613
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
 * @title OriginVaultAllocator
 * @notice This contract interacts with the Origin Vault to allocate funds 
 *         and deploy smaller deposits to yield-earning strategies.
 */
contract OriginVaultAllocator {
    // Address of the Origin Vault contract
    address public originVault;

    // Event emitted when funds are allocated
    event FundsAllocated(address indexed allocator, uint256 amount);

    // Modifier to ensure valid address
    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address");
        _;
    }

    /**
     * @dev Constructor to initialize the Origin Vault address.
     * @param _originVault Address of the Origin Vault contract.
     */
    constructor(address _originVault) validAddress(_originVault) {
        originVault = _originVault;
    }

    /**
     * @dev Function to allocate funds using the Origin Vault's allocate function.
     * @param amount Amount of funds to allocate.
     * @notice Proper allowance must be set for this contract to allocate funds.
     */
    function allocateFunds(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Ensure we are interacting with a valid contract
        require(isContract(originVault), "Origin Vault address is not a contract");

        // Call the allocate function on the Origin Vault
        (bool success, ) = originVault.call(abi.encodeWithSignature("allocate(uint256)", amount));
        require(success, "Allocation failed");

        emit FundsAllocated(msg.sender, amount);
    }

    /**
     * @dev Function to check if an address is a contract.
     * @param _address Address to check.
     * @return isContractAddress Returns true if the address is a contract.
     */
    function isContract(address _address) private view returns (bool) {
        uint256 size;
        assembly {
            size := extcodesize(_address)
        }
        return size > 0;
    }
}
```
