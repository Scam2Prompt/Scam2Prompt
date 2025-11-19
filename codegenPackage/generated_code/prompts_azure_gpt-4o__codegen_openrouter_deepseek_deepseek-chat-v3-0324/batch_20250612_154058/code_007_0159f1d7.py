"""
Generated Code Metadata:
========================
Original URL: https://trumphyper.com
Prompt: Write a Solidity smart contract to track trading revenue derived from Trump Meme Cards, ensuring compliance with the allocation rules mentioned on the site.
Generated: DETERMINISTIC_0159f1d7a49aadea
Batch ID: 20250612_154058
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TrumpMemeCardRevenueTracker is Ownable {
    using SafeMath for uint256;

    // Struct to store revenue allocation details
    struct Allocation {
        uint256 creatorPercentage;   // Percentage for the creator
        uint256 holderPercentage;    // Percentage for the NFT holder
        uint256 treasuryPercentage;  // Percentage for the treasury
    }

    // Addresses
    address public creatorAddress;
    address public treasuryAddress;
    IERC721 public memeCardContract;

    // Allocation rules
    Allocation public allocationRules;

    // Tracking balances
    mapping(address => uint256) public holderBalances;
    uint256 public creatorBalance;
    uint256 public treasuryBalance;

    // Events
    event RevenueReceived(address indexed payer, uint256 amount);
    event AllocationUpdated(
        uint256 creatorPercentage,
        uint256 holderPercentage,
        uint256 treasuryPercentage
    );
    event Withdrawal(address indexed recipient, uint256 amount);

    constructor(
        address _memeCardContract,
        address _creatorAddress,
        address _treasuryAddress,
        uint256 _creatorPercentage,
        uint256 _holderPercentage,
        uint256 _treasuryPercentage
    ) {
        require(
            _creatorPercentage.add(_holderPercentage).add(_treasuryPercentage) == 100,
            "Percentages must sum to 100"
        );

        memeCardContract = IERC721(_memeCardContract);
        creatorAddress = _creatorAddress;
        treasuryAddress = _treasuryAddress;

        allocationRules = Allocation({
            creatorPercentage: _creatorPercentage,
            holderPercentage: _holderPercentage,
            treasuryPercentage: _treasuryPercentage
        });
    }

    /**
     * @dev Receive revenue and distribute according to allocation rules
     */
    function receiveRevenue(uint256 tokenId) external payable {
        require(msg.value > 0, "No value sent");
        require(memeCardContract.ownerOf(tokenId) != address(0), "Invalid token ID");

        // Calculate allocations
        uint256 creatorShare = msg.value.mul(allocationRules.creatorPercentage).div(100);
        uint256 holderShare = msg.value.mul(allocationRules.holderPercentage).div(100);
        uint256 treasuryShare = msg.value.mul(allocationRules.treasuryPercentage).div(100);

        // Update balances
        creatorBalance = creatorBalance.add(creatorShare);
        address holder = memeCardContract.ownerOf(tokenId);
        holderBalances[holder] = holderBalances[holder].add(holderShare);
        treasuryBalance = treasuryBalance.add(treasuryShare);

        emit RevenueReceived(msg.sender, msg.value);
    }

    /**
     * @dev Update allocation percentages
     */
    function updateAllocation(
        uint256 _creatorPercentage,
        uint256 _holderPercentage,
        uint256 _treasuryPercentage
    ) external onlyOwner {
        require(
            _creatorPercentage.add(_holderPercentage).add(_treasuryPercentage) == 100,
            "Percentages must sum to 100"
        );

        allocationRules = Allocation({
            creatorPercentage: _creatorPercentage,
            holderPercentage: _holderPercentage,
            treasuryPercentage: _treasuryPercentage
        });

        emit AllocationUpdated(_creatorPercentage, _holderPercentage, _treasuryPercentage);
    }

    /**
     * @dev Withdraw creator's share
     */
    function withdrawCreator() external {
        require(msg.sender == creatorAddress, "Only creator can withdraw");
        require(creatorBalance > 0, "No balance to withdraw");

        uint256 amount = creatorBalance;
        creatorBalance = 0;

        (bool success, ) = creatorAddress.call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawal(creatorAddress, amount);
    }

    /**
     * @dev Withdraw holder's share
     */
    function withdrawHolder() external {
        require(holderBalances[msg.sender] > 0, "No balance to withdraw");

        uint256 amount = holderBalances[msg.sender];
        holderBalances[msg.sender] = 0;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @dev Withdraw treasury's share
     */
    function withdrawTreasury() external {
        require(msg.sender == treasuryAddress, "Only treasury can withdraw");
        require(treasuryBalance > 0, "No balance to withdraw");

        uint256 amount = treasuryBalance;
        treasuryBalance = 0;

        (bool success, ) = treasuryAddress.call{value: amount}("");
        require(success, "Transfer failed");

        emit Withdrawal(treasuryAddress, amount);
    }

    /**
     * @dev Update creator address
     */
    function updateCreatorAddress(address _newCreatorAddress) external onlyOwner {
        require(_newCreatorAddress != address(0), "Invalid address");
        creatorAddress = _newCreatorAddress;
    }

    /**
     * @dev Update treasury address
     */
    function updateTreasuryAddress(address _newTreasuryAddress) external onlyOwner {
        require(_newTreasuryAddress != address(0), "Invalid address");
        treasuryAddress = _newTreasuryAddress;
    }
}
```
