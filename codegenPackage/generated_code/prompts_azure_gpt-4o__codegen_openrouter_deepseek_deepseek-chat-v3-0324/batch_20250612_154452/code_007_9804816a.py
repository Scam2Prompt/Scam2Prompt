"""
Generated Code Metadata:
========================
Original URL: https://growbit.tech
Prompt: Write a Solidity contract for tokenomics similar to GrowBTC, including features like capped supply, locked tokens for a specific duration, and transparent allocation.
Generated: DETERMINISTIC_9804816a794b483a
Batch ID: 20250612_154452
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

/**
 * @title GrowBTC-like Token Contract
 * @dev ERC20 token with capped supply, locked tokens, and transparent allocation
 */
contract GrowLikeToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token supply constants
    uint256 public constant MAX_SUPPLY = 21_000_000 * 10**18; // 21 million tokens with 18 decimals
    uint256 public constant TEAM_ALLOCATION = 2_100_000 * 10**18; // 10% for team
    uint256 public constant ECOSYSTEM_ALLOCATION = 4_200_000 * 10**18; // 20% for ecosystem
    uint256 public constant PUBLIC_SALE_ALLOCATION = 10_500_000 * 10**18; // 50% for public sale
    uint256 public constant ADVISORS_ALLOCATION = 2_100_000 * 10**18; // 10% for advisors
    uint256 public constant MARKETING_ALLOCATION = 2_100_000 * 10**18; // 10% for marketing

    // Lockup periods (in seconds)
    uint256 public constant TEAM_LOCKUP = 365 days;
    uint256 public constant ADVISORS_LOCKUP = 180 days;
    uint256 public constant ECOSYSTEM_LOCKUP = 90 days;

    // Allocation addresses
    address public teamAddress;
    address public ecosystemAddress;
    address public advisorsAddress;
    address public marketingAddress;

    // Lockup tracking
    mapping(address => uint256) private _lockedUntil;
    mapping(address => uint256) private _lockedAmounts;

    // Track minted allocations
    bool private _teamMinted;
    bool private _ecosystemMinted;
    bool private _publicSaleMinted;
    bool private _advisorsMinted;
    bool private _marketingMinted;

    event TokensLocked(address indexed beneficiary, uint256 amount, uint256 until);
    event TokensReleased(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor that sets up initial allocations
     * @param _teamAddress Address for team allocation
     * @param _ecosystemAddress Address for ecosystem allocation
     * @param _advisorsAddress Address for advisors allocation
     * @param _marketingAddress Address for marketing allocation
     */
    constructor(
        address _teamAddress,
        address _ecosystemAddress,
        address _advisorsAddress,
        address _marketingAddress
    ) ERC20("GrowLikeToken", "GLT") {
        require(_teamAddress != address(0), "Team address cannot be zero");
        require(_ecosystemAddress != address(0), "Ecosystem address cannot be zero");
        require(_advisorsAddress != address(0), "Advisors address cannot be zero");
        require(_marketingAddress != address(0), "Marketing address cannot be zero");

        teamAddress = _teamAddress;
        ecosystemAddress = _ecosystemAddress;
        advisorsAddress = _advisorsAddress;
        marketingAddress = _marketingAddress;
    }

    /**
     * @dev Mint initial allocations with lockup periods where applicable
     */
    function mintAllocations() external onlyOwner {
        require(!_teamMinted, "Team allocation already minted");
        require(!_ecosystemMinted, "Ecosystem allocation already minted");
        require(!_publicSaleMinted, "Public sale allocation already minted");
        require(!_advisorsMinted, "Advisors allocation already minted");
        require(!_marketingMinted, "Marketing allocation already minted");

        // Mint team allocation with lockup
        _mintWithLock(teamAddress, TEAM_ALLOCATION, block.timestamp.add(TEAM_LOCKUP));
        _teamMinted = true;

        // Mint ecosystem allocation with lockup
        _mintWithLock(ecosystemAddress, ECOSYSTEM_ALLOCATION, block.timestamp.add(ECOSYSTEM_LOCKUP));
        _ecosystemMinted = true;

        // Mint public sale allocation (no lockup)
        _mint(owner(), PUBLIC_SALE_ALLOCATION);
        _publicSaleMinted = true;

        // Mint advisors allocation with lockup
        _mintWithLock(advisorsAddress, ADVISORS_ALLOCATION, block.timestamp.add(ADVISORS_LOCKUP));
        _advisorsMinted = true;

        // Mint marketing allocation (no lockup)
        _mint(marketingAddress, MARKETING_ALLOCATION);
        _marketingMinted = true;
    }

    /**
     * @dev Internal function to mint tokens with lockup period
     * @param to Address receiving the tokens
     * @param amount Amount of tokens to mint and lock
     * @param until Timestamp when tokens become unlocked
     */
    function _mintWithLock(address to, uint256 amount, uint256 until) internal {
        _mint(address(this), amount);
        _lockedUntil[to] = until;
        _lockedAmounts[to] = _lockedAmounts[to].add(amount);
        emit TokensLocked(to, amount, until);
    }

    /**
     * @dev Release locked tokens when lockup period is over
     */
    function releaseLockedTokens() external {
        require(_lockedAmounts[msg.sender] > 0, "No locked tokens");
        require(block.timestamp >= _lockedUntil[msg.sender], "Tokens are still locked");

        uint256 amount = _lockedAmounts[msg.sender];
        _lockedAmounts[msg.sender] = 0;
        _transfer(address(this), msg.sender, amount);
        emit TokensReleased(msg.sender, amount);
    }

    /**
     * @dev Override transfer to prevent locked tokens from being transferred
     * @param sender Address sending the tokens
     * @param recipient Address receiving the tokens
     * @param amount Amount of tokens to transfer
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        if (_lockedAmounts[sender] > 0) {
            uint256 availableBalance = balanceOf(sender).sub(_lockedAmounts[sender]);
            require(availableBalance >= amount, "Transfer amount exceeds available unlocked tokens");
        }
        super._transfer(sender, recipient, amount);
    }

    /**
     * @dev Get locked token information for an address
     * @param account Address to query
     * @return amount Locked token amount
     * @return until Lockup expiration timestamp
     */
    function getLockedInfo(address account) external view returns (uint256 amount, uint256 until) {
        return (_lockedAmounts[account], _lockedUntil[account]);
    }

    /**
     * @dev Get available unlocked balance for an address
     * @param account Address to query
     * @return Available unlocked token balance
     */
    function availableBalance(address account) external view returns (uint256) {
        return balanceOf(account).sub(_lockedAmounts[account]);
    }
}
```
