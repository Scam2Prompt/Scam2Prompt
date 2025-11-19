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

// Import necessary interfaces from Aave
import {FlashLoanSimpleReceiverBase} from "@aave/core-v3/contracts/flashloan/base/FlashLoanSimpleReceiverBase.sol";
import {IPoolAddressesProvider} from "@aave/core-v3/contracts/interfaces/IPoolAddressesProvider.sol";
import {IERC20} from "@aave/core-v3/contracts/dependencies/openzeppelin/contracts/IERC20.sol";

contract FlashLoanExample is FlashLoanSimpleReceiverBase {
    // Events for tracking loan execution
    event LoanExecuted(address asset, uint256 amount, uint256 premium);
    event LoanFailed(string reason);

    // Initialize the contract with Aave's PoolAddressesProvider
    constructor(IPoolAddressesProvider provider) FlashLoanSimpleReceiverBase(provider) {}

    /**
     * @notice Entry point for initiating a flash loan
     * @param asset The address of the asset to borrow
     * @param amount The amount of the asset to borrow
     */
    function requestFlashLoan(address asset, uint256 amount) external {
        // Get the Aave Pool contract
        address receiverAddress = address(this);
        bytes memory params = ""; // Additional parameters can be passed here if needed
        
        // Initiate the flash loan
        POOL.flashLoanSimple(
            receiverAddress,
            asset,
            amount,
            params,
            0 // Referral code (0 for none)
        );
    }

    /**
     * @notice This function is called after the contract has received the flash loan
     * @param asset The address of the borrowed asset
     * @param amount The amount borrowed
     * @param premium The fee to be repaid
     * @param initiator The initiator of the flash loan
     * @param params Additional parameters
     * @return Returns true if the operation was successful
     */
    function executeOperation(
        address asset,
        uint256 amount,
        uint256 premium,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        // Validate that only the Aave Pool can call this function
        require(msg.sender == address(POOL), "Caller must be Aave Pool");
        require(initiator == address(this), "Initiator must be this contract");

        // At this point, the contract has borrowed the asset
        // Implement your custom logic here (e.g., arbitrage, collateral swap, etc.)
        
        // Example: Simply approve the Pool to pull the owed amount (amount + premium)
        uint256 totalOwed = amount + premium;
        IERC20(asset).approve(address(POOL), totalOwed);

        emit LoanExecuted(asset, amount, premium);
        return true;
    }

    /**
     * @notice Emergency function to withdraw any ERC20 tokens stuck in the contract
     * @param tokenAddress The address of the token to withdraw
     * @param to The address to send the tokens to
     * @param amount The amount to withdraw
     */
    function withdrawToken(address tokenAddress, address to, uint256 amount) external {
        require(IERC20(tokenAddress).transfer(to, amount), "Withdrawal failed");
    }
}
```
