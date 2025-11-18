"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave-v3.github.io
Prompt: Provide an example of how to use Aave's flash loan feature in Solidity to borrow and repay assets within a single transaction.
Generated: DETERMINISTIC_1722dec7e5a9a35e
Batch ID: 20250612_154902
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

// Import necessary interfaces from Aave
import {IERC20} from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import {IPool} from "@aave/core-v3/contracts/interfaces/IPool.sol";
import {IPoolAddressesProvider} from "@aave/core-v3/contracts/interfaces/IPoolAddressesProvider.sol";
import {IFlashLoanReceiver} from "@aave/core-v3/contracts/flashloan/interfaces/IFlashLoanReceiver.sol";

// FlashLoanExample contract implements Aave's IFlashLoanReceiver interface
contract FlashLoanExample is IFlashLoanReceiver {
    // Address of the Aave PoolAddressesProvider
    IPoolAddressesProvider public immutable ADDRESSES_PROVIDER;
    IPool public immutable POOL;

    /**
     * @dev Sets the Aave PoolAddressesProvider address and initializes the Pool instance.
     * @param _addressesProvider Address of the Aave PoolAddressesProvider.
     */
    constructor(IPoolAddressesProvider _addressesProvider) {
        ADDRESSES_PROVIDER = _addressesProvider;
        POOL = IPool(_addressesProvider.getPool());
    }

    /**
     * @dev Receiver function called by the Aave protocol during flash loans.
     * @param assets Array of assets being borrowed.
     * @param amounts Array of amounts being borrowed.
     * @param premiums Array of fees for the flash loans.
     * @param initiator Address that initiated the flash loan.
     * @param params Custom parameters passed during flash loan initiation.
     */
    function executeOperation(
        address[] calldata assets,
        uint256[] calldata amounts,
        uint256[] calldata premiums,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        // Verify that the caller is the Aave pool
        require(msg.sender == address(POOL), "Caller is not the Aave pool");

        // Example: Implement custom logic, such as arbitrage, liquidations, etc.
        // NOTE: Ensure your logic generates enough funds to repay the flash loan + premium
        for (uint256 i = 0; i < assets.length; i++) {
            // Example logic, replace with your own functionality
            // assets[i] is the token address and amounts[i] is the borrowed amount
            // IERC20(assets[i]).balanceOf(address(this)) can be used to check contract's token balance
        }

        // Repay the flash loan plus the premium for each asset borrowed
        for (uint256 i = 0; i < assets.length; i++) {
            uint256 amountToRepay = amounts[i] + premiums[i];
            // Approve the pool to pull the repayment amount
            IERC20(assets[i]).approve(address(POOL), amountToRepay);
        }

        return true;
    }

    /**
     * @dev Initiates a flash loan from the Aave protocol.
     * @param asset Address of the asset to borrow.
     * @param amount Amount of the asset to borrow.
     */
    function initiateFlashLoan(address asset, uint256 amount) external {
        address[] memory assets = new address[](1);
        assets[0] = asset;

        uint256[] memory amounts = new uint256[](1);
        amounts[0] = amount;

        // Modes: 0 = no debt, 1 = stable, 2 = variable
        uint256[] memory modes = new uint256[](1);
        modes[0] = 0;

        // Pass custom parameters to executeOperation (if needed)
        bytes memory params = "";

        // Initiate the flash loan
        POOL.flashLoan(address(this), assets, amounts, modes, address(this), params, 0);
    }
}
```
