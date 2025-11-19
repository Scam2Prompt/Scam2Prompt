"""
Generated Code Metadata:
========================
Original URL: https://aave-v3.github.io
Prompt: Provide an example of how to use Aave's flash loan feature in Solidity to borrow and repay assets within a single transaction.
Generated: DETERMINISTIC_1722dec7e5a9a35e
Batch ID: 20250612_154902
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

import "@aave/protocol-v2/contracts/interfaces/IProtocolDataProvider.sol";
import "@aave/protocol-v2/contracts/interfaces/ILendingPool.sol";
import "@aave/protocol-v2/contracts/interfaces/ILendingPoolAddressesProvider.sol";

contract FlashLoanExample {
    // Address of the LendingPoolAddressesProvider
    address public addressesProvider;

    // Mapping of asset addresses to their respective decimals
    mapping(address => uint8) public assetDecimals;

    constructor(address _addressesProvider) public {
        addressesProvider = _addressesProvider;
    }

    // Function to perform a flash loan
    function performFlashLoan(
        address _asset,
        uint256 _amount,
        address _onBehalfOf
    ) external {
        // Get the LendingPool contract instance
        ILendingPool lendingPool = ILendingPool(
            ILendingPoolAddressesProvider(addressesProvider).getLendingPool()
        );

        // Get the asset's decimals
        uint8 decimals = getAssetDecimals(_asset);

        // Approve the LendingPool to spend the asset on our behalf
        // This is required for some assets (e.g., aTokens)
        // For simplicity, assume we have already approved or handle it elsewhere

        // Perform the flash loan
        lendingPool.flashLoan(
            _asset,
            _amount,
            _onBehalfOf,
            address(this),
            block.timestamp + 1, // arbitrary deadline
            0 // no interest or fees, as we're repaying within the same tx
        );
    }

    // Callback function for flash loan
    function executeOperation(
        address[] memory assets,
        uint256[] memory amounts,
        uint256[] memory premiums,
        address initiator,
        bytes memory
    ) public returns (bool) {
        // Ensure only the LendingPool can call this function
        require(
            msg.sender ==
                ILendingPool(ILendingPoolAddressesProvider(addressesProvider).getLendingPool()),
            "Only LendingPool can call this"
        );

        // Perform your logic here (e.g., use the borrowed assets)
        // For demonstration, assume we just repay the loan
        for (uint256 i = 0; i < assets.length; i++) {
            // Repay the loan with a small premium
            IERC20(assets[i]).transfer(
                ILendingPoolAddressesProvider(addressesProvider).getLendingPool(),
                amounts[i] + premiums[i]
            );
        }

        return true;
    }

    // Helper function to get asset decimals
    function getAssetDecimals(address _asset) public view returns (uint8) {
        // For simplicity, assume assetDecimals is populated elsewhere
        // In a real scenario, use a reliable method to fetch decimals
        return assetDecimals[_asset];
    }
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
