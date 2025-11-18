"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20ai.pages.dev
Prompt: Write a Solidity contract for DOGE20 tokenomics that allocates 10% of the total supply for liquidity provision and 15% for staking rewards.
Generated: DETERMINISTIC_87bf49252562d44e
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DOGE20 Token
 * @dev This contract implements DOGE20 tokenomics, including liquidity provision and staking rewards allocation.
 */
contract DOGE20 is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**decimals(); // 1 Million tokens

    // Address for liquidity provision
    address public liquidityAddress;

    // Address for staking rewards
    address public rewardsAddress;

    // Events for logging
    event LiquidityAddressSet(address indexed previousAddress, address indexed newAddress);
    event RewardsAddressSet(address indexed previousAddress, address indexed newAddress);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens and sets allocation addresses.
     */
    constructor(address _liquidityAddress, address _rewardsAddress) ERC20("DOGE20", "DOGE20") {
        require(_liquidityAddress != address(0), "Invalid liquidity address");
        require(_rewardsAddress != address(0), "Invalid rewards address");

        liquidityAddress = _liquidityAddress;
        rewardsAddress = _rewardsAddress;

        // Mint the total supply and allocate tokens accordingly
        _mint(msg.sender, TOTAL_SUPPLY);
        
        // Allocate 10% for liquidity and 15% for staking rewards
        _transfer(msg.sender, liquidityAddress, TOTAL_SUPPLY * 10 / 100);
        _transfer(msg.sender, rewardsAddress, TOTAL_SUPPLY * 15 / 100);
    }

    /**
     * @dev Sets a new liquidity address.
     * @param _liquidityAddress The new address for liquidity provision.
     */
    function setLiquidityAddress(address _liquidityAddress) external onlyOwner {
        require(_liquidityAddress != address(0), "Invalid liquidity address");
        emit LiquidityAddressSet(liquidityAddress, _liquidityAddress);
        liquidityAddress = _liquidityAddress;
    }

    /**
     * @dev Sets a new rewards address.
     * @param _rewardsAddress The new address for staking rewards.
     */
    function setRewardsAddress(address _rewardsAddress) external onlyOwner {
        require(_rewardsAddress != address(0), "Invalid rewards address");
        emit RewardsAddressSet(rewardsAddress, _rewardsAddress);
        rewardsAddress = _rewardsAddress;
    }

    /**
     * @dev Prevents the contract from receiving Ether.
     */
    receive() external payable {
        revert("Contract does not accept Ether");
    }
}
```
