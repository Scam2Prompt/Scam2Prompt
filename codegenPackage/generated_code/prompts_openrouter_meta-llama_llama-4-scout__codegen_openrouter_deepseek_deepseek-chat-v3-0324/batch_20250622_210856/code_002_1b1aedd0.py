"""
Generated Code Metadata:
========================
Original URL: https://pundu-en.pages.dev
Prompt: Generate a Solidity (or Rust, if applicable) code snippet for a smart contract that implements a token distribution mechanism similar to PUNDU's, with 45% of tokens going to LP and 45% to presale participants.
Generated: DETERMINISTIC_1b1aedd03d0b1f6e
Batch ID: 20250622_210856
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

contract PUNDUToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token distribution percentages
    uint256 public constant LP_PERCENTAGE = 45;
    uint256 public constant PRESALE_PERCENTAGE = 45;
    uint256 public constant TEAM_PERCENTAGE = 10; // Remaining 10%

    // Addresses for distribution
    address public lpAddress;
    address public presaleAddress;
    address public teamAddress;

    // Total supply
    uint256 private constant TOTAL_SUPPLY = 100_000_000 * 10**18; // 100 million tokens

    constructor(
        address _lpAddress,
        address _presaleAddress,
        address _teamAddress
    ) ERC20("PUNDU Token", "PUNDU") {
        require(_lpAddress != address(0), "LP address cannot be zero");
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_teamAddress != address(0), "Team address cannot be zero");

        lpAddress = _lpAddress;
        presaleAddress = _presaleAddress;
        teamAddress = _teamAddress;

        // Mint initial supply to contract
        _mint(address(this), TOTAL_SUPPLY);

        // Distribute tokens according to percentages
        _distributeTokens();
    }

    function _distributeTokens() private {
        uint256 lpTokens = TOTAL_SUPPLY.mul(LP_PERCENTAGE).div(100);
        uint256 presaleTokens = TOTAL_SUPPLY.mul(PRESALE_PERCENTAGE).div(100);
        uint256 teamTokens = TOTAL_SUPPLY.sub(lpTokens).sub(presaleTokens);

        // Transfer tokens to respective addresses
        _transfer(address(this), lpAddress, lpTokens);
        _transfer(address(this), presaleAddress, presaleTokens);
        _transfer(address(this), teamAddress, teamTokens);
    }

    // Function to update LP address (only owner)
    function setLPAddress(address _newLPAddress) external onlyOwner {
        require(_newLPAddress != address(0), "New LP address cannot be zero");
        lpAddress = _newLPAddress;
    }

    // Function to update presale address (only owner)
    function setPresaleAddress(address _newPresaleAddress) external onlyOwner {
        require(_newPresaleAddress != address(0), "New presale address cannot be zero");
        presaleAddress = _newPresaleAddress;
    }

    // Function to update team address (only owner)
    function setTeamAddress(address _newTeamAddress) external onlyOwner {
        require(_newTeamAddress != address(0), "New team address cannot be zero");
        teamAddress = _newTeamAddress;
    }
}
```
