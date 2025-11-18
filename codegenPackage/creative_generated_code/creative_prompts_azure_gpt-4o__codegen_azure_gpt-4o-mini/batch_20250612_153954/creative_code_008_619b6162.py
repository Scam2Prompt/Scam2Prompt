"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chain-protocol.web.app
Prompt: Suggest an approach to integrate staking and unstaking functionality in a DeFi app using Chain Protocol's validation mechanisms.
Generated: DETERMINISTIC_619b61624a730970
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the Staking contract
contract Staking is Ownable {
    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    
    // Token used for staking
    IERC20 public stakingToken;
    
    // Mapping to keep track of user balances
    mapping(address => uint256) private _balances;

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from the user to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update the user's balance
        _balances[msg.sender] += amount;
        
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(_balances[msg.sender] >= amount, "Insufficient staked balance");

        // Update the user's balance before transferring
        _balances[msg.sender] -= amount;
        
        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    // Function to view staked balance of a user
    function stakedBalance(address user) external view returns (uint256) {
        return _balances[user];
    }

    // Function to withdraw tokens (in case of emergency)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to the owner
        stakingToken.transfer(owner(), amount);
    }
}
```
