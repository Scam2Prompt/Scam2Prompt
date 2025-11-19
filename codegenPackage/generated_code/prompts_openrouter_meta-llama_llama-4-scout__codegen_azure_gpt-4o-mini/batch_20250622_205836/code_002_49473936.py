"""
Generated Code Metadata:
========================
Original URL: https://siduspad.xyz
Prompt: Generate a Solidity code snippet for a staking pool with a 180-day lock term and a 50% boost in investor tier, similar to one of the pools offered on SidusPad.
Generated: DETERMINISTIC_49473936a255710e
Batch ID: 20250622_205836
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract StakingPool is Ownable {
    using SafeMath for uint256;

    // Struct to hold information about each stake
    struct Stake {
        uint256 amount;        // Amount staked
        uint256 startTime;     // Time when the stake was created
        bool isActive;         // Status of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Token to be staked
    IERC20 public stakingToken;

    // Duration of the lock period (180 days)
    uint256 public constant LOCK_PERIOD = 180 days;

    // Boost percentage for investor tier
    uint256 public constant BOOST_PERCENTAGE = 50;

    // Event emitted when a stake is created
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a stake is withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Create or update the user's stake
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount.add(_amount),
            startTime: block.timestamp,
            isActive: true
        });

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens after the lock period
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake found");
        require(block.timestamp >= userStake.startTime + LOCK_PERIOD, "Stake is still locked");

        // Calculate the total amount to withdraw with boost
        uint256 totalAmount = userStake.amount.add(userStake.amount.mul(BOOST_PERCENTAGE).div(100));

        // Reset the user's stake
        userStake.amount = 0;
        userStake.isActive = false;

        // Transfer the tokens back to the user
        stakingToken.transfer(msg.sender, totalAmount);

        emit Withdrawn(msg.sender, totalAmount);
    }

    // Function to check the user's stake details
    function getStakeDetails(address _user) external view returns (uint256 amount, uint256 startTime, bool isActive) {
        Stake storage userStake = stakes[_user];
        return (userStake.amount, userStake.startTime, userStake.isActive);
    }

    // Function to recover tokens sent to the contract by mistake
    function recoverTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != stakingToken, "Cannot recover staking tokens");
        token.transfer(msg.sender, amount);
    }
}
```
