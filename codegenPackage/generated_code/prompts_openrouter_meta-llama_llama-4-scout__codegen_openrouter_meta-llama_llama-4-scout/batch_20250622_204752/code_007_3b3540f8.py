"""
Generated Code Metadata:
========================
Original URL: https://fffrfh.pages.dev
Prompt: Develop a smart contract in Solidity to automate the distribution of MOR token rewards to Capital Providers and Compute contributors.
Generated: DETERMINISTIC_3b3540f8979189ad
Batch ID: 20250622_204752
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MOR Token Rewards Distribution Contract
 * @author [Your Name]
 * @notice This contract automates the distribution of MOR token rewards to Capital Providers and Compute contributors.
 */
contract MORTokenRewardsDistribution is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective roles
    mapping(address => Role) public roles;

    // Mapping of addresses to their reward balances
    mapping(address => uint256) public rewardBalances;

    // MOR token contract instance
    ERC20 public morToken;

    // Total MOR token rewards available for distribution
    uint256 public totalRewards;

    /**
     * @dev Enum representing the different roles
     */
    enum Role {
        CAPITAL_PROVIDER,
        COMPUTE_CONTRIBUTOR,
        NONE
    }

    /**
     * @dev Event emitted when rewards are distributed
     * @param to Address receiving the rewards
     * @param amount Reward amount
     */
    event RewardsDistributed(address indexed to, uint256 amount);

    /**
     * @dev Event emitted when a role is assigned
     * @param to Address receiving the role
     * @param role Assigned role
     */
    event RoleAssigned(address indexed to, Role role);

    /**
     * @dev Constructor
     * @param _morTokenAddress Address of the MOR token contract
     */
    constructor(address _morTokenAddress) {
        require(_morTokenAddress != address(0), "MOR token address cannot be zero");
        morToken = ERC20(_morTokenAddress);
    }

    /**
     * @dev Assign a role to an address
     * @param _address Address to assign the role to
     * @param _role Role to assign
     */
    function assignRole(address _address, Role _role) public onlyOwner {
        roles[_address] = _role;
        emit RoleAssigned(_address, _role);
    }

    /**
     * @dev Distribute MOR token rewards to Capital Providers and Compute contributors
     * @param _addresses Addresses to distribute rewards to
     * @param _amounts Reward amounts
     */
    function distributeRewards(address[] memory _addresses, uint256[] memory _amounts) public onlyOwner {
        require(_addresses.length == _amounts.length, "Addresses and amounts arrays must have the same length");

        for (uint256 i = 0; i < _addresses.length; i++) {
            address _address = _addresses[i];
            uint256 _amount = _amounts[i];

            require(roles[_address] != Role.NONE, "Address does not have a valid role");
            require(morToken.balanceOf(address(this)) >= _amount, "Insufficient MOR token balance");

            // Update reward balance
            rewardBalances[_address] = rewardBalances[_address].add(_amount);

            // Transfer MOR tokens
            morToken.transfer(_address, _amount);

            emit RewardsDistributed(_address, _amount);
        }

        // Update total rewards
        totalRewards = totalRewards.add(_amounts);
    }

    /**
     * @dev Claim rewards for a specific address
     * @param _address Address to claim rewards for
     */
    function claimRewards(address _address) public {
        require(roles[_address] != Role.NONE, "Address does not have a valid role");

        uint256 _rewardBalance = rewardBalances[_address];
        require(_rewardBalance > 0, "No rewards to claim");

        // Reset reward balance
        rewardBalances[_address] = 0;

        // Transfer MOR tokens
        morToken.transfer(_address, _rewardBalance);
    }

    /**
     * @dev Modifier to restrict access to the owner
     */
    modifier onlyOwner {
        require(msg.sender == owner(), "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Returns the owner of the contract
     * @return address Owner address
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
