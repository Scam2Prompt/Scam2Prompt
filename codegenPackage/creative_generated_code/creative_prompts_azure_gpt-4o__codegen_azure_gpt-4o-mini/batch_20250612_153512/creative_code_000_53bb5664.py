"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimspopofrog.web.app
Prompt: Write a smart contract in Solidity for staking $FROP tokens, ensuring compatibility with multichain functionality as described in the Popo ecosystem.
Generated: DETERMINISTIC_53bb566404b117ad
Batch ID: 20250612_153512
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

// Import the interface for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FROPStaking
 * @dev A smart contract for staking $FROP tokens with multichain compatibility
 */
contract FROPStaking is Ownable {
    // State variable to store the token being staked
    IERC20 public fropToken;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 stakedAt;
    }

    // Mapping to track stakers and their information
    mapping(address => Staker) private stakers;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    
    // Error for insufficient balance
    error InsufficientBalance(uint256 requested, uint256 available);

    /**
     * @dev Constructor to initialize the contract
     * @param _fropToken The address of the $FROP token contract
     */
    constructor(address _fropToken) {
        require(_fropToken != address(0), "Token address cannot be zero");
        fropToken = IERC20(_fropToken);
    }

    /**
     * @dev Function to stake $FROP tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Check the user's balance
        uint256 balance = fropToken.balanceOf(msg.sender);
        if (balance < amount) {
            revert InsufficientBalance({requested: amount, available: balance});
        }

        // Transfer tokens from the user to the contract
        fropToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staker information
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].stakedAt = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake $FROP tokens
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        Staker storage staker = stakers[msg.sender];
        
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker's staked amount
        staker.amountStaked -= amount;

        // Transfer tokens back to the user
        fropToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Function to get the staked amount of the caller
     * @return The amount of tokens staked by the caller
     */
    function getStakedAmount() external view returns (uint256) {
        return stakers[msg.sender].amountStaked;
    }

    /**
     * @dev Function to withdraw contract's tokens to owner (for emergency)
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(fropToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        fropToken.transfer(msg.sender, amount);
    }
}
```
