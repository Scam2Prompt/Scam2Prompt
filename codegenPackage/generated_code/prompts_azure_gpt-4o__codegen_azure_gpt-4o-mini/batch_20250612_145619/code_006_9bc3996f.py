"""
Generated Code Metadata:
========================
Original URL: https://ethhix.com
Prompt: Create a Solidity function for calculating the total pledged ETH and distributing it to beneficiaries based on predefined conditions.
Generated: DETERMINISTIC_9bc3996f73713f93
Batch ID: 20250612_145619
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

contract PledgeDistribution {
    // State variable to store total pledged ETH
    uint256 public totalPledged;

    // Mapping to track beneficiaries and their shares
    mapping(address => uint256) public beneficiaries;
    address[] public beneficiaryList;

    // Event to log the distribution of funds
    event FundsDistributed(uint256 totalAmount, address[] beneficiaries);

    // Function to pledge ETH to the contract
    function pledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");
        totalPledged += msg.value;
    }

    // Function to set beneficiaries and their shares
    function setBeneficiaries(address[] calldata _beneficiaries, uint256[] calldata _shares) external {
        require(_beneficiaries.length == _shares.length, "Beneficiaries and shares length mismatch");
        
        // Resetting previous beneficiaries
        for (uint256 i = 0; i < beneficiaryList.length; i++) {
            delete beneficiaries[beneficiaryList[i]];
        }
        delete beneficiaryList;

        // Setting new beneficiaries and their shares
        for (uint256 i = 0; i < _beneficiaries.length; i++) {
            require(_beneficiaries[i] != address(0), "Invalid beneficiary address");
            require(_shares[i] > 0, "Share must be greater than zero");
            beneficiaries[_beneficiaries[i]] = _shares[i];
            beneficiaryList.push(_beneficiaries[i]);
        }
    }

    // Function to distribute pledged ETH to beneficiaries based on their shares
    function distributeFunds() external {
        require(totalPledged > 0, "No funds to distribute");
        
        uint256 totalShares = 0;
        for (uint256 i = 0; i < beneficiaryList.length; i++) {
            totalShares += beneficiaries[beneficiaryList[i]];
        }

        require(totalShares > 0, "No valid shares to distribute");

        // Distributing funds to each beneficiary
        for (uint256 i = 0; i < beneficiaryList.length; i++) {
            address beneficiary = beneficiaryList[i];
            uint256 share = beneficiaries[beneficiary];
            uint256 amount = (totalPledged * share) / totalShares;

            // Transfer funds to beneficiary
            (bool success, ) = beneficiary.call{value: amount}("");
            require(success, "Transfer failed");

            // Emit event for logging
            emit FundsDistributed(amount, beneficiaryList);
        }

        // Reset total pledged after distribution
        totalPledged = 0;
    }

    // Fallback function to accept ETH
    receive() external payable {
        pledge();
    }
}
```
