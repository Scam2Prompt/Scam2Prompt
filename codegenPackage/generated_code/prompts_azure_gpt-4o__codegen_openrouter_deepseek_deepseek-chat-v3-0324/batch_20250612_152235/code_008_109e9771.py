"""
Generated Code Metadata:
========================
Original URL: https://lopecoin-presale.pages.dev
Prompt: Develop a Solidity contract for managing locked tokens, ensuring a 5-year lock period for team allocations, as described in LopeCoin's tokenomics.
Generated: DETERMINISTIC_109e9771c9d959d4
Batch ID: 20250612_152235
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title LopeCoinTeamLock
 * @dev Contract for managing locked team tokens with a 5-year vesting period
 */
contract LopeCoinTeamLock is Ownable {
    using SafeMath for uint256;

    // The token being locked
    IERC20 public token;

    // Lock duration in seconds (5 years)
    uint256 public constant LOCK_DURATION = 5 * 365 days;

    // Total locked amount
    uint256 public totalLocked;

    // Lock start timestamp
    uint256 public lockStart;

    // Mapping of addresses to their locked amounts
    mapping(address => uint256) public lockedBalances;

    // Mapping of addresses to their claimed amounts
    mapping(address => uint256) public claimedBalances;

    // Events
    event TokensLocked(address indexed beneficiary, uint256 amount);
    event TokensReleased(address indexed beneficiary, uint256 amount);

    /**
     * @dev Constructor
     * @param _token Address of the ERC20 token being locked
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
        lockStart = block.timestamp;
    }

    /**
     * @dev Lock tokens for a beneficiary
     * @param _beneficiary Address of the beneficiary
     * @param _amount Amount of tokens to lock
     */
    function lockTokens(address _beneficiary, uint256 _amount) external onlyOwner {
        require(_beneficiary != address(0), "Beneficiary address cannot be zero");
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from owner to this contract
        require(
            token.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        lockedBalances[_beneficiary] = lockedBalances[_beneficiary].add(_amount);
        totalLocked = totalLocked.add(_amount);

        emit TokensLocked(_beneficiary, _amount);
    }

    /**
     * @dev Release vested tokens to the beneficiary
     */
    function releaseTokens() external {
        uint256 releasable = releasableAmount(msg.sender);
        require(releasable > 0, "No tokens available for release");

        claimedBalances[msg.sender] = claimedBalances[msg.sender].add(releasable);
        totalLocked = totalLocked.sub(releasable);

        require(
            token.transfer(msg.sender, releasable),
            "Token transfer failed"
        );

        emit TokensReleased(msg.sender, releasable);
    }

    /**
     * @dev Calculate the releasable amount for a beneficiary
     * @param _beneficiary Address of the beneficiary
     * @return Amount of tokens that can be released
     */
    function releasableAmount(address _beneficiary) public view returns (uint256) {
        uint256 vested = vestedAmount(_beneficiary);
        return vested.sub(claimedBalances[_beneficiary]);
    }

    /**
     * @dev Calculate the vested amount for a beneficiary
     * @param _beneficiary Address of the beneficiary
     * @return Amount of tokens that have vested
     */
    function vestedAmount(address _beneficiary) public view returns (uint256) {
        uint256 locked = lockedBalances[_beneficiary];
        if (block.timestamp < lockStart) {
            return 0;
        } else if (block.timestamp >= lockStart.add(LOCK_DURATION)) {
            return locked;
        } else {
            return locked.mul(block.timestamp.sub(lockStart)).div(LOCK_DURATION);
        }
    }

    /**
     * @dev Get remaining locked amount for a beneficiary
     * @param _beneficiary Address of the beneficiary
     * @return Amount of tokens still locked
     */
    function remainingLockedAmount(address _beneficiary) external view returns (uint256) {
        return lockedBalances[_beneficiary].sub(claimedBalances[_beneficiary]);
    }
}
```
