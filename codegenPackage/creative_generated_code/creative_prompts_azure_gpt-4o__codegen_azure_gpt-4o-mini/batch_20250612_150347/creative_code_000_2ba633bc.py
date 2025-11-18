"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethlido.pages.dev
Prompt: Write a Solidity smart contract that interacts with the Lido protocol to stake ETH and mint stETH tokens. Ensure the contract includes functionality for withdrawing stETH and converting it back to ETH.
Generated: DETERMINISTIC_2ba633bcedb99c05
Batch ID: 20250612_150347
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

// Importing the interfaces for the Lido protocol
interface ILido {
    function submit(address _referral) external payable returns (uint256);
    function withdraw(uint256 _stETHAmount) external;
}

interface IStETH {
    function getStETHByETH(uint256 _ethAmount) external view returns (uint256);
    function getETHByStETH(uint256 _stETHAmount) external view returns (uint256);
}

// This contract allows users to stake ETH and mint stETH tokens using Lido
contract LidoStaker {
    // The Lido contract address on the Ethereum network
    ILido public lido;
    IStETH public stETH;

    // Events to log transactions
    event Staked(address indexed user, uint256 ethAmount, uint256 stETHReceived);
    event Withdrawn(address indexed user, uint256 stETHAmount, uint256 ethReceived);

    // Initializing the Lido and stETH contract addresses
    constructor(address _lidoAddress, address _stETHAddress) {
        lido = ILido(_lidoAddress);
        stETH = IStETH(_stETHAddress);
    }

    // Function to stake ETH and receive stETH
    function stakeETH() external payable {
        require(msg.value > 0, "Must send ETH to stake");

        // Call the Lido submit function to stake ETH
        uint256 stETHReceived = lido.submit{value: msg.value}(address(0));
        
        emit Staked(msg.sender, msg.value, stETHReceived);
    }

    // Function to withdraw stETH and convert it back to ETH
    function withdrawStETH(uint256 _stETHAmount) external {
        require(_stETHAmount > 0, "Must withdraw a positive amount of stETH");

        // Withdraw stETH from Lido
        lido.withdraw(_stETHAmount);

        // Convert stETH to ETH
        uint256 ethReceived = stETH.getETHByStETH(_stETHAmount);
        require(ethReceived > 0, "Conversion resulted in zero ETH");

        // Transfer the ETH to the sender
        (bool success, ) = msg.sender.call{value: ethReceived}("");
        require(success, "Failed to transfer ETH");

        emit Withdrawn(msg.sender, _stETHAmount, ethReceived);
    }

    // Function to receive ETH directly
    receive() external payable {}

    // Fallback function to prevent sending ETH directly to the contract
    fallback() external {
        revert("Direct ETH transfers not allowed");
    }
}
```
