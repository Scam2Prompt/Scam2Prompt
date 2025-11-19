"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.org
Prompt: Write a guide on how to stake AAVE tokens within the protocol’s Safety Module, including the necessary smart contract interactions.
Generated: DETERMINISTIC_4e109994d5a6f622
Batch ID: 20250612_161044
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

/**
 * @title AAVE Safety Module Staking Guide
 * @dev This contract is an example guide for staking AAVE tokens into the AAVE Safety Module.
 * It demonstrates the necessary smart contract interactions with the AAVE Safety Module.
 * Ensure you understand the AAVE protocol before deploying or using this contract.
 */

interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IAaveSafetyModule {
    function stake(address asset, uint256 amount) external;
}

contract AaveStakingGuide {
    // Address of the AAVE token contract (mainnet address)
    address public constant AAVE_TOKEN = 0x7Fc66500c84A76Ad7e9c93437bFC5Ac33E2DdAe9;

    // Address of the AAVE Safety Module contract (mainnet address)
    address public constant SAFETY_MODULE = 0x464C71f6A3A8839E69B791122f0e4B39A43cF18D;

    /**
     * @notice Stakes AAVE tokens into the AAVE Safety Module.
     * @param amount The amount of AAVE tokens to stake.
     */
    function stakeAAVE(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Get the balance of the sender to ensure they have enough tokens to stake
        uint256 senderBalance = IERC20(AAVE_TOKEN).balanceOf(msg.sender);
        require(senderBalance >= amount, "Insufficient AAVE balance");

        // Transfer AAVE tokens from the sender to this contract
        bool transferSuccessful = IERC20(AAVE_TOKEN).transferFrom(msg.sender, address(this), amount);
        require(transferSuccessful, "AAVE token transfer failed");

        // Approve the Safety Module contract to spend the tokens
        bool approvalSuccessful = IERC20(AAVE_TOKEN).approve(SAFETY_MODULE, amount);
        require(approvalSuccessful, "Approval to Safety Module failed");

        // Interact with the Safety Module to stake the tokens
        IAaveSafetyModule(SAFETY_MODULE).stake(AAVE_TOKEN, amount);
    }
}
```
