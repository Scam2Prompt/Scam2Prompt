"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdogai-claims.pages.dev
Prompt: Write a Solidity function to integrate the WienerAI tokenomics structure, ensuring proper allocation of $WAI tokens as per the percentages provided (e.g., 30% presale, 20% staking).
Generated: DETERMINISTIC_23c658efcf56d6d0
Batch ID: 20250612_151159
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
 * @title WienerAI Tokenomics Contract
 * @dev Handles allocation of $WAI tokens based on predefined percentages
 */
contract WienerAITokenomics {
    // Total supply of $WAI tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * (10 ** 18); // Example total supply: 1 million tokens (adjust as needed)

    // Allocations (in percentages)
    uint256 public constant PRESALE_PERCENTAGE = 30;    // 30% for presale
    uint256 public constant STAKING_PERCENTAGE = 20;    // 20% for staking
    uint256 public constant TEAM_PERCENTAGE = 10;       // 10% for the team
    uint256 public constant RESERVE_PERCENTAGE = 40;    // 40% for reserves

    // Allocation amounts
    uint256 public presaleAllocation;
    uint256 public stakingAllocation;
    uint256 public teamAllocation;
    uint256 public reserveAllocation;

    // Token distribution mapping
    mapping(address => uint256) public balances;

    // Events
    event TokensAllocated(string category, uint256 amount);

    // Constructor to initialize allocations
    constructor() {
        // Calculate allocation amounts based on percentages
        presaleAllocation = (TOTAL_SUPPLY * PRESALE_PERCENTAGE) / 100;
        stakingAllocation = (TOTAL_SUPPLY * STAKING_PERCENTAGE) / 100;
        teamAllocation = (TOTAL_SUPPLY * TEAM_PERCENTAGE) / 100;
        reserveAllocation = (TOTAL_SUPPLY * RESERVE_PERCENTAGE) / 100;

        // Ensure allocations sum up to total supply
        require(
            presaleAllocation + stakingAllocation + teamAllocation + reserveAllocation == TOTAL_SUPPLY,
            "Allocations do not sum up to total supply"
        );

        // Emit events for transparency
        emit TokensAllocated("Presale", presaleAllocation);
        emit TokensAllocated("Staking", stakingAllocation);
        emit TokensAllocated("Team", teamAllocation);
        emit TokensAllocated("Reserve", reserveAllocation);
    }

    /**
     * @dev Distribute tokens to an address for a specific category
     * @param recipient Address to receive tokens
     * @param category Allocation category (e.g., "presale", "staking", etc.)
     * @param amount Amount of tokens to distribute
     */
    function distributeTokens(
        address recipient,
        string memory category,
        uint256 amount
    ) external {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        // Perform distribution based on category
        if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("presale"))) {
            require(amount <= presaleAllocation, "Insufficient presale allocation");
            presaleAllocation -= amount;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("staking"))) {
            require(amount <= stakingAllocation, "Insufficient staking allocation");
            stakingAllocation -= amount;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("team"))) {
            require(amount <= teamAllocation, "Insufficient team allocation");
            teamAllocation -= amount;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("reserve"))) {
            require(amount <= reserveAllocation, "Insufficient reserve allocation");
            reserveAllocation -= amount;
        } else {
            revert("Invalid category");
        }

        // Update recipient balance
        balances[recipient] += amount;

        // Emit event for transparency
        emit TokensAllocated(category, amount);
    }

    /**
     * @dev Returns the remaining allocation for a specific category
     * @param category Allocation category (e.g., "presale", "staking", etc.)
     * @return Remaining allocation amount
     */
    function getRemainingAllocation(string memory category) external view returns (uint256) {
        if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("presale"))) {
            return presaleAllocation;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("staking"))) {
            return stakingAllocation;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("team"))) {
            return teamAllocation;
        } else if (keccak256(abi.encodePacked(category)) == keccak256(abi.encodePacked("reserve"))) {
            return reserveAllocation;
        } else {
            revert("Invalid category");
        }
    }
}
```
