"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dexwin.top
Prompt: Generate a smart contract snippet for verifying wallet connections and distributing rewards, inspired by the reward claim process on the "REWARD Portal v2."
Generated: DETERMINISTIC_7cd835c3ab2b36e3
Batch ID: 20250612_153832
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract RewardDistribution is Ownable {
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Mapping to track if an address has connected their wallet
    mapping(address => bool) public hasWalletConnected;

    // Mapping to store user rewards
    mapping(address => uint256) private userRewards;

    // ERC20 token used for rewards
    IERC20 public rewardToken;

    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    /**
     * @dev Connects the user's wallet for rewards
     * @param user The address of the user whose wallet is being connected
     */
    function connectWallet(address user) external {
        require(!hasWalletConnected[user], "Wallet already connected.");
        hasWalletConnected[user] = true;
    }

    /**
     * @dev Allows the owner to distribute rewards to users
     * @param recipients Array of recipient addresses
     * @param amounts Array of reward amounts corresponding to each recipient
     */
    function distributeRewards(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Mismatched input lengths");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(hasWalletConnected[recipients[i]], "Wallet not connected.");
            userRewards[recipients[i]] += amounts[i];
        }
    }

    /**
     * @dev Allows users to claim their accumulated rewards
     */
    function claimRewards() external {
        uint256 amount = userRewards[msg.sender];
        require(amount > 0, "No rewards to claim.");

        userRewards[msg.sender] = 0; // Reset rewards to prevent re-entrancy
        require(rewardToken.transfer(msg.sender, amount), "Transfer failed.");

        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to withdraw any ERC20 tokens from the contract
     * @param token The address of the ERC20 token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(msg.sender, amount), "Withdrawal failed.");
    }
}
```
