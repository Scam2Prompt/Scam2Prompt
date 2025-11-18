"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-en.web.app
Prompt: Generate Solidity code for a smart contract that implements the "Stake-to-Mine" mechanism, where users stake BTCMTX tokens to earn non-transferable mining credits that can be burned for Bitcoin cloud mining power.
Generated: DETERMINISTIC_1c186e1408c93e4e
Batch ID: 20250612_151648
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

// Importing the ERC20 interface to interact with the BTCMTX token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract StakeToMine {
    // State variables
    IERC20 public btcmtxToken; // The BTCMTX token contract
    mapping(address => uint256) public stakedAmount; // User's staked amount
    mapping(address => uint256) public miningCredits; // Non-transferable mining credits
    uint256 public totalStaked; // Total amount of BTCMTX staked
    uint256 public creditsPerToken = 100; // Mining credits earned per BTCMTX staked

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event CreditsBurned(address indexed user, uint256 credits);

    // Modifier to check if user has enough staked amount
    modifier hasStaked(address user) {
        require(stakedAmount[user] > 0, "No tokens staked");
        _;
    }

    // Constructor to set the BTCMTX token contract address
    constructor(address _btcmtxToken) {
        require(_btcmtxToken != address(0), "Invalid token address");
        btcmtxToken = IERC20(_btcmtxToken);
    }

    // Function to stake BTCMTX tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        // Transfer BTCMTX tokens from user to this contract
        btcmtxToken.transferFrom(msg.sender, address(this), amount);

        // Update user's staked amount and total staked
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        // Calculate and assign mining credits
        miningCredits[msg.sender] += amount * creditsPerToken;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake BTCMTX tokens
    function unstake(uint256 amount) external hasStaked(msg.sender) {
        require(amount > 0 && amount <= stakedAmount[msg.sender], "Invalid unstake amount");

        // Update user's staked amount and total staked
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer BTCMTX tokens back to the user
        btcmtxToken.transfer(msg.sender, amount);

        // Deduct mining credits to account for unstaking
        miningCredits[msg.sender] -= amount * creditsPerToken;

        emit Unstaked(msg.sender, amount);
    }

    // Function to burn mining credits for cloud mining power
    function burnCredits(uint256 credits) external hasStaked(msg.sender) {
        require(credits > 0 && credits <= miningCredits[msg.sender], "Invalid burn amount");
        
        // Deduct credits from the user
        miningCredits[msg.sender] -= credits;

        // Emit event for burned credits
        emit CreditsBurned(msg.sender, credits);
    }

    // Function to check user's mining credits
    function getMiningCredits(address user) external view returns (uint256) {
        return miningCredits[user];
    }

    // Function to check user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }
}
```
