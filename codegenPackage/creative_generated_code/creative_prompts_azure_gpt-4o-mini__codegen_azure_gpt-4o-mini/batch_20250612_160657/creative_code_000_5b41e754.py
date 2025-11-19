"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.network
Prompt: How can I implement a borrowing function using the Aave Protocol's overcollateralized borrowing feature?
Generated: DETERMINISTIC_5b41e754b2321714
Batch ID: 20250612_160657
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

// Import necessary Aave contracts and interfaces
import "@aave/protocol-v2/contracts/interfaces/ILendingPool.sol";
import "@aave/protocol-v2/contracts/interfaces/ILendingPoolAddressesProvider.sol";
import "@aave/protocol-v2/contracts/interfaces/IERC20.sol";

contract AaveBorrower {
    ILendingPoolAddressesProvider public addressesProvider;
    ILendingPool public lendingPool;

    // Event for logging borrow actions
    event Borrowed(address indexed borrower, uint256 amount, address asset);

    constructor(address _addressesProvider) {
        // Initialize the addresses provider
        addressesProvider = ILendingPoolAddressesProvider(_addressesProvider);
        lendingPool = ILendingPool(addressesProvider.getLendingPool());
    }

    /**
     * @notice Function to borrow assets from Aave
     * @param asset The address of the asset to borrow
     * @param amount The amount to borrow
     * @param rateMode The interest rate mode (1 = stable, 2 = variable)
     */
    function borrow(address asset, uint256 amount, uint256 rateMode) external {
        // Validate parameters
        require(amount > 0, "Borrow amount must be greater than zero");

        // Check if the asset is an Aave supported asset
        require(isSupportedAsset(asset), "Asset not supported by Aave");

        // Execute the borrowing function from Aave's lending pool
        lendingPool.borrow(asset, amount, rateMode, 0, msg.sender);

        // Emit an event for logging purposes
        emit Borrowed(msg.sender, amount, asset);
    }

    /**
     * @notice Function to check if an asset is supported by Aave
     * @param asset The address of the asset to check
     * @return bool True if the asset is supported, otherwise false
     */
    function isSupportedAsset(address asset) internal view returns (bool) {
        try lendingPool.getReserveData(asset) returns (/* ReserveData */) {
            return true;
        } catch {
            return false;
        }
    }

    /**
     * @notice Function to withdraw borrowed funds
     * @param asset The address of the asset to withdraw
     * @param amount The amount to withdraw
     */
    function withdraw(address asset, uint256 amount) external {
        // Withdraw funds from the Aave protocol
        uint256 withdrawnAmount = lendingPool.withdraw(asset, amount, msg.sender);

        // Ensure withdrawal was successful
        require(withdrawnAmount > 0, "Withdrawal failed or amount is zero");
    }
}
```

This Solidity smart contract allows users to borrow assets from the Aave protocol using its overcollateralized borrowing feature. The code includes checks to ensure the asset is supported and emits events for logging purposes. Proper error handling is implemented to ensure smooth transactions.
