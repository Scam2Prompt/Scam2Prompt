"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aaaaaaaaaaaa-eqr.pages.dev
Prompt: Provide an example of a smart contract that distributes AERO emissions to liquidity pools based on veAERO voter preferences, ensuring compliance with Aerodrome's vote-lock governance model.
Generated: DETERMINISTIC_90a1fd9659463bd0
Batch ID: 20250612_153225
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

interface IVeAERO {
    function getVotes(address voter) external view returns (uint256);
}

interface ILiquidityPool {
    function receiveAERO(uint256 amount) external;
}

contract AeroEmissionDistributor {
    // Address of the veAERO contract
    IVeAERO public veAERO;

    // Mapping of liquidity pools to their respective voters
    mapping(address => address[]) public liquidityPoolsToVoters;

    // Event to log the distribution of AERO emissions
    event AERODistributed(address indexed liquidityPool, uint256 amount);

    // Constructor to set the veAERO contract address
    constructor(address _veAERO) {
        veAERO = IVeAERO(_veAERO);
    }

    // Function to distribute AERO emissions based on voter preferences
    function distributeAERO(address[] memory liquidityPools, uint256 totalAERO) external {
        require(liquidityPools.length > 0, "No liquidity pools provided");
        require(totalAERO > 0, "Total AERO must be greater than zero");

        uint256 totalVotes = 0;

        // Calculate total votes for all liquidity pools
        for (uint256 i = 0; i < liquidityPools.length; i++) {
            totalVotes += veAERO.getVotes(liquidityPools[i]);
        }

        require(totalVotes > 0, "Total votes must be greater than zero");

        // Distribute AERO emissions to each liquidity pool based on its vote weight
        for (uint256 i = 0; i < liquidityPools.length; i++) {
            address liquidityPool = liquidityPools[i];
            uint256 votes = veAERO.getVotes(liquidityPool);
            uint256 allocation = (votes * totalAERO) / totalVotes;

            if (allocation > 0) {
                ILiquidityPool(liquidityPool).receiveAERO(allocation);
                emit AERODistributed(liquidityPool, allocation);
            }
        }
    }

    // Function to add a voter for a liquidity pool
    function addVoterForPool(address liquidityPool, address voter) external {
        liquidityPoolsToVoters[liquidityPool].push(voter);
    }

    // Function to remove a voter for a liquidity pool
    function removeVoterForPool(address liquidityPool, address voter) external {
        address[] storage voters = liquidityPoolsToVoters[liquidityPool];
        for (uint256 i = 0; i < voters.length; i++) {
            if (voters[i] == voter) {
                voters[i] = voters[voters.length - 1];
                voters.pop();
                break;
            }
        }
    }

    // Function to retrieve voters for a specific liquidity pool
    function getVotersForPool(address liquidityPool) external view returns (address[] memory) {
        return liquidityPoolsToVoters[liquidityPool];
    }
}
```
