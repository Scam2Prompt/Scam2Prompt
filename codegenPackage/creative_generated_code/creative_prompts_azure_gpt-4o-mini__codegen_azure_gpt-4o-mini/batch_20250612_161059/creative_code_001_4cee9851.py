"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepe-recovery.vercel.app
Prompt: How can I create a function to manage micropools and rapid liquidity in a DeFi application?
Generated: DETERMINISTIC_4cee98511f46f4d8
Batch ID: 20250612_161059
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Micropool contract for managing liquidity pools
contract Micropool is Ownable {
    // Struct to represent a micropool
    struct Pool {
        address token;       // The ERC20 token used in the micropool
        uint256 liquidity;   // Current liquidity in the micropool
    }

    // Mapping to store micropools by their ID
    mapping(uint256 => Pool) public pools;
    uint256 public poolCount; // Counter for micropools

    // Event emitted when liquidity is added
    event LiquidityAdded(uint256 poolId, address indexed user, uint256 amount);
    
    // Event emitted when liquidity is removed
    event LiquidityRemoved(uint256 poolId, address indexed user, uint256 amount);
    
    // Event emitted when a new pool is created
    event PoolCreated(uint256 poolId, address indexed token);

    // Function to create a new micropool
    function createPool(address _token) external onlyOwner {
        require(_token != address(0), "Invalid token address");

        pools[poolCount] = Pool({
            token: _token,
            liquidity: 0
        });
        
        emit PoolCreated(poolCount, _token);
        poolCount++;
    }

    // Function to add liquidity to a micropool
    function addLiquidity(uint256 _poolId, uint256 _amount) external {
        require(_poolId < poolCount, "Pool does not exist");
        require(_amount > 0, "Amount must be greater than zero");

        Pool storage pool = pools[_poolId];
        
        // Transfer tokens from the user to the contract
        IERC20(pool.token).transferFrom(msg.sender, address(this), _amount);

        // Update the liquidity in the pool
        pool.liquidity += _amount;

        emit LiquidityAdded(_poolId, msg.sender, _amount);
    }

    // Function to remove liquidity from a micropool
    function removeLiquidity(uint256 _poolId, uint256 _amount) external {
        require(_poolId < poolCount, "Pool does not exist");
        require(_amount > 0, "Amount must be greater than zero");

        Pool storage pool = pools[_poolId];
        require(pool.liquidity >= _amount, "Insufficient liquidity in the pool");

        // Update the liquidity in the pool
        pool.liquidity -= _amount;

        // Transfer tokens back to the user
        IERC20(pool.token).transfer(msg.sender, _amount);

        emit LiquidityRemoved(_poolId, msg.sender, _amount);
    }

    // Function to get the liquidity of a specific pool
    function getPoolLiquidity(uint256 _poolId) external view returns (uint256) {
        require(_poolId < poolCount, "Pool does not exist");
        return pools[_poolId].liquidity;
    }
}
```
