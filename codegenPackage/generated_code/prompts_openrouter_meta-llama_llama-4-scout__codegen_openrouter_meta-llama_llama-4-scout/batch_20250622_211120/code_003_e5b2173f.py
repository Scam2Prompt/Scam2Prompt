"""
Generated Code Metadata:
========================
Original URL: https://penpie.io
Prompt: Develop a smart contract to lock PNP and get vlPNP at a 1:1 ratio, with a 60-day cooldown period for unlocking vlPNP.
Generated: DETERMINISTIC_e5b2173f5273d3d3
Batch ID: 20250622_211120
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
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title vlPNP Locking Contract
 * @author [Your Name]
 * @notice This contract allows users to lock PNP tokens and receive vlPNP tokens at a 1:1 ratio.
 *          There is a 60-day cooldown period for unlocking vlPNP tokens.
 */
contract vlPNPContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user lock information
    mapping (address => LockInfo) public lockInfo;

    // PNP token contract
    IERC20 public pnpToken;

    // vlPNP token contract
    IERC20 public vlpnpToken;

    // Cooldown period in seconds (60 days)
    uint256 public constant COOLDOWN_PERIOD = 60 * 24 * 60 * 60;

    // Event emitted when user locks PNP tokens
    event LockPNP(address indexed user, uint256 amount);

    // Event emitted when user unlocks vlPNP tokens
    event UnlockvlPNP(address indexed user, uint256 amount);

    /**
     * @param _pnpToken Address of PNP token contract
     * @param _vlpnpToken Address of vlPNP token contract
     */
    constructor(address _pnpToken, address _vlpnpToken) public {
        require(_pnpToken != address(0) && _vlpnpToken != address(0), "Invalid token address");

        pnpToken = IERC20(_pnpToken);
        vlpnpToken = IERC20(_vlpnpToken);
    }

    /**
     * @notice Locks PNP tokens and mints vlPNP tokens at a 1:1 ratio
     * @param amount Amount of PNP tokens to lock
     */
    function lockPNP(uint256 amount) external nonReentrant {
        require(amount > 0, "Invalid lock amount");
        require(pnpToken.balanceOf(msg.sender) >= amount, "Insufficient PNP balance");

        // Transfer PNP tokens to contract
        pnpToken.transferFrom(msg.sender, address(this), amount);

        // Mint vlPNP tokens
        vlpnpToken.mint(msg.sender, amount);

        // Update user lock information
        if (lockInfo[msg.sender].lockEnd > 0) {
            lockInfo[msg.sender].lockedAmount = lockInfo[msg.sender].lockedAmount.add(amount);
            lockInfo[msg.sender].lockEnd = block.timestamp.add(COOLDOWN_PERIOD);
        } else {
            lockInfo[msg.sender] = LockInfo(amount, block.timestamp.add(COOLDOWN_PERIOD));
        }

        emit LockPNP(msg.sender, amount);
    }

    /**
     * @notice Unlocks vlPNP tokens after cooldown period
     */
    function unlockvlPNP() external nonReentrant {
        require(lockInfo[msg.sender].lockEnd > 0 && lockInfo[msg.sender].lockEnd <= block.timestamp, "Cooldown period not over");

        // Burn vlPNP tokens
        vlpnpToken.burn(msg.sender, lockInfo[msg.sender].lockedAmount);

        // Transfer PNP tokens back to user
        pnpToken.transfer(msg.sender, lockInfo[msg.sender].lockedAmount);

        // Reset user lock information
        lockInfo[msg.sender] = LockInfo(0, 0);

        emit UnlockvlPNP(msg.sender, lockInfo[msg.sender].lockedAmount);
    }

    // Struct to store user lock information
    struct LockInfo {
        uint256 lockedAmount;
        uint256 lockEnd;
    }
}
```
