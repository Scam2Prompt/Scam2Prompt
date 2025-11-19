"""
Generated Code Metadata:
========================
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Create a Solidity contract to manage the Crudo Protocol's tokenomics, including allocations for presale, rewards, marketing, development, and liquidity, as outlined in the webpage content.
Generated: DETERMINISTIC_7fc4848c725b578b
Batch ID: 20250612_151141
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

contract CrudoToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token allocation percentages (basis points)
    uint256 public constant PRESALE_ALLOCATION = 3000; // 30%
    uint256 public constant REWARDS_ALLOCATION = 2000; // 20%
    uint256 public constant MARKETING_ALLOCATION = 1500; // 15%
    uint256 public constant DEVELOPMENT_ALLOCATION = 1500; // 15%
    uint256 public constant LIQUIDITY_ALLOCATION = 2000; // 20%

    // Allocation addresses
    address public presaleAddress;
    address public rewardsAddress;
    address public marketingAddress;
    address public developmentAddress;
    address public liquidityAddress;

    // Total supply (1 billion tokens with 18 decimals)
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;

    // Track allocated tokens
    bool private presaleAllocated = false;
    bool private rewardsAllocated = false;
    bool private marketingAllocated = false;
    bool private developmentAllocated = false;
    bool private liquidityAllocated = false;

    constructor() ERC20("Crudo Protocol", "CRUDO") {
        // Mint total supply to contract for later distribution
        _mint(address(this), TOTAL_SUPPLY);
    }

    /**
     * @dev Set allocation addresses (can only be called by owner)
     * @param _presale Address for presale allocation
     * @param _rewards Address for rewards allocation
     * @param _marketing Address for marketing allocation
     * @param _development Address for development allocation
     * @param _liquidity Address for liquidity allocation
     */
    function setAllocationAddresses(
        address _presale,
        address _rewards,
        address _marketing,
        address _development,
        address _liquidity
    ) external onlyOwner {
        require(_presale != address(0), "Invalid presale address");
        require(_rewards != address(0), "Invalid rewards address");
        require(_marketing != address(0), "Invalid marketing address");
        require(_development != address(0), "Invalid development address");
        require(_liquidity != address(0), "Invalid liquidity address");

        presaleAddress = _presale;
        rewardsAddress = _rewards;
        marketingAddress = _marketing;
        developmentAddress = _development;
        liquidityAddress = _liquidity;
    }

    /**
     * @dev Allocate presale tokens (can only be called once by owner)
     */
    function allocatePresale() external onlyOwner {
        require(!presaleAllocated, "Presale already allocated");
        require(presaleAddress != address(0), "Presale address not set");

        uint256 amount = TOTAL_SUPPLY.mul(PRESALE_ALLOCATION).div(10000);
        _transfer(address(this), presaleAddress, amount);
        presaleAllocated = true;
    }

    /**
     * @dev Allocate rewards tokens (can only be called once by owner)
     */
    function allocateRewards() external onlyOwner {
        require(!rewardsAllocated, "Rewards already allocated");
        require(rewardsAddress != address(0), "Rewards address not set");

        uint256 amount = TOTAL_SUPPLY.mul(REWARDS_ALLOCATION).div(10000);
        _transfer(address(this), rewardsAddress, amount);
        rewardsAllocated = true;
    }

    /**
     * @dev Allocate marketing tokens (can only be called once by owner)
     */
    function allocateMarketing() external onlyOwner {
        require(!marketingAllocated, "Marketing already allocated");
        require(marketingAddress != address(0), "Marketing address not set");

        uint256 amount = TOTAL_SUPPLY.mul(MARKETING_ALLOCATION).div(10000);
        _transfer(address(this), marketingAddress, amount);
        marketingAllocated = true;
    }

    /**
     * @dev Allocate development tokens (can only be called once by owner)
     */
    function allocateDevelopment() external onlyOwner {
        require(!developmentAllocated, "Development already allocated");
        require(developmentAddress != address(0), "Development address not set");

        uint256 amount = TOTAL_SUPPLY.mul(DEVELOPMENT_ALLOCATION).div(10000);
        _transfer(address(this), developmentAddress, amount);
        developmentAllocated = true;
    }

    /**
     * @dev Allocate liquidity tokens (can only be called once by owner)
     */
    function allocateLiquidity() external onlyOwner {
        require(!liquidityAllocated, "Liquidity already allocated");
        require(liquidityAddress != address(0), "Liquidity address not set");

        uint256 amount = TOTAL_SUPPLY.mul(LIQUIDITY_ALLOCATION).div(10000);
        _transfer(address(this), liquidityAddress, amount);
        liquidityAllocated = true;
    }

    /**
     * @dev Batch allocate all tokens (can only be called by owner)
     * Requires all allocation addresses to be set first
     */
    function batchAllocate() external onlyOwner {
        require(presaleAddress != address(0), "Presale address not set");
        require(rewardsAddress != address(0), "Rewards address not set");
        require(marketingAddress != address(0), "Marketing address not set");
        require(developmentAddress != address(0), "Development address not set");
        require(liquidityAddress != address(0), "Liquidity address not set");

        if (!presaleAllocated) allocatePresale();
        if (!rewardsAllocated) allocateRewards();
        if (!marketingAllocated) allocateMarketing();
        if (!developmentAllocated) allocateDevelopment();
        if (!liquidityAllocated) allocateLiquidity();
    }

    /**
     * @dev Check if all allocations have been completed
     */
    function allocationsComplete() external view returns (bool) {
        return presaleAllocated && 
               rewardsAllocated && 
               marketingAllocated && 
               developmentAllocated && 
               liquidityAllocated;
    }
}
```
