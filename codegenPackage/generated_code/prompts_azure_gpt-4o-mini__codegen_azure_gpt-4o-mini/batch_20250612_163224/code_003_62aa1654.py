"""
Generated Code Metadata:
========================
Original URL: https://sayloud.io
Prompt: Generate a smart contract in Solidity that mimics Loud's fee split mechanism for distributing rewards to contributors.
Generated: DETERMINISTIC_62aa1654465f2509
Batch ID: 20250612_163224
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

contract FeeSplitter {
    // State variables
    address[] public contributors; // List of contributors
    mapping(address => uint256) public shares; // Mapping of contributor addresses to their shares
    uint256 public totalShares; // Total shares for distribution

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);
    event SharesUpdated(address indexed contributor, uint256 shares);
    event RewardsDistributed(uint256 totalAmount);

    // Modifier to check if the caller is a contributor
    modifier onlyContributor() {
        require(shares[msg.sender] > 0, "Not a contributor");
        _;
    }

    // Constructor to initialize the contract with contributors and their shares
    constructor(address[] memory _contributors, uint256[] memory _shares) {
        require(_contributors.length == _shares.length, "Mismatched input lengths");
        for (uint256 i = 0; i < _contributors.length; i++) {
            require(_shares[i] > 0, "Shares must be greater than zero");
            contributors.push(_contributors[i]);
            shares[_contributors[i]] = _shares[i];
            totalShares += _shares[i];
            emit SharesUpdated(_contributors[i], _shares[i]);
        }
    }

    // Function to receive Ether contributions
    receive() external payable {
        emit ContributionReceived(msg.sender, msg.value);
    }

    // Function to distribute rewards based on shares
    function distributeRewards() external payable {
        require(msg.value > 0, "No rewards to distribute");
        emit RewardsDistributed(msg.value);

        for (uint256 i = 0; i < contributors.length; i++) {
            address contributor = contributors[i];
            uint256 contributorShare = (msg.value * shares[contributor]) / totalShares;
            payable(contributor).transfer(contributorShare);
        }
    }

    // Function to update shares for a contributor
    function updateShares(address contributor, uint256 newShares) external {
        require(newShares > 0, "Shares must be greater than zero");
        require(shares[contributor] > 0, "Contributor not found");

        // Update total shares
        totalShares = totalShares - shares[contributor] + newShares;
        shares[contributor] = newShares;

        emit SharesUpdated(contributor, newShares);
    }

    // Function to get the balance of the contract
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
