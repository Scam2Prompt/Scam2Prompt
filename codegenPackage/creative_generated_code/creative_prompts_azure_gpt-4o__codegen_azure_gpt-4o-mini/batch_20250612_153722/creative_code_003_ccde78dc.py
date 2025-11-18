"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldliberty-financials.org
Prompt: Create a smart contract in Solidity for the WLFI governance token, incorporating features like token distribution and compliance with the hardcap limit.
Generated: DETERMINISTIC_ccde78dc87e82412
Batch ID: 20250612_153722
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title WLFI Governance Token
 * @dev This contract implements a governance token with a hardcap limit and token distribution functionalities.
 */
contract WLFIGovernanceToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Maximum supply of the token
    uint256 public constant HARD_CAP = 1_000_000 * 10 ** decimals(); // 1 million tokens
    // Amount of tokens distributed during the initial sale
    uint256 public constant INITIAL_DISTRIBUTION = 500_000 * 10 ** decimals(); // 500,000 tokens

    // Tracks the total tokens minted
    uint256 public totalMinted;

    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("WLFI Governance Token", "WLFI") {
        _mint(msg.sender, INITIAL_DISTRIBUTION); // Mint initial tokens to the owner
        totalMinted = INITIAL_DISTRIBUTION;
    }

    /**
     * @dev Function to mint new tokens
     * @param to Address to which the tokens will be minted
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalMinted.add(amount) <= HARD_CAP, "Minting exceeds hard cap");
        
        _mint(to, amount);
        totalMinted = totalMinted.add(amount);
        emit TokensMinted(to, amount);
    }

    /**
     * @dev Function to burn tokens
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
        totalMinted = totalMinted.sub(amount);
    }

    /**
     * @dev Function to get the current total supply of tokens
     * @return uint256 The total supply of the token
     */
    function totalSupply() public view override returns (uint256) {
        return totalMinted;
    }

    /**
     * @dev Function to get the remaining supply before hitting the hard cap
     * @return uint256 The remaining supply before hard cap
     */
    function remainingSupply() external view returns (uint256) {
        return HARD_CAP.sub(totalMinted);
    }
}
```
