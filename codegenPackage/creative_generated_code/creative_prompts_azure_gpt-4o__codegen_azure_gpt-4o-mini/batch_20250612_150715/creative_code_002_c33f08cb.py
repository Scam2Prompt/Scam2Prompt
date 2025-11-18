"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdapp.pages.dev
Prompt: Generate code to implement a staking feature in a DApp, ensuring assets are returned to the user's wallet upon redemption, as described in the staking/harvest section of the webpage.
Generated: DETERMINISTIC_c33f08cb113d8fa1
Batch ID: 20250612_150715
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

// Import the ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for a decentralized application (DApp)
contract Staking is Ownable {
    // Struct to hold details of each staker
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 lastStakedAt; // Timestamp of the last staking action
    }

    // Mapping from user addresses to their staking details
    mapping(address => Staker) private stakers;

    // The token being staked
    IERC20 public stakingToken;

    // Event emitted when tokens are staked
    event Staked(address indexed staker, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed staker, uint256 amount);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the staker to this contract
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staker details
        stakers[msg.sender].amount += _amount;
        stakers[msg.sender].lastStakedAt = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens and return them to the user's wallet
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];

        require(staker.amount >= _amount, "Insufficient staked amount");

        // Update the staked amount
        staker.amount -= _amount;

        // Transfer tokens back to the staker
        require(stakingToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Getter function to retrieve staked amount for a user
    function getStakedAmount(address _staker) external view returns (uint256) {
        return stakers[_staker].amount;
    }

    // Function to retrieve the total staked amount in the contract
    function totalStaked() external view returns (uint256 total) {
        for (uint256 i = 0; i < getStakerCount(); i++) {
            total += stakers[getStakerAt(i)].amount;
        }
    }

    // Internal function to count stakers (requires additional implementation)
    function getStakerCount() internal view returns (uint256) {
        // Implementation depends on how you plan to store and track unique stakers
    }

    // Internal function to get staker address at a given index (requires additional implementation)
    function getStakerAt(uint256 index) internal view returns (address) {
        // Implementation depends on how you plan to store and track unique stakers
    }
}
```
