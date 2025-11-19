"""
Generated Code Metadata:
========================
Original URL: https://borpartoken.com
Prompt: Write a smart contract in Solidity for a memecoin token launch claim process similar to BorpaToken's, including a whitelist and overflow phases.
Generated: DETERMINISTIC_7ae9686827859b1d
Batch ID: 20250622_211357
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

contract MemecoinToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to whitelist status
    mapping(address => bool) public whitelist;

    // Mapping of addresses to claimed status
    mapping(address => bool) public claimed;

    // Overflow phase flag
    bool public overflowPhase;

    // Total supply cap
    uint256 public totalSupplyCap;

    // Whitelist phase cap
    uint256 public whitelistCap;

    // Overflow phase cap
    uint256 public overflowCap;

    // Token launch timestamp
    uint256 public launchTimestamp;

    // Claim deadline
    uint256 public claimDeadline;

    // Event emitted when a user claims tokens
    event Claim(address indexed user, uint256 amount);

    // Event emitted when overflow phase is triggered
    event OverflowPhaseTriggered();

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 totalSupplyCap_,
        uint256 whitelistCap_,
        uint256 overflowCap_,
        uint256 claimDeadline_
    ) ERC20(name_, symbol_) {
        totalSupplyCap = totalSupplyCap_;
        whitelistCap = whitelistCap_;
        overflowCap = overflowCap_;
        claimDeadline = claimDeadline_;
        launchTimestamp = block.timestamp;
    }

    // Add address to whitelist
    function addToWhitelist(address[] memory addresses) public onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = true;
        }
    }

    // Remove address from whitelist
    function removeFromWhitelist(address[] memory addresses) public onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            whitelist[addresses[i]] = false;
        }
    }

    // Trigger overflow phase
    function triggerOverflowPhase() public onlyOwner {
        require(block.timestamp >= launchTimestamp + 1 days, "Cannot trigger overflow phase yet");
        overflowPhase = true;
        emit OverflowPhaseTriggered();
    }

    // Claim tokens
    function claim(uint256 amount) public nonReentrant {
        require(claimed[msg.sender] == false, "Already claimed");
        require(whitelist[msg.sender] || overflowPhase, "Not whitelisted and not in overflow phase");

        if (whitelist[msg.sender]) {
            require(totalSupply().add(amount) <= whitelistCap, "Exceeds whitelist cap");
        } else {
            require(overflowPhase, "Not in overflow phase");
            require(totalSupply().add(amount) <= whitelistCap.add(overflowCap), "Exceeds overflow cap");
        }

        claimed[msg.sender] = true;
        _mint(msg.sender, amount);
        emit Claim(msg.sender, amount);
    }

    // Restrict minting
    function _mint(address account, uint256 amount) internal override {
        require(totalSupply().add(amount) <= totalSupplyCap, "Exceeds total supply cap");
        super._mint(account, amount);
    }

    // Restrict burning
    function _burn(address account, uint256 amount) internal override {
        require(totalSupply().sub(amount) >= 0, "Below zero supply");
        super._burn(account, amount);
    }
}
```
