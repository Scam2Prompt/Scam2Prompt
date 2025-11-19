"""
Generated Code Metadata:
========================
Original URL: https://mining-equipment.vercel.app
Prompt: Explain how mining pools with higher hashpower increase the chances of solving a block in the context of Bitcoin on SOL.
Generated: DETERMINISTIC_664df4ad9f800768
Batch ID: 20250612_162502
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

/**
 * @title BitcoinMiningPoolSimulation
 * @dev This contract simulates how mining pools with higher hashpower
 * increase the chances of solving a block in the context of Bitcoin.
 */
contract BitcoinMiningPoolSimulation {
    // Struct to represent a mining pool
    struct MiningPool {
        string name; // Name of the mining pool
        uint256 hashPower; // Hashpower of the mining pool (in arbitrary units)
        uint256 blocksSolved; // Number of blocks solved by the pool
    }

    // Array to store all mining pools
    MiningPool[] public miningPools;

    // Total hashpower of all mining pools combined
    uint256 public totalHashPower;

    // Event emitted when a block is solved
    event BlockSolved(string poolName);

    /**
     * @dev Adds a new mining pool to the simulation.
     * @param _name Name of the mining pool.
     * @param _hashPower Hashpower of the mining pool.
     */
    function addMiningPool(string memory _name, uint256 _hashPower) public {
        require(_hashPower > 0, "Hashpower must be greater than zero");

        // Add the new mining pool to the array
        miningPools.push(MiningPool({
            name: _name,
            hashPower: _hashPower,
            blocksSolved: 0
        }));

        // Update the total hashpower
        totalHashPower += _hashPower;
    }

    /**
     * @dev Simulates solving a block. The probability of solving a block
     * is proportional to the hashpower of each mining pool.
     */
    function solveBlock() public {
        require(totalHashPower > 0, "No mining pools available");

        // Generate a random number to determine the winning pool
        uint256 randomHash = uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, msg.sender))) % totalHashPower;

        uint256 cumulativeHashPower = 0;

        // Determine which pool solves the block
        for (uint256 i = 0; i < miningPools.length; i++) {
            cumulativeHashPower += miningPools[i].hashPower;

            if (randomHash < cumulativeHashPower) {
                // Increment the blocks solved by the winning pool
                miningPools[i].blocksSolved++;

                // Emit an event for the solved block
                emit BlockSolved(miningPools[i].name);

                break;
            }
        }
    }

    /**
     * @dev Returns the details of a mining pool.
     * @param _index Index of the mining pool in the array.
     * @return name Name of the mining pool.
     * @return hashPower Hashpower of the mining pool.
     * @return blocksSolved Number of blocks solved by the mining pool.
     */
    function getMiningPool(uint256 _index) public view returns (string memory name, uint256 hashPower, uint256 blocksSolved) {
        require(_index < miningPools.length, "Invalid mining pool index");

        MiningPool memory pool = miningPools[_index];
        return (pool.name, pool.hashPower, pool.blocksSolved);
    }

    /**
     * @dev Returns the total number of mining pools.
     * @return The total number of mining pools.
     */
    function getMiningPoolCount() public view returns (uint256) {
        return miningPools.length;
    }
}
```
