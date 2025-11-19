"""
Generated Code Metadata:
========================
Original URL: https://moonbag-claiming.pages.dev
Prompt: Create a function in Solidity to implement tokenomics for an ERC20 token, including allocations for staking, liquidity, presale, community incentives, and team tokens, as outlined in MoonBag's Moonomics.
Generated: DETERMINISTIC_8dbc1eaffcc19c70
Batch ID: 20250612_145625
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

contract MoonToken is ERC20, Ownable {
    // Token allocation percentages
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant STAKING_ALLOCATION = 400_000_000 * 10**18; // 40%
    uint256 public constant LIQUIDITY_ALLOCATION = 250_000_000 * 10**18; // 25%
    uint256 public constant PRESALE_ALLOCATION = 150_000_000 * 10**18; // 15%
    uint256 public constant COMMUNITY_ALLOCATION = 150_000_000 * 10**18; // 15%
    uint256 public constant TEAM_ALLOCATION = 50_000_000 * 10**18; // 5%

    // Allocation addresses
    address public stakingAddress;
    address public liquidityAddress;
    address public presaleAddress;
    address public communityAddress;
    address public teamAddress;

    // Vesting for team tokens
    uint256 public constant VESTING_PERIOD = 365 days; // 1 year
    uint256 public constant VESTING_CLIFF = 90 days; // 3 months
    uint256 public teamVestingStart;
    uint256 public teamTokensReleased;

    event AllocationAddressSet(string allocationType, address allocationAddress);
    event TeamTokensReleased(uint256 amount);

    constructor() ERC20("MoonToken", "MOON") {
        _mint(address(this), TOTAL_SUPPLY);
    }

    /**
     * @dev Set allocation addresses (can only be called by owner)
     */
    function setAllocationAddresses(
        address _stakingAddress,
        address _liquidityAddress,
        address _presaleAddress,
        address _communityAddress,
        address _teamAddress
    ) external onlyOwner {
        require(_stakingAddress != address(0), "Invalid staking address");
        require(_liquidityAddress != address(0), "Invalid liquidity address");
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_communityAddress != address(0), "Invalid community address");
        require(_teamAddress != address(0), "Invalid team address");

        stakingAddress = _stakingAddress;
        liquidityAddress = _liquidityAddress;
        presaleAddress = _presaleAddress;
        communityAddress = _communityAddress;
        teamAddress = _teamAddress;

        emit AllocationAddressSet("staking", _stakingAddress);
        emit AllocationAddressSet("liquidity", _liquidityAddress);
        emit AllocationAddressSet("presale", _presaleAddress);
        emit AllocationAddressSet("community", _communityAddress);
        emit AllocationAddressSet("team", _teamAddress);
    }

    /**
     * @dev Distribute initial token allocations (can only be called by owner)
     */
    function distributeInitialAllocations() external onlyOwner {
        require(stakingAddress != address(0), "Staking address not set");
        require(liquidityAddress != address(0), "Liquidity address not set");
        require(presaleAddress != address(0), "Presale address not set");
        require(communityAddress != address(0), "Community address not set");
        require(teamAddress != address(0), "Team address not set");

        _transfer(address(this), stakingAddress, STAKING_ALLOCATION);
        _transfer(address(this), liquidityAddress, LIQUIDITY_ALLOCATION);
        _transfer(address(this), presaleAddress, PRESALE_ALLOCATION);
        _transfer(address(this), communityAddress, COMMUNITY_ALLOCATION);

        // Start team vesting
        teamVestingStart = block.timestamp;
    }

    /**
     * @dev Release vested team tokens (can be called by anyone)
     */
    function releaseTeamTokens() external {
        require(teamVestingStart > 0, "Team vesting not started");
        require(block.timestamp >= teamVestingStart + VESTING_CLIFF, "Cliff period not over");

        uint256 totalVested = calculateVestedTeamTokens();
        uint256 releasable = totalVested - teamTokensReleased;

        require(releasable > 0, "No tokens to release");

        teamTokensReleased += releasable;
        _transfer(address(this), teamAddress, releasable);

        emit TeamTokensReleased(releasable);
    }

    /**
     * @dev Calculate vested team tokens
     */
    function calculateVestedTeamTokens() public view returns (uint256) {
        if (teamVestingStart == 0 || block.timestamp < teamVestingStart + VESTING_CLIFF) {
            return 0;
        }

        uint256 elapsed = block.timestamp - teamVestingStart;
        if (elapsed >= VESTING_PERIOD) {
            return TEAM_ALLOCATION;
        }

        return (TEAM_ALLOCATION * elapsed) / VESTING_PERIOD;
    }

    /**
     * @dev Get remaining team tokens
     */
    function getRemainingTeamTokens() public view returns (uint256) {
        return TEAM_ALLOCATION - teamTokensReleased;
    }
}
```
