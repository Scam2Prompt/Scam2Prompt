"""
Generated Code Metadata:
========================
Original URL: https://popofrogclaim.pages.dev
Prompt: Write a script in Solidity to implement a fixed token supply of 111,111,111,111 $FROP tokens, with allocations for presale, staking, marketing, rewards, and liquidity as outlined in the tokenomics section of the Popo The Frog webpage.
Generated: DETERMINISTIC_78623ea128dd13bc
Batch ID: 20250612_151648
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

contract FROPToken is ERC20, Ownable {
    // Token allocations
    uint256 public constant TOTAL_SUPPLY = 111_111_111_111 * 10**18; // 111,111,111,111 FROP
    
    // Allocation percentages (multiplied by 100 for precision)
    uint256 public constant PRESALE_PERCENT = 30_00; // 30%
    uint256 public constant STAKING_PERCENT = 20_00; // 20%
    uint256 public constant MARKETING_PERCENT = 15_00; // 15%
    uint256 public constant REWARDS_PERCENT = 15_00; // 15%
    uint256 public constant LIQUIDITY_PERCENT = 20_00; // 20%
    
    // Allocation addresses
    address public presaleWallet;
    address public stakingWallet;
    address public marketingWallet;
    address public rewardsWallet;
    address public liquidityWallet;
    
    // Track if allocations have been distributed
    bool private allocationsDistributed = false;
    
    constructor(
        address _presaleWallet,
        address _stakingWallet,
        address _marketingWallet,
        address _rewardsWallet,
        address _liquidityWallet
    ) ERC20("Popo The Frog", "FROP") {
        require(
            _presaleWallet != address(0) &&
            _stakingWallet != address(0) &&
            _marketingWallet != address(0) &&
            _rewardsWallet != address(0) &&
            _liquidityWallet != address(0),
            "Allocation wallets cannot be zero address"
        );
        
        presaleWallet = _presaleWallet;
        stakingWallet = _stakingWallet;
        marketingWallet = _marketingWallet;
        rewardsWallet = _rewardsWallet;
        liquidityWallet = _liquidityWallet;
        
        _mint(address(this), TOTAL_SUPPLY);
    }
    
    /**
     * @dev Distribute token allocations to respective wallets
     * Can only be called once by the owner
     */
    function distributeAllocations() external onlyOwner {
        require(!allocationsDistributed, "Allocations already distributed");
        
        uint256 presaleAmount = (TOTAL_SUPPLY * PRESALE_PERCENT) / 100_00;
        uint256 stakingAmount = (TOTAL_SUPPLY * STAKING_PERCENT) / 100_00;
        uint256 marketingAmount = (TOTAL_SUPPLY * MARKETING_PERCENT) / 100_00;
        uint256 rewardsAmount = (TOTAL_SUPPLY * REWARDS_PERCENT) / 100_00;
        uint256 liquidityAmount = (TOTAL_SUPPLY * LIQUIDITY_PERCENT) / 100_00;
        
        // Verify the sum matches total supply (accounting for potential rounding)
        uint256 sum = presaleAmount + stakingAmount + marketingAmount + rewardsAmount + liquidityAmount;
        require(sum <= TOTAL_SUPPLY, "Allocation sum exceeds total supply");
        
        _transfer(address(this), presaleWallet, presaleAmount);
        _transfer(address(this), stakingWallet, stakingAmount);
        _transfer(address(this), marketingWallet, marketingAmount);
        _transfer(address(this), rewardsWallet, rewardsAmount);
        _transfer(address(this), liquidityWallet, liquidityAmount);
        
        allocationsDistributed = true;
    }
    
    /**
     * @dev Update allocation wallets
     * Can only be called by the owner
     */
    function updateAllocationWallets(
        address _presaleWallet,
        address _stakingWallet,
        address _marketingWallet,
        address _rewardsWallet,
        address _liquidityWallet
    ) external onlyOwner {
        require(!allocationsDistributed, "Allocations already distributed");
        require(
            _presaleWallet != address(0) &&
            _stakingWallet != address(0) &&
            _marketingWallet != address(0) &&
            _rewardsWallet != address(0) &&
            _liquidityWallet != address(0),
            "Allocation wallets cannot be zero address"
        );
        
        presaleWallet = _presaleWallet;
        stakingWallet = _stakingWallet;
        marketingWallet = _marketingWallet;
        rewardsWallet = _rewardsWallet;
        liquidityWallet = _liquidityWallet;
    }
}
```
