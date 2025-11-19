"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20claim-now.pages.dev
Prompt: Develop a smart contract in Solidity that implements fixed tokenomics similar to DOGE20, including allocations for presale, marketing, treasury, staking rewards, and liquidity.
Generated: DETERMINISTIC_07ba91af08487c17
Batch ID: 20250612_150552
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract Doge20Token is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics allocations
    uint256 public constant PRESALE_ALLOCATION = 20 * 10**6 * 10**18; // 20%
    uint256 public constant MARKETING_ALLOCATION = 10 * 10**6 * 10**18; // 10%
    uint256 public constant TREASURY_ALLOCATION = 15 * 10**6 * 10**18; // 15%
    uint256 public constant STAKING_REWARDS_ALLOCATION = 20 * 10**6 * 10**18; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 35 * 10**6 * 10**18; // 35%

    // Total supply
    uint256 public constant TOTAL_SUPPLY = 100 * 10**6 * 10**18;

    // Mapping of addresses to their respective allocations
    mapping(address => uint256) public allocations;

    // Presale, marketing, treasury, staking rewards, and liquidity addresses
    address public presaleAddress;
    address public marketingAddress;
    address public treasuryAddress;
    address public stakingRewardsAddress;
    address public liquidityAddress;

    // Flag to track if tokenomics have been allocated
    bool public tokenomicsAllocated;

    // Events
    event TokenomicsAllocated(
        address indexed presaleAddress,
        address indexed marketingAddress,
        address indexed treasuryAddress,
        address stakingRewardsAddress,
        address liquidityAddress
    );

    // Constructor
    constructor() ERC20("DOGE20", "D20") {
        // Mint total supply to the contract address
        _mint(address(this), TOTAL_SUPPLY);
    }

    // Function to allocate tokenomics
    function allocateTokenomics(
        address _presaleAddress,
        address _marketingAddress,
        address _treasuryAddress,
        address _stakingRewardsAddress,
        address _liquidityAddress
    ) external onlyOwner {
        require(!tokenomicsAllocated, "Tokenomics already allocated");

        presaleAddress = _presaleAddress;
        marketingAddress = _marketingAddress;
        treasuryAddress = _treasuryAddress;
        stakingRewardsAddress = _stakingRewardsAddress;
        liquidityAddress = _liquidityAddress;

        allocations[presaleAddress] = PRESALE_ALLOCATION;
        allocations[marketingAddress] = MARKETING_ALLOCATION;
        allocations[treasuryAddress] = TREASURY_ALLOCATION;
        allocations[stakingRewardsAddress] = STAKING_REWARDS_ALLOCATION;
        allocations[liquidityAddress] = LIQUIDITY_ALLOCATION;

        _transfer(address(this), presaleAddress, PRESALE_ALLOCATION);
        _transfer(address(this), marketingAddress, MARKETING_ALLOCATION);
        _transfer(address(this), treasuryAddress, TREASURY_ALLOCATION);
        _transfer(address(this), stakingRewardsAddress, STAKING_REWARDS_ALLOCATION);
        _transfer(address(this), liquidityAddress, LIQUIDITY_ALLOCATION);

        tokenomicsAllocated = true;

        emit TokenomicsAllocated(
            presaleAddress,
            marketingAddress,
            treasuryAddress,
            stakingRewardsAddress,
            liquidityAddress
        );
    }

    // Override transfer function to prevent transfers before tokenomics allocation
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        require(tokenomicsAllocated, "Tokenomics not allocated");

        return super.transfer(recipient, amount);
    }

    // Override transferFrom function to prevent transfers before tokenomics allocation
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        require(tokenomicsAllocated, "Tokenomics not allocated");

        return super.transferFrom(sender, recipient, amount);
    }
}
```
