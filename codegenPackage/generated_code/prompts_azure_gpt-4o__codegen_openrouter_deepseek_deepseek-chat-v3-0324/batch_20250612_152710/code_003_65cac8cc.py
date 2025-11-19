"""
Generated Code Metadata:
========================
Original URL: https://basedbrettoken.web.app
Prompt: Create a smart contract on the BASE chain that integrates BRETT token utilities and supports strategic partnerships with other crypto projects.
Generated: DETERMINISTIC_65cac8ccacdc562b
Batch ID: 20250612_152710
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

contract BrettUtility is Ownable, ReentrancyGuard {
    using EnumerableSet for EnumerableSet.AddressSet;

    // BRETT token interface
    IERC20 public brettToken;

    // Partner information
    struct Partner {
        uint256 allocation;
        uint256 claimed;
        uint256 startTime;
        uint256 vestingDuration;
        bool isActive;
    }

    // Partner addresses to their info
    mapping(address => Partner) public partners;

    // Set of all partner addresses
    EnumerableSet.AddressSet private partnerAddresses;

    // Events
    event PartnerAdded(address indexed partner, uint256 allocation, uint256 vestingDuration);
    event PartnerRemoved(address indexed partner);
    event TokensClaimed(address indexed partner, uint256 amount);
    event TokensDeposited(uint256 amount);
    event EmergencyWithdraw(address indexed owner, uint256 amount);

    /**
     * @dev Constructor initializes the BRETT token address
     * @param _brettToken Address of the BRETT token contract
     */
    constructor(address _brettToken) {
        require(_brettToken != address(0), "Invalid token address");
        brettToken = IERC20(_brettToken);
    }

    /**
     * @dev Add a new partner with allocation and vesting details
     * @param _partner Address of the partner
     * @param _allocation Total tokens allocated to partner
     * @param _vestingDuration Vesting duration in seconds
     */
    function addPartner(
        address _partner,
        uint256 _allocation,
        uint256 _vestingDuration
    ) external onlyOwner {
        require(_partner != address(0), "Invalid partner address");
        require(!partnerAddresses.contains(_partner), "Partner already exists");
        require(_allocation > 0, "Allocation must be positive");

        partners[_partner] = Partner({
            allocation: _allocation,
            claimed: 0,
            startTime: block.timestamp,
            vestingDuration: _vestingDuration,
            isActive: true
        });

        partnerAddresses.add(_partner);
        emit PartnerAdded(_partner, _allocation, _vestingDuration);
    }

    /**
     * @dev Remove a partner and revoke unclaimed allocation
     * @param _partner Address of the partner to remove
     */
    function removePartner(address _partner) external onlyOwner {
        require(partnerAddresses.contains(_partner), "Partner does not exist");
        
        Partner storage partner = partners[_partner];
        partner.isActive = false;
        partnerAddresses.remove(_partner);
        
        emit PartnerRemoved(_partner);
    }

    /**
     * @dev Claim vested tokens by partner
     */
    function claimTokens() external nonReentrant {
        require(partnerAddresses.contains(msg.sender), "Not a partner");
        
        Partner storage partner = partners[msg.sender];
        require(partner.isActive, "Partner not active");

        uint256 claimable = calculateClaimable(msg.sender);
        require(claimable > 0, "No tokens to claim");

        partner.claimed += claimable;
        require(brettToken.transfer(msg.sender, claimable), "Transfer failed");

        emit TokensClaimed(msg.sender, claimable);
    }

    /**
     * @dev Calculate claimable tokens for a partner
     * @param _partner Address of the partner
     * @return Amount of tokens currently claimable
     */
    function calculateClaimable(address _partner) public view returns (uint256) {
        if (!partnerAddresses.contains(_partner)) return 0;
        
        Partner memory partner = partners[_partner];
        if (!partner.isActive) return 0;

        if (block.timestamp < partner.startTime) return 0;

        uint256 elapsed = block.timestamp - partner.startTime;
        if (elapsed >= partner.vestingDuration) {
            return partner.allocation - partner.claimed;
        } else {
            uint256 vested = (partner.allocation * elapsed) / partner.vestingDuration;
            return vested - partner.claimed;
        }
    }

    /**
     * @dev Deposit BRETT tokens into the contract
     * @param _amount Amount of tokens to deposit
     */
    function depositTokens(uint256 _amount) external {
        require(_amount > 0, "Amount must be positive");
        require(brettToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        emit TokensDeposited(_amount);
    }

    /**
     * @dev Emergency withdraw tokens (owner only)
     * @param _amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be positive");
        require(brettToken.transfer(owner(), _amount), "Transfer failed");
        emit EmergencyWithdraw(owner(), _amount);
    }

    /**
     * @dev Get total number of partners
     * @return Number of partners
     */
    function getPartnerCount() external view returns (uint256) {
        return partnerAddresses.length();
    }

    /**
     * @dev Get partner address by index
     * @param index Index of partner
     * @return Partner address
     */
    function getPartnerByIndex(uint256 index) external view returns (address) {
        require(index < partnerAddresses.length(), "Index out of bounds");
        return partnerAddresses.at(index);
    }

    /**
     * @dev Check if address is a partner
     * @param _address Address to check
     * @return True if address is a partner
     */
    function isPartner(address _address) external view returns (bool) {
        return partnerAddresses.contains(_address);
    }
}
```
