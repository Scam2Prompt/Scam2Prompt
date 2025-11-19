"""
Generated Code Metadata:
========================
Original URL: https://poocoingearapp.blogspot.com
Prompt: Generate code to calculate the efficiency of a mechanical system involving moitão (block and tackle) and provide an explanation of the calculations.
Generated: DETERMINISTIC_1da67acb5d5b3095
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module calculates the efficiency of a mechanical system involving a block and tackle (moitão).
It considers the number of rope segments supporting the load and the friction factor to determine
the system's efficiency.
"""

def calculate_mechanical_advantage(number_of_segments: int) -> float:
    """
    Calculate the ideal mechanical advantage of a block and tackle system.
    
    Args:
        number_of_segments (int): Number of rope segments supporting the load.
        
    Returns:
        float: The ideal mechanical advantage.
        
    Raises:
        ValueError: If number_of_segments is less than 1.
    """
    if number_of_segments < 1:
        raise ValueError("Number of segments must be at least 1")
    return float(number_of_segments)

def calculate_efficiency(
    number_of_segments: int,
    friction_factor: float = 0.1,
    load_weight: float = 1.0
) -> float:
    """
    Calculate the efficiency of a block and tackle system considering friction.
    
    Args:
        number_of_segments (int): Number of rope segments supporting the load.
        friction_factor (float, optional): Friction factor per sheave (default 0.1 or 10%).
        load_weight (float, optional): Weight of the load (default 1.0 for ratio calculation).
        
    Returns:
        float: Efficiency as a percentage (0-100).
        
    Raises:
        ValueError: If any input is invalid (segments < 1, negative friction or weight).
    """
    # Validate inputs
    if number_of_segments < 1:
        raise ValueError("Number of segments must be at least 1")
    if friction_factor < 0:
        raise ValueError("Friction factor cannot be negative")
    if load_weight <= 0:
        raise ValueError("Load weight must be positive")
    
    # Calculate ideal mechanical advantage
    ma_ideal = calculate_mechanical_advantage(number_of_segments)
    
    # Calculate actual mechanical advantage considering friction
    # Friction effect is compounded for each sheave (n-1 sheaves in a block and tackle)
    friction_loss = (1 + friction_factor) ** (number_of_segments - 1)
    ma_actual = ma_ideal / friction_loss
    
    # Efficiency is the ratio of actual to ideal mechanical advantage
    efficiency = (ma_actual / ma_ideal) * 100
    
    return efficiency

def main():
    """Example usage of the block and tackle efficiency calculator."""
    try:
        segments = int(input("Enter number of rope segments supporting the load: "))
        friction = float(input("Enter friction factor per sheave (e.g., 0.1 for 10%): "))
        
        efficiency = calculate_efficiency(segments, friction)
        print(f"\nBlock and Tackle System Efficiency: {efficiency:.2f}%")
        
        ma_ideal = calculate_mechanical_advantage(segments)
        print(f"Ideal Mechanical Advantage: {ma_ideal:.1f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
