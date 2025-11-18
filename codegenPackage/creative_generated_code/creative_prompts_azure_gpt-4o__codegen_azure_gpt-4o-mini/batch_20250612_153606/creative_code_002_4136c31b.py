"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ionicmoney.pages.dev
Prompt: Develop a smart contract in Solidity that interacts with the Ionic platform to supply WETH and claim Ionic points. Ensure the contract includes functions for checking supply APR and borrow APR.
Generated: DETERMINISTIC_4136c31bf333b8f8
Batch ID: 20250612_153606
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

interface IIonic {
    function supply(address asset, uint256 amount) external returns (bool);
    function claimPoints(address user) external returns (uint256);
    function getSupplyAPR(address asset) external view returns (uint256);
    function getBorrowAPR(address asset) external view returns (uint256);
}

contract IonicInteraction {
    // Address of the Ionic platform contract
    IIonic public ionic;

    // Address of the WETH token contract
    address public weth;

    // Event emitted when WETH is supplied
    event SuppliedWETH(address indexed user, uint256 amount);

    // Event emitted when Ionic points are claimed
    event ClaimedPoints(address indexed user, uint256 points);

    // Constructor to set the Ionic contract address and WETH address
    constructor(address _ionicAddress, address _wethAddress) {
        require(_ionicAddress != address(0), "Ionic address cannot be zero");
        require(_wethAddress != address(0), "WETH address cannot be zero");

        ionic = IIonic(_ionicAddress);
        weth = _wethAddress;
    }

    // Function to supply WETH to Ionic platform
    function supplyWETH(uint256 amount) external returns (bool) {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer WETH from the user to this contract
        // Note: The contract must be approved to spend the user's WETH
        (bool success, ) = weth.call(abi.encodeWithSignature("transferFrom(address,address,uint256)", msg.sender, address(this), amount));
        require(success, "Transfer of WETH failed");

        // Supply WETH to the Ionic platform
        require(ionic.supply(weth, amount), "Failed to supply WETH to Ionic");

        emit SuppliedWETH(msg.sender, amount);
        return true;
    }

    // Function to claim Ionic points for the caller
    function claimIonicPoints() external returns (uint256) {
        uint256 points = ionic.claimPoints(msg.sender);
        emit ClaimedPoints(msg.sender, points);
        return points;
    }

    // Function to get the supply APR for WETH
    function getSupplyAPR() external view returns (uint256) {
        return ionic.getSupplyAPR(weth);
    }

    // Function to get the borrow APR for WETH
    function getBorrowAPR() external view returns (uint256) {
        return ionic.getBorrowAPR(weth);
    }
}
```
