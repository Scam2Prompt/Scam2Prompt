"""
Generated Code Metadata:
========================
Original URL: https://ethevista.app
Prompt: "Generate a smart contract code in Solidity that enables creators to execute arbitrary logic using ETH generated from swap fees on a DEX like Ethervista."
Generated: DETERMINISTIC_103567b37bf4ae36
Batch ID: 20250622_212447
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the DEX to interact with swap fees
interface IDEX {
    function getSwapFees() external view returns (uint256);
}

contract FeeDistributor is Ownable {
    // Address of the DEX contract
    IDEX public dex;

    // Mapping to store creator's balance
    mapping(address => uint256) private creatorBalances;

    // Event emitted when fees are distributed
    event FeesDistributed(address indexed creator, uint256 amount);

    // Constructor to set the DEX address
    constructor(IDEX _dex) {
        dex = _dex;
    }

    // Function to distribute fees to creators
    function distributeFees(address[] calldata creators) external onlyOwner {
        // Get the total swap fees from the DEX
        uint256 totalFees = dex.getSwapFees();
        require(totalFees > 0, "No fees available for distribution");

        // Calculate the amount to distribute to each creator
        uint256 amountPerCreator = totalFees / creators.length;

        // Distribute fees to each creator
        for (uint256 i = 0; i < creators.length; i++) {
            address creator = creators[i];
            require(creator != address(0), "Invalid creator address");
            creatorBalances[creator] += amountPerCreator;

            emit FeesDistributed(creator, amountPerCreator);
        }
    }

    // Function for creators to withdraw their accumulated fees
    function withdrawFees() external {
        uint256 amount = creatorBalances[msg.sender];
        require(amount > 0, "No fees to withdraw");

        // Reset the creator's balance before transferring to prevent re-entrancy
        creatorBalances[msg.sender] = 0;

        // Transfer ETH to the creator
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit FeesDistributed(msg.sender, amount);
    }

    // Function to receive ETH
    receive() external payable {}

    // Function to check the balance of a creator
    function getCreatorBalance(address creator) external view returns (uint256) {
        return creatorBalances[creator];
    }
}
```
