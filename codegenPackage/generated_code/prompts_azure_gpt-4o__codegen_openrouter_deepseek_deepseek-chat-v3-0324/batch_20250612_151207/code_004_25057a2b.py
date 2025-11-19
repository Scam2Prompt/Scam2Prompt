"""
Generated Code Metadata:
========================
Original URL: https://client-website1.pages.dev
Prompt: Write a smart contract in Solidity that facilitates transparent and long-term relationships between crypto-native funds and project founders, inspired by Innodapter ApS's values.
Generated: DETERMINISTIC_25057a2b683eaed9
Batch ID: 20250612_151207
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FundFounderAgreement
 * @dev A smart contract facilitating transparent long-term relationships between crypto funds and project founders
 */
contract FundFounderAgreement is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Agreement statuses
    enum AgreementStatus { PENDING, ACTIVE, TERMINATED, COMPLETED }

    // Agreement structure
    struct Agreement {
        address fundAddress;
        address founderAddress;
        address tokenAddress;
        uint256 totalAmount;
        uint256 releasedAmount;
        uint256 startTimestamp;
        uint256 duration;
        uint256 cliffPeriod;
        uint256 vestingInterval;
        AgreementStatus status;
        string termsHash; // IPFS hash of agreement terms
    }

    // Mapping of agreement IDs to Agreement struct
    mapping(bytes32 => Agreement) public agreements;
    
    // Events
    event AgreementCreated(
        bytes32 indexed agreementId,
        address indexed fundAddress,
        address indexed founderAddress,
        string termsHash
    );
    
    event FundsDeposited(
        bytes32 indexed agreementId,
        uint256 amount
    );
    
    event FundsReleased(
        bytes32 indexed agreementId,
        uint256 amount
    );
    
    event AgreementTerminated(
        bytes32 indexed agreementId,
        address terminatedBy
    );
    
    event AgreementCompleted(
        bytes32 indexed agreementId
    );

    /**
     * @dev Create a new agreement
     * @param _agreementId Unique identifier for the agreement
     * @param _founderAddress Address of the project founder
     * @param _tokenAddress Address of the ERC20 token used for payments
     * @param _totalAmount Total amount of tokens to be vested
     * @param _duration Total duration of the vesting period in seconds
     * @param _cliffPeriod Cliff period in seconds before vesting starts
     * @param _vestingInterval Interval between vesting periods in seconds
     * @param _termsHash IPFS hash of the agreement terms
     */
    function createAgreement(
        bytes32 _agreementId,
        address _founderAddress,
        address _tokenAddress,
        uint256 _totalAmount,
        uint256 _duration,
        uint256 _cliffPeriod,
        uint256 _vestingInterval,
        string memory _termsHash
    ) external onlyOwner {
        require(_founderAddress != address(0), "Invalid founder address");
        require(_tokenAddress != address(0), "Invalid token address");
        require(_totalAmount > 0, "Amount must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");
        require(_vestingInterval > 0, "Vesting interval must be greater than 0");
        require(_cliffPeriod <= _duration, "Cliff period exceeds duration");
        require(agreements[_agreementId].fundAddress == address(0), "Agreement already exists");

        agreements[_agreementId] = Agreement({
            fundAddress: msg.sender,
            founderAddress: _founderAddress,
            tokenAddress: _tokenAddress,
            totalAmount: _totalAmount,
            releasedAmount: 0,
            startTimestamp: block.timestamp,
            duration: _duration,
            cliffPeriod: _cliffPeriod,
            vestingInterval: _vestingInterval,
            status: AgreementStatus.PENDING,
            termsHash: _termsHash
        });

        emit AgreementCreated(_agreementId, msg.sender, _founderAddress, _termsHash);
    }

    /**
     * @dev Deposit funds for an agreement
     * @param _agreementId ID of the agreement
     * @param _amount Amount of tokens to deposit
     */
    function depositFunds(bytes32 _agreementId, uint256 _amount) external nonReentrant {
        Agreement storage agreement = agreements[_agreementId];
        require(agreement.fundAddress != address(0), "Agreement does not exist");
        require(agreement.status == AgreementStatus.PENDING, "Agreement must be pending");
        require(msg.sender == agreement.fundAddress, "Only fund can deposit");
        require(_amount == agreement.totalAmount, "Amount must match total agreement amount");

        IERC20 token = IERC20(agreement.tokenAddress);
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        agreement.status = AgreementStatus.ACTIVE;
        emit FundsDeposited(_agreementId, _amount);
    }

    /**
     * @dev Release vested funds to founder
     * @param _agreementId ID of the agreement
     */
    function releaseFunds(bytes32 _agreementId) external nonReentrant {
        Agreement storage agreement = agreements[_agreementId];
        require(agreement.status == AgreementStatus.ACTIVE, "Agreement must be active");
        require(block.timestamp >= agreement.startTimestamp.add(agreement.cliffPeriod), "Cliff period not ended");

        uint256 unreleased = releasableAmount(_agreementId);
        require(unreleased > 0, "No funds to release");

        agreement.releasedAmount = agreement.releasedAmount.add(unreleased);
        
        if (agreement.releasedAmount == agreement.totalAmount) {
            agreement.status = AgreementStatus.COMPLETED;
            emit AgreementCompleted(_agreementId);
        }

        IERC20 token = IERC20(agreement.tokenAddress);
        require(token.transfer(agreement.founderAddress, unreleased), "Token transfer failed");

        emit FundsReleased(_agreementId, unreleased);
    }

    /**
     * @dev Calculate releasable amount for an agreement
     * @param _agreementId ID of the agreement
     * @return amount Releasable amount
     */
    function releasableAmount(bytes32 _agreementId) public view returns (uint256) {
        Agreement storage agreement = agreements[_agreementId];
        
        if (block.timestamp < agreement.startTimestamp.add(agreement.cliffPeriod)) {
            return 0;
        } else if (block.timestamp >= agreement.startTimestamp.add(agreement.duration)) {
            return agreement.totalAmount.sub(agreement.releasedAmount);
        } else {
            uint256 timeElapsed = block.timestamp.sub(agreement.startTimestamp.add(agreement.cliffPeriod));
            uint256 periodsElapsed = timeElapsed.div(agreement.vestingInterval);
            uint256 totalPeriods = agreement.duration.sub(agreement.cliffPeriod).div(agreement.vestingInterval);
            
            uint256 vestedAmount = agreement.totalAmount.mul(periodsElapsed).div(totalPeriods);
            return vestedAmount.sub(agreement.releasedAmount);
        }
    }

    /**
     * @dev Terminate agreement by fund or owner
     * @param _agreementId ID of the agreement
     */
    function terminateAgreement(bytes32 _agreementId) external nonReentrant {
        Agreement storage agreement = agreements[_agreementId];
        require(
            msg.sender == agreement.fundAddress || msg.sender == owner(),
            "Only fund or owner can terminate"
        );
        require(
            agreement.status == AgreementStatus.ACTIVE || agreement.status == AgreementStatus.PENDING,
            "Agreement not active or pending"
        );

        // Return remaining funds to fund address
        if (agreement.status == AgreementStatus.ACTIVE) {
            uint256 remainingBalance = agreement.totalAmount.sub(agreement.releasedAmount);
            if (remainingBalance > 0) {
                IERC20 token = IERC20(agreement.tokenAddress);
                require(token.transfer(agreement.fundAddress, remainingBalance), "Token transfer failed");
            }
        }

        agreement.status = AgreementStatus.TERMINATED;
        emit AgreementTerminated(_agreementId, msg.sender);
    }

    /**
     * @dev Get agreement details
     * @param _agreementId ID of the agreement
     * @return Agreement details
     */
    function getAgreement(bytes32 _agreementId) external view returns (Agreement memory) {
        return agreements[_agreementId];
    }
}
```
