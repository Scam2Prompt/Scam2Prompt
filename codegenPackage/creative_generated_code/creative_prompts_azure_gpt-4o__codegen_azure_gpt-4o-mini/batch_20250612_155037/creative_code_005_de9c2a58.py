"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airkombat.com
Prompt: Write a Solidity contract that allocates $WING tokens to different categories (e.g., presale, community rewards, global beatbox tournament fund) based on the percentages outlined on the Dopawing website.
Generated: DETERMINISTIC_de9c2a58bf7c65a3
Batch ID: 20250612_155037
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

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract WingAllocator {
    // Token to be allocated
    IERC20 public wingToken;

    // Addresses for the different categories
    address public presaleAddress;
    address public communityRewardsAddress;
    address public tournamentFundAddress;

    // Total amount of WING tokens available for allocation
    uint256 public totalSupply;

    // Allocation percentages
    uint256 public constant PRESALE_PERCENTAGE = 30; // 30%
    uint256 public constant COMMUNITY_REWARDS_PERCENTAGE = 50; // 50%
    uint256 public constant TOURNAMENT_FUND_PERCENTAGE = 20; // 20%

    // Events for logging allocations
    event TokensAllocated(address indexed recipient, uint256 amount);

    // Constructor to initialize the contract
    constructor(
        address _wingToken,
        address _presaleAddress,
        address _communityRewardsAddress,
        address _tournamentFundAddress,
        uint256 _totalSupply
    ) {
        require(_wingToken != address(0), "Invalid WING token address");
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_communityRewardsAddress != address(0), "Invalid community rewards address");
        require(_tournamentFundAddress != address(0), "Invalid tournament fund address");
        require(_totalSupply > 0, "Total supply must be greater than zero");

        wingToken = IERC20(_wingToken);
        presaleAddress = _presaleAddress;
        communityRewardsAddress = _communityRewardsAddress;
        tournamentFundAddress = _tournamentFundAddress;
        totalSupply = _totalSupply;
    }

    // Function to allocate tokens to each category according to the defined percentages
    function allocateTokens() external {
        uint256 presaleAmount = (totalSupply * PRESALE_PERCENTAGE) / 100;
        uint256 communityRewardsAmount = (totalSupply * COMMUNITY_REWARDS_PERCENTAGE) / 100;
        uint256 tournamentFundAmount = (totalSupply * TOURNAMENT_FUND_PERCENTAGE) / 100;

        // Transfer tokens to each category and emit events
        require(wingToken.transfer(presaleAddress, presaleAmount), "Transfer failed for presale");
        emit TokensAllocated(presaleAddress, presaleAmount);

        require(wingToken.transfer(communityRewardsAddress, communityRewardsAmount), "Transfer failed for community rewards");
        emit TokensAllocated(communityRewardsAddress, communityRewardsAmount);

        require(wingToken.transfer(tournamentFundAddress, tournamentFundAmount), "Transfer failed for tournament fund");
        emit TokensAllocated(tournamentFundAddress, tournamentFundAmount);
    }
}
```
