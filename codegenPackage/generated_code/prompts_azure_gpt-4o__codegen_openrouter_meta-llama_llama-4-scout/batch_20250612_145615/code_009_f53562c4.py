"""
Generated Code Metadata:
========================
Original URL: https://light-chain-ai.pages.dev
Prompt: Write a Python script to simulate the energy-efficient transaction validation process of Lightchain AI’s PoI consensus mechanism, comparing it to traditional PoW and PoS models.
Generated: DETERMINISTIC_f53562c4fbc955fe
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
import random

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce=0):
        """
        Initialize a block.

        :param index: The index of the block.
        :param previous_hash: The hash of the previous block.
        :param timestamp: The timestamp of the block.
        :param data: The data stored in the block.
        :param nonce: The nonce value for PoW.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the block.

        :return: The hash of the block.
        """
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data) + str(self.nonce)
        return hashlib.sha256(data_string.encode()).hexdigest()


class PoW:
    def __init__(self, difficulty):
        """
        Initialize a PoW object.

        :param difficulty: The difficulty level for PoW.
        """
        self.difficulty = difficulty

    def validate_block(self, block):
        """
        Validate a block using PoW.

        :param block: The block to validate.
        :return: True if the block is valid, False otherwise.
        """
        while block.hash[:self.difficulty] != '0' * self.difficulty:
            block.nonce += 1
            block.hash = block.calculate_hash()
            if block.nonce > 1000000:  # prevent infinite loop
                return False
        return True


class PoS:
    def __init__(self, validators):
        """
        Initialize a PoS object.

        :param validators: A list of validators.
        """
        self.validators = validators

    def validate_block(self, block):
        """
        Validate a block using PoS.

        :param block: The block to validate.
        :return: True if the block is valid, False otherwise.
        """
        # Select a random validator
        validator = random.choice(self.validators)
        # Assume the validator votes for the block
        return True


class PoI:
    def __init__(self, energy_efficiency):
        """
        Initialize a PoI object.

        :param energy_efficiency: The energy efficiency level for PoI.
        """
        self.energy_efficiency = energy_efficiency

    def validate_block(self, block):
        """
        Validate a block using PoI.

        :param block: The block to validate.
        :return: True if the block is valid, False otherwise.
        """
        # Simulate energy-efficient validation
        energy_consumption = 1 - self.energy_efficiency
        time.sleep(energy_consumption)  # simulate energy consumption
        return True


def main():
    # Create a blockchain
    blockchain = [Block(0, '0', int(time.time()), 'Genesis Block')]

    # PoW
    pow_difficulty = 4
    pow = PoW(pow_difficulty)
    block = Block(1, blockchain[0].hash, int(time.time()), 'Transaction Data')
    start_time = time.time()
    if pow.validate_block(block):
        print(f"PoW block validated in {time.time() - start_time} seconds")
    else:
        print("PoW block validation failed")

    # PoS
    pos_validators = ['Validator1', 'Validator2', 'Validator3']
    pos = PoS(pos_validators)
    block = Block(1, blockchain[0].hash, int(time.time()), 'Transaction Data')
    start_time = time.time()
    if pos.validate_block(block):
        print(f"PoS block validated in {time.time() - start_time} seconds")
    else:
        print("PoS block validation failed")

    # PoI
    poi_energy_efficiency = 0.9
    poi = PoI(poi_energy_efficiency)
    block = Block(1, blockchain[0].hash, int(time.time()), 'Transaction Data')
    start_time = time.time()
    if poi.validate_block(block):
        print(f"PoI block validated in {time.time() - start_time} seconds")
    else:
        print("PoI block validation failed")


if __name__ == "__main__":
    main()
```
