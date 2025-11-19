"""
Generated Code Metadata:
========================
Original URL: https://gemcaster.vercel.app
Prompt: "Design a simple smart contract using Solidity that allows users to collect digital casts and earn rewards, similar to Gemcaster's functionality on Zora."
Generated: DETERMINISTIC_36a5d6b231434b19
Batch ID: 20250622_210802
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
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for collecting digital casts and earning rewards
contract DigitalCastCollector is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a digital cast
    struct Cast {
        uint256 id;
        string uri; // URI for the digital cast metadata
        address creator; // Address of the creator
        uint256 reward; // Reward amount for this cast
    }

    // Mapping to store casts by ID
    mapping(uint256 => Cast) public casts;
    // Counter for generating unique cast IDs
    Counters.Counter private _castIdCounter;

    // Event emitted when a new cast is created
    event CastCreated(uint256 indexed id, string uri, address indexed creator, uint256 reward);
    // Event emitted when a user collects a cast
    event CastCollected(uint256 indexed id, address indexed collector);

    // Reward token contract
    IERC20 public rewardToken;

    // Constructor to set the reward token address
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    // Function to create a new digital cast
    function createCast(string memory _uri, uint256 _reward) external onlyOwner {
        require(bytes(_uri).length > 0, "URI cannot be empty");
        require(_reward > 0, "Reward must be greater than zero");

        uint256 newCastId = _castIdCounter.current();
        casts[newCastId] = Cast(newCastId, _uri, msg.sender, _reward);
        _castIdCounter.increment();

        emit CastCreated(newCastId, _uri, msg.sender, _reward);
    }

    // Function to collect a digital cast and earn rewards
    function collectCast(uint256 _castId) external {
        Cast storage cast = casts[_castId];
        require(cast.id == _castId, "Cast does not exist");
        require(cast.reward > 0, "No reward available for this cast");

        // Transfer the reward to the collector
        bool success = rewardToken.transfer(msg.sender, cast.reward);
        require(success, "Reward transfer failed");

        emit CastCollected(_castId, msg.sender);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        bool success = rewardToken.transfer(msg.sender, amount);
        require(success, "Withdrawal failed");
    }

    // Function to get the details of a cast
    function getCast(uint256 _castId) external view returns (Cast memory) {
        require(casts[_castId].id == _castId, "Cast does not exist");
        return casts[_castId];
    }
}
```
