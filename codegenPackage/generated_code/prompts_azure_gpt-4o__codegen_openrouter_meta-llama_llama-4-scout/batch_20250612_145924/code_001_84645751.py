"""
Generated Code Metadata:
========================
Original URL: https://app-basemafia-com.pages.dev
Prompt: Generate code to implement a buy-back-and-burn mechanism for $MAFIA tokens, ensuring half of the tokens are added to a rewards pool and the other half are burned.
Generated: DETERMINISTIC_84645751aad3a44f
Batch ID: 20250612_145924
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MafiaTokenBuyBackAndBurn
 * @author [Your Name]
 * @notice Contract for implementing buy-back-and-burn mechanism for $MAFIA tokens.
 */
contract MafiaTokenBuyBackAndBurn is ReentrancyGuard {
    // Mapping of rewards pool
    mapping (address => uint256) public rewardsPool;

    // Address of $MAFIA token
    address public immutable mafiaTokenAddress;

    // Address of rewards pool recipient
    address public immutable rewardsPoolRecipient;

    /**
     * @param _mafiaTokenAddress Address of $MAFIA token
     * @param _rewardsPoolRecipient Address of rewards pool recipient
     */
    constructor(address _mafiaTokenAddress, address _rewardsPoolRecipient) {
        require(_mafiaTokenAddress != address(0), "MafiaTokenBuyBackAndBurn: Mafia token address cannot be zero");
        require(_rewardsPoolRecipient != address(0), "MafiaTokenBuyBackAndBurn: Rewards pool recipient address cannot be zero");

        mafiaTokenAddress = _mafiaTokenAddress;
        rewardsPoolRecipient = _rewardsPoolRecipient;
    }

    /**
     * @notice Function to buy-back-and-burn $MAFIA tokens
     * @param _amount Amount of $MAFIA tokens to buy-back-and-burn
     */
    function buyBackAndBurn(uint256 _amount) external nonReentrant {
        // Check if amount is valid
        require(_amount > 0, "MafiaTokenBuyBackAndBurn: Amount must be greater than zero");

        // Transfer $MAFIA tokens to contract
        ERC20(mafiaTokenAddress).transferFrom(msg.sender, address(this), _amount);

        // Calculate rewards pool amount and burn amount
        uint256 rewardsPoolAmount = _amount / 2;
        uint256 burnAmount = _amount - rewardsPoolAmount;

        // Add to rewards pool
        rewardsPool[rewardsPoolRecipient] += rewardsPoolAmount;

        // Burn $MAFIA tokens
        ERC20Burnable(mafiaTokenAddress).burn(burnAmount);
    }

    /**
     * @notice Function to withdraw rewards pool
     */
    function withdrawRewardsPool() external {
        require(rewardsPool[msg.sender] > 0, "MafiaTokenBuyBackAndBurn: Rewards pool balance is zero");

        uint256 rewardsPoolBalance = rewardsPool[msg.sender];
        rewardsPool[msg.sender] = 0;

        // Transfer $MAFIA tokens to recipient
        ERC20(mafiaTokenAddress).transfer(msg.sender, rewardsPoolBalance);
    }
}
```
