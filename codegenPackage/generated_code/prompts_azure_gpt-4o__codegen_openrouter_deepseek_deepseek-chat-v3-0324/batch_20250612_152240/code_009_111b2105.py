"""
Generated Code Metadata:
========================
Original URL: https://claim-wienerdogs.pages.dev
Prompt: Create a Solidity contract for WienerAI tokenomics, ensuring proper allocation for presale, staking, community rewards, liquidity, and marketing.
Generated: DETERMINISTIC_111b21059f9ec905
Batch ID: 20250612_152240
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

contract WienerAI is ERC20, Ownable {
    using SafeMath for uint256;

    // Token allocation percentages
    uint256 public constant PRESALE_PERCENT = 30;
    uint256 public constant STAKING_PERCENT = 25;
    uint256 public constant COMMUNITY_REWARDS_PERCENT = 20;
    uint256 public constant LIQUIDITY_PERCENT = 15;
    uint256 public constant MARKETING_PERCENT = 10;

    // Allocation addresses
    address public presaleAddress;
    address public stakingAddress;
    address public communityRewardsAddress;
    address public liquidityAddress;
    address public marketingAddress;

    // Total supply (1 trillion tokens with 18 decimals)
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000_000 * 10**18;

    // Track if allocations have been distributed
    bool private allocationsDistributed = false;

    constructor() ERC20("WienerAI", "WAI") {
        _mint(address(this), TOTAL_SUPPLY);
    }

    /**
     * @dev Set allocation addresses (can only be called once by owner)
     * @param _presale Address for presale allocation
     * @param _staking Address for staking rewards
     * @param _community Address for community rewards
     * @param _liquidity Address for liquidity pool
     * @param _marketing Address for marketing funds
     */
    function setAllocationAddresses(
        address _presale,
        address _staking,
        address _community,
        address _liquidity,
        address _marketing
    ) external onlyOwner {
        require(!allocationsDistributed, "Allocations already distributed");
        require(
            _presale != address(0) &&
                _staking != address(0) &&
                _community != address(0) &&
                _liquidity != address(0) &&
                _marketing != address(0),
            "Invalid address"
        );

        presaleAddress = _presale;
        stakingAddress = _staking;
        communityRewardsAddress = _community;
        liquidityAddress = _liquidity;
        marketingAddress = _marketing;
    }

    /**
     * @dev Distribute token allocations to respective addresses
     */
    function distributeAllocations() external onlyOwner {
        require(!allocationsDistributed, "Allocations already distributed");
        require(
            presaleAddress != address(0) &&
                stakingAddress != address(0) &&
                communityRewardsAddress != address(0) &&
                liquidityAddress != address(0) &&
                marketingAddress != address(0),
            "Allocation addresses not set"
        );

        allocationsDistributed = true;

        // Calculate and transfer allocations
        uint256 presaleAmount = TOTAL_SUPPLY.mul(PRESALE_PERCENT).div(100);
        uint256 stakingAmount = TOTAL_SUPPLY.mul(STAKING_PERCENT).div(100);
        uint256 communityAmount = TOTAL_SUPPLY.mul(COMMUNITY_REWARDS_PERCENT).div(100);
        uint256 liquidityAmount = TOTAL_SUPPLY.mul(LIQUIDITY_PERCENT).div(100);
        uint256 marketingAmount = TOTAL_SUPPLY.mul(MARKETING_PERCENT).div(100);

        _transfer(address(this), presaleAddress, presaleAmount);
        _transfer(address(this), stakingAddress, stakingAmount);
        _transfer(address(this), communityRewardsAddress, communityAmount);
        _transfer(address(this), liquidityAddress, liquidityAmount);
        _transfer(address(this), marketingAddress, marketingAmount);
    }

    /**
     * @dev Recover any ERC20 tokens accidentally sent to this contract
     * @param tokenAddress Address of the token contract
     * @param tokenAmount Amount of tokens to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
