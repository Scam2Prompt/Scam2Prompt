"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-minetrex.pages.dev
Prompt: Generate Solidity code for a smart contract that implements the "Stake-to-Mine" mechanism described on the Bitcoin Minetrix platform, where staking BTCMTX tokens generates non-tradable ERC-20 mining credits.
Generated: DETERMINISTIC_a62a8237ffc26dc9
Batch ID: 20250612_153648
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the mining credit token
interface IMiningCredit {
    function mint(address to, uint256 amount) external;
}

// StakeToMine contract implementing the stake-to-mine mechanism
contract StakeToMine is Ownable {
    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event CreditsMinted(address indexed user, uint256 amount);

    // Variables
    IERC20 public btcmtxToken; // BTCMTX token contract
    IMiningCredit public miningCreditToken; // Mining credit token contract

    // Mapping of user stakes
    mapping(address => uint256) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Constructor to initialize the contract with token addresses
    constructor(IERC20 _btcmtxToken, IMiningCredit _miningCreditToken) {
        btcmtxToken = _btcmtxToken;
        miningCreditToken = _miningCreditToken;
    }

    // Function to stake BTCMTX tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer BTCMTX tokens from user to contract
        require(btcmtxToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        
        // Update user stakes and total staked amount
        stakes[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake BTCMTX tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update user stakes and total staked amount
        stakes[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer BTCMTX tokens back to user
        require(btcmtxToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to mint mining credits proportional to staked amount
    function mintCredits() external {
        uint256 userStake = stakes[msg.sender];
        require(userStake > 0, "No stakes found for user");

        // Calculate mining credits based on user stakes and total staked
        uint256 creditsToMint = calculateCredits(userStake);
        require(creditsToMint > 0, "No credits to mint");

        // Mint the calculated credits to the user
        miningCreditToken.mint(msg.sender, creditsToMint);

        emit CreditsMinted(msg.sender, creditsToMint);
    }

    // Internal function to calculate mining credits based on staked amount
    function calculateCredits(uint256 userStake) internal view returns (uint256) {
        // Custom logic to determine credits based on staked amount
        // For demonstration, this could be a simple proportion
        return userStake * 10; // Example: 10 credits per staked token
    }
}
```
