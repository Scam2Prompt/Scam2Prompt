"""
Generated Code Metadata:
========================
Original URL: https://pollux.ai
Prompt: Implement a simulation scene in Isaac Lab using Python, starting with an empty environment and customizing it for reinforcement learning experiments, as described on Pollux.AI.
Generated: DETERMINISTIC_ba8e92c3ed6ed1cc
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import omni
from omni.isaac.lab import sim
from omni.isaac.lab.utils import extensions
from omni.isaac.lab.utils.assets import get_assets_root_path
from omni.isaac.lab.simulation_context import SimulationContext
from omni.isaac.lab.robots import Articulation
from omni.isaac.lab.envs import RLTaskEnv
from omni.isaac.lab.tasks import RLTask
from omni.isaac.lab.controllers import DifferentialController
from omni.isaac.lab.utils.torch.maths import set_seed
from omni.isaac.lab.utils.configclass import configclass, partial
from dataclasses import dataclass
import numpy as np
import torch
import carb

@configclass
class RLEnvCfg:
    # Configuration for the RL environment
    seed: int = 42
    num_envs: int = 16
    env_spacing: float = 3.0
    episode_length_s: float = 10.0
    physics_dt: float = 1.0 / 60.0
    rendering_dt: float = 1.0 / 60.0
    sim_device: str = "cuda:0"
    headless: bool = False

@configclass
class CustomTaskCfg:
    # Configuration for the custom task
    robot_urdf_path: str = "path/to/robot.urdf"
    robot_name: str = "robot"
    default_robot_pos: np.ndarray = np.array([0.0, 0.0, 0.5])
    default_robot_orientation: np.ndarray = np.array([1.0, 0.0, 0.0, 0.0])
    goal_position: np.ndarray = np.array([5.0, 0.0, 0.0])
    max_velocity: float = 1.0
    max_angular_velocity: float = 1.0

class CustomTask(RLTask):
    def __init__(self, cfg: CustomTaskCfg, sim_config: RLEnvCfg) -> None:
        super().__init__(cfg, sim_config)
        self._cfg = cfg
        self._sim_config = sim_config

        # Initialize robot
        self._robot = None
        self._goal_position = torch.tensor(cfg.goal_position, device=sim_config.sim_device)

    def set_up_scene(self, scene) -> None:
        super().set_up_scene(scene)
        
        # Load robot
        self._robot = Articulation(
            prim_path=f"/World/{self._cfg.robot_name}",
            name=self._cfg.robot_name,
            usd_path=self._cfg.robot_urdf_path,
            position=self._cfg.default_robot_pos,
            orientation=self._cfg.default_robot_orientation,
        )
        scene.add(self._robot)

        # Add ground plane
        scene.add_ground_plane(size=100.0, color=np.array([0.5, 0.5, 0.5]))

    def get_observations(self) -> dict:
        # Get robot state
        robot_pos, robot_rot = self._robot.get_world_pose()
        robot_vel = self._robot.get_linear_velocity()
        robot_ang_vel = self._robot.get_angular_velocity()

        # Calculate distance to goal
        distance_to_goal = torch.norm(self._goal_position - robot_pos, dim=-1)

        # Return observations
        return {
            "robot_position": robot_pos,
            "robot_rotation": robot_rot,
            "robot_velocity": robot_vel,
            "robot_angular_velocity": robot_ang_vel,
            "distance_to_goal": distance_to_goal
        }

    def calculate_reward(self) -> torch.Tensor:
        # Get current observations
        obs = self.get_observations()
        
        # Reward for moving towards goal
        progress_reward = -obs["distance_to_goal"]
        
        # Penalty for high velocities
        velocity_penalty = -torch.sum(torch.square(obs["robot_velocity"]), dim=-1)
        angular_velocity_penalty = -torch.sum(torch.square(obs["robot_angular_velocity"]), dim=-1)
        
        # Total reward
        total_reward = progress_reward + 0.1 * velocity_penalty + 0.1 * angular_velocity_penalty
        
        return total_reward

    def is_done(self) -> torch.Tensor:
        # Get current observations
        obs = self.get_observations()
        
        # Episode terminates if robot reaches goal or episode length is exceeded
        reached_goal = obs["distance_to_goal"] < 0.5
        exceeded_time = self._env_step_count >= int(self._sim_config.episode_length_s / self._sim_config.physics_dt)
        
        return reached_goal | exceeded_time

class CustomRLEnv(RLTaskEnv):
    def __init__(self, cfg: RLEnvCfg, task_cfg: CustomTaskCfg):
        super().__init__(cfg, task=CustomTask(task_cfg, cfg))

def main():
    # Initialize simulation context
    sim_context = SimulationContext()
    
    # Set up configuration
    env_cfg = RLEnvCfg()
    task_cfg = CustomTaskCfg()
    
    # Set random seed for reproducibility
    set_seed(env_cfg.seed)
    
    try:
        # Create environment
        env = CustomRLEnv(env_cfg, task_cfg)
        
        # Initialize simulation
        sim_context.initialize_simulation()
        
        # Reset environment
        env.reset()
        
        # Main simulation loop
        while not sim_context.is_exiting():
            # Step simulation
            sim_context.step()
            
            # Get actions (random for demonstration)
            actions = torch.rand((env_cfg.num_envs, 2), device=env_cfg.sim_device) * 2 - 1
            
            # Apply actions and step environment
            env.step(actions)
            
            # Render if not headless
            if not env_cfg.headless:
                sim_context.render()
                
    except Exception as e:
        carb.log_error(f"Error in simulation: {e}")
    finally:
        # Cleanup
        sim_context.close()

if __name__ == "__main__":
    main()
```
