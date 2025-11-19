"""
Generated Code Metadata:
========================
Original URL: https://claimtontigertokenapp.pages.dev
Prompt: Write a smart contract code in Solidity (or relevant language) for distributing $TIGER tokens during a Fairlaunch event on TON blockchain.
Generated: DETERMINISTIC_cad334566fd9ae5f
Batch ID: 20250622_211405
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

// FairLaunch contract for distributing $TIGER tokens
contract FairLaunch is Ownable {
    // State variables
    IERC20 public tigerToken; // The $TIGER token contract
    uint256 public totalTokens; // Total tokens to distribute
    uint256 public tokensDistributed; // Tokens already distributed
    uint256 public startTime; // Start time of the FairLaunch
    uint256 public endTime; // End time of the FairLaunch
    mapping(address => uint256) public contributions; // User contributions

    // Events
    event TokensDistributed(address indexed user, uint256 amount);
    event FairLaunchStarted(uint256 startTime, uint256 endTime);
    event FairLaunchEnded(uint256 totalDistributed);

    // Constructor to initialize the contract
    constructor(IERC20 _tigerToken, uint256 _totalTokens) {
        require(address(_tigerToken) != address(0), "Invalid token address");
        require(_totalTokens > 0, "Total tokens must be greater than zero");

        tigerToken = _tigerToken;
        totalTokens = _totalTokens;
    }

    // Function to start the FairLaunch
    function startFairLaunch(uint256 duration) external onlyOwner {
        require(startTime == 0, "FairLaunch already started");
        startTime = block.timestamp;
        endTime = startTime + duration;

        emit FairLaunchStarted(startTime, endTime);
    }

    // Function to contribute to the FairLaunch
    function contribute(uint256 amount) external {
        require(block.timestamp >= startTime, "FairLaunch not started");
        require(block.timestamp <= endTime, "FairLaunch ended");
        require(amount > 0, "Contribution must be greater than zero");
        require(tokensDistributed + amount <= totalTokens, "Exceeds total tokens");

        // Transfer $TIGER tokens from the contributor to the contract
        require(tigerToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        contributions[msg.sender] += amount;
        tokensDistributed += amount;

        emit TokensDistributed(msg.sender, amount);
    }

    // Function to end the FairLaunch and withdraw remaining tokens
    function endFairLaunch() external onlyOwner {
        require(block.timestamp > endTime, "FairLaunch not ended yet");

        // Transfer remaining tokens back to the owner
        uint256 remainingTokens = totalTokens - tokensDistributed;
        if (remainingTokens > 0) {
            require(tigerToken.transfer(owner(), remainingTokens), "Token transfer failed");
        }

        emit FairLaunchEnded(tokensDistributed);
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(amount <= tigerToken.balanceOf(address(this)), "Insufficient balance");

        require(tigerToken.transfer(owner(), amount), "Token transfer failed");
    }
}
```
