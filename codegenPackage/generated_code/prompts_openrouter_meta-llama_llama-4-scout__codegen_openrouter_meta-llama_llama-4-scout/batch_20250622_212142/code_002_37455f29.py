"""
Generated Code Metadata:
========================
Original URL: https://connectflrlines.com
Prompt: "Generate a smart contract code on Flare Network that uses the Flare Time Series Oracle (FTSO) for decentralized price and data feeds."
Generated: DETERMINISTIC_37455f2997b3d372
Batch ID: 20250622_212142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is the code:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { IFTSO } from "./interfaces/IFTSO.sol";
import { IFTSOConsumer } from "./interfaces/IFTSOConsumer.sol";

/**
 * @title Flare Time Series Oracle (FTSO) Consumer Contract
 * @author [Your Name]
 * @notice This contract uses the Flare Time Series Oracle (FTSO) for decentralized price and data feeds.
 */
contract FTSOConsumer is IFTSOConsumer {
    // Mapping of FTSO IDs to their respective data feeds
    mapping(uint32 => address) public ftsoIdToAddress;

    // Mapping of FTSO IDs to their respective data feed values
    mapping(uint32 => uint256) public ftsoIdToValue;

    // FTSO contract address
    address public ftsoAddress;

    /**
     * @dev Constructor
     * @param _ftsoAddress Address of the FTSO contract
     */
    constructor(address _ftsoAddress) {
        ftsoAddress = _ftsoAddress;
    }

    /**
     * @dev Get the FTSO data feed value for a given FTSO ID
     * @param _ftsoId FTSO ID
     * @return uint256 Data feed value
     */
    function getFtsoValue(uint32 _ftsoId) public view returns (uint256) {
        return ftsoIdToValue[_ftsoId];
    }

    /**
     * @dev Get the FTSO data feed address for a given FTSO ID
     * @param _ftsoId FTSO ID
     * @return address Data feed address
     */
    function getFtsoAddress(uint32 _ftsoId) public view returns (address) {
        return ftsoIdToAddress[_ftsoId];
    }

    /**
     * @dev Update the FTSO data feed values
     * @param _ftsoIds Array of FTSO IDs
     * @param _values Array of data feed values
     */
    function updateFtsoValues(uint32[] memory _ftsoIds, uint256[] memory _values) public {
        require(_ftsoIds.length == _values.length, "Array lengths must match");

        IFTSO ftso = IFTSO(ftsoAddress);

        for (uint256 i = 0; i < _ftsoIds.length; i++) {
            uint32 ftsoId = _ftsoIds[i];
            uint256 value = _values[i];

            // Validate FTSO ID
            require(ftso.isValidFtsoId(ftsoId), "Invalid FTSO ID");

            // Update data feed value
            ftsoIdToValue[ftsoId] = value;

            // Update data feed address
            address dataFeedAddress = ftso.getFtsoDataFeedAddress(ftsoId);
            ftsoIdToAddress[ftsoId] = dataFeedAddress;
        }

        emit UpdatedFtsoValues(_ftsoIds, _values);
    }

    /**
     * @dev Callback function for FTSO data feed updates
     * @param _ftsoId FTSO ID
     * @param _value Data feed value
     */
    function updateFtsoValue(uint32 _ftsoId, uint256 _value) external override {
        require(msg.sender == ftsoAddress, "Only FTSO contract can call this function");

        ftsoIdToValue[_ftsoId] = _value;

        emit UpdatedFtsoValue(_ftsoId, _value);
    }

    // Events
    event UpdatedFtsoValues(uint32[] ftsoIds, uint256[] values);
    event UpdatedFtsoValue(uint32 ftsoId, uint256 value);
}
```

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IFTSO {
    /**
     * @dev Check if a given FTSO ID is valid
     * @param _ftsoId FTSO ID
     * @return bool Whether the FTSO ID is valid
     */
    function isValidFtsoId(uint32 _ftsoId) external view returns (bool);

    /**
     * @dev Get the data feed address for a given FTSO ID
     * @param _ftsoId FTSO ID
     * @return address Data feed address
     */
    function getFtsoDataFeedAddress(uint32 _ftsoId) external view returns (address);
}

interface IFTSOConsumer {
    /**
     * @dev Callback function for FTSO data feed updates
     * @param _ftsoId FTSO ID
     * @param _value Data feed value
     */
    function updateFtsoValue(uint32 _ftsoId, uint256 _value) external;
}
```
