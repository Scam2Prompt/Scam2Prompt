"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-ai.pages.dev
Prompt: Generate code for a token burn program in Solidity, ensuring unsold tokens from a presale are burned and implementing a periodic burn every three months for three years.
Generated: DETERMINISTIC_808cada97af62761
Batch ID: 20250612_152249
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
 * @title TokenBurner
 * @dev A contract to handle unsold token burns after a presale and periodic burns every three months for three years.
 */
contract TokenBurner {
    IERC20 public immutable token; // ERC20 token to be burned
    address public immutable presaleAddress; // Address holding unsold tokens
    uint256 public immutable periodicBurnAmount; // Amount of tokens to burn every three months
    uint256 public immutable burnStartTime; // Start time for periodic burn
    uint256 public constant BURN_INTERVAL = 90 days; // 3-month interval
    uint256 public constant MAX_BURN_PERIODS = 12; // 12 periods (3 years)
    uint256 public periodicBurnsExecuted; // Counter for periodic burns

    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @dev Initializes the contract.
     * @param _token Address of the ERC20 token.
     * @param _presaleAddress Address holding unsold tokens.
     * @param _periodicBurnAmount Amount of tokens to burn every 3 months.
     * @param _burnStartTime Start time for periodic burns.
     */
    constructor(
        IERC20 _token,
        address _presaleAddress,
        uint256 _periodicBurnAmount,
        uint256 _burnStartTime
    ) {
        require(address(_token) != address(0), "TokenBurner: Invalid token address");
        require(_presaleAddress != address(0), "TokenBurner: Invalid presale address");
        require(_periodicBurnAmount > 0, "TokenBurner: Burn amount must be greater than 0");
        require(_burnStartTime > block.timestamp, "TokenBurner: Burn start time must be in the future");

        token = _token;
        presaleAddress = _presaleAddress;
        periodicBurnAmount = _periodicBurnAmount;
        burnStartTime = _burnStartTime;
    }

    /**
     * @dev Burns unsold tokens from presale.
     * Callable once after the presale has ended.
     */
    function burnUnsoldTokens() external {
        uint256 unsoldTokens = token.balanceOf(presaleAddress);
        require(unsoldTokens > 0, "TokenBurner: No unsold tokens to burn");
        require(token.transferFrom(presaleAddress, address(0), unsoldTokens), "TokenBurner: Burn failed");

        emit TokensBurned(presaleAddress, unsoldTokens);
    }

    /**
     * @dev Burns tokens periodically every three months.
     * Can only execute up to 12 times (3 years) and must adhere to the interval.
     */
    function burnPeriodicTokens() external {
        require(periodicBurnsExecuted < MAX_BURN_PERIODS, "TokenBurner: Max periodic burns reached");
        uint256 currentPeriod = (block.timestamp - burnStartTime) / BURN_INTERVAL;
        require(currentPeriod > periodicBurnsExecuted, "TokenBurner: Invalid burn period");

        require(token.balanceOf(address(this)) >= periodicBurnAmount, "TokenBurner: Insufficient tokens to burn");
        require(token.transfer(address(0), periodicBurnAmount), "TokenBurner: Burn failed");

        periodicBurnsExecuted++;
        emit TokensBurned(address(this), periodicBurnAmount);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);

    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
