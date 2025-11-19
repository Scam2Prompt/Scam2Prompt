"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://omikamicoin-ie.web.app
Prompt: Provide an example of how to stake and unstake OMIKAMI tokens using a smart contract.
Generated: DETERMINISTIC_6392c4709e81d2d0
Batch ID: 20250612_155446
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Staking contract for OMIKAMI tokens
contract OMIKAMIStaking {
    using SafeMath for uint256;

    // Token being staked
    IERC20 public immutable omikamiToken;

    // Struct to store staking details
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user address to their stakes
    mapping(address => Stake) private stakes;

    // Events to log staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(IERC20 _omikamiToken) {
        require(address(_omikamiToken) != address(0), "Invalid token address");
        omikamiToken = _omikamiToken;
    }

    // Function to stake OMIKAMI tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(omikamiToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        omikamiToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;

        // Emit event for staking
        emit Staked(msg.sender, amount);
    }

    // Function to unstake OMIKAMI tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake
        userStake.amount = userStake.amount.sub(amount);

        // Transfer tokens from contract to user
        omikamiToken.transfer(msg.sender, amount);

        // Emit event for unstaking
        emit Unstaked(msg.sender, amount);
    }

    // Function to check the user's staked amount
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to check the staking timestamp
    function stakingTimestamp(address user) external view returns (uint256) {
        return stakes[user].timestamp;
    }
}
```
