"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Develop a smart contract that integrates with Instadapp Lite to execute cross-protocol refinancing strategies, leveraging protocols like AAVE and Compound.
Generated: DETERMINISTIC_c8cfd0e6c5f834d7
Batch ID: 20250612_145208
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
 * @title CrossProtocolRefinancing
 * @notice This smart contract integrates with Instadapp Lite to execute cross-protocol refinancing strategies
 * @dev The contract interacts with AAVE and Compound protocols via Instadapp Lite for lending and borrowing operations.
 */
contract CrossProtocolRefinancing {
    address public owner;

    // Instadapp Lite addresses
    address public instadappLiteAddress;

    constructor(address _instadappLiteAddress) {
        require(_instadappLiteAddress != address(0), "Invalid Instadapp Lite address");
        instadappLiteAddress = _instadappLiteAddress;
        owner = msg.sender;
    }

    // Modifier to restrict access to the owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @notice Execute refinancing strategy between AAVE and Compound
     * @param collateralAsset The asset used as collateral (e.g., USDC)
     * @param debtAsset The asset borrowed (e.g., DAI)
     * @param amount The amount to refinance
     * @param targetProtocol The target protocol for refinancing (e.g., "AAVE" or "Compound")
     */
    function executeRefinancing(
        address collateralAsset,
        address debtAsset,
        uint256 amount,
        string memory targetProtocol
    ) external onlyOwner {
        require(collateralAsset != address(0), "Invalid collateral asset");
        require(debtAsset != address(0), "Invalid debt asset");
        require(amount > 0, "Invalid amount");
        require(
            keccak256(abi.encodePacked(targetProtocol)) == keccak256("AAVE") ||
            keccak256(abi.encodePacked(targetProtocol)) == keccak256("Compound"),
            "Unsupported target protocol"
        );

        // Call to Instadapp Lite for refinancing operations
        // Instadapp Lite combines protocols internally for these types of operations
        try IInstadappLite(instadappLiteAddress).refinance(
            collateralAsset,
            debtAsset,
            amount,
            targetProtocol
        ) {
            // Refinancing was successfully initiated
            emit RefinancingExecuted(collateralAsset, debtAsset, amount, targetProtocol);
        } catch (bytes memory error) {
            // Handle errors during refinancing
            emit RefinancingFailed(error);
        }
    }

    /**
     * @notice Update the Instadapp Lite address
     * @param _instadappLiteAddress The new Instadapp Lite address
     */
    function updateInstadappLiteAddress(address _instadappLiteAddress) external onlyOwner {
        require(_instadappLiteAddress != address(0), "Invalid Instadapp Lite address");
        instadappLiteAddress = _instadappLiteAddress;
        emit InstadappLiteAddressUpdated(_instadappLiteAddress);
    }

    /**
     * @notice Transfer ownership of the contract
     * @param newOwner The new owner of the contract
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner");
        owner = newOwner;
        emit OwnershipTransferred(newOwner);
    }

    /**
     * @dev Events to notify external systems of contract activities
     */
    event RefinancingExecuted(address collateralAsset, address debtAsset, uint256 amount, string targetProtocol);
    event RefinancingFailed(bytes error);
    event InstadappLiteAddressUpdated(address newAddress);
    event OwnershipTransferred(address newOwner);
}

/**
 * @title IInstadappLite
 * @dev Interface for Instadapp Lite contract
 */
interface IInstadappLite {
    function refinance(
        address collateralAsset,
        address debtAsset,
        uint256 amount,
        string calldata targetProtocol
    ) external;
}
```
