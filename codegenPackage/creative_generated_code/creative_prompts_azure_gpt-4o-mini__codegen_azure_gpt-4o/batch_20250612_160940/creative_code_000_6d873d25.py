"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeib57x2i3wjq47prbs73dicwjrqmh4z6xefonlbo3qd3bojsesqjra.ipfs.dweb.link
Prompt: How can I implement restaking of ETH using EigenLayer to provide cryptoeconomic security for new protocols?
Generated: DETERMINISTIC_6d873d25c89bb175
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s the code for implementing restaking of ETH using EigenLayer. The code provided assumes familiarity with Solidity and EigenLayer's APIs.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title ETH Restaking Contract using EigenLayer
 * @author [Your Name]
 * @notice This contract allows users to restake their ETH with EigenLayer to provide cryptoeconomic security for new protocols.
 * @dev Ensure you have the EigenLayer infrastructure deployed and accessible.
 */

interface IEigenLayer {
    function restake(address validator, uint256 amount) external;
    function withdrawStake(address validator, uint256 amount) external;
    function getStakedAmount(address validator) external view returns (uint256);
}

contract EthRestaking {
    // Address of the EigenLayer contract
    IEigenLayer public eigenLayer;

    // Mapping to track staked ETH by each user
    mapping(address => uint256) public userStakes;

    // Event to log restaking activities
    event ETHRestaked(address indexed user, uint256 amount);
    event ETHWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the EigenLayer contract address
     * @param _eigenLayer Address of the deployed EigenLayer contract
     */
    constructor(address _eigenLayer) {
        require(_eigenLayer != address(0), "Invalid EigenLayer contract address");
        eigenLayer = IEigenLayer(_eigenLayer);
    }

    /**
     * @notice Restake ETH on EigenLayer
     * @dev Users need to send ETH to this function. It will be deposited into EigenLayer.
     */
    function restakeETH() external payable {
        require(msg.value > 0, "Must send ETH to restake");

        // Record the user's staked amount
        userStakes[msg.sender] += msg.value;

        // Interact with EigenLayer to restake the ETH
        eigenLayer.restake(msg.sender, msg.value);

        emit ETHRestaked(msg.sender, msg.value);
    }

    /**
     * @notice Withdraw staked ETH from EigenLayer
     * @param amount The amount of ETH to withdraw
     */
    function withdrawStake(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(userStakes[msg.sender] >= amount, "Insufficient staked balance");

        // Reduce the user's staked balance
        userStakes[msg.sender] -= amount;

        // Interact with EigenLayer to withdraw the ETH
        eigenLayer.withdrawStake(msg.sender, amount);

        // Transfer the ETH back to the user
        (bool success,) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");

        emit ETHWithdrawn(msg.sender, amount);
    }

    /**
     * @notice Get the total staked ETH for a user
     * @param user Address of the user
     * @return The total staked ETH for the user
     */
    function getUserStakedAmount(address user) external view returns (uint256) {
        return userStakes[user];
    }

    /**
     * @notice Get the total staked ETH on EigenLayer for a validator
     * @param validator Address of the validator
     * @return The total staked ETH on EigenLayer for the validator
     */
    function getEigenLayerStakedAmount(address validator) external view returns (uint256) {
        return eigenLayer.getStakedAmount(validator);
    }

    /**
     * @dev Fallback function to prevent accidental ETH deposits
     */
    receive() external payable {
        revert("Direct ETH deposits are not allowed");
    }

    /**
     * @dev Fallback function to prevent accidental calls
     */
    fallback() external payable {
        revert("Invalid function call");
    }
}
```

Make sure to replace `[Your Name]` with your name and ensure compatibility with EigenLayer’s API by consulting its documentation and deployed contract addresses.
