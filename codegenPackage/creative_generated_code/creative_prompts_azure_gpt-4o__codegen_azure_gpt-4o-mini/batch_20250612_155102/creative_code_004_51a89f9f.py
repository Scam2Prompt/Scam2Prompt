"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://threshold-network.web.app
Prompt: Write a smart contract function to stake tBTC and retrieve the user's staked balance using the Threshold Network.
Generated: DETERMINISTIC_51a89f9f57f2514b
Batch ID: 20250612_155102
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TBtcStaking is Ownable {
    // Declare the tBTC token interface
    IERC20 public tBTC;

    // Mapping to track user staked balances
    mapping(address => uint256) private stakedBalances;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the tBTC token address
    constructor(address _tBTCAddress) {
        require(_tBTCAddress != address(0), "Invalid tBTC address");
        tBTC = IERC20(_tBTCAddress);
    }

    // Function to stake tBTC tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(tBTC.balanceOf(msg.sender) >= amount, "Insufficient tBTC balance");
        
        // Transfer tBTC from the user to this contract
        tBTC.transferFrom(msg.sender, address(this), amount);

        // Update the user's staked balance
        stakedBalances[msg.sender] += amount;

        // Emit Staked event
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tBTC tokens
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update the user's staked balance before transferring
        stakedBalances[msg.sender] -= amount;

        // Transfer tBTC tokens back to the user
        tBTC.transfer(msg.sender, amount);

        // Emit Withdrawn event
        emit Withdrawn(msg.sender, amount);
    }

    // Function to retrieve the user's staked balance
    function getStakedBalance() external view returns (uint256) {
        return stakedBalances[msg.sender];
    }
}
```
