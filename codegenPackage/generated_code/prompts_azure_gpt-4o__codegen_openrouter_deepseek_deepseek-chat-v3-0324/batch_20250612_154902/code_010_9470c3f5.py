"""
Generated Code Metadata:
========================
Original URL: https://crudo-protocol.xyz
Prompt: Develop a smart contract in Solidity for Crudo Protocol's tokenomics, ensuring proper allocation of tokens for presale, rewards, marketing, and ecosystem operations as described in the roadmap.
Generated: DETERMINISTIC_9470c3f5f5cf9f3a
Batch ID: 20250612_154902
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

contract CrudoToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token allocation percentages (basis points)
    uint256 public constant PRESALE_ALLOCATION = 3000; // 30%
    uint256 public constant REWARDS_ALLOCATION = 2500; // 25%
    uint256 public constant MARKETING_ALLOCATION = 2000; // 20%
    uint256 public constant ECOSYSTEM_ALLOCATION = 2500; // 25%

    // Addresses for token allocations
    address public presaleAddress;
    address public rewardsAddress;
    address public marketingAddress;
    address public ecosystemAddress;

    // Total supply: 1 billion tokens with 18 decimals
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;

    // Track if allocations have been distributed
    bool private _allocationsDistributed = false;

    /**
     * @dev Constructor that initializes the token and mints total supply to owner.
     * Allocation addresses must be set before distribution.
     */
    constructor() ERC20("Crudo Protocol", "CRUDO") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Set allocation addresses. Can only be called by the owner.
     * @param _presaleAddress Address for presale allocation
     * @param _rewardsAddress Address for rewards allocation
     * @param _marketingAddress Address for marketing allocation
     * @param _ecosystemAddress Address for ecosystem allocation
     */
    function setAllocationAddresses(
        address _presaleAddress,
        address _rewardsAddress,
        address _marketingAddress,
        address _ecosystemAddress
    ) external onlyOwner {
        require(!_allocationsDistributed, "Allocations already distributed");
        require(
            _presaleAddress != address(0) &&
                _rewardsAddress != address(0) &&
                _marketingAddress != address(0) &&
                _ecosystemAddress != address(0),
            "Invalid address"
        );

        presaleAddress = _presaleAddress;
        rewardsAddress = _rewardsAddress;
        marketingAddress = _marketingAddress;
        ecosystemAddress = _ecosystemAddress;
    }

    /**
     * @dev Distribute tokens according to allocation percentages.
     * Can only be called by the owner and only once.
     */
    function distributeAllocations() external onlyOwner {
        require(!_allocationsDistributed, "Allocations already distributed");
        require(
            presaleAddress != address(0) &&
                rewardsAddress != address(0) &&
                marketingAddress != address(0) &&
                ecosystemAddress != address(0),
            "Allocation addresses not set"
        );

        _allocationsDistributed = true;

        // Calculate and transfer allocations
        uint256 presaleAmount = TOTAL_SUPPLY.mul(PRESALE_ALLOCATION).div(10000);
        uint256 rewardsAmount = TOTAL_SUPPLY.mul(REWARDS_ALLOCATION).div(10000);
        uint256 marketingAmount = TOTAL_SUPPLY.mul(MARKETING_ALLOCATION).div(10000);
        uint256 ecosystemAmount = TOTAL_SUPPLY.mul(ECOSYSTEM_ALLOCATION).div(10000);

        _transfer(owner(), presaleAddress, presaleAmount);
        _transfer(owner(), rewardsAddress, rewardsAmount);
        _transfer(owner(), marketingAddress, marketingAmount);
        _transfer(owner(), ecosystemAddress, ecosystemAmount);
    }

    /**
     * @dev Override to prevent transfers until allocations are distributed.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);

        // Allow minting and initial distribution
        if (from == address(0) || from == owner()) {
            return;
        }

        require(_allocationsDistributed, "Token transfers are locked until allocations are distributed");
    }
}
```
