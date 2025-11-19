"""
Generated Code Metadata:
========================
Original URL: https://doge2014sale.pages.dev
Prompt: Develop a function in Solidity to handle token allocation for the Doge2014 presale, considering the 60% presale allocation, 25% staking allocation, 10% liquidity allocation, and 5% marketing allocation.
Generated: DETERMINISTIC_84ec2ff2f985f8bc
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Doge2014TokenAllocation is Ownable {
    using SafeMath for uint256;

    IERC20 public token;

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 60;
    uint256 public constant STAKING_ALLOCATION = 25;
    uint256 public constant LIQUIDITY_ALLOCATION = 10;
    uint256 public constant MARKETING_ALLOCATION = 5;

    // Allocation addresses
    address public presaleAddress;
    address public stakingAddress;
    address public liquidityAddress;
    address public marketingAddress;

    // Track allocated tokens
    bool public tokensAllocated = false;

    event TokensAllocated(
        uint256 presaleAmount,
        uint256 stakingAmount,
        uint256 liquidityAmount,
        uint256 marketingAmount
    );

    constructor(
        IERC20 _token,
        address _presaleAddress,
        address _stakingAddress,
        address _liquidityAddress,
        address _marketingAddress
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_stakingAddress != address(0), "Staking address cannot be zero");
        require(_liquidityAddress != address(0), "Liquidity address cannot be zero");
        require(_marketingAddress != address(0), "Marketing address cannot be zero");

        token = _token;
        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;
    }

    function allocateTokens() external onlyOwner {
        require(!tokensAllocated, "Tokens already allocated");
        
        uint256 totalSupply = token.totalSupply();
        require(totalSupply > 0, "Token has no supply");

        uint256 presaleAmount = totalSupply.mul(PRESALE_ALLOCATION).div(100);
        uint256 stakingAmount = totalSupply.mul(STAKING_ALLOCATION).div(100);
        uint256 liquidityAmount = totalSupply.mul(LIQUIDITY_ALLOCATION).div(100);
        uint256 marketingAmount = totalSupply.mul(MARKETING_ALLOCATION).div(100);

        // Verify allocations sum to total supply (accounting for potential rounding)
        uint256 allocatedTotal = presaleAmount.add(stakingAmount).add(liquidityAmount).add(marketingAmount);
        require(allocatedTotal <= totalSupply, "Allocation exceeds total supply");

        // Transfer tokens to respective addresses
        require(token.transfer(presaleAddress, presaleAmount), "Presale transfer failed");
        require(token.transfer(stakingAddress, stakingAmount), "Staking transfer failed");
        require(token.transfer(liquidityAddress, liquidityAmount), "Liquidity transfer failed");
        require(token.transfer(marketingAddress, marketingAmount), "Marketing transfer failed");

        tokensAllocated = true;

        emit TokensAllocated(
            presaleAmount,
            stakingAmount,
            liquidityAmount,
            marketingAmount
        );
    }

    function updateAllocationAddresses(
        address _presaleAddress,
        address _stakingAddress,
        address _liquidityAddress,
        address _marketingAddress
    ) external onlyOwner {
        require(!tokensAllocated, "Cannot change addresses after allocation");
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_stakingAddress != address(0), "Staking address cannot be zero");
        require(_liquidityAddress != address(0), "Liquidity address cannot be zero");
        require(_marketingAddress != address(0), "Marketing address cannot be zero");

        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;
    }
}
```
