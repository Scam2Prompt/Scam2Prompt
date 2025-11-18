"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rockketpool.github.io
Prompt: Generate Solidity code for a smart contract that integrates with Rocket Pool to allow users to deposit tokens and receive rETH as a representation of their stake.
Generated: DETERMINISTIC_2e8fc0866c9bc1fe
Batch ID: 20250612_145223
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

// Interface for interacting with Rocket Pool
interface IRocketPoolDeposit {
    function deposit() external payable;
}

// Interface for rETH token
interface IrETH {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingWithRocketPool {
    // Address of the Rocket Pool deposit contract
    address public immutable rocketPoolDepositAddress;
    // Address of the rETH token contract
    address public immutable rETHAddress;

    // Event emitted when a user deposits ETH and receives rETH
    event Deposited(address indexed user, uint256 ethAmount, uint256 rETHAmount);

    // Constructor to initialize contract with Rocket Pool addresses
    constructor(address _rocketPoolDepositAddress, address _rETHAddress) {
        require(_rocketPoolDepositAddress != address(0), "Invalid Rocket Pool address");
        require(_rETHAddress != address(0), "Invalid rETH address");

        rocketPoolDepositAddress = _rocketPoolDepositAddress;
        rETHAddress = _rETHAddress;
    }

    /**
     * @dev Allows users to deposit ETH and receive rETH in return.
     * The contract interacts with the Rocket Pool deposit contract to stake ETH.
     */
    function depositToRocketPool() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");

        // Record initial balance of rETH to calculate the amount received
        uint256 initialrETHBalance = IrETH(rETHAddress).balanceOf(address(this));

        // Deposit ETH to Rocket Pool
        IRocketPoolDeposit(rocketPoolDepositAddress).deposit{value: msg.value}();

        // Calculate the amount of rETH received
        uint256 newrETHBalance = IrETH(rETHAddress).balanceOf(address(this));
        uint256 rETHReceived = newrETHBalance - initialrETHBalance;

        require(rETHReceived > 0, "Failed to receive rETH from Rocket Pool");

        // Transfer rETH to the user
        bool transferSuccess = IrETH(rETHAddress).transfer(msg.sender, rETHReceived);
        require(transferSuccess, "rETH transfer failed");

        // Emit event
        emit Deposited(msg.sender, msg.value, rETHReceived);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }

    /**
     * @dev Fallback function to prevent accidental calls to non-existent functions.
     */
    fallback() external payable {
        revert("Fallback function called");
    }
}
```
