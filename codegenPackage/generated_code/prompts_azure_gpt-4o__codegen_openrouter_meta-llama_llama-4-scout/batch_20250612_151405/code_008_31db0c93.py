"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-en.web.app
Prompt: Develop a Solidity smart contract for $SCOTTY token distribution based on the tokenomics provided (e.g., public sale, staking, development, marketing).
Generated: DETERMINISTIC_31db0c933cb7cffd
Batch ID: 20250612_151405
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
 * @title ScottyToken
 * @author [Your Name]
 * @notice Token distribution smart contract for $SCOTTY
 */
contract ScottyToken is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of addresses to their respective roles
    mapping(address => bool) public isStaker;
    mapping(address => bool) public isDeveloper;
    mapping(address => bool) public isMarketer;

    // Tokenomics
    uint256 public publicSaleAmount;
    uint256 public stakingAmount;
    uint256 public developmentAmount;
    uint256 public marketingAmount;

    // Distribution status
    bool public isPublicSaleDistributed;
    bool public isStakingDistributed;
    bool public isDevelopmentDistributed;
    bool public isMarketingDistributed;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total token supply
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        // Mint total supply to owner
        _mint(msg.sender, totalSupply);

        // Initialize tokenomics
        publicSaleAmount = totalSupply * 30 / 100; // 30%
        stakingAmount = totalSupply * 20 / 100; // 20%
        developmentAmount = totalSupply * 20 / 100; // 20%
        marketingAmount = totalSupply * 30 / 100; // 30%
    }

    /**
     * @notice Distribute tokens for public sale
     * @param recipient Recipient address
     */
    function distributePublicSale(address recipient) external onlyOwner {
        require(!isPublicSaleDistributed, "Public sale already distributed");
        require(recipient != address(0), "Invalid recipient");

        uint256 amount = publicSaleAmount;
        _transfer(msg.sender, recipient, amount);

        isPublicSaleDistributed = true;
    }

    /**
     * @notice Distribute tokens for staking
     * @param staker Staker address
     * @param amount Amount to distribute
     */
    function distributeStaking(address staker, uint256 amount) external onlyOwner {
        require(!isStakingDistributed, "Staking already distributed");
        require(staker != address(0), "Invalid staker");
        require(amount <= stakingAmount, "Invalid amount");

        _transfer(msg.sender, staker, amount);
        isStaker[staker] = true;

        isStakingDistributed = true;
    }

    /**
     * @notice Distribute tokens for development
     * @param developer Developer address
     * @param amount Amount to distribute
     */
    function distributeDevelopment(address developer, uint256 amount) external onlyOwner {
        require(!isDevelopmentDistributed, "Development already distributed");
        require(developer != address(0), "Invalid developer");
        require(amount <= developmentAmount, "Invalid amount");

        _transfer(msg.sender, developer, amount);
        isDeveloper[developer] = true;

        isDevelopmentDistributed = true;
    }

    /**
     * @notice Distribute tokens for marketing
     * @param marketer Marketer address
     * @param amount Amount to distribute
     */
    function distributeMarketing(address marketer, uint256 amount) external onlyOwner {
        require(!isMarketingDistributed, "Marketing already distributed");
        require(marketer != address(0), "Invalid marketer");
        require(amount <= marketingAmount, "Invalid amount");

        _transfer(msg.sender, marketer, amount);
        isMarketer[marketer] = true;

        isMarketingDistributed = true;
    }

    /**
     * @notice Restrict token transfer for non-whitelisted addresses
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount to transfer
     */
    function _beforeTokenTransfer(address from, address to, uint256[] memory ids) internal override {
        // Restrict token transfer for non-whitelisted addresses
        if (from == address(0) || to == address(0)) {
            return;
        }

        require(isStaker[to] || isDeveloper[to] || isMarketer[to] || to == owner(), "Invalid recipient");
    }
}
```
