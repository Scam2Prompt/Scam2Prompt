"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubetas-ai.pages.dev
Prompt: How do I develop a decentralized application (dApp) that allows users to apply for listing on the InQubeta NFT marketplace for AI start-ups?
Generated: DETERMINISTIC_71f5f1e05ae12739
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary OpenZeppelin Contracts
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Define the main contract for the InQubeta NFT marketplace
contract InQubetaMarketplace is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent an AI startup application
    struct StartupApplication {
        uint256 id;
        string name;
        string description;
        address applicant;
        bool isListed;
        uint256 createdAt;
    }

    // Counters to keep track of applications
    Counters.Counter private _applicationIdCounter;

    // Mapping from application ID to StartupApplication
    mapping(uint256 => StartupApplication) private applications;

    // Event emitted when a new application is created
    event ApplicationCreated(uint256 indexed id, string name, address indexed applicant);
    
    // Event emitted when an application is listed
    event ApplicationListed(uint256 indexed id, address indexed applicant);
    
    // Event emitted when an application is removed from listing
    event ApplicationRemoved(uint256 indexed id, address indexed applicant);

    /**
     * @dev Apply for listing on the NFT marketplace
     * @param _name The name of the AI startup
     * @param _description A brief description of the startup
     */
    function applyForListing(string memory _name, string memory _description) external {
        require(bytes(_name).length > 0, "Startup name cannot be empty");
        require(bytes(_description).length > 0, "Description cannot be empty");

        // Increment application ID and create a new application
        _applicationIdCounter.increment();
        uint256 newApplicationId = _applicationIdCounter.current();

        applications[newApplicationId] = StartupApplication({
            id: newApplicationId,
            name: _name,
            description: _description,
            applicant: msg.sender,
            isListed: false,
            createdAt: block.timestamp
        });

        // Emit the ApplicationCreated event
        emit ApplicationCreated(newApplicationId, _name, msg.sender);
    }

    /**
     * @dev List an application to the marketplace by its ID
     * @param _applicationId The ID of the application to list
     */
    function listApplication(uint256 _applicationId) external onlyOwner {
        StartupApplication storage application = applications[_applicationId];

        require(application.applicant != address(0), "Application does not exist");
        require(!application.isListed, "Application is already listed");

        // Mark the application as listed
        application.isListed = true;

        // Emit the ApplicationListed event
        emit ApplicationListed(_applicationId, application.applicant);
    }

    /**
     * @dev Remove an application from the marketplace by its ID
     * @param _applicationId The ID of the application to remove
     */
    function removeApplication(uint256 _applicationId) external onlyOwner {
        StartupApplication storage application = applications[_applicationId];

        require(application.applicant != address(0), "Application does not exist");
        require(application.isListed, "Application is not listed");

        // Mark the application as not listed
        application.isListed = false;

        // Emit the ApplicationRemoved event
        emit ApplicationRemoved(_applicationId, application.applicant);
    }

    /**
     * @dev Get the details of an application by its ID
     * @param _applicationId The ID of the application to retrieve
     * @return The StartupApplication struct containing the application details
     */
    function getApplication(uint256 _applicationId) external view returns (StartupApplication memory) {
        require(applications[_applicationId].applicant != address(0), "Application does not exist");
        return applications[_applicationId];
    }

    /**
     * @dev Get the total number of applications
     * @return Total count of applications
     */
    function totalApplications() external view returns (uint256) {
        return _applicationIdCounter.current();
    }
}
```
