"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitrader-site-7y6inq1vk-edrive.vercel.app
Prompt: Write a Solidity smart contract to automate token claiming and referral rewards, including 10% $AIT and 10% BNB rewards for referrals, as described in AI Trader's airdrop process.
Generated: DETERMINISTIC_848c023bed490845
Batch ID: 20250612_152620
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

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract AITraderAirdrop {
    // Address of the $AIT token contract
    IERC20 public aitToken;
    // Address of the contract owner
    address public owner;

    // Mapping to track claimed tokens
    mapping(address => bool) public hasClaimed;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed user, uint256 aitAmount, uint256 bnbAmount, address indexed referrer);

    // Modifier to restrict certain functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _aitTokenAddress) {
        aitToken = IERC20(_aitTokenAddress);
        owner = msg.sender;
    }

    // Function to claim tokens and referral rewards
    function claimAirdrop(address referrer) external payable {
        require(!hasClaimed[msg.sender], "You have already claimed your tokens");
        require(msg.value > 0, "You must send BNB to claim the airdrop");

        // Define reward amounts
        uint256 aitReward = 10 * 10**18; // 10 $AIT tokens
        uint256 bnbReward = (msg.value * 10) / 100; // 10% of sent BNB

        // Ensure the contract has enough $AIT tokens for the reward
        require(aitToken.balanceOf(address(this)) >= aitReward, "Insufficient $AIT token balance in contract");

        // Update state to mark the user as having claimed
        hasClaimed[msg.sender] = true;

        // Transfer $AIT tokens to the user
        require(aitToken.transfer(msg.sender, aitReward), "Failed to transfer $AIT tokens");

        // Send 10% BNB reward to the referrer
        if (referrer != address(0) && referrer != msg.sender) {
            payable(referrer).transfer(bnbReward);
        }

        // Emit event for tracking
        emit TokensClaimed(msg.sender, aitReward, bnbReward, referrer);
    }

    // Function to withdraw $AIT tokens from the contract (owner only)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(aitToken.balanceOf(address(this)) >= amount, "Insufficient $AIT token balance");
        require(aitToken.transfer(owner, amount), "Failed to transfer tokens");
    }

    // Function to withdraw BNB from the contract (owner only)
    function withdrawBNB(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient BNB balance");
        payable(owner).transfer(amount);
    }

    // Fallback function to accept BNB deposits
    receive() external payable {}

    // Function to change the $AIT token address (owner only)
    function setAITTokenAddress(address newTokenAddress) external onlyOwner {
        aitToken = IERC20(newTokenAddress);
    }
}
```
