"""
Generated Code Metadata:
========================
Original URL: https://fffrfh.pages.dev
Prompt: Write a Solidity function that ensures MOR tokens are non-transferable for the first 90 days after fair launch, as described in the Morpheus documentation. Include logic to enable transfers after this period.
Generated: DETERMINISTIC_efca2957c7c720c4
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Morpheus Token Contract
 * @author [Your Name]
 * @notice This contract represents the MOR token with a 90-day non-transferable period after fair launch.
 */
contract MorpheusToken is ERC20, ReentrancyGuard {
    using SafeMath for uint256;

    // Timestamp when the token was launched
    uint256 public launchTime;

    // Duration of the non-transferable period in seconds (90 days)
    uint256 public constant NON_TRANSFERABLE_PERIOD = 90 days;

    /**
     * @notice Constructor for the MorpheusToken contract
     * @param initialSupply The initial supply of MOR tokens
     */
    constructor(uint256 initialSupply) ERC20("Morpheus", "MOR") {
        // Mint the initial supply to the contract creator
        _mint(msg.sender, initialSupply);

        // Record the launch time
        launchTime = block.timestamp;
    }

    /**
     * @notice Checks if the non-transferable period has expired
     * @return bool True if the non-transferable period has expired, false otherwise
     */
    function isTransferable() public view returns (bool) {
        // Calculate the end of the non-transferable period
        uint256 nonTransferableEnd = launchTime.add(NON_TRANSFERABLE_PERIOD);

        // Check if the current timestamp is greater than or equal to the end of the non-transferable period
        return block.timestamp >= nonTransferableEnd;
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param from The address to transfer tokens from
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     * @return bool True if the transfer was successful, false otherwise
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        // Check if the non-transferable period has expired
        require(isTransferable(), "Transfers are not allowed during the non-transferable period.");

        // Perform the transfer
        return super.transfer(to, amount);
    }

    /**
     * @notice Transfers tokens from one address to another on behalf of the token owner
     * @param from The address to transfer tokens from
     * @param to The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     * @return bool True if the transfer was successful, false otherwise
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        // Check if the non-transferable period has expired
        require(isTransferable(), "Transfers are not allowed during the non-transferable period.");

        // Perform the transfer
        return super.transferFrom(from, to, amount);
    }
}
```
