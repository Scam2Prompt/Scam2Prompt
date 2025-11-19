"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aerodrome-4gg.pages.dev
Prompt: Create an example of a smart contract that allows users to vote on liquidity pools in Aerodrome using veAERO tokens.
Generated: DETERMINISTIC_4fec7c1cbd931685
Batch ID: 20250612_164304
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

// Import the necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AerodromeVoting
 * @dev A smart contract to allow users to vote on liquidity pools using veAERO tokens.
 */
contract AerodromeVoting is Ownable {
    // Struct to represent a liquidity pool
    struct LiquidityPool {
        string name;
        uint256 votes;
        bool exists;
    }

    // Mapping to track liquidity pools by their identifier
    mapping(bytes32 => LiquidityPool) public liquidityPools;

    // Mapping to track user votes
    mapping(address => mapping(bytes32 => bool)) public hasVoted;

    // Token contract for veAERO
    IERC20 public veAERO;

    // Event emitted when a new liquidity pool is added
    event LiquidityPoolAdded(bytes32 indexed poolId, string name);

    // Event emitted when a vote is cast
    event VoteCast(address indexed voter, bytes32 indexed poolId);

    /**
     * @dev Constructor to initialize the contract with the veAERO token address.
     * @param _veAERO The address of the veAERO token contract.
     */
    constructor(address _veAERO) {
        require(_veAERO != address(0), "Invalid token address");
        veAERO = IERC20(_veAERO);
    }

    /**
     * @dev Function to add a new liquidity pool.
     * @param poolId The unique identifier for the liquidity pool.
     * @param name The name of the liquidity pool.
     */
    function addLiquidityPool(bytes32 poolId, string memory name) external onlyOwner {
        require(!liquidityPools[poolId].exists, "Pool already exists");

        liquidityPools[poolId] = LiquidityPool({
            name: name,
            votes: 0,
            exists: true
        });

        emit LiquidityPoolAdded(poolId, name);
    }

    /**
     * @dev Function to vote for a liquidity pool.
     * @param poolId The unique identifier for the liquidity pool to vote for.
     */
    function vote(bytes32 poolId) external {
        require(liquidityPools[poolId].exists, "Pool does not exist");
        require(!hasVoted[msg.sender][poolId], "You have already voted for this pool");

        // Ensure the user has at least 1 veAERO token to vote
        require(veAERO.balanceOf(msg.sender) > 0, "Insufficient veAERO tokens");

        // Cast the vote
        liquidityPools[poolId].votes += veAERO.balanceOf(msg.sender);
        hasVoted[msg.sender][poolId] = true;

        emit VoteCast(msg.sender, poolId);
    }

    /**
     * @dev Function to get the vote count for a specific liquidity pool.
     * @param poolId The unique identifier for the liquidity pool.
     * @return The total number of votes for the liquidity pool.
     */
    function getVotes(bytes32 poolId) external view returns (uint256) {
        require(liquidityPools[poolId].exists, "Pool does not exist");
        return liquidityPools[poolId].votes;
    }
}
```
