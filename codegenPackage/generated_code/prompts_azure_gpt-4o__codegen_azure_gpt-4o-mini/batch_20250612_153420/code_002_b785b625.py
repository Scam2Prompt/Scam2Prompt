"""
Generated Code Metadata:
========================
Original URL: https://aero-4dm.pages.dev
Prompt: Create a Solidity smart contract that allows protocols to offer incentives to veAERO voters to attract votes and build liquidity, as outlined on Aerodrome Finance.
Generated: DETERMINISTIC_b785b6251526a411
Batch ID: 20250612_153420
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract to manage incentives for veAERO voters
contract VeAeroIncentives is Ownable {
    // Struct to hold incentive details
    struct Incentive {
        address token; // Token address for the incentive
        uint256 amount; // Amount of tokens to be distributed
        uint256 startTime; // Start time for the incentive
        uint256 endTime; // End time for the incentive
        bool isActive; // Status of the incentive
    }

    // Mapping to store incentives by their ID
    mapping(uint256 => Incentive) public incentives;
    uint256 public incentiveCount; // Counter for the number of incentives

    // Event emitted when a new incentive is created
    event IncentiveCreated(uint256 indexed incentiveId, address indexed token, uint256 amount, uint256 startTime, uint256 endTime);
    
    // Event emitted when an incentive is claimed
    event IncentiveClaimed(uint256 indexed incentiveId, address indexed voter, uint256 amount);

    // Modifier to check if the incentive is active
    modifier onlyActiveIncentive(uint256 incentiveId) {
        require(incentives[incentiveId].isActive, "Incentive is not active");
        require(block.timestamp >= incentives[incentiveId].startTime, "Incentive has not started yet");
        require(block.timestamp <= incentives[incentiveId].endTime, "Incentive has ended");
        _;
    }

    // Function to create a new incentive
    function createIncentive(address token, uint256 amount, uint256 duration) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer tokens to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Create a new incentive
        incentives[incentiveCount] = Incentive({
            token: token,
            amount: amount,
            startTime: block.timestamp,
            endTime: block.timestamp + duration,
            isActive: true
        });

        emit IncentiveCreated(incentiveCount, token, amount, block.timestamp, block.timestamp + duration);
        incentiveCount++;
    }

    // Function to claim incentives
    function claimIncentive(uint256 incentiveId) external onlyActiveIncentive(incentiveId) {
        Incentive storage incentive = incentives[incentiveId];
        
        // Transfer the incentive amount to the caller
        IERC20(incentive.token).transfer(msg.sender, incentive.amount);
        
        // Mark the incentive as inactive after claiming
        incentive.isActive = false;

        emit IncentiveClaimed(incentiveId, msg.sender, incentive.amount);
    }

    // Function to withdraw tokens in case of emergency
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
