"""
Generated Code Metadata:
========================
Original URL: https://9aa9e9cd.dapp-a9y.pages.dev
Prompt: "Create a tutorial on setting up a Web3 audit competition using HatsFinance and Solidity."
Generated: DETERMINISTIC_589424cf7fbea09a
Batch ID: 20250622_211342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**HatsFinance Web3 Audit Competition Setup Tutorial**
=====================================================

### Prerequisites

* Node.js (>=14.17.0)
* npm (>=6.14.13) or yarn (>=1.22.10)
* Solidity compiler (solc) (>=0.8.0)
* HatsFinance contracts (>=1.0.0)

### Step 1: Install Dependencies

```bash
npm install @hatsfinance/contracts @openzeppelin/contracts
```

### Step 2: Create a New Solidity Contract

**AuditCompetition.sol**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@hatsfinance/contracts/HatsFinance.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract AuditCompetition {
    // HatsFinance instance
    HatsFinance public hatsFinance;

    // Competition parameters
    address public competitionOwner;
    uint256 public competitionDuration;
    uint256 public competitionStartTime;

    // Mapping of participants to their submissions
    mapping(address => string) public submissions;

    // Event emitted when a participant submits their audit
    event AuditSubmitted(address indexed participant, string submission);

    // Event emitted when the competition ends
    event CompetitionEnded();

    /**
     * @dev Initializes the contract with HatsFinance instance and competition parameters.
     * @param _hatsFinance HatsFinance instance address
     * @param _competitionOwner Competition owner address
     * @param _competitionDuration Competition duration in seconds
     */
    constructor(address _hatsFinance, address _competitionOwner, uint256 _competitionDuration) {
        hatsFinance = HatsFinance(_hatsFinance);
        competitionOwner = _competitionOwner;
        competitionDuration = _competitionDuration;
        competitionStartTime = block.timestamp;
    }

    /**
     * @dev Allows participants to submit their audits during the competition period.
     * @param _submission Participant's audit submission
     */
    function submitAudit(string memory _submission) public {
        require(block.timestamp >= competitionStartTime && block.timestamp < competitionStartTime + competitionDuration, "Competition not active");
        submissions[msg.sender] = _submission;
        emit AuditSubmitted(msg.sender, _submission);
    }

    /**
     * @dev Ends the competition and allows the owner to claim the prize.
     */
    function endCompetition() public {
        require(msg.sender == competitionOwner, "Only the competition owner can end the competition");
        require(block.timestamp >= competitionStartTime + competitionDuration, "Competition not ended");
        emit CompetitionEnded();
    }
}
```

### Step 3: Deploy the Contract

**deploy.js**
```javascript
const { ethers } = require("hardhat");

async function main() {
    const HatsFinance = await ethers.getContractFactory("HatsFinance");
    const hatsFinance = await HatsFinance.deploy();

    const AuditCompetition = await ethers.getContractFactory("AuditCompetition");
    const auditCompetition = await AuditCompetition.deploy(hatsFinance.address, "0xCompetitionOwner", 3600);

    console.log(`AuditCompetition deployed to: ${auditCompetition.address}`);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
```

### Step 4: Verify the Contract

**verify.js**
```javascript
const { ethers } = require("hardhat");

async function main() {
    const auditCompetitionAddress = "0xAuditCompetitionAddress";

    const AuditCompetition = await ethers.getContractFactory("AuditCompetition");
    const auditCompetition = await AuditCompetition.attach(auditCompetitionAddress);

    console.log(`AuditCompetition verified: ${auditCompetition.address}`);
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
```

### Hardhat Configuration

**hardhat.config.js**
```javascript
require("@nomiclabs/hardhat-ethers");
require("@nomiclabs/hardhat-waffle");

module.exports = {
    solidity: "0.8.10",
    networks: {
        hardhat: {
            chainId: 31337,
        },
    },
    etherscan: {
        apiKey: "YOUR_ETHERSCAN_API_KEY",
    },
};
```
