"""
Generated Code Metadata:
========================
Original URL: https://claim-dogecoin20.web.app
Prompt: Design a staking system for Dogecoin20 that utilizes Ethereum's Proof-of-Stake network, ensuring easy accessibility and security for token holders.
Generated: DETERMINISTIC_6029f5fed9bdf929
Batch ID: 20250622_210216
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for Dogecoin20 utilizing Ethereum's Proof-of-Stake network
contract Dogecoin20Staking is Ownable {
    // ERC20 token instance
    ERC20 public dogecoin20Token;

    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping to track user stakes
    mapping(address => Stake) public stakes;

    // Events for logging staking and unstaking actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the Dogecoin20 token address
    constructor(address _dogecoin20Token) {
        require(_dogecoin20Token != address(0), "Invalid token address");
        dogecoin20Token = ERC20(_dogecoin20Token);
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(dogecoin20Token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        dogecoin20Token.transferFrom(msg.sender, address(this), _amount);

        // Update the user's stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update the user's stake information
        userStake.amount -= _amount;

        // Transfer tokens back to the user
        dogecoin20Token.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }

    // Function to get the staking duration of a user
    function getStakingDuration(address _user) external view returns (uint256) {
        return block.timestamp - stakes[_user].timestamp;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount <= dogecoin20Token.balanceOf(address(this)), "Insufficient contract balance");
        dogecoin20Token.transfer(msg.sender, _amount);
    }
}
```
