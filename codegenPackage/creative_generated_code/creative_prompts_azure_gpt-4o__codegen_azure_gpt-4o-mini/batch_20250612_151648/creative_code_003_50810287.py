"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoiinminetrix.pages.dev
Prompt: Create a smart contract in Solidity that burns mining credits (non-transferable ERC-20 tokens) in exchange for cloud mining power, as described in the Bitcoin Minetrix platform.
Generated: DETERMINISTIC_50810287a2b52ffc
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CloudMiningPower
 * @dev A smart contract for burning mining credits to acquire cloud mining power.
 */
contract CloudMiningPower is Ownable {
    // Event emitted when mining credits are burned
    event CreditsBurned(address indexed user, uint256 amount, uint256 powerGranted);
    
    // Token used for mining credits
    IERC20 public miningCreditsToken;
    
    // Mapping to track user cloud mining power
    mapping(address => uint256) private cloudMiningPower;

    // Conversion rate from mining credits to cloud mining power
    uint256 public creditsToPowerRate;

    /**
     * @dev Constructor to initialize the contract with the mining credits token and conversion rate.
     * @param _miningCreditsToken Address of the ERC-20 token used as mining credits.
     * @param _creditsToPowerRate Rate at which mining credits are converted to cloud mining power.
     */
    constructor(IERC20 _miningCreditsToken, uint256 _creditsToPowerRate) {
        miningCreditsToken = _miningCreditsToken;
        creditsToPowerRate = _creditsToPowerRate;
    }

    /**
     * @dev Burns the specified amount of mining credits in exchange for cloud mining power.
     * @param amount The amount of mining credits to burn.
     */
    function burnCredits(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer mining credits from user to the contract and burn them
        require(miningCreditsToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Burn the transferred tokens (not implemented here, assuming the token has a burn mechanism)
        // This should call the burn function of the miningCreditsToken if it supports it.
        
        // Calculate the power granted
        uint256 powerGranted = amount * creditsToPowerRate;

        // Update the user's cloud mining power
        cloudMiningPower[msg.sender] += powerGranted;

        // Emit an event for logging
        emit CreditsBurned(msg.sender, amount, powerGranted);
    }

    /**
     * @dev Retrieves the cloud mining power of a user.
     * @param user The address of the user.
     * @return The amount of cloud mining power the user has.
     */
    function getCloudMiningPower(address user) external view returns (uint256) {
        return cloudMiningPower[user];
    }

    /**
     * @dev Allows the contract owner to update the conversion rate for mining credits to cloud mining power.
     * @param newRate The new conversion rate.
     */
    function updateConversionRate(uint256 newRate) external onlyOwner {
        creditsToPowerRate = newRate;
    }

    /**
     * @dev Allows the contract to reclaim any tokens sent to it by mistake.
     * @param token The address of the token to reclaim.
     * @param amount The amount of tokens to reclaim.
     */
    function reclaimTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
