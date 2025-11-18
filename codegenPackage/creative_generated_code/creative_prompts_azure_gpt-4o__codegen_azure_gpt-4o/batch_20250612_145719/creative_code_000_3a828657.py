"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexus-mutual.xyz
Prompt: Write a smart contract on Ethereum that integrates with Nexus Mutual's API to automate the purchase of Smart Contract Cover when deploying new decentralized applications.
Generated: DETERMINISTIC_3a828657a2a95f83
Batch ID: 20250612_145719
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

// Importing OpenZeppelin's Ownable for access control
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for interacting with Nexus Mutual's API
interface INexusMutual {
    function buyCover(
        address smartContractAddress,
        uint256 coverAmount,
        uint256 coverPeriod,
        bytes calldata extraData
    ) external payable;
}

/**
 * @title NexusMutualCoverAutomator
 * @dev Automates purchasing of Nexus Mutual Smart Contract Cover when deploying new decentralized applications.
 */
contract NexusMutualCoverAutomator is Ownable {
    // Address of the Nexus Mutual API contract
    address public nexusMutualContract;

    // Event to log cover purchases
    event CoverPurchased(
        address indexed buyer,
        address indexed smartContract,
        uint256 coverAmount,
        uint256 coverPeriod
    );

    /**
     * @dev Constructor to set the Nexus Mutual contract address.
     * @param _nexusMutualContract Address of the Nexus Mutual API contract.
     */
    constructor(address _nexusMutualContract) {
        require(
            _nexusMutualContract != address(0),
            "Invalid Nexus Mutual contract address"
        );
        nexusMutualContract = _nexusMutualContract;
    }

    /**
     * @dev Function to update the Nexus Mutual contract address. Only callable by the owner.
     * @param _nexusMutualContract New Nexus Mutual contract address.
     */
    function setNexusMutualContract(address _nexusMutualContract)
        external
        onlyOwner
    {
        require(
            _nexusMutualContract != address(0),
            "Invalid Nexus Mutual contract address"
        );
        nexusMutualContract = _nexusMutualContract;
    }

    /**
     * @dev Automates the purchase of Nexus Mutual Smart Contract Cover.
     * @param smartContractAddress Address of the deployed smart contract to cover.
     * @param coverAmount Cover amount in wei (must be converted to ETH equivalent).
     * @param coverPeriod Period of the cover in days.
     * @param extraData Additional data if required by Nexus Mutual (optional).
     */
    function purchaseCover(
        address smartContractAddress,
        uint256 coverAmount,
        uint256 coverPeriod,
        bytes calldata extraData
    ) external payable {
        require(
            smartContractAddress != address(0),
            "Invalid smart contract address"
        );
        require(coverAmount > 0, "Cover amount must be greater than zero");
        require(coverPeriod > 0, "Cover period must be greater than zero");

        // Interfacing with the Nexus Mutual API to buy cover
        INexusMutual(nexusMutualContract).buyCover{value: msg.value}(
            smartContractAddress,
            coverAmount,
            coverPeriod,
            extraData
        );

        // Emit event for successful purchase
        emit CoverPurchased(
            msg.sender,
            smartContractAddress,
            coverAmount,
            coverPeriod
        );
    }

    /**
     * @dev Fallback function to handle any accidental sends of ETH to the contract.
     */
    receive() external payable {
        revert("ETH not accepted directly");
    }

    /**
     * @dev Withdraw any accidentally sent ETH to the contract. Only callable by the owner.
     */
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
