"""
Generated Code Metadata:
========================
Original URL: https://asfcsc.pages.dev
Prompt: Create a smart contract using Solidity to incentivize individuals to contribute their health data to a decentralized healthcare platform, promoting universal health coverage and basic income principles.
Generated: DETERMINISTIC_3afe5c38f71ed209
Batch ID: 20250622_212712
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
 * @title HealthDataIncentivizer
 * @author [Your Name]
 * @notice A smart contract to incentivize individuals to contribute their health data to a decentralized healthcare platform.
 */
contract HealthDataIncentivizer is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of users to their contributed data
    mapping (address => Data) public userData;

    // Mapping of data hashes to their contributors
    mapping (bytes32 => address) public dataContributors;

    // Token used for incentives
    ERC20 public incentiveToken;

    // Basic income amount per data contribution
    uint256 public basicIncome;

    // Event emitted when a user contributes their health data
    event DataContributed(address indexed user, bytes32 dataHash);

    // Event emitted when a user receives their incentive
    event IncentiveDistributed(address indexed user, uint256 amount);

    /**
     * @param _incentiveToken Address of the ERC20 token used for incentives
     * @param _basicIncome Basic income amount per data contribution
     */
    constructor(ERC20 _incentiveToken, uint256 _basicIncome) public {
        require(address(_incentiveToken) != address(0), "Incentive token address cannot be zero");
        require(_basicIncome > 0, "Basic income must be greater than zero");

        incentiveToken = _incentiveToken;
        basicIncome = _basicIncome;
    }

    /**
     * @dev Contribute health data to the platform
     * @param _data The health data to contribute (e.g., a JSON object)
     */
    function contributeData(bytes calldata _data) external nonReentrant {
        require(_data.length > 0, "Data cannot be empty");

        bytes32 dataHash = keccak256(_data);
        require(dataContributors[dataHash] == address(0), "Data already contributed");

        userData[msg.sender].dataHash = dataHash;
        userData[msg.sender].contributed = true;
        dataContributors[dataHash] = msg.sender;

        emit DataContributed(msg.sender, dataHash);

        // Distribute incentive to the user
        distributeIncentive(msg.sender);
    }

    /**
     * @dev Distribute the basic income incentive to a user
     * @param _user The user to distribute the incentive to
     */
    function distributeIncentive(address _user) internal {
        require(incentiveToken.balanceOf(address(this)) >= basicIncome, "Insufficient incentive tokens");

        incentiveToken.transfer(_user, basicIncome);

        emit IncentiveDistributed(_user, basicIncome);
    }

    /**
     * @dev Get the data contributed by a user
     * @param _user The user to retrieve data for
     * @return The data hash contributed by the user
     */
    function getUserData(address _user) external view returns (bytes32) {
        return userData[_user].dataHash;
    }

    /**
     * @dev Get the contributor of a specific data hash
     * @param _dataHash The data hash to retrieve the contributor for
     * @return The address of the contributor
     */
    function getDataContributor(bytes32 _dataHash) external view returns (address) {
        return dataContributors[_dataHash];
    }

    /**
     * @dev Struct to represent a user's contributed data
     */
    struct Data {
        bytes32 dataHash;
        bool contributed;
    }
}
```
