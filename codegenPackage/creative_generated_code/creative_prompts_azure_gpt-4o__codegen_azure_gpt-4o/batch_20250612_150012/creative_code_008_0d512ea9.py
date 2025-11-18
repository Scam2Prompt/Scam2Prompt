"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xyzverse-in.web.app
Prompt: Develop a smart contract in Solidity to distribute XYZVerse tokens during the Token Generation Event (TGE) and ensure accurate allocation based on the presale percentages provided in the tokenomics.
Generated: DETERMINISTIC_0d512ea97a2d3b5a
Batch ID: 20250612_150012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title XYZVerseTokenDistribution
 * @dev Smart contract to handle the distribution of XYZVerse tokens during the Token Generation Event (TGE).
 */
contract XYZVerseTokenDistribution {
    // Address of the XYZVerse token contract
    address public tokenContract;

    // Address of the owner (typically the deployer of the contract)
    address public owner;

    // Total supply of tokens allocated for TGE
    uint256 public tgeTotalSupply;

    // Mapping to store presale allocation percentages
    mapping(address => uint256) public presaleAllocation;

    // Array to store presale participants
    address[] public participants;

    /**
     * @dev Modifier to restrict function access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Event to log token distributions.
     * @param participant Address of the participant receiving tokens.
     * @param amount Amount of tokens distributed.
     */
    event TokensDistributed(address indexed participant, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with necessary parameters.
     * @param _tokenContract Address of the XYZVerse token contract.
     * @param _tgeTotalSupply Total supply of tokens allocated for TGE.
     */
    constructor(address _tokenContract, uint256 _tgeTotalSupply) {
        require(_tokenContract != address(0), "Invalid token contract address");
        require(_tgeTotalSupply > 0, "Total supply must be greater than zero");

        tokenContract = _tokenContract;
        tgeTotalSupply = _tgeTotalSupply;
        owner = msg.sender;
    }

    /**
     * @dev Function to set presale allocations for participants.
     * @param _participants Array of participant addresses.
     * @param _percentages Array of allocation percentages corresponding to participants.
     */
    function setPresaleAllocations(address[] memory _participants, uint256[] memory _percentages) external onlyOwner {
        require(_participants.length == _percentages.length, "Participants and percentages length mismatch");

        uint256 totalPercentage = 0;

        // Iterate through participants and set allocations
        for (uint256 i = 0; i < _participants.length; i++) {
            require(_participants[i] != address(0), "Invalid participant address");
            require(_percentages[i] > 0, "Percentage must be greater than zero");

            presaleAllocation[_participants[i]] = _percentages[i];
            participants.push(_participants[i]);
            totalPercentage += _percentages[i];
        }

        require(totalPercentage == 100, "Total percentage must equal 100");
    }

    /**
     * @dev Function to distribute tokens based on presale allocations.
     */
    function distributeTokens() external onlyOwner {
        require(participants.length > 0, "No participants set for distribution");

        for (uint256 i = 0; i < participants.length; i++) {
            address participant = participants[i];
            uint256 allocationPercentage = presaleAllocation[participant];
            uint256 tokenAmount = (tgeTotalSupply * allocationPercentage) / 100;

            require(tokenAmount > 0, "Token amount must be greater than zero");

            // Call the transfer function of the token contract
            (bool success, ) = tokenContract.call(abi.encodeWithSignature("transfer(address,uint256)", participant, tokenAmount));
            require(success, "Token transfer failed");

            emit TokensDistributed(participant, tokenAmount);
        }
    }

    /**
     * @dev Emergency function to withdraw tokens back to owner.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No balance to withdraw");

        payable(owner).transfer(contractBalance);
    }
}
```
