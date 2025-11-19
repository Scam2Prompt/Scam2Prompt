"""
Generated Code Metadata:
========================
Original URL: https://pepelovesinu.pages.dev
Prompt: Create a Solidity contract that integrates charitable donations into the Pepe Love Inu ecosystem, leveraging the token's unique value proposition of combining meme culture with financial empowerment.
Generated: DETERMINISTIC_a794ef774f6bb615
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PepeLoveInuCharity
 * @dev A contract that integrates charitable donations into the Pepe Love Inu ecosystem
 */
contract PepeLoveInuCharity is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // The Pepe Love Inu token contract
    IERC20 public pepeLoveInuToken;

    // Charity information
    struct Charity {
        string name;
        string description;
        address walletAddress;
        bool isActive;
        uint256 totalDonated;
    }

    // Mapping of charity IDs to Charity struct
    mapping(uint256 => Charity) public charities;

    // Total number of charities
    uint256 public charityCount;

    // Donation event
    event DonationMade(
        uint256 indexed charityId,
        address indexed donor,
        uint256 amount,
        uint256 timestamp
    );

    // Charity added event
    event CharityAdded(
        uint256 indexed charityId,
        string name,
        address walletAddress
    );

    // Charity status changed event
    event CharityStatusChanged(
        uint256 indexed charityId,
        bool isActive
    );

    /**
     * @dev Constructor function
     * @param _pepeLoveInuToken Address of the Pepe Love Inu token contract
     */
    constructor(address _pepeLoveInuToken) {
        require(_pepeLoveInuToken != address(0), "Invalid token address");
        pepeLoveInuToken = IERC20(_pepeLoveInuToken);
    }

    /**
     * @dev Add a new charity
     * @param _name Name of the charity
     * @param _description Description of the charity
     * @param _walletAddress Wallet address to receive donations
     */
    function addCharity(
        string memory _name,
        string memory _description,
        address _walletAddress
    ) external onlyOwner {
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(_walletAddress != address(0), "Invalid wallet address");

        charityCount++;
        charities[charityCount] = Charity({
            name: _name,
            description: _description,
            walletAddress: _walletAddress,
            isActive: true,
            totalDonated: 0
        });

        emit CharityAdded(charityCount, _name, _walletAddress);
    }

    /**
     * @dev Toggle charity active status
     * @param _charityId ID of the charity to update
     */
    function toggleCharityStatus(uint256 _charityId) external onlyOwner {
        require(_charityId > 0 && _charityId <= charityCount, "Invalid charity ID");
        charities[_charityId].isActive = !charities[_charityId].isActive;
        emit CharityStatusChanged(_charityId, charities[_charityId].isActive);
    }

    /**
     * @dev Donate to a charity
     * @param _charityId ID of the charity to donate to
     * @param _amount Amount of tokens to donate
     */
    function donate(uint256 _charityId, uint256 _amount) external nonReentrant {
        require(_charityId > 0 && _charityId <= charityCount, "Invalid charity ID");
        require(charities[_charityId].isActive, "Charity is not active");
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer tokens from donor to this contract
        bool success = pepeLoveInuToken.transferFrom(
            msg.sender,
            address(this),
            _amount
        );
        require(success, "Token transfer failed");

        // Transfer tokens to charity wallet
        success = pepeLoveInuToken.transfer(
            charities[_charityId].walletAddress,
            _amount
        );
        require(success, "Charity transfer failed");

        // Update donation stats
        charities[_charityId].totalDonated = charities[_charityId].totalDonated.add(_amount);

        emit DonationMade(_charityId, msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Get charity information
     * @param _charityId ID of the charity
     * @return Charity information
     */
    function getCharity(uint256 _charityId) external view returns (
        string memory name,
        string memory description,
        address walletAddress,
        bool isActive,
        uint256 totalDonated
    ) {
        require(_charityId > 0 && _charityId <= charityCount, "Invalid charity ID");
        Charity storage charity = charities[_charityId];
        return (
            charity.name,
            charity.description,
            charity.walletAddress,
            charity.isActive,
            charity.totalDonated
        );
    }

    /**
     * @dev Emergency withdraw any ERC20 tokens sent to this contract by mistake
     * @param _token Address of the token contract
     * @param _amount Amount to withdraw
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(pepeLoveInuToken), "Cannot withdraw Pepe Love Inu tokens");
        IERC20 token = IERC20(_token);
        bool success = token.transfer(owner(), _amount);
        require(success, "Withdrawal failed");
    }
}
```
