"""
Generated Code Metadata:
========================
Original URL: https://pawthereum.pages.dev
Prompt: Create a Solidity smart contract that integrates with the $PAWTH token for animal welfare initiatives, referencing the community's mission.
Generated: DETERMINISTIC_2f7cf7c85b85dcf4
Batch ID: 20250612_160940
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
 * @title PAWTHAnimalWelfare
 * @dev A smart contract for managing animal welfare initiatives using PAWTH tokens
 * @notice Allows donation, fund allocation, and initiative tracking for animal welfare
 */
contract PAWTHAnimalWelfare is Ownable, ReentrancyGuard {
    // PAWTH token interface
    IERC20 public immutable pawthToken;

    // Initiative structure
    struct Initiative {
        string name;
        string description;
        uint256 targetAmount;
        uint256 raisedAmount;
        bool isActive;
        address beneficiary;
    }

    // Mapping of initiative IDs to Initiative structs
    mapping(uint256 => Initiative) public initiatives;
    uint256 public nextInitiativeId;

    // Events
    event InitiativeCreated(
        uint256 indexed initiativeId,
        string name,
        uint256 targetAmount,
        address beneficiary
    );
    event DonationMade(
        uint256 indexed initiativeId,
        address indexed donor,
        uint256 amount
    );
    event FundsWithdrawn(
        uint256 indexed initiativeId,
        address beneficiary,
        uint256 amount
    );
    event InitiativeStatusChanged(uint256 indexed initiativeId, bool isActive);

    /**
     * @dev Constructor initializes the contract with PAWTH token address
     * @param _pawthTokenAddress Address of the PAWTH ERC20 token
     */
    constructor(address _pawthTokenAddress) {
        require(
            _pawthTokenAddress != address(0),
            "PAWTH token address cannot be zero"
        );
        pawthToken = IERC20(_pawthTokenAddress);
    }

    /**
     * @dev Creates a new animal welfare initiative
     * @param _name Name of the initiative
     * @param _description Description of the initiative
     * @param _targetAmount Target funding amount in PAWTH tokens
     * @param _beneficiary Address that will receive the funds
     */
    function createInitiative(
        string memory _name,
        string memory _description,
        uint256 _targetAmount,
        address _beneficiary
    ) external onlyOwner {
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_targetAmount > 0, "Target amount must be greater than zero");
        require(
            _beneficiary != address(0),
            "Beneficiary address cannot be zero"
        );

        uint256 initiativeId = nextInitiativeId++;
        initiatives[initiativeId] = Initiative({
            name: _name,
            description: _description,
            targetAmount: _targetAmount,
            raisedAmount: 0,
            isActive: true,
            beneficiary: _beneficiary
        });

        emit InitiativeCreated(
            initiativeId,
            _name,
            _targetAmount,
            _beneficiary
        );
    }

    /**
     * @dev Donates PAWTH tokens to a specific initiative
     * @param _initiativeId ID of the initiative to donate to
     * @param _amount Amount of PAWTH tokens to donate
     */
    function donateToInitiative(uint256 _initiativeId, uint256 _amount)
        external
        nonReentrant
    {
        require(_initiativeId < nextInitiativeId, "Invalid initiative ID");
        Initiative storage initiative = initiatives[_initiativeId];
        require(initiative.isActive, "Initiative is not active");
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer PAWTH tokens from donor to this contract
        bool success = pawthToken.transferFrom(
            msg.sender,
            address(this),
            _amount
        );
        require(success, "Token transfer failed");

        initiative.raisedAmount += _amount;

        emit DonationMade(_initiativeId, msg.sender, _amount);
    }

    /**
     * @dev Withdraws funds to the initiative beneficiary
     * @param _initiativeId ID of the initiative to withdraw from
     */
    function withdrawInitiativeFunds(uint256 _initiativeId)
        external
        nonReentrant
    {
        require(_initiativeId < nextInitiativeId, "Invalid initiative ID");
        Initiative storage initiative = initiatives[_initiativeId];
        require(
            msg.sender == initiative.beneficiary || msg.sender == owner(),
            "Not authorized to withdraw"
        );
        require(initiative.raisedAmount > 0, "No funds to withdraw");

        uint256 amount = initiative.raisedAmount;
        initiative.raisedAmount = 0;

        bool success = pawthToken.transfer(initiative.beneficiary, amount);
        require(success, "Token transfer failed");

        emit FundsWithdrawn(_initiativeId, initiative.beneficiary, amount);
    }

    /**
     * @dev Toggles the active status of an initiative
     * @param _initiativeId ID of the initiative to update
     * @param _isActive New status of the initiative
     */
    function setInitiativeStatus(uint256 _initiativeId, bool _isActive)
        external
        onlyOwner
    {
        require(_initiativeId < nextInitiativeId, "Invalid initiative ID");
        Initiative storage initiative = initiatives[_initiativeId];
        initiative.isActive = _isActive;

        emit InitiativeStatusChanged(_initiativeId, _isActive);
    }

    /**
     * @dev Gets initiative details
     * @param _initiativeId ID of the initiative
     * @return Initiative details
     */
    function getInitiative(uint256 _initiativeId)
        external
        view
        returns (
            string memory name,
            string memory description,
            uint256 targetAmount,
            uint256 raisedAmount,
            bool isActive,
            address beneficiary
        )
    {
        require(_initiativeId < nextInitiativeId, "Invalid initiative ID");
        Initiative storage initiative = initiatives[_initiativeId];
        return (
            initiative.name,
            initiative.description,
            initiative.targetAmount,
            initiative.raisedAmount,
            initiative.isActive,
            initiative.beneficiary
        );
    }

    /**
     * @dev Emergency function to recover any ERC20 tokens sent to the contract by mistake
     * @param _tokenAddress Address of the token to recover
     * @param _amount Amount to recover
     */
    function recoverERC20(address _tokenAddress, uint256 _amount)
        external
        onlyOwner
    {
        require(
            _tokenAddress != address(pawthToken),
            "Cannot withdraw PAWTH tokens"
        );
        IERC20(_tokenAddress).transfer(owner(), _amount);
    }
}
```
