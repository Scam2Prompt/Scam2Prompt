"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shaven.top
Prompt: Write a smart contract for managing decentralized inheritance plans, referencing the features of Inheriti®, including multi-party access and secure asset distribution.
Generated: DETERMINISTIC_5003f15c9ba5f10e
Batch ID: 20250612_155024
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for managing decentralized inheritance plans
contract InheritanceManager is Ownable {
    using SafeMath for uint256;

    // Struct to represent an heir
    struct Heir {
        address payable heirAddress;
        uint256 share; // Share percentage (e.g., 50 means 50%)
    }

    // Mapping of asset IDs to their respective heirs
    mapping(uint256 => Heir[]) public assetHeirs;

    // Event to log the creation of an inheritance plan
    event InheritancePlanCreated(uint256 assetId);

    // Event to log the distribution of assets
    event AssetsDistributed(uint256 assetId);

    // Modifier to check if the caller is an heir
    modifier onlyHeir(uint256 assetId) {
        bool isHeir = false;
        for (uint256 i = 0; i < assetHeirs[assetId].length; i++) {
            if (assetHeirs[assetId][i].heirAddress == msg.sender) {
                isHeir = true;
                break;
            }
        }
        require(isHeir, "Caller is not an heir for this asset.");
        _;
    }

    // Function to create an inheritance plan for an asset
    function createInheritancePlan(uint256 assetId, address payable[] memory heirs, uint256[] memory shares) public onlyOwner {
        require(heirs.length == shares.length, "Heirs and shares length mismatch.");
        require(heirs.length > 0, "At least one heir must be added.");
        
        // Clear previous heirs for the asset
        delete assetHeirs[assetId];

        uint256 totalShares = 0;

        for (uint256 i = 0; i < heirs.length; i++) {
            // Ensure each share is greater than zero
            require(shares[i] > 0, "Share must be greater than zero");

            // Add heir to the plan
            assetHeirs[assetId].push(Heir({
                heirAddress: heirs[i],
                share: shares[i]
            }));

            totalShares = totalShares.add(shares[i]);
        }
        require(totalShares == 100, "Total shares must equal 100.");

        emit InheritancePlanCreated(assetId);
    }

    // Function to distribute assets to heirs
    function distributeAssets(uint256 assetId) public onlyOwner {
        Heir[] storage heirs = assetHeirs[assetId];
        require(heirs.length > 0, "No heirs defined for this asset.");

        // Assume the contract holds Ether that will be distributed
        uint256 totalBalance = address(this).balance;

        for (uint256 i = 0; i < heirs.length; i++) {
            uint256 heirShare = totalBalance.mul(heirs[i].share).div(100);
            heirs[i].heirAddress.transfer(heirShare);
        }

        emit AssetsDistributed(assetId);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
