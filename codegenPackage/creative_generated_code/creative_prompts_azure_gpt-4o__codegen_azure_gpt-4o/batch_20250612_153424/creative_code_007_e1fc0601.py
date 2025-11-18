"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://benq-i.fi
Prompt: Generate a smart contract example for interacting with BENQI's Liquid Staking protocol to earn QI tokens.
Generated: DETERMINISTIC_e1fc06015fd4ae34
Batch ID: 20250612_153424
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
 * @title BENQI Liquid Staking Interaction Contract
 * @author [Your Name]
 * @notice This contract interacts with BENQI's Liquid Staking protocol to stake AVAX and earn QI tokens.
 * @dev Ensure BENQI's Liquid Staking contract address is up-to-date for production deployment.
 */
contract BENQILiquidStaking {
    // Address of BENQI Liquid Staking contract (replace with actual deployed address)
    address public constant BENQI_LIQUID_STAKING_ADDRESS = 0xXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX;

    // ABI interface for BENQI Liquid Staking contract
    interface ILiquidStaking {
        function stake() external payable;
        function unstake(uint256 amount) external;
        function claimRewards() external;
    }

    /**
     * @notice Stakes AVAX into BENQI's Liquid Staking contract.
     * @dev Ensure the contract has enough AVAX before calling this function.
     */
    function stakeAVAX() external payable {
        require(msg.value > 0, "You must send AVAX to stake.");
        
        // Interfacing with BENQI Liquid Staking contract
        ILiquidStaking(BENQI_LIQUID_STAKING_ADDRESS).stake{value: msg.value}();
    }

    /**
     * @notice Unstakes AVAX from BENQI's Liquid Staking contract.
     * @param amount The amount of AVAX to unstake.
     */
    function unstakeAVAX(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero.");
        
        // Interfacing with BENQI Liquid Staking contract
        ILiquidStaking(BENQI_LIQUID_STAKING_ADDRESS).unstake(amount);
    }

    /**
     * @notice Claims QI token rewards from BENQI's Liquid Staking contract.
     */
    function claimQIRewards() external {
        // Interfacing with BENQI Liquid Staking contract
        ILiquidStaking(BENQI_LIQUID_STAKING_ADDRESS).claimRewards();
    }

    /**
     * @notice Fallback function to accept AVAX deposits.
     */
    receive() external payable {
        // Accept AVAX deposits
    }

    /**
     * @notice Withdraws accidentally sent AVAX from the contract.
     * @dev Only owner should be able to call this in a production contract.
     */
    function withdrawAVAX() external {
        // Replace with appropriate access control mechanism
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
