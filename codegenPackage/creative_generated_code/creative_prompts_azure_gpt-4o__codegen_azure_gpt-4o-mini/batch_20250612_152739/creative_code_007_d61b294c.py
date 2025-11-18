"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://backup-ar.pages.dev
Prompt: Provide an example of a decentralized launchpad implementation using DTORO Studio for token creation and crowdpooling.
Generated: DETERMINISTIC_d61b294c68f9c2f2
Batch ID: 20250612_152739
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Contract for the Token to be launched
contract CustomToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Events
    event TokensMinted(address indexed to, uint256 amount);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    // Mint tokens to a specified address
    function mintTokens(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }
}

// Main Launchpad contract
contract Launchpad is Ownable {
    using SafeMath for uint256;

    // Struct to hold crowdpooling details
    struct Pool {
        address tokenAddress;
        uint256 startTime;
        uint256 endTime;
        uint256 totalRaised;
        bool isActive;
    }

    // Mapping of pool IDs to Pool details
    mapping(uint256 => Pool) public pools;
    uint256 public poolCount;

    // Events
    event PoolCreated(uint256 indexed poolId, address tokenAddress, uint256 startTime, uint256 endTime);
    event FundsRaised(uint256 indexed poolId, address investor, uint256 amount);

    // Create a new pool for crowdpooling
    function createPool(address tokenAddress, uint256 startTime, uint256 endTime) external onlyOwner {
        require(startTime < endTime, "Invalid time range");
        require(block.timestamp < startTime, "Start time must be in the future");

        poolCount++;
        pools[poolCount] = Pool(tokenAddress, startTime, endTime, 0, true);
        
        emit PoolCreated(poolCount, tokenAddress, startTime, endTime);
    }

    // Function for investors to contribute to a pool
    function contribute(uint256 poolId) external payable {
        Pool storage pool = pools[poolId];

        require(pool.isActive, "Pool is not active");
        require(block.timestamp >= pool.startTime && block.timestamp <= pool.endTime, "Not within pool timeframe");
        require(msg.value > 0, "Contribution must be greater than 0");

        pool.totalRaised += msg.value;
        
        emit FundsRaised(poolId, msg.sender, msg.value);
    }

    // Withdraw funds from the pool
    function withdrawFunds(uint256 poolId) external onlyOwner {
        Pool storage pool = pools[poolId];

        require(!pool.isActive, "Pool is still active");
        require(pool.totalRaised > 0, "No funds to withdraw");

        uint256 amount = pool.totalRaised;
        pool.totalRaised = 0;

        // Transfer funds to the owner
        payable(owner()).transfer(amount);
    }

    // Close the pool
    function closePool(uint256 poolId) external onlyOwner {
        Pool storage pool = pools[poolId];

        require(pool.isActive, "Pool is already closed");
        pool.isActive = false;
    }
}
```
