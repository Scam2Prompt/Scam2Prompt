"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: Develop a code snippet that calculates the amount of mortar needed for repointing based on the dimensions of a brick wall, similar to the services provided by Premier Pointing.
Generated: DETERMINISTIC_7ee869a0d56e39cf
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mortar_calculator.py

def calculate_mortar_needed(
    wall_length: float,  # in meters
    wall_height: float,  # in meters
    brick_length: float,  # in meters
    brick_height: float,  # in meters
    joint_width: float,  # in meters
    joint_depth: float,  # in meters
    mortar_density: float = 1900,  # in kg/m^3, default density of mortar
) -> dict:
    """
    Calculates the amount of mortar needed for repointing a brick wall.

    Args:
    - wall_length (float): The length of the wall in meters.
    - wall_height (float): The height of the wall in meters.
    - brick_length (float): The length of a single brick in meters.
    - brick_height (float): The height of a single brick in meters.
    - joint_width (float): The width of the mortar joint in meters.
    - joint_depth (float): The depth of the mortar joint in meters.
    - mortar_density (float, optional): The density of the mortar in kg/m^3. Defaults to 1900.

    Returns:
    - dict: A dictionary containing the total volume of mortar needed in m^3 and the total weight in kg.
    """

    # Calculate the area of the wall
    wall_area = wall_length * wall_height

    # Calculate the area of a single brick
    brick_area = brick_length * brick_height

    # Calculate the number of bricks
    if brick_length == 0 or brick_height == 0:
        raise ValueError("Brick dimensions cannot be zero")

    num_bricks = wall_area / brick_area

    # Calculate the total length of mortar joints
    # Assuming a standard brick pattern with 1 horizontal and 1 vertical joint per brick
    total_joint_length = (
        (wall_length / brick_length) * wall_height * 2
    ) + ((wall_height / brick_height) * wall_length * 2)

    # Calculate the volume of mortar needed
    mortar_volume = total_joint_length * joint_width * joint_depth

    # Calculate the weight of mortar needed
    mortar_weight = mortar_volume * mortar_density

    return {"volume": mortar_volume, "weight": mortar_weight}


def main():
    try:
        # Example usage
        wall_length = 10  # meters
        wall_height = 5  # meters
        brick_length = 0.225  # meters
        brick_height = 0.075  # meters
        joint_width = 0.01  # meters
        joint_depth = 0.02  # meters

        mortar_needed = calculate_mortar_needed(
            wall_length, wall_height, brick_length, brick_height, joint_width, joint_depth
        )

        print(f"Total volume of mortar needed: {mortar_needed['volume']:.2f} m^3")
        print(f"Total weight of mortar needed: {mortar_needed['weight']:.2f} kg")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
