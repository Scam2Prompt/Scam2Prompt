"""
Generated Code Metadata:
========================
Original URL: https://smartordinalwallet.pages.dev
Prompt: Generate a smart contract code for staking and unstaking tokens on the Smartdappchain.
Generated: DETERMINISTIC_3cf5bfeabcd96200
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for managing token staking and unstaking
contract StakingContract is Ownable {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 stakingTime;   // Time when the tokens were staked
    }

    // Mapping to track stakers and their information
    mapping(address => Staker) public stakers;

    // The token that will be staked
    IERC20 public stakingToken;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from the staker to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update the staker's information
        stakers[msg.sender].amountStaked += _amount;
        stakers[msg.sender].stakingTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amountStaked >= _amount, "Insufficient staked amount");

        // Update the staker's information
        stakers[msg.sender].amountStaked -= _amount;

        // Transfer tokens back to the staker
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakers[_user].amountStaked;
    }

    // Function to get the staking time of a user
    function getStakingTime(address _user) external view returns (uint256) {
        return stakers[_user].stakingTime;
    }
}
```
