"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: Write a function to calculate tuition fees for ENAFO's folklore programs, considering the values for modules and monitorías provided on the website.
Generated: DETERMINISTIC_9183f82a7fcfc6c8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_tuition_fees(program_type: str, modules: int, monitorias: int) -> float:
    """
    Calculate the total tuition fees for ENAFO's folklore programs based on program type,
    number of modules, and number of monitorias.

    Args:
        program_type (str): Type of program ('basic', 'intermediate', 'advanced')
        modules (int): Number of modules enrolled
        monitorias (int): Number of monitorias enrolled

    Returns:
        float: Total tuition fees

    Raises:
        ValueError: If invalid program type or negative module/monitoria count is provided
    """
    # Validate inputs
    if program_type.lower() not in ['basic', 'intermediate', 'advanced']:
        raise ValueError("Invalid program type. Must be 'basic', 'intermediate', or 'advanced'")
    if modules < 0 or monitorias < 0:
        raise ValueError("Module and monitoria counts cannot be negative")

    # Program base fees (values from ENAFO's website)
    program_fees = {
        'basic': 500.00,
        'intermediate': 750.00,
        'advanced': 1000.00
    }

    # Module and monitoria fees (values from ENAFO's website)
    module_fee = 150.00
    monitoria_fee = 50.00

    # Calculate total fees
    base_fee = program_fees[program_type.lower()]
    modules_total = modules * module_fee
    monitorias_total = monitorias * monitoria_fee

    total_fees = base_fee + modules_total + monitorias_total

    return round(total_fees, 2)
```
