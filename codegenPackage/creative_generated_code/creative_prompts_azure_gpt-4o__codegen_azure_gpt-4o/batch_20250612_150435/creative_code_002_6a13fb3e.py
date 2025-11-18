"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ustddiststage.pages.dev
Prompt: Provide a step-by-step implementation in Solidity for a smart contract that handles FCFS token distribution similar to the $USDC airdrop described on the webpage.
Generated: DETERMINISTIC_6a13fb3e01a93ec5
Batch ID: 20250612_150435
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

/**
 * @title FCFS Token Distribution
 * @dev This contract implements a First-Come-First-Served (FCFS) token distribution mechanism.
 * Users can claim tokens until the total token allocation runs out.
 */
contract FCFS_Airdrop {
    // Address of the token being distributed
    IERC20 public token;

    // Max tokens allocated for distribution
    uint256 public totalAllocation;

    // Tokens claimed so far
    uint256 public totalClaimed;

    // Amount of tokens each user is eligible to claim
    uint256 public claimAmount;

    // Mapping to track if an address has claimed tokens
    mapping(address => bool) public hasClaimed;

    // FCFS airdrop start and end timestamps
    uint256 public startTime;
    uint256 public endTime;

    // Address of the owner (admin)
    address public owner;

    // Events
    event TokensClaimed(address indexed user, uint256 amount);
    event EmergencyWithdrawal(address indexed owner, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier airdropActive() {
        require(
            block.timestamp >= startTime && block.timestamp <= endTime,
            "Airdrop is not active"
        );
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the ERC-20 token being distributed.
     * @param _totalAllocation Total tokens allocated for the airdrop.
     * @param _claimAmount Amount of tokens each user can claim.
     * @param _startTime Timestamp when the airdrop starts.
     * @param _endTime Timestamp when the airdrop ends.
     */
    constructor(
        IERC20 _token,
        uint256 _totalAllocation,
        uint256 _claimAmount,
        uint256 _startTime,
        uint256 _endTime
    ) {
        require(
            _startTime < _endTime,
            "Start time must be before end time"
        );
        require(
            _totalAllocation > 0 && _claimAmount > 0,
            "Allocation and claim amount must be greater than zero"
        );

        token = _token;
        totalAllocation = _totalAllocation;
        claimAmount = _claimAmount;
        startTime = _startTime;
        endTime = _endTime;
        owner = msg.sender;
    }

    /**
     * @dev Function for users to claim tokens.
     */
    function claimTokens() external airdropActive {
        require(
            !hasClaimed[msg.sender],
            "You have already claimed your tokens"
        );
        require(
            totalClaimed + claimAmount <= totalAllocation,
            "Not enough tokens left to claim"
        );

        hasClaimed[msg.sender] = true; // Mark the user as claimed
        totalClaimed += claimAmount; // Update the total claimed count

        // Transfer the tokens to the user
        require(
            token.transfer(msg.sender, claimAmount),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, claimAmount); // Emit event
    }

    /**
     * @dev Emergency withdrawal function for the owner to retrieve remaining tokens after the airdrop ends.
     */
    function emergencyWithdraw() external onlyOwner {
        require(
            block.timestamp > endTime,
            "Cannot withdraw tokens before airdrop ends"
        );

        uint256 remainingTokens = token.balanceOf(address(this));
        require(
            remainingTokens > 0,
            "No tokens left to withdraw"
        );

        // Transfer remaining tokens to the owner
        require(
            token.transfer(owner, remainingTokens),
            "Token transfer failed"
        );

        emit EmergencyWithdrawal(owner, remainingTokens); // Emit event
    }
}

// Interface for ERC-20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
