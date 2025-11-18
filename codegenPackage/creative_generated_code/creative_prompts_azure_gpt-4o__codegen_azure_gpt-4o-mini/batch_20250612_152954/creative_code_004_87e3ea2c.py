"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cybro-en.pages.dev
Prompt: Develop a smart contract to implement CYBRO's "EasyFarming" feature, allowing users to invest in farming pools with one click.
Generated: DETERMINISTIC_87e3ea2c05751a4b
Batch ID: 20250612_152954
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

// Importing necessary OpenZeppelin contracts for security and standard compliance
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Defining the EasyFarming smart contract
contract EasyFarming is Ownable {
    // Struct to represent a farming pool
    struct FarmingPool {
        address token; // Address of the ERC20 token used for farming
        uint256 totalStaked; // Total amount staked in the pool
        mapping(address => uint256) stakedAmounts; // Amount staked by each user
    }

    // Mapping to store farming pools by their identifier
    mapping(bytes32 => FarmingPool) public farmingPools;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, bytes32 indexed poolId, uint256 amount);
    
    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, bytes32 indexed poolId, uint256 amount);

    // Function to create a new farming pool
    function createFarmingPool(bytes32 poolId, address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(farmingPools[poolId].token == address(0), "Pool already exists");

        // Initialize the farming pool
        farmingPools[poolId].token = token;
    }

    // Function for users to stake tokens in a farming pool
    function stake(bytes32 poolId, uint256 amount) external {
        // Validate the existence of the pool
        require(farmingPools[poolId].token != address(0), "Pool does not exist");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from user to contract
        IERC20 token = IERC20(farmingPools[poolId].token);
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staking information
        farmingPools[poolId].stakedAmounts[msg.sender] += amount;
        farmingPools[poolId].totalStaked += amount;

        // Emit the staking event
        emit Staked(msg.sender, poolId, amount);
    }

    // Function for users to withdraw tokens from a farming pool
    function withdraw(bytes32 poolId, uint256 amount) external {
        // Validate the existence of the pool
        require(farmingPools[poolId].token != address(0), "Pool does not exist");
        require(amount > 0, "Amount must be greater than zero");
        require(farmingPools[poolId].stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Update staking information
        farmingPools[poolId].stakedAmounts[msg.sender] -= amount;
        farmingPools[poolId].totalStaked -= amount;

        // Transfer tokens back to the user
        IERC20 token = IERC20(farmingPools[poolId].token);
        require(token.transfer(msg.sender, amount), "Transfer failed");

        // Emit the withdrawal event
        emit Withdrawn(msg.sender, poolId, amount);
    }

    // Function to view staked amount of a user in a specific pool
    function getStakedAmount(bytes32 poolId, address user) external view returns (uint256) {
        return farmingPools[poolId].stakedAmounts[user];
    }
}
```
