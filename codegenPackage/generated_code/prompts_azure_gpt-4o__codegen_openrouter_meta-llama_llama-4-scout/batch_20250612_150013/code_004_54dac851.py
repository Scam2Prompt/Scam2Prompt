"""
Generated Code Metadata:
========================
Original URL: https://popofrogs.pages.dev
Prompt: Write a Solidity contract for a fixed total supply token like $FROP, with allocations for presale, staking, marketing, rewards, and liquidity as outlined in the tokenomics section.
Generated: DETERMINISTIC_54dac851669b0c01
Batch ID: 20250612_150013
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title FROP Token Contract
 * @author [Your Name]
 * @notice A fixed total supply token with allocations for presale, staking, marketing, rewards, and liquidity.
 */
contract FROPToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of address to allocation
    mapping(address => uint256) private _allocations;

    // Allocations
    address public presaleAddress;
    address public stakingAddress;
    address public marketingAddress;
    address public rewardsAddress;
    address public liquidityAddress;

    // Allocation percentages
    uint256 public presaleAllocation;
    uint256 public stakingAllocation;
    uint256 public marketingAllocation;
    uint256 public rewardsAllocation;
    uint256 public liquidityAllocation;

    // Total supply
    uint256 public totalSupply;

    /**
     * @notice Constructor
     * @param _presaleAddress Presale address
     * @param _stakingAddress Staking address
     * @param _marketingAddress Marketing address
     * @param _rewardsAddress Rewards address
     * @param _liquidityAddress Liquidity address
     * @param _presaleAllocation Presale allocation percentage
     * @param _stakingAllocation Staking allocation percentage
     * @param _marketingAllocation Marketing allocation percentage
     * @param _rewardsAllocation Rewards allocation percentage
     * @param _liquidityAllocation Liquidity allocation percentage
     */
    constructor(
        address _presaleAddress,
        address _stakingAddress,
        address _marketingAddress,
        address _rewardsAddress,
        address _liquidityAddress,
        uint256 _presaleAllocation,
        uint256 _stakingAllocation,
        uint256 _marketingAllocation,
        uint256 _rewardsAllocation,
        uint256 _liquidityAllocation
    ) ERC20("FROP", "FROP") {
        require(
            _presaleAllocation + _stakingAllocation + _marketingAllocation + _rewardsAllocation + _liquidityAllocation == 100,
            "Allocations must add up to 100%"
        );

        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        marketingAddress = _marketingAddress;
        rewardsAddress = _rewardsAddress;
        liquidityAddress = _liquidityAddress;

        presaleAllocation = _presaleAllocation;
        stakingAllocation = _stakingAllocation;
        marketingAllocation = _marketingAllocation;
        rewardsAllocation = _rewardsAllocation;
        liquidityAllocation = _liquidityAllocation;

        totalSupply = 10**9 * 10**18; // 1 billion tokens with 18 decimals

        _allocations[presaleAddress] = (presaleAllocation * totalSupply) / 100;
        _allocations[stakingAddress] = (stakingAllocation * totalSupply) / 100;
        _allocations[marketingAddress] = (marketingAllocation * totalSupply) / 100;
        _allocations[rewardsAddress] = (rewardsAllocation * totalSupply) / 100;
        _allocations[liquidityAddress] = (liquidityAllocation * totalSupply) / 100;

        _mint(presaleAddress, _allocations[presaleAddress]);
        _mint(stakingAddress, _allocations[stakingAddress]);
        _mint(marketingAddress, _allocations[marketingAddress]);
        _mint(rewardsAddress, _allocations[rewardsAddress]);
        _mint(liquidityAddress, _allocations[liquidityAddress]);
    }

    /**
     * @notice Get allocation for an address
     * @param _address Address to get allocation for
     * @return Allocation for the address
     */
    function getAllocation(address _address) public view returns (uint256) {
        return _allocations[_address];
    }

    /**
     * @notice Transfer tokens
     * @param _to Address to transfer tokens to
     * @param _amount Amount of tokens to transfer
     * @return Whether the transfer was successful
     */
    function transfer(address _to, uint256 _amount) public override nonReentrant returns (bool) {
        require(_amount > 0, "Transfer amount must be greater than 0");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        _transfer(msg.sender, _to, _amount);
        return true;
    }

    /**
     * @notice Transfer tokens from one address to another
     * @param _from Address to transfer tokens from
     * @param _to Address to transfer tokens to
     * @param _amount Amount of tokens to transfer
     * @return Whether the transfer was successful
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _amount
    ) public override nonReentrant returns (bool) {
        require(_amount > 0, "Transfer amount must be greater than 0");
        require(balanceOf(_from) >= _amount, "Insufficient balance");
        require(allowance(_from, msg.sender) >= _amount, "Insufficient allowance");

        _transfer(_from, _to, _amount);
        _approve(_from, msg.sender, allowance(_from, msg.sender) - _amount);
        return true;
    }

    /**
     * @notice Burn tokens
     * @param _amount Amount of tokens to burn
     */
    function burn(uint256 _amount) public override nonReentrant {
        require(_amount > 0, "Burn amount must be greater than 0");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        _burn(msg.sender, _amount);
    }
}
```
