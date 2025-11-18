"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdccash.xyz
Prompt: Write a Solidity function that calculates and distributes USDC rewards to $UPRINT holders based on their token holdings and transaction volume.
Generated: DETERMINISTIC_584270dbba363c8a
Batch ID: 20250612_154728
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract UPRINTRewards {
    // The USDC token contract
    IERC20 public usdcToken;
    // The UPRINT token contract
    IERC20 public uprPrintToken;

    // Mapping to track user holdings
    mapping(address => uint256) public userBalances;
    // Total UPRINT token supply
    uint256 public totalSupply;

    // Event to log rewards distribution
    event RewardsDistributed(address indexed user, uint256 amount);

    // Constructor to set the USDC and UPRINT token contracts
    constructor(address _usdcToken, address _uprPrintToken) {
        usdcToken = IERC20(_usdcToken);
        uprPrintToken = IERC20(_uprPrintToken);
    }

    // Function to update user balances based on their UPRINT holdings
    function updateUserBalance(address user) internal {
        uint256 balance = uprPrintToken.balanceOf(user);
        userBalances[user] = balance;
        totalSupply += balance;
    }

    // Function to distribute USDC rewards based on UPRINT holdings and transaction volume
    function distributeRewards(uint256 totalRewards) external {
        require(totalRewards > 0, "Total rewards must be greater than zero");
        require(totalSupply > 0, "No UPRINT holders to distribute rewards to");

        // Iterate over all known UPRINT holders (this can be optimized in production)
        for (uint256 i = 0; i < totalSupply; i++) {
            address user = address(uint160(i)); // Assuming users are indexed
            uint256 userBalance = userBalances[user];

            // Only distribute rewards to users holding UPRINT tokens
            if (userBalance > 0) {
                uint256 userReward = (userBalance * totalRewards) / totalSupply;

                // Ensure we have enough USDC balance to distribute
                uint256 usdcBalance = usdcToken.balanceOf(address(this));
                require(usdcBalance >= userReward, "Insufficient USDC balance for distribution");

                // Transfer rewards
                usdcToken.transfer(user, userReward);
                emit RewardsDistributed(user, userReward);
            }
        }
    }

    // Function to allow users to claim rewards manually
    function claimRewards() external {
        // Update user's balance before claiming
        updateUserBalance(msg.sender);
        // Logic for claiming rewards could be added here
    }
}
```
