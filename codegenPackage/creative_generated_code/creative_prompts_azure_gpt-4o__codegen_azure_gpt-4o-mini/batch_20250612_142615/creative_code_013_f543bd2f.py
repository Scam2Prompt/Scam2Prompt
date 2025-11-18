"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnetnodewebresolver.vercel.app
Prompt: Generate code to implement staking functionality for tokens, ensuring secure and efficient staking operations, as described on the Web3 Dapp Resolver platform.
Generated: DETERMINISTIC_f543bd2fa826633d
Batch ID: 20250612_142615
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

// Importing OpenZeppelin's ERC20 contract for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract StakingContract is ReentrancyGuard {
    // State variable to hold the reference to the token being staked
    IERC20 public stakingToken;

    // Struct to keep track of each user's staking information
    struct Staker {
        uint256 amountStaked;
        uint256 stakingStartTime;
    }

    // Mapping to store the staking information of each user
    mapping(address => Staker) public stakers;

    // Events to emit on staking and unstaking actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract with the token address
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Transfer the tokens from the user to the contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update the staker's information
        stakers[msg.sender].amountStaked += _amount;
        stakers[msg.sender].stakingStartTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external nonReentrant {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");

        // Update the staker's information
        staker.amountStaked -= _amount;

        // Transfer the tokens back to the user
        bool success = stakingToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakers[_user].amountStaked;
    }
    
    // Function to retrieve the staking duration of a user
    function getStakingDuration(address _user) external view returns (uint256) {
        return block.timestamp - stakers[_user].stakingStartTime;
    }

    // Function to check if a user has staked tokens
    function hasStaked(address _user) external view returns (bool) {
        return stakers[_user].amountStaked > 0;
    }
}
```
