"""
Generated Code Metadata:
========================
Original URL: https://earnm-io.web.app
Prompt: "Generate a smart contract code for distributing $EARNM coins and Mystery Boxes to users based on their online activities, using a vesting and distribution mechanism."
Generated: DETERMINISTIC_06b0fde8d5b89321
Batch ID: 20250622_212723
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Mystery Box contract
interface IMysteryBox {
    function mint(address to) external;
}

// Smart contract for distributing $EARNM tokens and Mystery Boxes
contract EarnMDistributor is Ownable {
    using SafeMath for uint256;

    // ERC20 token for $EARNM
    ERC20 public earnMToken;
    IMysteryBox public mysteryBoxContract;

    // Struct to hold user distribution data
    struct UserDistribution {
        uint256 totalEarnM;
        uint256 claimedEarnM;
        uint256 vestingStart;
        uint256 vestingDuration;
    }

    // Mapping of user addresses to their distribution data
    mapping(address => UserDistribution) public userDistributions;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed user, uint256 amount);
    event MysteryBoxMinted(address indexed user);

    // Constructor to initialize the contract with the token and mystery box contract addresses
    constructor(address _earnMToken, address _mysteryBoxContract) {
        earnMToken = ERC20(_earnMToken);
        mysteryBoxContract = IMysteryBox(_mysteryBoxContract);
    }

    // Function to distribute tokens and mint mystery boxes based on user activity
    function distributeTokens(address user, uint256 amount, uint256 vestingDuration) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than zero");
        require(vestingDuration > 0, "Vesting duration must be greater than zero");

        // Update user distribution data
        userDistributions[user].totalEarnM = userDistributions[user].totalEarnM.add(amount);
        userDistributions[user].vestingStart = block.timestamp;
        userDistributions[user].vestingDuration = vestingDuration;

        // Transfer tokens to the contract
        require(earnMToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit TokensDistributed(user, amount);
    }

    // Function to claim vested tokens
    function claimTokens() external {
        UserDistribution storage userDist = userDistributions[msg.sender];

        // Calculate the amount of tokens that can be claimed
        uint256 vestedAmount = calculateVestedAmount(msg.sender);
        require(vestedAmount > 0, "No tokens available for claim");

        // Update claimed amount
        userDist.claimedEarnM = userDist.claimedEarnM.add(vestedAmount);

        // Transfer tokens to the user
        require(earnMToken.transfer(msg.sender, vestedAmount), "Token transfer failed");
    }

    // Function to calculate the vested amount for a user
    function calculateVestedAmount(address user) public view returns (uint256) {
        UserDistribution storage userDist = userDistributions[user];

        // Check if the vesting period has started
        if (block.timestamp < userDist.vestingStart) {
            return 0;
        }

        // Calculate the elapsed time
        uint256 elapsedTime = block.timestamp.sub(userDist.vestingStart);
        uint256 totalVestingAmount = userDist.totalEarnM;
        uint256 vestedAmount = totalVestingAmount.mul(elapsedTime).div(userDist.vestingDuration);

        // Ensure the user does not claim more than they are entitled to
        return vestedAmount.sub(userDist.claimedEarnM);
    }

    // Function to mint a mystery box for a user
    function mintMysteryBox() external {
        require(userDistributions[msg.sender].totalEarnM > 0, "No tokens distributed to user");

        // Mint a mystery box for the user
        mysteryBoxContract.mint(msg.sender);
        emit MysteryBoxMinted(msg.sender);
    }

    // Function to withdraw remaining tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(earnMToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        require(earnMToken.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
