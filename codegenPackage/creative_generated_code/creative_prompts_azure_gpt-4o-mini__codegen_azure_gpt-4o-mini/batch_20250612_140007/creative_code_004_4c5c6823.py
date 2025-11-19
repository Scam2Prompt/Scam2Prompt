"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://velodrome-7zz.pages.dev
Prompt: Provide an example of a smart contract that allows users to lock their tokens and convert them to veVELO for governance participation.
Generated: DETERMINISTIC_4c5c6823a39d453e
Batch ID: 20250612_140007
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

// Importing SafeERC20 to safely handle ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the VELO token contract
interface IVeVELO {
    function lockTokens(address user, uint256 amount) external;
}

contract TokenLocker is Ownable {
    using SafeERC20 for IERC20;

    // ERC20 token instance
    IERC20 public token;
    // veVELO contract instance
    IVeVELO public veVELO;

    // Mapping to keep track of locked tokens for each user
    mapping(address => uint256) public lockedBalances;

    // Event emitted when tokens are locked
    event TokensLocked(address indexed user, uint256 amount);
    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, uint256 amount);

    // Constructor to set the token and veVELO contract addresses
    constructor(IERC20 _token, IVeVELO _veVELO) {
        token = _token;
        veVELO = _veVELO;
    }

    /**
     * @notice Locks tokens for governance participation
     * @param amount The amount of tokens to lock
     */
    function lockTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the user to the contract
        token.safeTransferFrom(msg.sender, address(this), amount);

        // Update the locked balance
        lockedBalances[msg.sender] += amount;

        // Call the VELO contract to lock tokens for governance
        veVELO.lockTokens(msg.sender, amount);

        emit TokensLocked(msg.sender, amount);
    }

    /**
     * @notice Unlocks tokens and transfers them back to the user
     * @param amount The amount of tokens to unlock
     */
    function unlockTokens(uint256 amount) external {
        require(lockedBalances[msg.sender] >= amount, "Insufficient locked balance");

        // Update the locked balance
        lockedBalances[msg.sender] -= amount;

        // Transfer tokens back to the user
        token.safeTransfer(msg.sender, amount);

        emit TokensUnlocked(msg.sender, amount);
    }

    /**
     * @notice Allows the owner to withdraw any tokens sent to the contract
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        
        // Transfer tokens to the owner
        token.safeTransfer(owner(), amount);
    }

    // Fallback function to accept ETH (if needed)
    receive() external payable {}
}
```
