"""
Generated Code Metadata:
========================
Original URL: https://mauvworld.pages.dev
Prompt: Generate a smart contract in Solidity that implements a token distribution schedule similar to MAUW's, including locked periods for marketing, staking, and competitions.
Generated: DETERMINISTIC_d252dfef44f9e936
Batch ID: 20250612_150919
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

/**
 * @title MAUW Token Distribution Schedule Smart Contract
 * @author [Your Name]
 * @notice This contract implements a token distribution schedule similar to MAUW's,
 *          including locked periods for marketing, staking, and competitions.
 */
contract MAUWToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Token distribution schedule
    mapping(address => Distribution) public distributions;

    // Distribution periods
    uint256 public constant MARKETING_LOCK_PERIOD = 30 days;
    uint256 public constant STAKING_LOCK_PERIOD = 60 days;
    uint256 public constant COMPETITION_LOCK_PERIOD = 90 days;

    // Distribution types
    enum DistributionType { Marketing, Staking, Competition }

    // Distribution struct
    struct Distribution {
        DistributionType distributionType;
        uint256 lockPeriod;
        uint256 releaseTime;
        uint256 amount;
        bool isReleased;
    }

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply Total token supply
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _mint(msg.sender, totalSupply);

        // Initialize distributions
        distributions[address(this)] = Distribution(
            DistributionType.Marketing,
            MARKETING_LOCK_PERIOD,
            block.timestamp + MARKETING_LOCK_PERIOD,
            totalSupply.mul(20).div(100), // 20%
            false
        );

        distributions[address(0xStaking)] = Distribution(
            DistributionType.Staking,
            STAKING_LOCK_PERIOD,
            block.timestamp + STAKING_LOCK_PERIOD,
            totalSupply.mul(30).div(100), // 30%
            false
        );

        distributions[address(0xCompetition)] = Distribution(
            DistributionType.Competition,
            COMPETITION_LOCK_PERIOD,
            block.timestamp + COMPETITION_LOCK_PERIOD,
            totalSupply.mul(10).div(100), // 10%
            false
        );
    }

    /**
     * @notice Release tokens from distribution
     * @param account Account address
     */
    function releaseTokens(address account) external nonReentrant {
        require(distributions[account].releaseTime <= block.timestamp, "Tokens are not yet releasable");
        require(!distributions[account].isReleased, "Tokens already released");

        uint256 amount = distributions[account].amount;
        distributions[account].isReleased = true;

        _transfer(address(this), account, amount);
    }

    /**
     * @notice Get distribution details
     * @param account Account address
     * @return Distribution details
     */
    function getDistributionDetails(address account) external view returns (
        DistributionType distributionType,
        uint256 lockPeriod,
        uint256 releaseTime,
        uint256 amount,
        bool isReleased
    ) {
        Distribution memory distribution = distributions[account];
        return (
            distribution.distributionType,
            distribution.lockPeriod,
            distribution.releaseTime,
            distribution.amount,
            distribution.isReleased
        );
    }

    /**
     * @dev Hook to prevent direct transfers of tokens
     */
    function _beforeTokenTransfer(address from, address to, uint256[] memory ids) internal virtual override {
        for (uint256 i = 0; i < ids.length; i++) {
            require(from == address(this) || distributions[from].isReleased, "Tokens are locked");
        }
        super._beforeTokenTransfer(from, to, ids);
    }
}
```
