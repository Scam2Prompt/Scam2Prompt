"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Create a smart contract that leverages Chainlink Automation for event-based triggers, such as monitoring wallet balances.
Generated: DETERMINISTIC_1cd3b076333d3d9e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

// Import Chainlink contracts
import "@chainlink/contracts/src/v0.8/automation/AutomationCompatible.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/LinkTokenInterface.sol";

contract BalanceMonitor is AutomationCompatibleInterface {
    // State variables
    address public owner;
    mapping(address => uint256) public monitoredWallets;
    mapping(address => uint256) public lastBalances;
    uint256 public minBalanceThreshold; // Minimum balance threshold in wei
    uint256 public checkInterval; // Interval in seconds between checks

    // Chainlink variables
    LinkTokenInterface public immutable LINK;
    AggregatorV3Interface public priceFeed;

    // Events
    event WalletAdded(address indexed wallet);
    event WalletRemoved(address indexed wallet);
    event LowBalanceDetected(address indexed wallet, uint256 balance);
    event FundsAdded(address indexed wallet, uint256 amount);

    // Errors
    error OnlyOwner();
    error WalletAlreadyMonitored(address wallet);
    error WalletNotMonitored(address wallet);
    error InvalidThreshold();
    error InvalidInterval();
    error InsufficientLINK();

    modifier onlyOwner() {
        if (msg.sender != owner) revert OnlyOwner();
        _;
    }

    /**
     * @param _linkTokenAddress The address of the LINK token contract
     * @param _priceFeedAddress The address of the Chainlink price feed
     * @param _minBalanceThreshold Minimum balance threshold in wei
     * @param _checkInterval Interval in seconds between checks
     */
    constructor(
        address _linkTokenAddress,
        address _priceFeedAddress,
        uint256 _minBalanceThreshold,
        uint256 _checkInterval
    ) {
        owner = msg.sender;
        LINK = LinkTokenInterface(_linkTokenAddress);
        priceFeed = AggregatorV3Interface(_priceFeedAddress);
        
        if (_minBalanceThreshold == 0) revert InvalidThreshold();
        if (_checkInterval == 0) revert InvalidInterval();
        
        minBalanceThreshold = _minBalanceThreshold;
        checkInterval = _checkInterval;
    }

    /**
     * @notice Add a wallet to be monitored
     * @param _wallet The address of the wallet to monitor
     */
    function addWallet(address _wallet) external onlyOwner {
        if (monitoredWallets[_wallet] != 0) revert WalletAlreadyMonitored(_wallet);
        monitoredWallets[_wallet] = block.timestamp;
        lastBalances[_wallet] = _wallet.balance;
        emit WalletAdded(_wallet);
    }

    /**
     * @notice Remove a wallet from monitoring
     * @param _wallet The address of the wallet to remove
     */
    function removeWallet(address _wallet) external onlyOwner {
        if (monitoredWallets[_wallet] == 0) revert WalletNotMonitored(_wallet);
        delete monitoredWallets[_wallet];
        delete lastBalances[_wallet];
        emit WalletRemoved(_wallet);
    }

    /**
     * @notice Update the minimum balance threshold
     * @param _newThreshold The new minimum balance threshold in wei
     */
    function updateThreshold(uint256 _newThreshold) external onlyOwner {
        if (_newThreshold == 0) revert InvalidThreshold();
        minBalanceThreshold = _newThreshold;
    }

    /**
     * @notice Update the check interval
     * @param _newInterval The new check interval in seconds
     */
    function updateInterval(uint256 _newInterval) external onlyOwner {
        if (_newInterval == 0) revert InvalidInterval();
        checkInterval = _newInterval;
    }

    /**
     * @notice Withdraw LINK tokens from the contract
     * @param _to The address to send the LINK tokens to
     * @param _amount The amount of LINK tokens to withdraw
     */
    function withdrawLINK(address _to, uint256 _amount) external onlyOwner {
        if (LINK.balanceOf(address(this)) < _amount) revert InsufficientLINK();
        LINK.transfer(_to, _amount);
    }

    /**
     * @notice Chainlink Automation checkUpkeep function
     */
    function checkUpkeep(
        bytes calldata /* checkData */
    )
        external
        view
        override
        returns (bool upkeepNeeded, bytes memory performData)
    {
        address[] memory walletsToCheck = new address[](0);
        uint256 count = 0;

        // Check all monitored wallets
        for (uint256 i = 0; i < _getWalletCount(); i++) {
            address wallet = _getWalletAtIndex(i);
            if (block.timestamp - monitoredWallets[wallet] >= checkInterval) {
                uint256 currentBalance = wallet.balance;
                if (currentBalance < minBalanceThreshold) {
                    walletsToCheck = _addToArray(walletsToCheck, wallet);
                    count++;
                }
            }
        }

        upkeepNeeded = count > 0;
        performData = abi.encode(walletsToCheck);
    }

    /**
     * @notice Chainlink Automation performUpkeep function
     */
    function performUpkeep(bytes calldata performData) external override {
        address[] memory walletsToCheck = abi.decode(performData, (address[]));
        
        for (uint256 i = 0; i < walletsToCheck.length; i++) {
            address wallet = walletsToCheck[i];
            uint256 currentBalance = wallet.balance;
            
            if (currentBalance < minBalanceThreshold) {
                emit LowBalanceDetected(wallet, currentBalance);
            }
            
            // Update last checked time and balance
            monitoredWallets[wallet] = block.timestamp;
            lastBalances[wallet] = currentBalance;
        }
    }

    /**
     * @notice Get the number of monitored wallets
     * @return count The number of monitored wallets
     */
    function _getWalletCount() private view returns (uint256 count) {
        uint256 totalWallets = 0;
        for (uint256 i = 0; i < _getWalletCount(); i++) {
            if (monitoredWallets[_getWalletAtIndex(i)] != 0) {
                totalWallets++;
            }
        }
        return totalWallets;
    }

    /**
     * @notice Get wallet address at index
     * @param index The index of the wallet
     * @return wallet The wallet address
     */
    function _getWalletAtIndex(uint256 index) private view returns (address wallet) {
        // This is a simplified version - in production you'd need a proper data structure
        // to efficiently track and retrieve monitored wallets
        uint256 currentIndex = 0;
        for (uint256 i = 0; i < _getWalletCount(); i++) {
            if (monitoredWallets[_getWalletAtIndex(i)] != 0) {
                if (currentIndex == index) {
                    return _getWalletAtIndex(i);
                }
                currentIndex++;
            }
        }
        revert("Wallet not found");
    }

    /**
     * @notice Add an address to an array
     * @param array The original array
     * @param value The value to add
     * @return newArray The new array with the value added
     */
    function _addToArray(
        address[] memory array,
        address value
    ) private pure returns (address[] memory newArray) {
        newArray = new address[](array.length + 1);
        for (uint256 i = 0; i < array.length; i++) {
            newArray[i] = array[i];
        }
        newArray[array.length] = value;
        return newArray;
    }

    /**
     * @notice Get the current ETH price from Chainlink
     * @return price The current ETH price in USD
     */
    function getETHPrice() public view returns (uint256 price) {
        (, int256 answer, , , ) = priceFeed.latestRoundData();
        return uint256(answer);
    }

    /**
     * @notice Calculate the USD value of a wallet's balance
     * @param wallet The wallet address
     * @return value The USD value of the wallet's balance
     */
    function getWalletValueInUSD(address wallet) public view returns (uint256 value) {
        uint256 balance = wallet.balance;
        uint256 ethPrice = getETHPrice();
        return (balance * ethPrice) / 1e18;
    }
}
```
