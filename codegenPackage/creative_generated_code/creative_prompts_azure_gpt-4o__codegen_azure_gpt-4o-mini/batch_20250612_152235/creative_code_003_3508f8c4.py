"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophpon.pages.dev
Prompt: Generate Solidity code for staking $BEAM tokens to qualify for a $SOPH airdrop, ensuring compliance with the staking terms described in the Sophon ecosystem.
Generated: DETERMINISTIC_3508f8c42dcbd2ec
Batch ID: 20250612_152235
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

// Import the ERC20 interface for interacting with $BEAM tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the Staking contract
contract BeamStaking is Ownable {
    // Declare state variables
    IERC20 public beamToken;  // The $BEAM token contract
    uint256 public totalStaked; // Total amount of $BEAM staked
    mapping(address => uint256) public stakedAmount; // Amount staked per user
    mapping(address => bool) public hasClaimedAirdrop; // Track airdrop claim status

    // Event declarations
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event AirdropClaimed(address indexed user, uint256 amount);

    // Constructor to set the $BEAM token address
    constructor(address _beamToken) {
        require(_beamToken != address(0), "Invalid token address");
        beamToken = IERC20(_beamToken);
    }

    // Function to stake $BEAM tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(beamToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staking details
        totalStaked += amount;
        stakedAmount[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $BEAM tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update staking details
        totalStaked -= amount;
        stakedAmount[msg.sender] -= amount;

        require(beamToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim $SOPH airdrop
    function claimAirdrop(uint256 airdropAmount) external {
        require(stakedAmount[msg.sender] > 0, "No staked tokens found");
        require(!hasClaimedAirdrop[msg.sender], "Airdrop already claimed");

        // Logic for airdrop distribution can be implemented here
        // For simplicity, we will just mark the airdrop as claimed

        hasClaimedAirdrop[msg.sender] = true;

        // Assuming airdrop amount is managed elsewhere, emit event
        emit AirdropClaimed(msg.sender, airdropAmount);
    }

    // Function to withdraw $BEAM tokens from the contract by owner (for emergencies)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= beamToken.balanceOf(address(this)), "Insufficient token balance");
        require(beamToken.transfer(msg.sender, amount), "Transfer failed");
    }

    // Function to get the staking balance of a user
    function getStakeBalance(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get the total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
