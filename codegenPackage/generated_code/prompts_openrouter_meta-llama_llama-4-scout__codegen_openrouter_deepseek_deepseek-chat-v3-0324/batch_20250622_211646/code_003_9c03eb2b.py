"""
Generated Code Metadata:
========================
Original URL: https://nexus-mutual.xyz
Prompt: "Design a smart contract using Solidity that interacts with Nexus Mutual's platform for decentralized insurance coverage."
Generated: DETERMINISTIC_9c03eb2bf451268c
Batch ID: 20250622_211646
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

// Interface for Nexus Mutual's Cover Contract
interface INexusMutualCover {
    function buyCover(
        uint16 _coverPeriod,
        uint256 _coverAmount,
        address _contractAddress,
        bytes4 _coverCurrency,
        address _nexusContractAddress,
        bytes4 _coverReason
    ) external payable;

    function withdrawClaim(address _contractAddress) external;

    function getCover(uint256 _coverId) external view returns (
        uint16 coverPeriod,
        uint256 coverAmount,
        address contractAddress,
        bytes4 coverCurrency,
        address nexusContractAddress,
        bytes4 coverReason,
        bool isActive
    );
}

contract NexusMutualCoverManager {
    address public owner;
    INexusMutualCover public nexusMutualCover;
    uint256 public coverId;
    bool public coverActive;

    event CoverPurchased(uint256 coverId, uint256 amount, uint16 period);
    event ClaimWithdrawn(address indexed recipient);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _nexusMutualCoverAddress) {
        require(_nexusMutualCoverAddress != address(0), "Invalid Nexus Mutual address");
        owner = msg.sender;
        nexusMutualCover = INexusMutualCover(_nexusMutualCoverAddress);
    }

    /**
     * @dev Purchase cover from Nexus Mutual
     * @param _coverPeriod Cover period in days (max 365)
     * @param _coverAmount Amount of cover to purchase (in wei)
     * @param _contractAddress Address of the contract to cover
     * @param _coverCurrency Currency of cover (e.g., ETH)
     * @param _nexusContractAddress Nexus Mutual contract address
     * @param _coverReason Reason for cover (e.g., SMART_CONTRACT_FAILURE)
     */
    function purchaseCover(
        uint16 _coverPeriod,
        uint256 _coverAmount,
        address _contractAddress,
        bytes4 _coverCurrency,
        address _nexusContractAddress,
        bytes4 _coverReason
    ) external payable onlyOwner {
        require(_coverPeriod > 0 && _coverPeriod <= 365, "Invalid cover period");
        require(_coverAmount > 0, "Cover amount must be > 0");
        require(_contractAddress != address(0), "Invalid contract address");
        require(_nexusContractAddress != address(0), "Invalid Nexus contract address");

        nexusMutualCover.buyCover{value: msg.value}(
            _coverPeriod,
            _coverAmount,
            _contractAddress,
            _coverCurrency,
            _nexusContractAddress,
            _coverReason
        );

        coverActive = true;
        emit CoverPurchased(coverId, _coverAmount, _coverPeriod);
    }

    /**
     * @dev Withdraw claim from Nexus Mutual
     * @param _contractAddress Address of the covered contract
     */
    function withdrawClaim(address _contractAddress) external onlyOwner {
        require(_contractAddress != address(0), "Invalid contract address");
        nexusMutualCover.withdrawClaim(_contractAddress);
        coverActive = false;
        emit ClaimWithdrawn(msg.sender);
    }

    /**
     * @dev Get cover details
     * @param _coverId ID of the cover to query
     */
    function getCoverDetails(uint256 _coverId) external view returns (
        uint16 coverPeriod,
        uint256 coverAmount,
        address contractAddress,
        bytes4 coverCurrency,
        address nexusContractAddress,
        bytes4 coverReason,
        bool isActive
    ) {
        return nexusMutualCover.getCover(_coverId);
    }

    /**
     * @dev Transfer ownership of the contract
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Receive function to accept ETH
     */
    receive() external payable {}
}
```
