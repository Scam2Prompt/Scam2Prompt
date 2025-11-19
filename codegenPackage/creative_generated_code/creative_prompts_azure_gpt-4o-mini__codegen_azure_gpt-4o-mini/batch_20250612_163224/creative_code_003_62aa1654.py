"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sayloud.io
Prompt: Generate a smart contract in Solidity that mimics Loud's fee split mechanism for distributing rewards to contributors.
Generated: DETERMINISTIC_62aa1654465f2509
Batch ID: 20250612_163224
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

contract FeeSplit {
    // Event to log reward distribution
    event RewardsDistributed(address indexed contributor, uint256 amount);

    // Structure to hold contributor information
    struct Contributor {
        address payable wallet;
        uint256 share; // Share of the total reward
    }

    // State variables
    Contributor[] public contributors; // List of contributors
    uint256 public totalShares; // Total shares for calculating rewards

    // Modifier to check the validity of shares
    modifier validShares(uint256 _shares) {
        require(_shares > 0, "Shares must be greater than zero");
        _;
    }

    // Constructor to initialize the contract with contributors
    constructor(Contributor[] memory _contributors) {
        for (uint256 i = 0; i < _contributors.length; i++) {
            addContributor(_contributors[i].wallet, _contributors[i].share);
        }
    }

    // Function to add a contributor
    function addContributor(address payable _wallet, uint256 _share) public validShares(_share) {
        totalShares += _share;
        contributors.push(Contributor({ wallet: _wallet, share: _share }));
    }

    // Function to distribute rewards among contributors
    function distributeRewards() public payable {
        require(msg.value > 0, "No rewards to distribute");

        // Calculate and distribute rewards based on shares
        for (uint256 i = 0; i < contributors.length; i++) {
            Contributor storage contributor = contributors[i];
            uint256 reward = (msg.value * contributor.share) / totalShares;

            // Transfer reward to contributor
            (bool success, ) = contributor.wallet.call{value: reward}("");
            require(success, "Transfer failed");

            emit RewardsDistributed(contributor.wallet, reward);
        }
    }

    // Function to get the number of contributors
    function getContributorCount() public view returns (uint256) {
        return contributors.length;
    }

    // Function to get contributor's details by index
    function getContributor(uint256 index) public view returns (address, uint256) {
        require(index < contributors.length, "Contributor index out of bounds");
        Contributor memory contributor = contributors[index];
        return (contributor.wallet, contributor.share);
    }
}
```
