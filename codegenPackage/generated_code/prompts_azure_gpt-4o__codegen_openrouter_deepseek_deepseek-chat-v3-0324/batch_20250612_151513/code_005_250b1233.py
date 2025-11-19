"""
Generated Code Metadata:
========================
Original URL: https://btc-etftoken.web.app
Prompt: Generate code in Solidity for an ERC-20 token with tokenomics similar to BTCETF, including presale allocation, staking rewards, liquidity allocation, and a burn mechanism tied to milestones.
Generated: DETERMINISTIC_250b12339ea7e145
Batch ID: 20250612_151513
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract BTCETF is ERC20, ERC20Burnable, Ownable, Pausable {
    // Tokenomics parameters
    uint256 public constant TOTAL_SUPPLY = 21_000_000 * 10**18; // 21 million tokens
    uint256 public constant PRESALE_ALLOCATION = 4_200_000 * 10**18; // 20%
    uint256 public constant STAKING_REWARDS = 6_300_000 * 10**18; // 30%
    uint256 public constant LIQUIDITY_POOL = 4_200_000 * 10**18; // 20%
    uint256 public constant TEAM_ALLOCATION = 2_100_000 * 10**18; // 10%
    uint256 public constant MARKETING_ALLOCATION = 2_100_000 * 10**18; // 10%
    uint256 public constant COMMUNITY_REWARDS = 2_100_000 * 10**18; // 10%

    // Milestone burn thresholds (percentage of total supply)
    uint256[] public burnMilestones = [10, 25, 50, 75];
    uint256 public currentBurnMilestone = 0;

    // Addresses
    address public presaleAddress;
    address public stakingAddress;
    address public liquidityPoolAddress;
    address public teamAddress;
    address public marketingAddress;
    address public communityAddress;

    // Events
    event TokensBurned(uint256 amount);
    event MilestoneReached(uint256 milestone);

    constructor(
        address _presaleAddress,
        address _stakingAddress,
        address _liquidityPoolAddress,
        address _teamAddress,
        address _marketingAddress,
        address _communityAddress
    ) ERC20("BTCETF", "BTCETF") {
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_stakingAddress != address(0), "Invalid staking address");
        require(_liquidityPoolAddress != address(0), "Invalid liquidity address");
        require(_teamAddress != address(0), "Invalid team address");
        require(_marketingAddress != address(0), "Invalid marketing address");
        require(_communityAddress != address(0), "Invalid community address");

        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        liquidityPoolAddress = _liquidityPoolAddress;
        teamAddress = _teamAddress;
        marketingAddress = _marketingAddress;
        communityAddress = _communityAddress;

        // Initial token distribution
        _mint(presaleAddress, PRESALE_ALLOCATION);
        _mint(stakingAddress, STAKING_REWARDS);
        _mint(liquidityPoolAddress, LIQUIDITY_POOL);
        _mint(teamAddress, TEAM_ALLOCATION);
        _mint(marketingAddress, MARKETING_ALLOCATION);
        _mint(communityAddress, COMMUNITY_REWARDS);
    }

    // Pause token transfers in case of emergency
    function pause() public onlyOwner {
        _pause();
    }

    // Unpause token transfers
    function unpause() public onlyOwner {
        _unpause();
    }

    // Override transfer to include pausable functionality
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }

    // Check and execute burn if milestone is reached
    function checkBurnMilestone() public {
        require(currentBurnMilestone < burnMilestones.length, "All milestones reached");

        uint256 currentSupply = totalSupply();
        uint256 threshold = (TOTAL_SUPPLY * burnMilestones[currentBurnMilestone]) / 100;

        if (currentSupply <= threshold) {
            uint256 burnAmount = (TOTAL_SUPPLY * 5) / 100; // Burn 5% of total supply
            _burn(address(this), burnAmount);
            currentBurnMilestone++;
            emit TokensBurned(burnAmount);
            emit MilestoneReached(currentBurnMilestone);
        }
    }

    // Manual burn function (owner only)
    function manualBurn(uint256 amount) public onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        _burn(msg.sender, amount);
        emit TokensBurned(amount);
    }

    // Update staking contract address
    function updateStakingAddress(address newAddress) public onlyOwner {
        require(newAddress != address(0), "Invalid address");
        stakingAddress = newAddress;
    }

    // Update liquidity pool address
    function updateLiquidityPoolAddress(address newAddress) public onlyOwner {
        require(newAddress != address(0), "Invalid address");
        liquidityPoolAddress = newAddress;
    }

    // Recover any ERC20 tokens sent to the contract by mistake
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
