"""
Generated Code Metadata:
========================
Original URL: https://stash-airdrop.vercel.app
Prompt: Generate a smart contract code snippet for a similar airdrop campaign, incorporating a time-sensitive claim mechanism like the one on the Stash Mega Airdrop page.
Generated: DETERMINISTIC_90a03046b9f195c2
Batch ID: 20250622_211141
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

/**
 * @title AirdropCampaign
 * @dev Smart contract for a time-sensitive token airdrop campaign.
 */
contract AirdropCampaign {
    // Address of the token to be airdropped
    IERC20 public token;

    // Owner of the contract
    address public owner;

    // Timestamp when the airdrop starts
    uint256 public startTime;

    // Timestamp when the airdrop ends
    uint256 public endTime;

    // Mapping to track claimed addresses
    mapping(address => bool) public hasClaimed;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Modifier to check if the airdrop is active
    modifier isAirdropActive() {
        require(block.timestamp >= startTime, "Airdrop has not started yet");
        require(block.timestamp <= endTime, "Airdrop has ended");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the token to be airdropped.
     * @param _startTime Timestamp when the airdrop starts.
     * @param _endTime Timestamp when the airdrop ends.
     */
    constructor(IERC20 _token, uint256 _startTime, uint256 _endTime) {
        require(_startTime < _endTime, "Start time must be before end time");
        token = _token;
        startTime = _startTime;
        endTime = _endTime;
        owner = msg.sender;
    }

    /**
     * @dev Function to claim airdrop tokens.
     * @param amount Amount of tokens to claim.
     */
    function claimTokens(uint256 amount) external isAirdropActive {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Mark the address as having claimed
        hasClaimed[msg.sender] = true;

        // Transfer tokens to the claimant
        token.transfer(msg.sender, amount);

        // Emit the claim event
        emit TokensClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw remaining tokens after the airdrop ends.
     */
    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp > endTime, "Airdrop is still active");

        uint256 remainingBalance = token.balanceOf(address(this));
        require(remainingBalance > 0, "No tokens to withdraw");

        token.transfer(owner, remainingBalance);
    }

    /**
     * @dev Function to update the airdrop time window.
     * @param _startTime New start time.
     * @param _endTime New end time.
     */
    function updateAirdropTime(uint256 _startTime, uint256 _endTime) external onlyOwner {
        require(_startTime < _endTime, "Start time must be before end time");
        require(block.timestamp < startTime, "Cannot update after airdrop has started");

        startTime = _startTime;
        endTime = _endTime;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
