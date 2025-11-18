"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimfloki.pages.dev
Prompt: Develop a smart contract for staking FLOKI tokens that integrates with the Floki staking platform and supports reward claiming in TokenFi.
Generated: DETERMINISTIC_4370091340a11c1d
Batch ID: 20250612_151301
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the TokenFi reward system
interface ITokenFi {
    function claimRewards(address user) external;
}

// Smart contract for staking FLOKI tokens
contract FlokiStaking is Ownable {
    // State variables
    IERC20 public flokiToken; // The FLOKI token contract
    ITokenFi public tokenFi;   // The TokenFi contract for reward claiming

    struct Stake {
        uint256 amount;          // Amount of tokens staked
        uint256 timestamp;       // Time the tokens were staked
    }

    // Mapping to track staked amounts and timestamps for each user
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user);

    // Constructor to set the FLOKI token and TokenFi contract addresses
    constructor(IERC20 _flokiToken, ITokenFi _tokenFi) {
        flokiToken = _flokiToken;
        tokenFi = _tokenFi;
    }

    // Function to stake FLOKI tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(flokiToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake FLOKI tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked amount");

        // Update user's stake
        stakes[msg.sender].amount -= _amount;
        require(flokiToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards from TokenFi
    function claimRewards() external {
        require(stakes[msg.sender].amount > 0, "No staked amount");

        tokenFi.claimRewards(msg.sender);
        emit RewardsClaimed(msg.sender);
    }

    // Function to get the user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to retrieve the total staked amount in the contract
    function totalStaked() external view returns (uint256 total) {
        for (uint256 i = 0; i < _users.length; i++) {
            total += stakes[_users[i]].amount;
        }
    }
}
```
