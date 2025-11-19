"""
Generated Code Metadata:
========================
Original URL: https://99bitcoin-presale.pages.dev
Prompt: Generate a Solidity contract that implements the tokenomics of $99BTC, including allocations for presale, staking, project funds, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_d1e6304ce1c52ee5
Batch ID: 20250612_150241
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

contract BTC99 is ERC20, Ownable {
    using SafeMath for uint256;

    // Token allocations
    uint256 public constant TOTAL_SUPPLY = 99_000_000 * 10**18; // 99 million tokens
    uint256 public constant PRESALE_ALLOCATION = TOTAL_SUPPLY.mul(20).div(100); // 20%
    uint256 public constant STAKING_ALLOCATION = TOTAL_SUPPLY.mul(25).div(100); // 25%
    uint256 public constant PROJECT_FUNDS = TOTAL_SUPPLY.mul(15).div(100); // 15%
    uint256 public constant COMMUNITY_REWARDS = TOTAL_SUPPLY.mul(10).div(100); // 10%
    uint256 public constant LIQUIDITY = TOTAL_SUPPLY.mul(20).div(100); // 20%
    uint256 public constant MARKETING = TOTAL_SUPPLY.mul(10).div(100); // 10%

    // Allocation addresses
    address public presaleAddress;
    address public stakingAddress;
    address public projectFundsAddress;
    address public communityRewardsAddress;
    address public liquidityAddress;
    address public marketingAddress;

    // Track minted allocations
    bool public presaleMinted = false;
    bool public stakingMinted = false;
    bool public projectFundsMinted = false;
    bool public communityRewardsMinted = false;
    bool public liquidityMinted = false;
    bool public marketingMinted = false;

    constructor() ERC20("99BTC", "99BTC") {
        // Mint initial supply to contract creator for distribution
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Set allocation addresses (only owner)
    function setAllocationAddresses(
        address _presaleAddress,
        address _stakingAddress,
        address _projectFundsAddress,
        address _communityRewardsAddress,
        address _liquidityAddress,
        address _marketingAddress
    ) external onlyOwner {
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_stakingAddress != address(0), "Invalid staking address");
        require(_projectFundsAddress != address(0), "Invalid project funds address");
        require(_communityRewardsAddress != address(0), "Invalid community rewards address");
        require(_liquidityAddress != address(0), "Invalid liquidity address");
        require(_marketingAddress != address(0), "Invalid marketing address");

        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        projectFundsAddress = _projectFundsAddress;
        communityRewardsAddress = _communityRewardsAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;
    }

    // Mint presale allocation
    function mintPresale() external onlyOwner {
        require(!presaleMinted, "Presale already minted");
        require(presaleAddress != address(0), "Presale address not set");
        
        _transfer(owner(), presaleAddress, PRESALE_ALLOCATION);
        presaleMinted = true;
    }

    // Mint staking allocation
    function mintStaking() external onlyOwner {
        require(!stakingMinted, "Staking already minted");
        require(stakingAddress != address(0), "Staking address not set");
        
        _transfer(owner(), stakingAddress, STAKING_ALLOCATION);
        stakingMinted = true;
    }

    // Mint project funds allocation
    function mintProjectFunds() external onlyOwner {
        require(!projectFundsMinted, "Project funds already minted");
        require(projectFundsAddress != address(0), "Project funds address not set");
        
        _transfer(owner(), projectFundsAddress, PROJECT_FUNDS);
        projectFundsMinted = true;
    }

    // Mint community rewards allocation
    function mintCommunityRewards() external onlyOwner {
        require(!communityRewardsMinted, "Community rewards already minted");
        require(communityRewardsAddress != address(0), "Community rewards address not set");
        
        _transfer(owner(), communityRewardsAddress, COMMUNITY_REWARDS);
        communityRewardsMinted = true;
    }

    // Mint liquidity allocation
    function mintLiquidity() external onlyOwner {
        require(!liquidityMinted, "Liquidity already minted");
        require(liquidityAddress != address(0), "Liquidity address not set");
        
        _transfer(owner(), liquidityAddress, LIQUIDITY);
        liquidityMinted = true;
    }

    // Mint marketing allocation
    function mintMarketing() external onlyOwner {
        require(!marketingMinted, "Marketing already minted");
        require(marketingAddress != address(0), "Marketing address not set");
        
        _transfer(owner(), marketingAddress, MARKETING);
        marketingMinted = true;
    }

    // Recover any ERC20 tokens sent to the contract by mistake
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
