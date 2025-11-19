"""
Generated Code Metadata:
========================
Original URL: https://tess-9x2.pages.dev
Prompt: Design a smart contract for secure token distribution on autopilot, inspired by Magna's audited smart contracts on Ethereum and Solana.
Generated: DETERMINISTIC_1e9a6e197c78a6be
Batch ID: 20250622_204552
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title SecureTokenDistributor
 * @dev A secure, automated token distribution contract with vesting capabilities
 */
contract SecureTokenDistributor is Ownable, ReentrancyGuard {
    // Token to be distributed
    IERC20 public immutable token;

    // Distribution parameters
    struct Distribution {
        uint256 totalAmount;
        uint256 releasedAmount;
        uint256 startTime;
        uint256 duration;
        uint256 cliff;
        bool revoked;
    }

    // Beneficiary to distribution mapping
    mapping(address => Distribution) public distributions;

    // Events
    event DistributionCreated(
        address indexed beneficiary,
        uint256 totalAmount,
        uint256 startTime,
        uint256 duration,
        uint256 cliff
    );
    event TokensReleased(address indexed beneficiary, uint256 amount);
    event DistributionRevoked(address indexed beneficiary);

    /**
     * @dev Constructor
     * @param _token Address of the ERC20 token to be distributed
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @dev Creates a new token distribution
     * @param _beneficiary Address of the beneficiary
     * @param _totalAmount Total amount of tokens to distribute
     * @param _startTime When the distribution starts (unix timestamp)
     * @param _duration Duration of the distribution in seconds
     * @param _cliff Cliff period in seconds
     */
    function createDistribution(
        address _beneficiary,
        uint256 _totalAmount,
        uint256 _startTime,
        uint256 _duration,
        uint256 _cliff
    ) external onlyOwner {
        require(_beneficiary != address(0), "Beneficiary cannot be zero");
        require(_totalAmount > 0, "Amount must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");
        require(_cliff <= _duration, "Cliff must be less than or equal to duration");
        require(distributions[_beneficiary].totalAmount == 0, "Distribution already exists");

        distributions[_beneficiary] = Distribution({
            totalAmount: _totalAmount,
            releasedAmount: 0,
            startTime: _startTime,
            duration: _duration,
            cliff: _cliff,
            revoked: false
        });

        emit DistributionCreated(_beneficiary, _totalAmount, _startTime, _duration, _cliff);
    }

    /**
     * @dev Releases vested tokens to beneficiary
     */
    function release() external nonReentrant {
        Distribution storage distribution = distributions[msg.sender];
        require(distribution.totalAmount > 0, "No distribution exists");
        require(!distribution.revoked, "Distribution was revoked");

        uint256 unreleased = _releasableAmount(msg.sender);
        require(unreleased > 0, "No tokens to release");

        distribution.releasedAmount += unreleased;
        require(token.transfer(msg.sender, unreleased), "Token transfer failed");

        emit TokensReleased(msg.sender, unreleased);
    }

    /**
     * @dev Revokes a distribution
     * @param _beneficiary Address of the beneficiary
     */
    function revokeDistribution(address _beneficiary) external onlyOwner {
        Distribution storage distribution = distributions[_beneficiary];
        require(distribution.totalAmount > 0, "No distribution exists");
        require(!distribution.revoked, "Already revoked");

        uint256 unreleased = _releasableAmount(_beneficiary);
        uint256 refund = distribution.totalAmount - distribution.releasedAmount - unreleased;

        distribution.revoked = true;
        distribution.totalAmount = distribution.releasedAmount + unreleased;

        if (refund > 0) {
            require(token.transfer(owner(), refund), "Token transfer failed");
        }

        emit DistributionRevoked(_beneficiary);
    }

    /**
     * @dev Calculates the amount that has already vested but hasn't been released yet
     * @param _beneficiary Address of the beneficiary
     * @return Amount of vested but unreleased tokens
     */
    function _releasableAmount(address _beneficiary) private view returns (uint256) {
        return _vestedAmount(_beneficiary) - distributions[_beneficiary].releasedAmount;
    }

    /**
     * @dev Calculates the amount that has already vested
     * @param _beneficiary Address of the beneficiary
     * @return Amount of vested tokens
     */
    function _vestedAmount(address _beneficiary) private view returns (uint256) {
        Distribution memory distribution = distributions[_beneficiary];
        uint256 totalAllocation = distribution.totalAmount;

        if (block.timestamp < distribution.startTime + distribution.cliff) {
            return 0;
        } else if (block.timestamp >= distribution.startTime + distribution.duration) {
            return totalAllocation;
        } else {
            uint256 timeElapsed = block.timestamp - distribution.startTime;
            return (totalAllocation * timeElapsed) / distribution.duration;
        }
    }

    /**
     * @dev Returns the releasable amount for a beneficiary
     * @param _beneficiary Address of the beneficiary
     * @return Amount of tokens that can be released
     */
    function releasableAmount(address _beneficiary) external view returns (uint256) {
        return _releasableAmount(_beneficiary);
    }

    /**
     * @dev Returns the vested amount for a beneficiary
     * @param _beneficiary Address of the beneficiary
     * @return Amount of tokens that have vested
     */
    function vestedAmount(address _beneficiary) external view returns (uint256) {
        return _vestedAmount(_beneficiary);
    }

    /**
     * @dev Emergency function to withdraw any ERC20 tokens sent to this contract by mistake
     * @param _token Address of the token to withdraw
     * @param _amount Amount to withdraw
     */
    function recoverERC20(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(token), "Cannot withdraw the distribution token");
        IERC20(_token).transfer(owner(), _amount);
    }
}
```
