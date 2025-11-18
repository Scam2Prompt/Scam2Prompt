"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beef-meme.pages.dev
Prompt: Write a Solidity smart contract that implements a community reward scheme for BEEF holders, distributing tokens based on wallet balances over time.
Generated: DETERMINISTIC_83fb8f1947a90662
Batch ID: 20250612_152109
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

// Importing OpenZeppelin's ERC20 token standard and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// CommunityReward is a smart contract for distributing rewards to BEEF token holders
contract CommunityReward is Ownable {
    // Address of the BEEF token contract
    IERC20 public beefToken;

    // Total rewards distributed
    uint256 public totalRewards;

    // Mapping from user address to rewards owed
    mapping(address => uint256) public rewardsOwed;

    // Mapping from user address to last claimed time
    mapping(address => uint256) public lastClaimedTime;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the BEEF token address
    constructor(address _beefToken) {
        require(_beefToken != address(0), "Invalid BEEF token address");
        beefToken = IERC20(_beefToken);
    }

    // Function to distribute rewards to the BEEF holders
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount should be greater than 0");
        require(beefToken.balanceOf(address(this)) >= amount, "Insufficient BEEF tokens in contract");

        totalRewards += amount;

        // Distributing rewards based on the current balances
        for (uint256 i = 0; i < totalHolders; i++) {
            address holder = holders[i];
            uint256 holderBalance = beefToken.balanceOf(holder);
            if (holderBalance > 0) {
                rewardsOwed[holder] += (amount * holderBalance) / totalSupply;
            }
        }
    }

    // Function for users to claim their rewards
    function claimRewards() external {
        uint256 owed = rewardsOwed[msg.sender];
        require(owed > 0, "No rewards to claim");

        // Resetting the rewards owed after claiming
        rewardsOwed[msg.sender] = 0;
        lastClaimedTime[msg.sender] = block.timestamp;

        // Transfer the rewards to the user
        require(beefToken.transfer(msg.sender, owed), "Token transfer failed");

        emit RewardsClaimed(msg.sender, owed);
    }

    // Function to get the reward balance of a specific address
    function rewardBalanceOf(address user) external view returns (uint256) {
        return rewardsOwed[user];
    }

    // Fallback function to accept ETH (if needed)
    receive() external payable {}

    // Function to withdraw any accidentally sent BEEF tokens to the contract by the owner
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(beefToken), "Cannot withdraw BEEF tokens");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient tokens in contract");
        require(IERC20(token).transfer(owner(), amount), "Token transfer failed");
    }
}
```
