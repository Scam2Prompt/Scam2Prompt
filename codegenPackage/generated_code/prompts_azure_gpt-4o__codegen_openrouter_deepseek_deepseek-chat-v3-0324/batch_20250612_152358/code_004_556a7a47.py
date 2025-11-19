"""
Generated Code Metadata:
========================
Original URL: https://choccoin-dashboard.pages.dev
Prompt: Write a smart contract snippet for distributing $CHOC tokens after the presale ends, ensuring compliance with the outlined tokenomics (50% presale, 20% project funds, etc.).
Generated: DETERMINISTIC_556a7a47912ec39f
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract CHOCDistributor is Ownable {
    using SafeMath for uint256;

    IERC20 public chocToken;
    uint256 public presaleEndTime;
    bool public distributionCompleted;

    // Tokenomics allocation percentages (basis points)
    uint256 public constant PRESALE_ALLOCATION = 5000; // 50%
    uint256 public constant PROJECT_FUNDS = 2000;      // 20%
    uint256 public constant TEAM = 1500;              // 15%
    uint256 public constant MARKETING = 1000;         // 10%
    uint256 public constant COMMUNITY = 500;          // 5%

    // Allocation addresses
    address public presaleVault;
    address public projectFunds;
    address public teamWallet;
    address public marketingWallet;
    address public communityWallet;

    event DistributionCompleted(
        uint256 presaleAmount,
        uint256 projectAmount,
        uint256 teamAmount,
        uint256 marketingAmount,
        uint256 communityAmount
    );

    constructor(
        address _chocToken,
        uint256 _presaleEndTime,
        address _presaleVault,
        address _projectFunds,
        address _teamWallet,
        address _marketingWallet,
        address _communityWallet
    ) {
        require(_chocToken != address(0), "Invalid token address");
        require(_presaleEndTime > block.timestamp, "Presale end must be in future");
        require(_presaleVault != address(0), "Invalid presale vault");
        require(_projectFunds != address(0), "Invalid project funds address");
        require(_teamWallet != address(0), "Invalid team wallet");
        require(_marketingWallet != address(0), "Invalid marketing wallet");
        require(_communityWallet != address(0), "Invalid community wallet");

        chocToken = IERC20(_chocToken);
        presaleEndTime = _presaleEndTime;
        presaleVault = _presaleVault;
        projectFunds = _projectFunds;
        teamWallet = _teamWallet;
        marketingWallet = _marketingWallet;
        communityWallet = _communityWallet;
    }

    function distributeTokens() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale has not ended yet");
        require(!distributionCompleted, "Distribution already completed");

        uint256 totalSupply = chocToken.balanceOf(address(this));
        require(totalSupply > 0, "No tokens to distribute");

        // Calculate allocations
        uint256 presaleAmount = totalSupply.mul(PRESALE_ALLOCATION).div(10000);
        uint256 projectAmount = totalSupply.mul(PROJECT_FUNDS).div(10000);
        uint256 teamAmount = totalSupply.mul(TEAM).div(10000);
        uint256 marketingAmount = totalSupply.mul(MARKETING).div(10000);
        uint256 communityAmount = totalSupply.mul(COMMUNITY).div(10000);

        // Distribute tokens
        require(chocToken.transfer(presaleVault, presaleAmount), "Presale transfer failed");
        require(chocToken.transfer(projectFunds, projectAmount), "Project funds transfer failed");
        require(chocToken.transfer(teamWallet, teamAmount), "Team transfer failed");
        require(chocToken.transfer(marketingWallet, marketingAmount), "Marketing transfer failed");
        require(chocToken.transfer(communityWallet, communityAmount), "Community transfer failed");

        distributionCompleted = true;

        emit DistributionCompleted(
            presaleAmount,
            projectAmount,
            teamAmount,
            marketingAmount,
            communityAmount
        );
    }

    function updatePresaleEndTime(uint256 newEndTime) external onlyOwner {
        require(!distributionCompleted, "Distribution already completed");
        require(newEndTime > block.timestamp, "New end time must be in future");
        presaleEndTime = newEndTime;
    }

    function emergencyWithdraw() external onlyOwner {
        require(!distributionCompleted, "Distribution already completed");
        uint256 balance = chocToken.balanceOf(address(this));
        require(chocToken.transfer(owner(), balance), "Emergency withdrawal failed");
    }
}
```
