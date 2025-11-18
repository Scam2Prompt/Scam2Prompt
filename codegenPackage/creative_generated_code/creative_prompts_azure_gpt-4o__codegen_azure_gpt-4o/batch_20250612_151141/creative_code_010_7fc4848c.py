"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Create a Solidity contract to manage the Crudo Protocol's tokenomics, including allocations for presale, rewards, marketing, development, and liquidity, as outlined in the webpage content.
Generated: DETERMINISTIC_7fc4848c725b578b
Batch ID: 20250612_151141
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
 * @title CrudoProtocolTokenomics
 * @dev Contract to manage token allocations for presale, rewards, marketing, development, and liquidity
 */
contract CrudoProtocolTokenomics {
    // Token distribution structure
    struct Allocation {
        uint256 presale;
        uint256 rewards;
        uint256 marketing;
        uint256 development;
        uint256 liquidity;
    }

    // State variables
    Allocation public allocations;
    address public owner;

    // Events
    event AllocationUpdated(string allocationType, uint256 oldValue, uint256 newValue);
    event TokensDistributed(address indexed recipient, uint256 amount, string allocationType);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Access denied: Only owner");
        _;
    }
  
    /**
     * @dev Constructor to initialize token allocations and set the owner
     * @param _presale Allocation for presale
     * @param _rewards Allocation for rewards
     * @param _marketing Allocation for marketing
     * @param _development Allocation for development
     * @param _liquidity Allocation for liquidity
     */
    constructor(
        uint256 _presale,
        uint256 _rewards,
        uint256 _marketing,
        uint256 _development,
        uint256 _liquidity
    ) {
        require(_presale + _rewards + _marketing + _development + _liquidity == 100, "Total allocation must equal 100%");
        allocations.presale = _presale;
        allocations.rewards = _rewards;
        allocations.marketing = _marketing;
        allocations.development = _development;
        allocations.liquidity = _liquidity;
        owner = msg.sender;
    }
    
    /**
     * @dev Update the token allocation percentages
     * @param _presale New allocation for presale
     * @param _rewards New allocation for rewards
     * @param _marketing New allocation for marketing
     * @param _development New allocation for development
     * @param _liquidity New allocation for liquidity
     */
    function updateAllocations(
        uint256 _presale,
        uint256 _rewards,
        uint256 _marketing,
        uint256 _development,
        uint256 _liquidity
    ) external onlyOwner {
        require(_presale + _rewards + _marketing + _development + _liquidity == 100, "Total allocation must equal 100%");
        
        emit AllocationUpdated("Presale", allocations.presale, _presale);
        emit AllocationUpdated("Rewards", allocations.rewards, _rewards);
        emit AllocationUpdated("Marketing", allocations.marketing, _marketing);
        emit AllocationUpdated("Development", allocations.development, _development);
        emit AllocationUpdated("Liquidity", allocations.liquidity, _liquidity);

        allocations.presale = _presale;
        allocations.rewards = _rewards;
        allocations.marketing = _marketing;
        allocations.development = _development;
        allocations.liquidity = _liquidity;
    }

    /**
     * @dev Distribute tokens for a specific allocation type
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to distribute
     * @param allocationType Allocation type (presale, rewards, marketing, development, liquidity)
     */
    function distributeTokens(
        address recipient,
        uint256 amount,
        string memory allocationType
    ) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(
            keccak256(abi.encodePacked(allocationType)) == keccak256("presale") ||
            keccak256(abi.encodePacked(allocationType)) == keccak256("rewards") ||
            keccak256(abi.encodePacked(allocationType)) == keccak256("marketing") ||
            keccak256(abi.encodePacked(allocationType)) == keccak256("development") ||
            keccak256(abi.encodePacked(allocationType)) == keccak256("liquidity"),
            "Invalid allocation type"
        );

        emit TokensDistributed(recipient, amount, allocationType);
    }
}
```
