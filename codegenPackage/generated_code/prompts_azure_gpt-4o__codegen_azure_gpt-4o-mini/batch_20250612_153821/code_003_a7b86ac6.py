"""
Generated Code Metadata:
========================
Original URL: https://rocket-pool.xyz
Prompt: Create a Solidity contract that facilitates the migration of solo Ethereum validators to Rocket Pool, converting 32 ETH validators to 8 ETH validators. Include functionality for interacting with Rocket Pool's migration tools.
Generated: DETERMINISTIC_a7b86ac6a6ae8c36
Batch ID: 20250612_153821
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

// Importing the necessary interfaces for ERC20 and Rocket Pool
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Rocket Pool's migration tools
interface IRocketPool {
    function migrateValidator(address validator, uint256 amount) external;
}

contract ValidatorMigration is Ownable {
    // State variables
    IERC20 public ethToken; // The ERC20 token representing ETH
    IRocketPool public rocketPool; // Instance of Rocket Pool's migration contract

    // Event emitted when a migration occurs
    event ValidatorMigrated(address indexed validator, uint256 amount);

    // Constructor to initialize the contract with the ETH token and Rocket Pool contract addresses
    constructor(address _ethToken, address _rocketPool) {
        require(_ethToken != address(0), "Invalid ETH token address");
        require(_rocketPool != address(0), "Invalid Rocket Pool address");

        ethToken = IERC20(_ethToken);
        rocketPool = IRocketPool(_rocketPool);
    }

    // Function to migrate a solo validator to Rocket Pool
    function migrate(uint256 amount) external {
        require(amount == 32 ether, "Must migrate exactly 32 ETH");
        require(ethToken.balanceOf(msg.sender) >= amount, "Insufficient ETH balance");

        // Transfer 32 ETH from the user to this contract
        bool success = ethToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed");

        // Approve Rocket Pool to spend the ETH on behalf of this contract
        ethToken.approve(address(rocketPool), amount);

        // Call the Rocket Pool migration function
        rocketPool.migrateValidator(msg.sender, amount);

        // Emit the migration event
        emit ValidatorMigrated(msg.sender, amount);
    }

    // Function to withdraw any ETH that may be stuck in the contract
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= ethToken.balanceOf(address(this)), "Insufficient contract balance");
        bool success = ethToken.transfer(msg.sender, amount);
        require(success, "Withdrawal failed");
    }

    // Function to set a new Rocket Pool contract address (onlyOwner)
    function setRocketPool(address _rocketPool) external onlyOwner {
        require(_rocketPool != address(0), "Invalid Rocket Pool address");
        rocketPool = IRocketPool(_rocketPool);
    }
}
```
