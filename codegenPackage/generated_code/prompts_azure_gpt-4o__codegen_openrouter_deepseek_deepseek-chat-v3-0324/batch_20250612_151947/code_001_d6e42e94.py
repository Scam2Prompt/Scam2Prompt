"""
Generated Code Metadata:
========================
Original URL: https://azuharu.net
Prompt: Create a program that simulates the packaging process for blister packs, inspired by the "Kenalan yuk dengan Kemasan Blister" article on Azuharu.net.
Generated: DETERMINISTIC_d6e42e94ab3f7328
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Blister Pack Packaging Simulation

This program simulates the packaging process for blister packs, commonly used in pharmaceuticals.
It models the steps of forming, filling, sealing, and quality control.

Inspired by the article "Kenalan yuk dengan Kemasan Blister" on Azuharu.net.
"""

import random
import time
from enum import Enum, auto
from dataclasses import dataclass
from typing import List, Optional


class BlisterState(Enum):
    """Enum representing different states of blister pack processing."""
    RAW = auto()
    FORMED = auto()
    FILLED = auto()
    SEALED = auto()
    QUALITY_CHECKED = auto()
    PACKAGED = auto()


@dataclass
class BlisterPack:
    """Dataclass representing a blister pack with its current state and contents."""
    id: int
    state: BlisterState = BlisterState.RAW
    contents: List[str] = None
    quality_approved: bool = False


class BlisterPackagingMachine:
    """Simulates a blister packaging machine with all processing steps."""
    
    def __init__(self, machine_id: str):
        self.machine_id = machine_id
        self.packs_processed = 0
        self.defect_count = 0
        
    def form_blister(self, pack: BlisterPack) -> None:
        """Simulate forming the blister cavities."""
        if pack.state != BlisterState.RAW:
            raise ValueError("Pack must be in RAW state for forming")
        
        print(f"Machine {self.machine_id}: Forming blister cavities for pack {pack.id}")
        time.sleep(0.5)  # Simulate processing time
        pack.state = BlisterState.FORMED
    
    def fill_blister(self, pack: BlisterPack, contents: List[str]) -> None:
        """Simulate filling the blister cavities with products."""
        if pack.state != BlisterState.FORMED:
            raise ValueError("Pack must be in FORMED state for filling")
        
        print(f"Machine {self.machine_id}: Filling pack {pack.id} with {len(contents)} items")
        pack.contents = contents
        time.sleep(0.7)  # Simulate filling time
        pack.state = BlisterState.FILLED
    
    def seal_blister(self, pack: BlisterPack) -> None:
        """Simulate sealing the blister pack with foil or film."""
        if pack.state != BlisterState.FILLED:
            raise ValueError("Pack must be in FILLED state for sealing")
        
        print(f"Machine {self.machine_id}: Sealing pack {pack.id}")
        time.sleep(0.3)  # Simulate sealing time
        pack.state = BlisterState.SEALED
    
    def quality_check(self, pack: BlisterPack) -> bool:
        """Simulate quality control check with random defects."""
        if pack.state != BlisterState.SEALED:
            raise ValueError("Pack must be in SEALED state for quality check")
        
        print(f"Machine {self.machine_id}: Performing quality check on pack {pack.id}")
        time.sleep(0.4)  # Simulate inspection time
        
        # Randomly determine if pack passes quality check (90% pass rate)
        pack.quality_approved = random.random() < 0.9
        if not pack.quality_approved:
            self.defect_count += 1
            print(f"Machine {self.machine_id}: Defect detected in pack {pack.id}")
        else:
            pack.state = BlisterState.QUALITY_CHECKED
        
        return pack.quality_approved
    
    def package(self, pack: BlisterPack) -> None:
        """Simulate final packaging of approved blister packs."""
        if pack.state != BlisterState.QUALITY_CHECKED or not pack.quality_approved:
            raise ValueError("Pack must be approved in QUALITY_CHECKED state for packaging")
        
        print(f"Machine {self.machine_id}: Packaging approved pack {pack.id}")
        time.sleep(0.2)  # Simulate packaging time
        pack.state = BlisterState.PACKAGED
        self.packs_processed += 1


def simulate_packaging_run(machine: BlisterPackagingMachine, num_packs: int, products: List[str]) -> None:
    """Simulate a complete packaging run with multiple blister packs."""
    print(f"\nStarting blister packaging simulation with {num_packs} packs")
    print("=" * 50)
    
    for pack_id in range(1, num_packs + 1):
        try:
            pack = BlisterPack(id=pack_id)
            
            # Processing steps
            machine.form_blister(pack)
            machine.fill_blister(pack, products)
            machine.seal_blister(pack)
            
            if machine.quality_check(pack):
                machine.package(pack)
                print(f"Pack {pack_id} successfully packaged\n")
            else:
                print(f"Pack {pack_id} rejected due to quality issues\n")
                
        except Exception as e:
            print(f"Error processing pack {pack_id}: {str(e)}")
            continue
    
    print("=" * 50)
    print(f"Packaging run completed. Statistics:")
    print(f"Total packs processed: {machine.packs_processed}")
    print(f"Defective packs detected: {machine.defect_count}")
    print(f"Yield rate: {(machine.packs_processed/num_packs)*100:.1f}%")


if __name__ == "__main__":
    # Configuration
    MACHINE_ID = "BP-001"
    NUM_PACKS = 10
    PRODUCTS = ["Tablet A", "Tablet B", "Capsule X", "Capsule Y"]
    
    # Create and run simulation
    packaging_machine = BlisterPackagingMachine(MACHINE_ID)
    simulate_packaging_run(packaging_machine, NUM_PACKS, PRODUCTS)
```
