"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrog-claim.pages.dev
Prompt: Create a Solidity contract that implements the tokenomics allocation for $FROP, distributing the fixed supply of 111,111,111,111 tokens across presale, staking, marketing, rewards, and liquidity.
Generated: DETERMINISTIC_5149dde16d312989
Batch ID: 20250612_154010
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
 * @title FROP Tokenomics Allocation Contract
 * @notice This contract implements the tokenomics allocation for $FROP.
 */
contract FROPTokenomics {
    // Fixed token supply for $FROP
    uint256 public constant TOTAL_SUPPLY = 111_111_111_111 * 10**18; // Tokens with 18 decimals

    // Allocation percentages (sum must be 100%)
    uint256 public constant PRESALE_PERCENTAGE = 30;  // 30%
    uint256 public constant STAKING_PERCENTAGE = 25;  // 25%
    uint256 public constant MARKETING_PERCENTAGE = 15; // 15%
    uint256 public constant REWARDS_PERCENTAGE = 20; // 20%
    uint256 public constant LIQUIDITY_PERCENTAGE = 10; // 10%

    // Allocations (in tokens)
    uint256 public presaleAllocation;
    uint256 public stakingAllocation;
    uint256 public marketingAllocation;
    uint256 public rewardsAllocation;
    uint256 public liquidityAllocation;

    // Address allocations
    address public presaleAddress;
    address public stakingAddress;
    address public marketingAddress;
    address public rewardsAddress;
    address public liquidityAddress;

    // Events
    event AllocationsSet(
        uint256 presaleAllocation,
        uint256 stakingAllocation,
        uint256 marketingAllocation,
        uint256 rewardsAllocation,
        uint256 liquidityAllocation
    );
    event AddressSet(string allocationType, address allocationAddress);

    /**
     * @dev Constructor that sets the token allocations based on percentages.
     * Ensure allocations sum up to TOTAL_SUPPLY.
     */
    constructor() {
        // Calculate allocations
        presaleAllocation = (TOTAL_SUPPLY * PRESALE_PERCENTAGE) / 100;
        stakingAllocation = (TOTAL_SUPPLY * STAKING_PERCENTAGE) / 100;
        marketingAllocation = (TOTAL_SUPPLY * MARKETING_PERCENTAGE) / 100;
        rewardsAllocation = (TOTAL_SUPPLY * REWARDS_PERCENTAGE) / 100;
        liquidityAllocation = (TOTAL_SUPPLY * LIQUIDITY_PERCENTAGE) / 100;

        // Emit event after setting allocations
        emit AllocationsSet(
            presaleAllocation,
            stakingAllocation,
            marketingAllocation,
            rewardsAllocation,
            liquidityAllocation
        );
    }

    /**
     * @dev Set the address for a specific allocation type. 
     * Only callable by the contract owner (this would require ownership logic, e.g., OpenZeppelin Ownable).
     * @param allocationType The type of allocation (e.g., "presale", "staking", etc.)
     * @param allocationAddress The address for the allocation
     */
    function setAllocationAddress(string calldata allocationType, address allocationAddress) external {
        require(allocationAddress != address(0), "Invalid address");
        
        if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("presale"))) {
            presaleAddress = allocationAddress;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("staking"))) {
            stakingAddress = allocationAddress;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("marketing"))) {
            marketingAddress = allocationAddress;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("rewards"))) {
            rewardsAddress = allocationAddress;
        } else if (keccak256(abi.encodePacked(allocationType)) == keccak256(abi.encodePacked("liquidity"))) {
            liquidityAddress = allocationAddress;
        } else {
            revert("Invalid allocation type");
        }
        
        emit AddressSet(allocationType, allocationAddress);
    }

    /**
     * @dev Get the allocation details.
     * @return Allocation details including addresses and token amounts.
     */
    function getAllocationDetails() external view returns (
        uint256 presaleTokens,
        uint256 stakingTokens,
        uint256 marketingTokens,
        uint256 rewardsTokens,
        uint256 liquidityTokens,
        address presaleAddr,
        address stakingAddr,
        address marketingAddr,
        address rewardsAddr,
        address liquidityAddr
    ) {
        return (
            presaleAllocation,
            stakingAllocation,
            marketingAllocation,
            rewardsAllocation,
            liquidityAllocation,
            presaleAddress,
            stakingAddress,
            marketingAddress,
            rewardsAddress,
            liquidityAddress
        );
    }
}
```
