"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Construct a Solidity smart contract that allows users to stake $BEAM tokens to qualify for the upcoming $SOPH airdrop.
Generated: DETERMINISTIC_ff62a5a6104d7b44
Batch ID: 20250612_160940
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

// Importing required interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Staking Contract for $BEAM Token
 * @dev Users can stake $BEAM to qualify for $SOPH airdrop
 */
contract BeamStaking is Ownable {
    // The BEAM token contract
    IERC20 public beamToken;

    // Structure to hold user staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Event for logging stake actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    
    // Constructor to set the BEAM token address
    constructor(address _beamToken) {
        require(_beamToken != address(0), "Invalid BEAM token address");
        beamToken = IERC20(_beamToken);
    }

    /**
     * @dev Allows users to stake BEAM tokens
     * @param amount The amount of BEAM tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(beamToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their BEAM tokens
     * @param amount The amount of BEAM tokens to unstake
     */
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        userStake.amount -= amount;

        require(beamToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Returns the staked amount of a user
     * @param user The address of the user
     * @return The staked amount of the user
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Allows the owner to withdraw BEAM tokens from the contract
     * @param amount The amount of BEAM tokens to withdraw
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(beamToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(beamToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
