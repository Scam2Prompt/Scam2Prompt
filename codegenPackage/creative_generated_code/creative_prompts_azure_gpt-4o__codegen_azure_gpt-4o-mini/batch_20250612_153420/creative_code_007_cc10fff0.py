"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claiming.pages.dev
Prompt: Write a Solidity contract that ensures DOGE20 tokens are stored securely in wallets compatible with ERC-20 standards, while enabling staking functionality.
Generated: DETERMINISTIC_cc10fff0ab9fbd0c
Batch ID: 20250612_153420
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

// Import the ERC20 interface and Ownable contract from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the DOGE20 token
interface IDOGE20 is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Main contract for DOGE20 staking
contract DOGE20Staking is Ownable {
    // The DOGE20 token contract
    IDOGE20 public doge20Token;

    // Structure to hold staking information for each user
    struct Staker {
        uint256 amountStaked;
        uint256 stakingTimestamp;
    }

    // Mapping to store staking information for each user
    mapping(address => Staker) private stakers;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when a user un-stakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the DOGE20 token address
    constructor(address _doge20Token) {
        require(_doge20Token != address(0), "DOGE20 token address cannot be zero");
        doge20Token = IDOGE20(_doge20Token);
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker information
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].stakingTimestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update staker information
        staker.amountStaked -= amount;

        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }

    // Function to get the staking duration of a user
    function getStakingDuration(address user) external view returns (uint256) {
        return block.timestamp - stakers[user].stakingTimestamp;
    }

    // Function to withdraw unallocated DOGE20 tokens (onlyOwner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
