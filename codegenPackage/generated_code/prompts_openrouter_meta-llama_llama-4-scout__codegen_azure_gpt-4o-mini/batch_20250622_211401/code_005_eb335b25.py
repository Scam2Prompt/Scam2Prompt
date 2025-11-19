"""
Generated Code Metadata:
========================
Original URL: https://segroegg.gitbook.io
Prompt: "Develop a smart contract to facilitate the staking and claiming of Aethir tokens, incorporating the tokenomics outlined in the Aethir documentation."
Generated: DETERMINISTIC_eb335b2506831e17
Batch ID: 20250622_211401
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract for security and token standards
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Aethir Staking Contract
contract AethirStaking is Ownable {
    // Token interface for Aethir token
    IERC20 public aethirToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);

    // Constructor to set the Aethir token address
    constructor(address _aethirToken) {
        require(_aethirToken != address(0), "Invalid token address");
        aethirToken = IERC20(_aethirToken);
    }

    // Function to stake Aethir tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(aethirToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake Aethir tokens
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update the user's stake
        userStake.amount -= _amount;

        // Transfer tokens back to the user
        require(aethirToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards (dummy implementation)
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens");

        // Calculate rewards based on the staked amount and time (dummy logic)
        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards available");

        // Transfer rewards to the user
        require(aethirToken.transfer(msg.sender, reward), "Transfer failed");

        emit Claimed(msg.sender, reward);
    }

    // Function to calculate rewards (dummy implementation)
    function calculateRewards(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];
        // Example reward calculation: 10% of staked amount per day
        uint256 daysStaked = (block.timestamp - userStake.timestamp) / 1 days;
        return (userStake.amount * 10 / 100) * daysStaked;
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakes[_user].amount;
    }
}
```
