"""
Generated Code Metadata:
========================
Original URL: https://appmemekombatclaim.pages.dev
Prompt: Generate a smart contract code in Solidity for a tokenomics system that allocates 50% of tokens for presale, 30% for staking and battle rewards, 10% for DEX, and 10% for community rewards.
Generated: DETERMINISTIC_f4be02fb07a2c0fd
Batch ID: 20250622_205842
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

contract TokenomicsToken is ERC20, Ownable {
    // Token allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 50;
    uint256 public constant REWARDS_ALLOCATION = 30;
    uint256 public constant DEX_ALLOCATION = 10;
    uint256 public constant COMMUNITY_ALLOCATION = 10;
    
    // Allocation addresses
    address public presaleAddress;
    address public rewardsAddress;
    address public dexAddress;
    address public communityAddress;
    
    // Total supply
    uint256 private constant TOTAL_SUPPLY = 100_000_000 * 10**18; // 100 million tokens
    
    // Track if allocations have been distributed
    bool private allocationsDistributed = false;

    constructor() ERC20("TokenomicsToken", "TKN") {
        _mint(address(this), TOTAL_SUPPLY);
    }

    /**
     * @dev Set allocation addresses
     * @param _presaleAddress Address for presale allocation
     * @param _rewardsAddress Address for staking/battle rewards
     * @param _dexAddress Address for DEX liquidity
     * @param _communityAddress Address for community rewards
     */
    function setAllocationAddresses(
        address _presaleAddress,
        address _rewardsAddress,
        address _dexAddress,
        address _communityAddress
    ) external onlyOwner {
        require(!allocationsDistributed, "Tokenomics: Allocations already distributed");
        require(_presaleAddress != address(0), "Tokenomics: Presale address cannot be zero");
        require(_rewardsAddress != address(0), "Tokenomics: Rewards address cannot be zero");
        require(_dexAddress != address(0), "Tokenomics: DEX address cannot be zero");
        require(_communityAddress != address(0), "Tokenomics: Community address cannot be zero");
        
        presaleAddress = _presaleAddress;
        rewardsAddress = _rewardsAddress;
        dexAddress = _dexAddress;
        communityAddress = _communityAddress;
    }

    /**
     * @dev Distribute tokens according to tokenomics
     */
    function distributeAllocations() external onlyOwner {
        require(!allocationsDistributed, "Tokenomics: Allocations already distributed");
        require(presaleAddress != address(0), "Tokenomics: Presale address not set");
        require(rewardsAddress != address(0), "Tokenomics: Rewards address not set");
        require(dexAddress != address(0), "Tokenomics: DEX address not set");
        require(communityAddress != address(0), "Tokenomics: Community address not set");
        
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        uint256 rewardsAmount = (TOTAL_SUPPLY * REWARDS_ALLOCATION) / 100;
        uint256 dexAmount = (TOTAL_SUPPLY * DEX_ALLOCATION) / 100;
        uint256 communityAmount = (TOTAL_SUPPLY * COMMUNITY_ALLOCATION) / 100;
        
        _transfer(address(this), presaleAddress, presaleAmount);
        _transfer(address(this), rewardsAddress, rewardsAmount);
        _transfer(address(this), dexAddress, dexAmount);
        _transfer(address(this), communityAddress, communityAmount);
        
        allocationsDistributed = true;
    }

    /**
     * @dev Recover any ERC20 tokens accidentally sent to this contract
     * @param tokenAddress Address of the token contract
     * @param tokenAmount Amount of tokens to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(this) || !allocationsDistributed, 
            "Tokenomics: Cannot recover main token after distribution");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
