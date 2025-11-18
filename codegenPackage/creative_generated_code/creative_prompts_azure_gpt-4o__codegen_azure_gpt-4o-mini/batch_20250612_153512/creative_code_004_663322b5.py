"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-ai.market
Prompt: Write a smart contract in Solidity to interact with Agora AI's tokenomics system, specifically for staking AGAI tokens.
Generated: DETERMINISTIC_663322b591ae5be7
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

// Importing the ERC20 interface for interaction with AGAI token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Staking contract for AGAI tokens
contract AGAIStaking is ReentrancyGuard {
    // The AGAI token contract
    IERC20 public agaiToken;

    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Time when the tokens were staked
    }

    // Mapping from user address to their staking information
    mapping(address => Stake) public stakes;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the AGAI token contract address
    constructor(address _agaiTokenAddress) {
        require(_agaiTokenAddress != address(0), "Invalid token address");
        agaiToken = IERC20(_agaiTokenAddress);
    }

    // Function to stake AGAI tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        require(agaiToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update the stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake AGAI tokens
    function unstake(uint256 _amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update the stake information
        userStake.amount -= _amount;

        // Transfer tokens back to the user
        require(agaiToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to get stake information of a user
    function getStakeInfo(address _user) external view returns (uint256 amount, uint256 timestamp) {
        Stake storage userStake = stakes[_user];
        return (userStake.amount, userStake.timestamp);
    }
}
```
