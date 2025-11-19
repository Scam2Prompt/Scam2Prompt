"""
Generated Code Metadata:
========================
Original URL: https://ocuvana.com
Prompt: Write a Python script to calculate the estimated lifespan of magnetic eyelashes based on user care habits, using the "1–2 years with good care" guideline mentioned on Ocuvana's site.
Generated: DETERMINISTIC_20a67da679fe1587
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum

class CareFrequency(Enum):
    """Enum representing the frequency of care for magnetic eyelashes."""
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3
    RARELY = 4

class StorageCondition(Enum):
    """Enum representing storage conditions for magnetic eyelashes."""
    PROPER_CASE = 1
    IMPROPER_CASE = 2
    EXPOSED = 3

class UsageFrequency(Enum):
    """Enum representing how often the eyelashes are used."""
    DAILY = 1
    WEEKLY = 2
    OCCASIONALLY = 3

def calculate_lifespan(
    care_frequency: CareFrequency,
    storage_condition: StorageCondition,
    usage_frequency: UsageFrequency
) -> float:
    """
    Calculate the estimated lifespan of magnetic eyelashes based on care habits.
    
    Args:
        care_frequency: How often the user cleans/maintains the eyelashes
        storage_condition: How the eyelashes are stored when not in use
        usage_frequency: How often the eyelashes are worn
    
    Returns:
        Estimated lifespan in years (float)
    """
    # Base lifespan with good care (1-2 years)
    base_lifespan = 1.5
    
    # Adjustments based on care frequency
    if care_frequency == CareFrequency.DAILY:
        care_factor = 1.2
    elif care_frequency == CareFrequency.WEEKLY:
        care_factor = 1.0
    elif care_frequency == CareFrequency.MONTHLY:
        care_factor = 0.8
    else:  # RARELY
        care_factor = 0.5
    
    # Adjustments based on storage conditions
    if storage_condition == StorageCondition.PROPER_CASE:
        storage_factor = 1.1
    elif storage_condition == StorageCondition.IMPROPER_CASE:
        storage_factor = 0.9
    else:  # EXPOSED
        storage_factor = 0.7
    
    # Adjustments based on usage frequency
    if usage_frequency == UsageFrequency.DAILY:
        usage_factor = 0.8
    elif usage_frequency == UsageFrequency.WEEKLY:
        usage_factor = 1.0
    else:  # OCCASIONALLY
        usage_factor = 1.2
    
    # Calculate final lifespan
    lifespan = base_lifespan * care_factor * storage_factor * usage_factor
    
    # Ensure lifespan stays within reasonable bounds (0.5-3 years)
    lifespan = max(0.5, min(3.0, lifespan))
    
    return round(lifespan, 1)

def get_user_input() -> tuple:
    """Get user input for care habits and return as tuple of enums."""
    print("Magnetic Eyelash Lifespan Calculator")
    print("-----------------------------------\n")
    
    print("How often do you clean/maintain your magnetic eyelashes?")
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    print("4. Rarely")
    care_choice = int(input("Enter choice (1-4): "))
    
    print("\nHow do you store your magnetic eyelashes when not in use?")
    print("1. In proper case/container")
    print("2. In improper case/container")
    print("3. Exposed (no case)")
    storage_choice = int(input("Enter choice (1-3): "))
    
    print("\nHow often do you wear your magnetic eyelashes?")
    print("1. Daily")
    print("2. Weekly")
    print("3. Occasionally")
    usage_choice = int(input("Enter choice (1-3): "))
    
    # Map choices to enums
    care_freq = CareFrequency(care_choice)
    storage_cond = StorageCondition(storage_choice)
    usage_freq = UsageFrequency(usage_choice)
    
    return care_freq, storage_cond, usage_freq

def main():
    try:
        care_freq, storage_cond, usage_freq = get_user_input()
        lifespan = calculate_lifespan(care_freq, storage_cond, usage_freq)
        
        print(f"\nEstimated lifespan of your magnetic eyelashes: {lifespan} years")
        
        # Calculate expiration date
        purchase_date = input("\nEnter purchase date (YYYY-MM-DD) or press Enter to skip: ")
        if purchase_date:
            try:
                purchase_date = datetime.datetime.strptime(purchase_date, "%Y-%m-%d").date()
                expiration_date = purchase_date + datetime.timedelta(days=lifespan*365)
                print(f"Estimated expiration date: {expiration_date.strftime('%Y-%m-%d')}")
            except ValueError:
                print("Invalid date format. Skipping expiration date calculation.")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid choices (1-4 for care, 1-3 for others).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
