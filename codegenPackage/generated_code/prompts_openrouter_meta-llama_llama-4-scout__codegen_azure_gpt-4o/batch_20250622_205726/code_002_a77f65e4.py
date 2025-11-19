"""
Generated Code Metadata:
========================
Original URL: https://flokidongerapp.com
Prompt: Design a smart contract for a token with a 8% APR passive yield, similar to FLOKIDONGER, using a library like OpenZeppelin.
Generated: DETERMINISTIC_a77f65e40c0776f6
Batch ID: 20250622_205726
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

// Import OpenZeppelin libraries for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PassiveYieldToken is ERC20, Ownable {
    // APR for passive yield (8% annual yield)
    uint256 public constant APR = 8;
    // Seconds in a year (used for yield calculation)
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    // Mapping to track last claim timestamps for each account
    mapping(address => uint256) private lastClaimTimestamp;

    // Event emitted when yield is claimed
    event YieldClaimed(address indexed account, uint256 amount);

    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        // Mint initial supply to the contract owner
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to calculate pending yield for an account.
     * @param account The address of the account to calculate yield for.
     * @return The amount of yield pending for the account.
     */
    function calculateYield(address account) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastClaimTimestamp[account];
        uint256 balance = balanceOf(account);

        // Calculate yield based on APR, time elapsed, and account balance
        uint256 yield = (balance * APR * timeElapsed) / (100 * SECONDS_IN_YEAR);
        return yield;
    }

    /**
     * @dev Function to claim yield for the caller's account.
     */
    function claimYield() external {
        uint256 yield = calculateYield(msg.sender);

        // Update last claim timestamp
        lastClaimTimestamp[msg.sender] = block.timestamp;

        // Mint the yield to the caller's account
        _mint(msg.sender, yield);

        emit YieldClaimed(msg.sender, yield);
    }

    /**
     * @dev Override transfer function to update last claim timestamp.
     * Ensures yield is calculated correctly for both sender and receiver.
     */
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);

        if (from != address(0)) {
            // Update yield for sender before transfer
            uint256 senderYield = calculateYield(from);
            lastClaimTimestamp[from] = block.timestamp;
            _mint(from, senderYield);
        }

        if (to != address(0)) {
            // Update yield for receiver before transfer
            uint256 receiverYield = calculateYield(to);
            lastClaimTimestamp[to] = block.timestamp;
            _mint(to, receiverYield);
        }
    }

    /**
     * @dev Function to mint new tokens (only callable by the owner).
     * @param account The address to mint tokens to.
     * @param amount The amount of tokens to mint.
     */
    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }

    /**
     * @dev Function to burn tokens (only callable by the owner).
     * @param account The address to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burn(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);
    }
}
```
