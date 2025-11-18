"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchainedclaims.pages.dev
Prompt: Write a smart contract in Solidity for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain, ensuring compatibility with Ethereum and Pepe Chain.
Generated: DETERMINISTIC_980a3c51b8c2d71d
Batch ID: 20250612_151038
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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $PEPU tokens
contract PepeStaking is Ownable {
    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Structure to hold staker information
    struct Staker {
        uint256 amountStaked;  // Amount of tokens staked
        uint256 lastStakedAt;  // Timestamp of last stake
    }

    IERC20 public pepuToken; // Instance of the $PEPU token contract
    mapping(address => Staker) public stakers; // Mapping of stakers

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _pepuToken) {
        pepuToken = _pepuToken;
    }

    // Function to stake $PEPU tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer $PEPU tokens from sender to the contract
        require(pepuToken.transferFrom(msg.sender, address(this), amount), "Stake transfer failed");

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastStakedAt = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked $PEPU tokens
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker information
        staker.amountStaked -= amount;

        // Transfer $PEPU tokens back to the staker
        require(pepuToken.transfer(msg.sender, amount), "Withdraw transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to get the staked balance of a user
    function getStakedBalance(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }

    // Function to recover accidentally sent ERC20 tokens
    function recoverTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != pepuToken, "Cannot recover $PEPU tokens");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens back to the owner
        require(token.transfer(msg.sender, amount), "Token recovery failed");
    }
}
```
