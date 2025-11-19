"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-ic.pages.dev
Prompt: Generate code in Solidity to implement tokenomics for WienerAI ($WAI), including allocations for presale, staking, community rewards, liquidity, and marketing as described on the website.
Generated: DETERMINISTIC_675fd186b06cd65d
Batch ID: 20250612_145203
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

contract WienerAI is ERC20, ERC20Burnable, Ownable, Pausable {
    // Token allocations
    uint256 public constant TOTAL_SUPPLY = 69_000_000_000 * 10**18; // 69 billion tokens
    uint256 public constant PRESALE_ALLOCATION = 30_000_000_000 * 10**18; // ~43.48%
    uint256 public constant STAKING_ALLOCATION = 20_000_000_000 * 10**18; // ~28.99%
    uint256 public constant COMMUNITY_REWARDS = 10_000_000_000 * 10**18; // ~14.49%
    uint256 public constant LIQUIDITY_ALLOCATION = 5_000_000_000 * 10**18; // ~7.25%
    uint256 public constant MARKETING_ALLOCATION = 4_000_000_000 * 10**18; // ~5.80%

    // Allocation addresses
    address public presaleAddress;
    address public stakingAddress;
    address public communityRewardsAddress;
    address public liquidityAddress;
    address public marketingAddress;

    // Track minted allocations
    bool public presaleMinted;
    bool public stakingMinted;
    bool public communityRewardsMinted;
    bool public liquidityMinted;
    bool public marketingMinted;

    constructor() ERC20("WienerAI", "WAI") {
        // Mint initial supply to contract owner for distribution
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Set allocation addresses (only owner)
    function setAllocationAddresses(
        address _presaleAddress,
        address _stakingAddress,
        address _communityRewardsAddress,
        address _liquidityAddress,
        address _marketingAddress
    ) external onlyOwner {
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_stakingAddress != address(0), "Invalid staking address");
        require(_communityRewardsAddress != address(0), "Invalid community rewards address");
        require(_liquidityAddress != address(0), "Invalid liquidity address");
        require(_marketingAddress != address(0), "Invalid marketing address");

        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        communityRewardsAddress = _communityRewardsAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;
    }

    // Mint presale allocation (only owner)
    function mintPresale() external onlyOwner {
        require(!presaleMinted, "Presale already minted");
        require(presaleAddress != address(0), "Presale address not set");
        
        _transfer(owner(), presaleAddress, PRESALE_ALLOCATION);
        presaleMinted = true;
    }

    // Mint staking allocation (only owner)
    function mintStaking() external onlyOwner {
        require(!stakingMinted, "Staking already minted");
        require(stakingAddress != address(0), "Staking address not set");
        
        _transfer(owner(), stakingAddress, STAKING_ALLOCATION);
        stakingMinted = true;
    }

    // Mint community rewards allocation (only owner)
    function mintCommunityRewards() external onlyOwner {
        require(!communityRewardsMinted, "Community rewards already minted");
        require(communityRewardsAddress != address(0), "Community rewards address not set");
        
        _transfer(owner(), communityRewardsAddress, COMMUNITY_REWARDS);
        communityRewardsMinted = true;
    }

    // Mint liquidity allocation (only owner)
    function mintLiquidity() external onlyOwner {
        require(!liquidityMinted, "Liquidity already minted");
        require(liquidityAddress != address(0), "Liquidity address not set");
        
        _transfer(owner(), liquidityAddress, LIQUIDITY_ALLOCATION);
        liquidityMinted = true;
    }

    // Mint marketing allocation (only owner)
    function mintMarketing() external onlyOwner {
        require(!marketingMinted, "Marketing already minted");
        require(marketingAddress != address(0), "Marketing address not set");
        
        _transfer(owner(), marketingAddress, MARKETING_ALLOCATION);
        marketingMinted = true;
    }

    // Pause token transfers (only owner)
    function pause() external onlyOwner {
        _pause();
    }

    // Unpause token transfers (only owner)
    function unpause() external onlyOwner {
        _unpause();
    }

    // Override transfer to respect pause state
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
