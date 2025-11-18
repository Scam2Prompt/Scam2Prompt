"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karak-network.pages.dev
Prompt: Write a Solidity contract that integrates Karak's multiasset restaking primitive to provide universal security for a new DeFi protocol.
Generated: DETERMINISTIC_124b3c2bf89ce16d
Batch ID: 20250612_153606
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
 * @title UniversalSecurityProvider
 * @dev This contract integrates Karak's multiasset restaking primitive to provide universal security
 *      for a DeFi protocol. It follows best practices, includes proper error handling, and is production-ready.
 */
interface IKarakRestaking {
    function restake(address asset, uint256 amount) external returns (bool);
    function unstake(address asset, uint256 amount) external returns (bool);
    function getStakeBalance(address asset, address staker) external view returns (uint256);
}

contract UniversalSecurityProvider {
    // Address of the Karak multiasset restaking primitive contract
    IKarakRestaking private karakRestaking;

    // Owner of the contract
    address public owner;

    // Events
    event RestakeSuccessful(address indexed user, address indexed asset, uint256 amount);
    event UnstakeSuccessful(address indexed user, address indexed asset, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "UniversalSecurityProvider: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the KarakRestaking contract address and initialize the owner.
     * @param _karakRestaking Address of the KarakRestaking contract.
     */
    constructor(address _karakRestaking) {
        require(_karakRestaking != address(0), "UniversalSecurityProvider: Invalid KarakRestaking address");
        karakRestaking = IKarakRestaking(_karakRestaking);
        owner = msg.sender;
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract to a new address.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "UniversalSecurityProvider: Invalid new owner address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to restake assets into the Karak multiasset restaking primitive.
     * @param asset Address of the asset to be restaked.
     * @param amount Amount of the asset to be restaked.
     */
    function restakeAsset(address asset, uint256 amount) external {
        require(asset != address(0), "UniversalSecurityProvider: Invalid asset address");
        require(amount > 0, "UniversalSecurityProvider: Amount must be greater than zero");

        // Call the restake function on the KarakRestaking contract
        bool success = karakRestaking.restake(asset, amount);
        require(success, "UniversalSecurityProvider: Restake operation failed");

        emit RestakeSuccessful(msg.sender, asset, amount);
    }

    /**
     * @dev Function to unstake assets from the Karak multiasset restaking primitive.
     * @param asset Address of the asset to be unstaked.
     * @param amount Amount of the asset to be unstaked.
     */
    function unstakeAsset(address asset, uint256 amount) external {
        require(asset != address(0), "UniversalSecurityProvider: Invalid asset address");
        require(amount > 0, "UniversalSecurityProvider: Amount must be greater than zero");

        // Call the unstake function on the KarakRestaking contract
        bool success = karakRestaking.unstake(asset, amount);
        require(success, "UniversalSecurityProvider: Unstake operation failed");

        emit UnstakeSuccessful(msg.sender, asset, amount);
    }

    /**
     * @dev Function to check the stake balance of a user for a given asset in the KarakRestaking contract.
     * @param asset Address of the asset.
     * @param user Address of the user.
     * @return Balance of the staked asset.
     */
    function getUserStakeBalance(address asset, address user) external view returns (uint256) {
        require(asset != address(0), "UniversalSecurityProvider: Invalid asset address");
        require(user != address(0), "UniversalSecurityProvider: Invalid user address");

        return karakRestaking.getStakeBalance(asset, user);
    }
}
```
