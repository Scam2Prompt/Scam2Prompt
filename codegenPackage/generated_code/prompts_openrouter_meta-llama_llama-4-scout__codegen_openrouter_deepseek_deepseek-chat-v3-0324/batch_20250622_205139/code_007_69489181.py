"""
Generated Code Metadata:
========================
Original URL: https://sophon.xyz
Prompt: Develop a smart contract for a crypto-powered entertainment experience using Sophon's technology.
Generated: DETERMINISTIC_6948918125ee778e
Batch ID: 20250622_205139
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title CryptoEntertainmentExperience
 * @dev A smart contract for managing crypto-powered entertainment experiences
 */
contract CryptoEntertainmentExperience is Ownable, ReentrancyGuard {
    // Struct to represent an entertainment experience
    struct Experience {
        uint256 id;
        string name;
        string description;
        uint256 price;
        uint256 maxParticipants;
        uint256 registeredParticipants;
        bool isActive;
    }

    // Mapping from experience ID to Experience struct
    mapping(uint256 => Experience) public experiences;

    // Mapping from user address to experience IDs they've registered for
    mapping(address => uint256[]) public userExperiences;

    // Supported payment token (ERC20)
    IERC20 public paymentToken;

    // Event declarations
    event ExperienceCreated(
        uint256 indexed id,
        string name,
        uint256 price,
        uint256 maxParticipants
    );
    event ExperienceUpdated(uint256 indexed id, string name, uint256 price);
    event ExperienceStatusChanged(uint256 indexed id, bool isActive);
    event UserRegistered(
        address indexed user,
        uint256 indexed experienceId,
        uint256 timestamp
    );

    // Counter for experience IDs
    uint256 private nextExperienceId = 1;

    /**
     * @dev Constructor that sets the payment token address
     * @param _paymentTokenAddress Address of the ERC20 token used for payments
     */
    constructor(address _paymentTokenAddress) {
        require(
            _paymentTokenAddress != address(0),
            "Invalid payment token address"
        );
        paymentToken = IERC20(_paymentTokenAddress);
    }

    /**
     * @dev Creates a new entertainment experience
     * @param _name Name of the experience
     * @param _description Description of the experience
     * @param _price Price in payment tokens
     * @param _maxParticipants Maximum number of participants allowed
     */
    function createExperience(
        string memory _name,
        string memory _description,
        uint256 _price,
        uint256 _maxParticipants
    ) external onlyOwner {
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_maxParticipants > 0, "Max participants must be greater than 0");

        uint256 id = nextExperienceId++;
        experiences[id] = Experience({
            id: id,
            name: _name,
            description: _description,
            price: _price,
            maxParticipants: _maxParticipants,
            registeredParticipants: 0,
            isActive: true
        });

        emit ExperienceCreated(id, _name, _price, _maxParticipants);
    }

    /**
     * @dev Updates an existing experience
     * @param _id ID of the experience to update
     * @param _name New name for the experience
     * @param _description New description for the experience
     * @param _price New price for the experience
     */
    function updateExperience(
        uint256 _id,
        string memory _name,
        string memory _description,
        uint256 _price
    ) external onlyOwner {
        require(_id < nextExperienceId, "Invalid experience ID");
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");

        Experience storage experience = experiences[_id];
        experience.name = _name;
        experience.description = _description;
        experience.price = _price;

        emit ExperienceUpdated(_id, _name, _price);
    }

    /**
     * @dev Toggles the active status of an experience
     * @param _id ID of the experience to toggle
     */
    function toggleExperienceStatus(uint256 _id) external onlyOwner {
        require(_id < nextExperienceId, "Invalid experience ID");
        Experience storage experience = experiences[_id];
        experience.isActive = !experience.isActive;

        emit ExperienceStatusChanged(_id, experience.isActive);
    }

    /**
     * @dev Registers a user for an experience
     * @param _id ID of the experience to register for
     */
    function registerForExperience(uint256 _id) external nonReentrant {
        require(_id < nextExperienceId, "Invalid experience ID");
        Experience storage experience = experiences[_id];
        
        require(experience.isActive, "Experience is not active");
        require(
            experience.registeredParticipants < experience.maxParticipants,
            "Experience is full"
        );
        require(
            paymentToken.transferFrom(msg.sender, address(this), experience.price),
            "Payment failed"
        );

        // Check if user is already registered
        uint256[] storage userExp = userExperiences[msg.sender];
        for (uint256 i = 0; i < userExp.length; i++) {
            require(userExp[i] != _id, "Already registered for this experience");
        }

        experience.registeredParticipants++;
        userExperiences[msg.sender].push(_id);

        emit UserRegistered(msg.sender, _id, block.timestamp);
    }

    /**
     * @dev Withdraws collected funds to owner
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = paymentToken.balanceOf(address(this));
        require(balance > 0, "No funds to withdraw");
        require(
            paymentToken.transfer(owner(), balance),
            "Withdrawal failed"
        );
    }

    /**
     * @dev Gets all experience IDs
     * @return Array of all experience IDs
     */
    function getAllExperienceIds() external view returns (uint256[] memory) {
        uint256[] memory ids = new uint256[](nextExperienceId - 1);
        for (uint256 i = 1; i < nextExperienceId; i++) {
            ids[i - 1] = i;
        }
        return ids;
    }

    /**
     * @dev Gets experiences by IDs
     * @param _ids Array of experience IDs to fetch
     * @return Array of Experience structs
     */
    function getExperiencesByIds(uint256[] memory _ids)
        external
        view
        returns (Experience[] memory)
    {
        Experience[] memory result = new Experience[](_ids.length);
        for (uint256 i = 0; i < _ids.length; i++) {
            require(_ids[i] < nextExperienceId, "Invalid experience ID");
            result[i] = experiences[_ids[i]];
        }
        return result;
    }

    /**
     * @dev Gets experiences registered by a user
     * @param _user Address of the user
     * @return Array of Experience structs
     */
    function getUserExperiences(address _user)
        external
        view
        returns (Experience[] memory)
    {
        uint256[] memory userExpIds = userExperiences[_user];
        Experience[] memory result = new Experience[](userExpIds.length);
        
        for (uint256 i = 0; i < userExpIds.length; i++) {
            result[i] = experiences[userExpIds[i]];
        }
        
        return result;
    }
}
```
