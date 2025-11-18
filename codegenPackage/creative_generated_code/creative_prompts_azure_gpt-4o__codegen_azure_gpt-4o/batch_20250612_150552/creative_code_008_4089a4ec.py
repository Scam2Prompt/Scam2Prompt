"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://burncat-buy.pages.dev
Prompt: Develop a smart contract in Solidity that prevents sniping bots during token listing by implementing a high initial tax rate that decreases over time, as described for $BCAT.
Generated: DETERMINISTIC_4089a4ec11f5d058
Batch ID: 20250612_150552
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
 * @title AntiSnipingToken
 * @dev Implements a token with a high initial tax rate that decreases over time to prevent sniping bots.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BCATToken is ERC20, Ownable {
    // Initial tax rate (in basis points, e.g., 10000 = 100%)
    uint256 public constant INITIAL_TAX_RATE_BP = 2000; // 20%
    // Minimum tax rate (in basis points)
    uint256 public constant MINIMUM_TAX_RATE_BP = 100; // 1%
    // Duration over which the tax rate decreases (in seconds)
    uint256 public constant TAX_DECREASE_DURATION = 1 days;

    // Timestamp of the token listing
    uint256 public listingStartTimestamp;
    // Address where the tax is collected
    address public taxCollector;

    /**
     * @dev Modifier to ensure listing has started.
     */
    modifier listingStarted() {
        require(listingStartTimestamp != 0, "Listing has not started");
        _;
    }

    /**
     * @notice Constructor
     * @param _initialSupply Initial token supply
     * @param _taxCollector Address to collect tax
     */
    constructor(uint256 _initialSupply, address _taxCollector) ERC20("BCAT Token", "BCAT") {
        require(_taxCollector != address(0), "Invalid tax collector address");
        taxCollector = _taxCollector;
        _mint(msg.sender, _initialSupply);
    }

    /**
     * @notice Set the listing start time
     * @dev Can only be called once by the owner
     */
    function startListing() external onlyOwner {
        require(listingStartTimestamp == 0, "Listing already started");
        listingStartTimestamp = block.timestamp;
    }

    /**
     * @dev Calculates the current tax rate based on the time elapsed since listing.
     * @return Current tax rate (in basis points)
     */
    function currentTaxRate() public view returns (uint256) {
        if (listingStartTimestamp == 0 || block.timestamp <= listingStartTimestamp) {
            return INITIAL_TAX_RATE_BP;
        }

        uint256 elapsedTime = block.timestamp - listingStartTimestamp;

        if (elapsedTime >= TAX_DECREASE_DURATION) {
            return MINIMUM_TAX_RATE_BP;
        }

        uint256 taxDecrease = INITIAL_TAX_RATE_BP - MINIMUM_TAX_RATE_BP;
        uint256 taxReduction = (taxDecrease * elapsedTime) / TAX_DECREASE_DURATION;

        return INITIAL_TAX_RATE_BP - taxReduction;
    }

    /**
     * @dev Overrides the ERC20 transfer function to include tax logic.
     * @param recipient Address to receive tokens
     * @param amount Amount of tokens to transfer
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override listingStarted {
        uint256 taxRateBp = currentTaxRate();
        uint256 taxAmount = (amount * taxRateBp) / 10000;
        uint256 transferAmount = amount - taxAmount;

        // Ensure tax is sent to the tax collector
        if (taxAmount > 0) {
            super._transfer(sender, taxCollector, taxAmount);
        }

        // Transfer the remaining amount to the recipient
        super._transfer(sender, recipient, transferAmount);
    }

    /**
     * @notice Update the tax collector address
     * @dev Can only be called by the owner
     * @param _taxCollector New tax collector address
     */
    function updateTaxCollector(address _taxCollector) external onlyOwner {
        require(_taxCollector != address(0), "Invalid tax collector address");
        taxCollector = _taxCollector;
    }
}
```
