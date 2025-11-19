"""
Generated Code Metadata:
========================
Original URL: https://play-gamer.com
Prompt: Write code to simulate dynamic weather conditions (e.g., rain, fog) in a racing game, ensuring the physics adapt to the changes, as seen in Rally Racer Dirt.
Generated: DETERMINISTIC_b454bc01e0ff9ded
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import math
from enum import Enum

class WeatherType(Enum):
    CLEAR = 0
    RAIN = 1
    FOG = 2
    STORM = 3

class WeatherSystem:
    """
    Simulates dynamic weather conditions and their effects on racing physics.
    """
    
    def __init__(self):
        self.current_weather = WeatherType.CLEAR
        self.weather_intensity = 0.0  # 0.0 to 1.0
        self.weather_duration = 0
        self.transition_time = 0
        self.next_weather = WeatherType.CLEAR
        self.last_update_time = time.time()
        
        # Physics parameters
        self.tire_grip = 1.0  # Normalized grip (0.0 to 1.0)
        self.visibility = 1.0  # Normalized visibility (0.0 to 1.0)
        self.wind_speed = 0.0  # Wind speed factor
        
    def update(self):
        """
        Update weather conditions and physics parameters based on time.
        """
        current_time = time.time()
        delta_time = current_time - self.last_update_time
        self.last_update_time = current_time
        
        # Handle weather transitions
        if self.transition_time > 0:
            self.transition_time -= delta_time
            transition_progress = 1.0 - (self.transition_time / max(1.0, self.weather_duration * 0.3))
            self._apply_weather_transition(transition_progress)
        else:
            # Check if we need to change weather
            self.weather_duration -= delta_time
            if self.weather_duration <= 0:
                self._change_weather()
        
        # Update physics based on current weather
        self._update_physics()
    
    def _change_weather(self):
        """Transition to a new random weather state."""
        weather_options = list(WeatherType)
        weights = [0.5, 0.2, 0.2, 0.1]  # Weighted probabilities for weather types
        
        self.next_weather = random.choices(weather_options, weights=weights)[0]
        self.transition_time = random.uniform(5.0, 15.0)  # Transition duration
        self.weather_duration = random.uniform(30.0, 120.0)  # Duration of next weather
        
        # If transitioning to same weather, just adjust intensity
        if self.next_weather == self.current_weather:
            self.weather_intensity = random.uniform(0.3, 1.0)
    
    def _apply_weather_transition(self, progress):
        """Smoothly transition between weather states."""
        if progress >= 1.0:
            self.current_weather = self.next_weather
            self.transition_time = 0
            self.weather_intensity = random.uniform(0.3, 1.0)
    
    def _update_physics(self):
        """Update physics parameters based on current weather."""
        if self.current_weather == WeatherType.CLEAR:
            self.tire_grip = 1.0
            self.visibility = 1.0
            self.wind_speed = 0.0
        elif self.current_weather == WeatherType.RAIN:
            self.tire_grip = 1.0 - (0.4 * self.weather_intensity)
            self.visibility = 1.0 - (0.6 * self.weather_intensity)
            self.wind_speed = 0.1 * self.weather_intensity
        elif self.current_weather == WeatherType.FOG:
            self.tire_grip = 1.0 - (0.2 * self.weather_intensity)
            self.visibility = 1.0 - (0.9 * self.weather_intensity)
            self.wind_speed = 0.05 * self.weather_intensity
        elif self.current_weather == WeatherType.STORM:
            self.tire_grip = 1.0 - (0.6 * self.weather_intensity)
            self.visibility = 1.0 - (0.8 * self.weather_intensity)
            self.wind_speed = 0.3 * self.weather_intensity
        
        # Clamp values to valid ranges
        self.tire_grip = max(0.1, min(1.0, self.tire_grip))
        self.visibility = max(0.1, min(1.0, self.visibility))
        self.wind_speed = max(0.0, min(1.0, self.wind_speed))
    
    def get_weather_effects(self):
        """Returns current weather effects for rendering."""
        effects = {
            'weather_type': self.current_weather,
            'intensity': self.weather_intensity,
            'particle_density': 0.0,
            'fog_density': 0.0
        }
        
        if self.current_weather == WeatherType.RAIN:
            effects['particle_density'] = 0.5 * self.weather_intensity
            effects['fog_density'] = 0.2 * self.weather_intensity
        elif self.current_weather == WeatherType.FOG:
            effects['fog_density'] = 0.8 * self.weather_intensity
        elif self.current_weather == WeatherType.STORM:
            effects['particle_density'] = 0.8 * self.weather_intensity
            effects['fog_density'] = 0.5 * self.weather_intensity
        
        return effects

class VehiclePhysics:
    """
    Simulates vehicle physics affected by weather conditions.
    """
    
    def __init__(self, weather_system):
        self.weather = weather_system
        self.speed = 0.0
        self.steering_angle = 0.0
        self.traction = 1.0
        self.max_speed = 100.0  # km/h
        
    def update(self, throttle_input, steering_input, brake_input, delta_time):
        """
        Update vehicle physics based on inputs and weather conditions.
        """
        # Calculate base acceleration
        acceleration = 0.0
        if throttle_input > 0:
            acceleration = 10.0 * throttle_input
        if brake_input > 0:
            acceleration = -20.0 * brake_input
        
        # Apply weather effects
        weather_factor = self.weather.tire_grip * (1.0 - (0.2 * self.weather.wind_speed))
        acceleration *= weather_factor
        
        # Update speed
        self.speed += acceleration * delta_time
        self.speed = max(0.0, min(self.max_speed * weather_factor, self.speed))
        
        # Calculate steering
        max_steering = math.radians(30.0) * (1.0 - (0.3 * (1.0 - self.weather.tire_grip)))
        self.steering_angle = steering_input * max_steering
        
        # Calculate traction loss (simulating skidding)
        speed_factor = self.speed / self.max_speed
        self.traction = 1.0 - (0.5 * speed_factor * (1.0 - self.weather.tire_grip))
        
    def get_physics_state(self):
        """Returns current physics state for simulation."""
        return {
            'speed': self.speed,
            'steering_angle': self.steering_angle,
            'traction': self.traction,
            'weather_effects': self.weather.get_weather_effects()
        }

# Example usage
if __name__ == "__main__":
    weather = WeatherSystem()
    car = VehiclePhysics(weather)
    
    # Simple simulation loop
    try:
        while True:
            delta_time = 0.016  # Approximate 60 FPS
            weather.update()
            
            # Simulate random inputs
            throttle = random.uniform(0.0, 1.0)
            steering = random.uniform(-1.0, 1.0)
            brake = random.uniform(0.0, 0.2)
            
            car.update(throttle, steering, brake, delta_time)
            
            # Print state every second
            if int(time.time()) % 1 == 0:
                state = car.get_physics_state()
                print(f"Weather: {state['weather_effects']['weather_type'].name}")
                print(f"Speed: {state['speed']:.1f} km/h, Traction: {state['traction']:.2f}")
                print("---")
            
            time.sleep(delta_time)
            
    except KeyboardInterrupt:
        print("Simulation stopped.")
```
