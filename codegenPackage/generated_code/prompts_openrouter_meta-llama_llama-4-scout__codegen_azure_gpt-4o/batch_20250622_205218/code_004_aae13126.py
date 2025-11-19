"""
Generated Code Metadata:
========================
Original URL: https://wormhole.ghost.io
Prompt: "Design a use case for Wormhole's W token in a decentralized identity protocol, such as Worldcoin's World ID."
Generated: DETERMINISTIC_aae13126319e5257
Batch ID: 20250622_205218
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

/**
 * @title Decentralized Identity Protocol with Wormhole's W Token Integration
 * @dev This contract demonstrates a use case for Wormhole's W token in a decentralized identity protocol.
 * Users can verify their identity using Worldcoin's World ID and stake W tokens to access premium features.
 */

interface IWormholeToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IWorldID {
    function verifyIdentity(address user, bytes32 proof) external view returns (bool);
}

contract DecentralizedIdentityProtocol {
    // Address of the Wormhole W token contract
    IWormholeToken public wormholeToken;

    // Address of the World ID contract
    IWorldID public worldID;

    // Mapping to store user identity verification status
    mapping(address => bool) public isVerified;

    // Mapping to store user staked W token balances
    mapping(address => uint256) public stakedTokens;

    // Event emitted when a user verifies their identity
    event IdentityVerified(address indexed user);

    // Event emitted when a user stakes W tokens
    event TokensStaked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws staked W tokens
    event TokensWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with Wormhole and World ID addresses.
     * @param _wormholeToken Address of the Wormhole W token contract.
     * @param _worldID Address of the World ID contract.
     */
    constructor(address _wormholeToken, address _worldID) {
        require(_wormholeToken != address(0), "Invalid Wormhole token address");
        require(_worldID != address(0), "Invalid World ID address");

        wormholeToken = IWormholeToken(_wormholeToken);
        worldID = IWorldID(_worldID);
    }

    /**
     * @dev Function to verify user identity using World ID.
     * @param proof The cryptographic proof provided by World ID.
     */
    function verifyIdentity(bytes32 proof) external {
        require(!isVerified[msg.sender], "User already verified");

        // Verify identity using World ID
        bool verified = worldID.verifyIdentity(msg.sender, proof);
        require(verified, "Identity verification failed");

        // Mark user as verified
        isVerified[msg.sender] = true;

        emit IdentityVerified(msg.sender);
    }

    /**
     * @dev Function to stake W tokens for premium features.
     * @param amount The amount of W tokens to stake.
     */
    function stakeTokens(uint256 amount) external {
        require(isVerified[msg.sender], "User must be verified to stake tokens");
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer W tokens from the user to the contract
        bool success = wormholeToken.transfer(address(this), amount);
        require(success, "Token transfer failed");

        // Update staked token balance
        stakedTokens[msg.sender] += amount;

        emit TokensStaked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked W tokens.
     * @param amount The amount of W tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external {
        require(stakedTokens[msg.sender] >= amount, "Insufficient staked balance");
        require(amount > 0, "Withdraw amount must be greater than zero");

        // Update staked token balance
        stakedTokens[msg.sender] -= amount;

        // Transfer W tokens back to the user
        bool success = wormholeToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to check the staked balance of a user.
     * @param user The address of the user.
     * @return The staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedTokens[user];
    }
}
```
