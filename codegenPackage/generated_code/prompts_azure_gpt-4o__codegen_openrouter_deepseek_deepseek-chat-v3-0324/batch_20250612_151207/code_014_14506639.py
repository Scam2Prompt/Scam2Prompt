"""
Generated Code Metadata:
========================
Original URL: https://furrevertokensale.pages.dev
Prompt: Write a Solidity contract snippet that implements a community token allocation mechanism for Furrever Token, as described in Phase 4 of its roadmap.
Generated: DETERMINISTIC_14506639dc1b1ac7
Batch ID: 20250612_151207
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FurreverToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Community allocation parameters
    uint256 public constant COMMUNITY_ALLOCATION = 25_000_000 * 10**18; // 25M tokens
    uint256 public constant VESTING_DURATION = 365 days; // 1 year vesting
    uint256 public constant CLIFF_DURATION = 90 days; // 3 month cliff

    uint256 public communityAllocationStartTime;
    bool public communityAllocationInitialized;

    // Track claimed tokens per address
    mapping(address => uint256) public claimedTokens;

    event CommunityAllocationInitialized(uint256 startTime);
    event TokensClaimed(address indexed recipient, uint256 amount);

    constructor() ERC20("Furrever Token", "FURR") {
        _mint(msg.sender, 100_000_000 * 10**18); // Total supply: 100M
    }

    /**
     * @dev Initialize community allocation with current timestamp
     * Can only be called once by the owner
     */
    function initializeCommunityAllocation() external onlyOwner {
        require(!communityAllocationInitialized, "Community allocation already initialized");
        communityAllocationStartTime = block.timestamp;
        communityAllocationInitialized = true;
        emit CommunityAllocationInitialized(communityAllocationStartTime);
    }

    /**
     * @dev Calculate claimable tokens for an address
     * @param recipient Address to check claimable tokens for
     * @return Amount of claimable tokens
     */
    function getClaimableTokens(address recipient) public view returns (uint256) {
        if (!communityAllocationInitialized || communityAllocationStartTime == 0) {
            return 0;
        }

        uint256 elapsedTime = block.timestamp.sub(communityAllocationStartTime);

        if (elapsedTime < CLIFF_DURATION) {
            return 0;
        }

        if (elapsedTime >= VESTING_DURATION) {
            return COMMUNITY_ALLOCATION.sub(claimedTokens[recipient]);
        }

        uint256 vestedAmount = COMMUNITY_ALLOCATION
            .mul(elapsedTime.sub(CLIFF_DURATION))
            .div(VESTING_DURATION.sub(CLIFF_DURATION));

        return vestedAmount.sub(claimedTokens[recipient]);
    }

    /**
     * @dev Claim available community tokens
     */
    function claimCommunityTokens() external {
        require(communityAllocationInitialized, "Community allocation not initialized");
        require(block.timestamp >= communityAllocationStartTime.add(CLIFF_DURATION), "Cliff period not ended");

        uint256 claimableAmount = getClaimableTokens(msg.sender);
        require(claimableAmount > 0, "No tokens available to claim");

        claimedTokens[msg.sender] = claimedTokens[msg.sender].add(claimableAmount);
        _mint(msg.sender, claimableAmount);

        emit TokensClaimed(msg.sender, claimableAmount);
    }

    /**
     * @dev Emergency function to recover any ERC20 tokens sent to this contract
     * @param tokenAddress Address of the token contract
     * @param to Address to send tokens to
     * @param amount Amount of tokens to recover
     */
    function recoverERC20(address tokenAddress, address to, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(to, amount);
    }
}
```
