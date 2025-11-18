"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsflrsync.online
Prompt: Provide code for implementing BNB Liquid Staking (LBNB) on Flare Network, ensuring compatibility with its EVM-based infrastructure.
Generated: DETERMINISTIC_c5e15de8c899247c
Batch ID: 20250612_154029
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

// Importing required OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Implementing the LBNB (Liquid BNB) contract
contract LBNB is ERC20, Ownable {
    // Address where the staked BNB is held
    address public stakingAddress;

    // Event emitted when BNB is staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when BNB is unstaked
    event Unstaked(address indexed user, uint256 amount);
    
    // Error to handle insufficient balance for unstaking
    error InsufficientBalance();

    // Constructor to initialize the token
    constructor(address _stakingAddress) ERC20("Liquid BNB", "LBNB") {
        // Set the staking address
        stakingAddress = _stakingAddress;
    }

    // Function to stake BNB and mint LBNB tokens
    function stake(uint256 amount) external payable {
        require(msg.value == amount, "Incorrect amount sent");
        
        // Mint LBNB tokens to the sender based on the staking amount
        _mint(msg.sender, amount);
        
        emit Staked(msg.sender, amount);
    }

    // Function to unstake BNB and burn LBNB tokens
    function unstake(uint256 amount) external {
        if (balanceOf(msg.sender) < amount) {
            revert InsufficientBalance();
        }

        // Burn the LBNB tokens from the sender
        _burn(msg.sender, amount);
        
        // Transfer BNB back to the user
        payable(msg.sender).transfer(amount);
        
        emit Unstaked(msg.sender, amount);
    }

    // Function to withdraw BNB from the contract by the owner
    function withdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient contract balance");

        // Transfer BNB to the owner
        payable(owner()).transfer(amount);
    }

    // Fallback function to receive BNB
    receive() external payable {}
    
    // Function to return the contract's BNB balance
    function getBNBBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
