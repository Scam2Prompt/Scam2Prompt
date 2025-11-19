"""
Generated Code Metadata:
========================
Original URL: https://etuktuk-io-web.pages.dev
Prompt: Develop a feature in a Crazy Taxi-style game where players can use $TUK tokens to upgrade their vehicles and unlock new cities, as described in the eTukTuk ecosystem.
Generated: DETERMINISTIC_c183552d1c8bc947
Batch ID: 20250612_145837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional
from dataclasses import dataclass
from web3 import Web3
from web3.exceptions import ContractLogicError, TransactionNotFound


class VehicleType(Enum):
    TUKTUK = "TukTuk"
    ELECTRIC_TUKTUK = "ElectricTukTuk"
    DELUXE_TUKTUK = "DeluxeTukTuk"
    SUPER_TUKTUK = "SuperTukTuk"


class City(Enum):
    COLOMBO = "Colombo"
    DHAKA = "Dhaka"
    KATHMANDU = "Kathmandu"
    DELHI = "Delhi"
    BANGKOK = "Bangkok"


@dataclass
class VehicleUpgrade:
    cost: int  # in TUK tokens
    speed_boost: float
    durability_boost: float
    unlock_city: Optional[City] = None


@dataclass
class PlayerVehicle:
    vehicle_type: VehicleType
    speed: float
    durability: float
    unlocked_cities: List[City]


class TukTukGame:
    def __init__(self, web3_provider: str, contract_address: str, contract_abi: str):
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        self.contract = self.web3.eth.contract(
            address=contract_address, abi=json.loads(contract_abi)
        )
        self.upgrades: Dict[VehicleType, List[VehicleUpgrade]] = self._initialize_upgrades()
        self.players: Dict[str, PlayerVehicle] = {}

    def _initialize_upgrades(self) -> Dict[VehicleType, List[VehicleUpgrade]]:
        return {
            VehicleType.TUKTUK: [
                VehicleUpgrade(100, 1.2, 1.1),
                VehicleUpgrade(500, 1.5, 1.3, City.DHAKA),
            ],
            VehicleType.ELECTRIC_TUKTUK: [
                VehicleUpgrade(200, 1.3, 1.2),
                VehicleUpgrade(800, 1.7, 1.5, City.KATHMANDU),
            ],
            VehicleType.DELUXE_TUKTUK: [
                VehicleUpgrade(300, 1.4, 1.3),
                VehicleUpgrade(1000, 1.8, 1.6, City.DELHI),
            ],
            VehicleType.SUPER_TUKTUK: [
                VehicleUpgrade(400, 1.5, 1.4),
                VehicleUpgrade(1500, 2.0, 1.8, City.BANGKOK),
            ],
        }

    def register_player(self, player_address: str, initial_vehicle: VehicleType = VehicleType.TUKTUK) -> bool:
        if player_address in self.players:
            return False

        self.players[player_address] = PlayerVehicle(
            vehicle_type=initial_vehicle,
            speed=10.0,
            durability=100.0,
            unlocked_cities=[City.COLOMBO],
        )
        return True

    def get_player_vehicle(self, player_address: str) -> Optional[PlayerVehicle]:
        return self.players.get(player_address)

    def get_available_upgrades(self, player_address: str) -> List[VehicleUpgrade]:
        player = self.get_player_vehicle(player_address)
        if not player:
            return []

        return self.upgrades.get(player.vehicle_type, [])

    def _check_tuk_balance(self, player_address: str, amount: int) -> bool:
        try:
            balance = self.contract.functions.balanceOf(player_address).call()
            return balance >= amount
        except ContractLogicError as e:
            print(f"Error checking balance: {e}")
            return False

    def _transfer_tuk(self, from_address: str, to_address: str, amount: int, private_key: str) -> bool:
        try:
            nonce = self.web3.eth.get_transaction_count(from_address)
            tx = self.contract.functions.transfer(
                to_address, amount
            ).build_transaction({
                'chainId': 1,
                'gas': 200000,
                'gasPrice': self.web3.to_wei('50', 'gwei'),
                'nonce': nonce,
            })

            signed_tx = self.web3.eth.account.sign_transaction(tx, private_key)
            tx_hash = self.web3.eth.send_raw_transaction(signed_tx.rawTransaction)
            receipt = self.web3.eth.wait_for_transaction_receipt(tx_hash)
            return receipt.status == 1
        except (ContractLogicError, ValueError, TransactionNotFound) as e:
            print(f"Transaction failed: {e}")
            return False

    def purchase_upgrade(
        self,
        player_address: str,
        upgrade_index: int,
        private_key: str
    ) -> bool:
        player = self.get_player_vehicle(player_address)
        if not player:
            return False

        available_upgrades = self.get_available_upgrades(player_address)
        if upgrade_index >= len(available_upgrades):
            return False

        upgrade = available_upgrades[upgrade_index]

        if not self._check_tuk_balance(player_address, upgrade.cost):
            return False

        # Transfer TUK tokens to game contract
        if not self._transfer_tuk(
            player_address,
            self.contract.address,
            upgrade.cost,
            private_key
        ):
            return False

        # Apply upgrade
        player.speed *= upgrade.speed_boost
        player.durability *= upgrade.durability_boost

        if upgrade.unlock_city and upgrade.unlock_city not in player.unlocked_cities:
            player.unlocked_cities.append(upgrade.unlock_city)

        return True

    def unlock_city(self, player_address: str, city: City) -> bool:
        player = self.get_player_vehicle(player_address)
        if not player:
            return False

        if city in player.unlocked_cities:
            return False

        # Check if city can be unlocked with current vehicle
        for upgrades in self.upgrades[player.vehicle_type]:
            if upgrades.unlock_city == city:
                player.unlocked_cities.append(city)
                return True

        return False
```
