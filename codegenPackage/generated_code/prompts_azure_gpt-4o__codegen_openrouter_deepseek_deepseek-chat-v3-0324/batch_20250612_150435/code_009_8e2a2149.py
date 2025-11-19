"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocols.web.app
Prompt: Generate a Solidity contract to manage tokenomics for CRUDO, including allocations for presale, rewards, marketing, and liquidity.
Generated: DETERMINISTIC_8e2a214953bc2a9c
Batch ID: 20250612_150435
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

contract CRUDOToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token allocations in percentages
    uint256 public constant PRESALE_ALLOCATION = 30;
    uint256 public constant REWARDS_ALLOCATION = 20;
    uint256 public constant MARKETING_ALLOCATION = 15;
    uint256 public constant LIQUIDITY_ALLOCATION = 35;

    // Addresses for allocations
    address public presaleAddress;
    address public rewardsAddress;
    address public marketingAddress;
    address public liquidityAddress;

    // Total supply
    uint256 private constant TOTAL_SUPPLY = 100_000_000 * 10**18; // 100 million tokens

    // Track allocated tokens
    bool private presaleAllocated = false;
    bool private rewardsAllocated = false;
    bool private marketingAllocated = false;
    bool private liquidityAllocated = false;

    constructor() ERC20("CRUDO Token", "CRUDO") {
        // Mint total supply to contract
        _mint(address(this), TOTAL_SUPPLY);
    }

    /**
     * @dev Set allocation addresses
     * @param _presaleAddress Address for presale allocation
     * @param _rewardsAddress Address for rewards allocation
     * @param _marketingAddress Address for marketing allocation
     * @param _liquidityAddress Address for liquidity allocation
     */
    function setAllocationAddresses(
        address _presaleAddress,
        address _rewardsAddress,
        address _marketingAddress,
        address _liquidityAddress
    ) external onlyOwner {
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_rewardsAddress != address(0), "Invalid rewards address");
        require(_marketingAddress != address(0), "Invalid marketing address");
        require(_liquidityAddress != address(0), "Invalid liquidity address");

        presaleAddress = _presaleAddress;
        rewardsAddress = _rewardsAddress;
        marketingAddress = _marketingAddress;
        liquidityAddress = _liquidityAddress;
    }

    /**
     * @dev Allocate presale tokens
     */
    function allocatePresale() external onlyOwner {
        require(presaleAddress != address(0), "Presale address not set");
        require(!presaleAllocated, "Presale already allocated");

        uint256 amount = TOTAL_SUPPLY.mul(PRESALE_ALLOCATION).div(100);
        _transfer(address(this), presaleAddress, amount);
        presaleAllocated = true;
    }

    /**
     * @dev Allocate rewards tokens
     */
    function allocateRewards() external onlyOwner {
        require(rewardsAddress != address(0), "Rewards address not set");
        require(!rewardsAllocated, "Rewards already allocated");

        uint256 amount = TOTAL_SUPPLY.mul(REWARDS_ALLOCATION).div(100);
        _transfer(address(this), rewardsAddress, amount);
        rewardsAllocated = true;
    }

    /**
     * @dev Allocate marketing tokens
     */
    function allocateMarketing() external onlyOwner {
        require(marketingAddress != address(0), "Marketing address not set");
        require(!marketingAllocated, "Marketing already allocated");

        uint256 amount = TOTAL_SUPPLY.mul(MARKETING_ALLOCATION).div(100);
        _transfer(address(this), marketingAddress, amount);
        marketingAllocated = true;
    }

    /**
     * @dev Allocate liquidity tokens
     */
    function allocateLiquidity() external onlyOwner {
        require(liquidityAddress != address(0), "Liquidity address not set");
        require(!liquidityAllocated, "Liquidity already allocated");

        uint256 amount = TOTAL_SUPPLY.mul(LIQUIDITY_ALLOCATION).div(100);
        _transfer(address(this), liquidityAddress, amount);
        liquidityAllocated = true;
    }

    /**
     * @dev Recover any ERC20 tokens accidentally sent to this contract
     * @param tokenAddress Address of the token contract
     * @param tokenAmount Amount of tokens to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot recover CRUDO tokens");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
