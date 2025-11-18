"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-in.pages.dev
Prompt: Develop a feature in Solidity that locks team tokens for 18 months and burns unsold tokens after the presale, as outlined in ETFSwap's anti-dump plan.
Generated: DETERMINISTIC_d4ced457e525bf35
Batch ID: 20250612_153401
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

/**
 * @title ETFSwapTokenLocker
 * @dev A contract to lock team tokens for 18 months and burn unsold tokens after presale.
 */
contract ETFSwapTokenLocker {
    // ERC20 token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
        function burn(uint256 amount) external;
    }

    // State variables
    IERC20 public token; // Token contract reference
    address public owner; // Contract owner
    address public teamWallet; // Wallet holding the team tokens
    uint256 public lockEndTimestamp; // Timestamp when lock period ends
    bool public presaleEnded; // Flag to track presale status
    uint256 public unsoldTokens; // Amount of unsold tokens to be burned

    // Events
    event TeamTokensLocked(address teamWallet, uint256 lockEndTimestamp);
    event TokensBurned(uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier afterLockPeriod() {
        require(block.timestamp >= lockEndTimestamp, "Lock period has not ended");
        _;
    }

    modifier presaleEndedCheck() {
        require(presaleEnded, "Presale has not ended");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the ERC20 token contract.
     * @param _teamWallet Address of the team wallet.
     */
    constructor(IERC20 _token, address _teamWallet) {
        require(address(_token) != address(0), "Invalid token address");
        require(_teamWallet != address(0), "Invalid team wallet address");

        token = _token;
        teamWallet = _teamWallet;
        owner = msg.sender;
        lockEndTimestamp = block.timestamp + 18 * 30 days; // Lock for 18 months (approx)
    }

    /**
     * @dev Function to lock team tokens.
     */
    function lockTeamTokens() external onlyOwner {
        emit TeamTokensLocked(teamWallet, lockEndTimestamp);
    }

    /**
     * @dev Function to end presale and set unsold tokens for burning.
     * @param _unsoldTokens Amount of unsold tokens to be burned.
     */
    function endPresale(uint256 _unsoldTokens) external onlyOwner {
        require(!presaleEnded, "Presale already ended");
        presaleEnded = true;
        unsoldTokens = _unsoldTokens;
    }

    /**
     * @dev Function to burn unsold tokens after presale.
     */
    function burnUnsoldTokens() external onlyOwner presaleEndedCheck {
        require(unsoldTokens > 0, "No unsold tokens to burn");
        token.burn(unsoldTokens);
        emit TokensBurned(unsoldTokens);
        unsoldTokens = 0; // Reset unsold tokens after burning
    }

    /**
     * @dev Function to release team tokens after lock period ends.
     */
    function releaseTeamTokens() external onlyOwner afterLockPeriod {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to release");

        token.transfer(teamWallet, balance);
    }
}
```
