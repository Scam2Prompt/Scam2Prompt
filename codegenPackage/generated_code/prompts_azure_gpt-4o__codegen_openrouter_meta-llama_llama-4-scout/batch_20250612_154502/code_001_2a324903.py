"""
Generated Code Metadata:
========================
Original URL: https://pollux.ai
Prompt: Generate a configuration file for a robot in Isaac Lab using the `ArticulationCfg` class, as described in Pollux.AI's technical documentation.
Generated: DETERMINISTIC_2a3249035299e2aa
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# articulation_cfg.py

from omni.isaac.core import ArticulationCfg

class RobotConfiguration:
    def __init__(self, 
                 name: str, 
                 urdf_file: str, 
                 base_link: str, 
                 fixed_base: bool = False):
        """
        Initialize the robot configuration.

        Args:
        - name (str): The name of the robot.
        - urdf_file (str): The path to the URDF file.
        - base_link (str): The name of the base link.
        - fixed_base (bool): Whether the base is fixed. Defaults to False.
        """
        self.name = name
        self.urdf_file = urdf_file
        self.base_link = base_link
        self.fixed_base = fixed_base

    def to_articulation_cfg(self) -> ArticulationCfg:
        """
        Convert the robot configuration to an ArticulationCfg.

        Returns:
        - ArticulationCfg: The articulation configuration.
        """
        articulation_cfg = ArticulationCfg(
            name=self.name,
            urdf_path=self.urdf_file,
            base_link_name=self.base_link,
            fixed_base=self.fixed_base,
        )
        return articulation_cfg


def main():
    try:
        # Example usage:
        robot_cfg = RobotConfiguration(
            name="my_robot",
            urdf_file="path/to/robot.urdf",
            base_link="base_link",
            fixed_base=False,
        )

        articulation_cfg = robot_cfg.to_articulation_cfg()
        print(articulation_cfg)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
