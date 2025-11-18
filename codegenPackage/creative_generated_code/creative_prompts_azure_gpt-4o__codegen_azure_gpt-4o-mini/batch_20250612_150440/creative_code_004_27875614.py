"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocketspool.github.io
Prompt: Write Solidity code to interact with Rocket Pool's staking contracts, focusing on retrieving rETH balances and validating staking transactions.
Generated: DETERMINISTIC_278756142bd17b9b
Batch ID: 20250612_150440
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

// Import the interface for the Rocket Pool staking contract
interface IRocketPool {
    function getRETHBalance(address _user) external view returns (uint256);
    function stakeETH() external payable returns (bool);
}

contract RocketPoolStaking {
    // Address of the Rocket Pool staking contract (update with actual address)
    address private constant ROCKET_POOL_CONTRACT_ADDRESS = 0xYourRocketPoolContractAddress;

    // Instance of the Rocket Pool contract
    IRocketPool private rocketPool;

    // Event emitted when staking is successful
    event StakingSuccessful(address indexed user, uint256 amount);
    
    // Event emitted when retrieving rETH balance
    event REthBalanceRetrieved(address indexed user, uint256 balance);

    // Constructor to initialize the Rocket Pool contract interface
    constructor() {
        rocketPool = IRocketPool(ROCKET_POOL_CONTRACT_ADDRESS);
    }

    /**
     * @dev Retrieves the rETH balance of the user.
     * @param user The address of the user whose rETH balance is to be retrieved.
     * @return balance The rETH balance of the user.
     */
    function getRETHBalance(address user) external returns (uint256 balance) {
        require(user != address(0), "Invalid address");
        
        balance = rocketPool.getRETHBalance(user);
        emit REthBalanceRetrieved(user, balance);
        
        return balance;
    }

    /**
     * @dev Stakes ETH into the Rocket Pool staking contract.
     * @return success A boolean indicating if the staking was successful.
     */
    function stake() external payable returns (bool success) {
        require(msg.value > 0, "Must send ETH to stake");

        // Attempt to stake the ETH and handle potential errors
        success = rocketPool.stakeETH{value: msg.value}();
        require(success, "Staking failed");

        emit StakingSuccessful(msg.sender, msg.value);
    }

    // Fallback function to accept ETH when sent directly
    receive() external payable {
        // This function can be used to handle direct ETH transfers
    }
}
```
