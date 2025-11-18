"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lopecoin-presale.pages.dev
Prompt: Write a Solidity contract for distributing tokens based on ecosystem allocation percentages (e.g., 30% for ecosystem, 10% for airdrops), as outlined in LopeCoin's tokenomics.
Generated: DETERMINISTIC_4b5cbf3dd8d8b65a
Batch ID: 20250612_152235
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
 * @title LopeCoinTokenDistributor
 * @notice A contract for distributing LopeCoin tokens based on predefined ecosystem allocation percentages.
 */
contract LopeCoinTokenDistributor {
    // ERC20 interface (simplified for transfer functionality)
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
    }

    IERC20 public immutable token; // Reference to the token contract
    address public owner; // Owner of the contract

    // Allocation percentages (in basis points: 10000 = 100%)
    uint256 public constant ECOSYSTEM_ALLOCATION = 3000; // 30%
    uint256 public constant AIRDROP_ALLOCATION = 1000;   // 10%
    uint256 public constant OTHER_ALLOCATION = 6000;     // 60%

    // Tracking total tokens allocated
    uint256 public totalTokensAllocated;

    // Events
    event TokensDistributed(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @notice Constructor to initialize the contract.
     * @param _token Address of the LopeCoin token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
        owner = msg.sender;
    }

    /**
     * @notice Distributes tokens to a recipient based on the specified allocation percentage.
     * @param recipient Address of the recipient.
     * @param allocationType Type of allocation (ecosystem, airdrop, other).
     * @param amount Total amount of tokens to distribute.
     */
    function distributeTokens(
        address recipient,
        string memory allocationType,
        uint256 amount
    ) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        uint256 allocationPercentage;

        // Determine allocation percentage
        if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("ecosystem"))) {
            allocationPercentage = ECOSYSTEM_ALLOCATION;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("airdrop"))) {
            allocationPercentage = AIRDROP_ALLOCATION;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("other"))) {
            allocationPercentage = OTHER_ALLOCATION;
        } else {
            revert("Invalid allocation type");
        }

        // Calculate the allocated amount
        uint256 allocatedAmount = (amount * allocationPercentage) / 10000;

        // Transfer tokens to the recipient
        require(token.transfer(recipient, allocatedAmount), "Token transfer failed");

        // Update total tokens allocated
        totalTokensAllocated += allocatedAmount;

        emit TokensDistributed(recipient, allocatedAmount);
    }

    /**
     * @notice Transfers ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is invalid");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
