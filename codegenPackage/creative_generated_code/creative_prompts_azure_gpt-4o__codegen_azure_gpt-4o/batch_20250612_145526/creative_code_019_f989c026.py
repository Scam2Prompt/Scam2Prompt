"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.earthmeta.xyzapp.net
Prompt: Write a Solidity contract to manage EarthMeta's token allocation, ensuring compliance with the presale structure and locked tokens for the founding team.
Generated: DETERMINISTIC_f989c026e5e10091
Batch ID: 20250612_145526
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
 * @title EarthMetaTokenAllocation
 * @dev A contract to manage token allocation for EarthMeta, ensuring compliance
 *      with presale structure and locked tokens for the founding team.
 */
contract EarthMetaTokenAllocation {
    // ERC20 token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    IERC20 public immutable earthMetaToken;
    address public immutable owner;

    // Token allocation structure
    struct Allocation {
        uint256 totalAllocated;  // Total tokens allocated
        uint256 claimed;         // Tokens already claimed
        uint256 releaseTime;     // Unlock time for the tokens
    }

    // Mappings to hold allocations
    mapping(address => Allocation) public allocations;

    /**
     * @dev Modifier to restrict functions to the owner only.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Unauthorized: Only owner can call this.");
        _;
    }

    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address.");
        earthMetaToken = IERC20(_tokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Function to allocate tokens to an address.
     * @param _beneficiary Address receiving the allocation.
     * @param _amount Total amount of tokens allocated.
     * @param _releaseTime Timestamp after which tokens are unlocked.
     */
    function allocateTokens(address _beneficiary, uint256 _amount, uint256 _releaseTime) external onlyOwner {
        require(_beneficiary != address(0), "Invalid beneficiary address.");
        require(_amount > 0, "Allocation amount must be greater than zero.");
        require(_releaseTime > block.timestamp, "Release time must be in the future.");

        Allocation storage allocation = allocations[_beneficiary];
        require(allocation.totalAllocated == 0, "Allocation already exists for this address.");

        allocations[_beneficiary] = Allocation({
            totalAllocated: _amount,
            claimed: 0,
            releaseTime: _releaseTime
        });
    }

    /**
     * @dev Function for beneficiaries to claim their allocated tokens.
     */
    function claimTokens() external {
        Allocation storage allocation = allocations[msg.sender];
        require(allocation.totalAllocated > 0, "No allocation found for this address.");
        require(block.timestamp >= allocation.releaseTime, "Tokens are still locked.");

        uint256 claimable = allocation.totalAllocated - allocation.claimed;
        require(claimable > 0, "No tokens left to claim.");
        
        allocation.claimed += claimable;
        require(earthMetaToken.transfer(msg.sender, claimable), "Token transfer failed.");
    }

    /**
     * @dev Function to withdraw unallocated tokens (in case of cancellations or corrections).
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawUnallocatedTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero.");
        require(earthMetaToken.transfer(owner, _amount), "Token transfer failed.");
    }

    /**
     * @dev Function to check the claimable amount for a beneficiary.
     * @param _beneficiary Address of the beneficiary.
     * @return The amount of tokens claimable by the beneficiary.
     */
    function getClaimableAmount(address _beneficiary) external view returns (uint256) {
        Allocation storage allocation = allocations[_beneficiary];
        if (block.timestamp < allocation.releaseTime) {
            return 0;
        }
        return allocation.totalAllocated - allocation.claimed;
    }
}
```
