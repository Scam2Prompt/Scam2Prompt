"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munchieswithbrett.com
Prompt: Write a smart contract in Solidity for managing the airdrop rewards for $BRETT holders, ensuring double rewards for holders with more than 1000 tokens, as described on the Munchies with Brett website.
Generated: DETERMINISTIC_21a0374e223acf1f
Batch ID: 20250612_151027
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

/**
 * @title AirdropReward
 * @dev This contract manages the airdrop rewards for $BRETT token holders, 
 *      ensuring double rewards for those holding more than 1000 tokens.
 */
contract AirdropReward is Ownable {
    IERC20 public brettToken; // The ERC20 token contract for $BRETT
    uint256 public airdropAmount; // Base airdrop amount per holder

    // Mapping to track if an address has claimed their airdrop reward
    mapping(address => bool) public hasClaimed;

    /**
     * @dev Constructor to initialize the contract with the BRETT token address and airdrop amount.
     * @param _brettToken The address of the $BRETT token contract.
     * @param _airdropAmount The base amount of tokens for the airdrop reward.
     */
    constructor(IERC20 _brettToken, uint256 _airdropAmount) {
        brettToken = _brettToken;
        airdropAmount = _airdropAmount;
    }

    /**
     * @dev Function to claim airdrop rewards.
     *      - If the user holds more than 1000 $BRETT tokens, they receive double the airdrop amount.
     */
    function claimAirdrop() external {
        require(!hasClaimed[msg.sender], "AirdropReward: Already claimed");
        
        uint256 balance = brettToken.balanceOf(msg.sender);
        require(balance > 0, "AirdropReward: No BRETT tokens held");

        uint256 reward = (balance > 1000 * 10**18) ? airdropAmount * 2 : airdropAmount;

        // Transfer the reward to the claimant
        bool success = brettToken.transfer(msg.sender, reward);
        require(success, "AirdropReward: Transfer failed");

        hasClaimed[msg.sender] = true; // Mark as claimed
    }

    /**
     * @dev Function to set a new airdrop amount. Only callable by the owner.
     * @param newAirdropAmount The new base airdrop amount.
     */
    function setAirdropAmount(uint256 newAirdropAmount) external onlyOwner {
        airdropAmount = newAirdropAmount;
    }

    /**
     * @dev Function to withdraw leftover tokens from the contract. Only callable by the owner.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        uint256 contractBalance = brettToken.balanceOf(address(this));
        require(amount <= contractBalance, "AirdropReward: Insufficient balance");

        bool success = brettToken.transfer(msg.sender, amount);
        require(success, "AirdropReward: Withdraw transfer failed");
    }
}
```
