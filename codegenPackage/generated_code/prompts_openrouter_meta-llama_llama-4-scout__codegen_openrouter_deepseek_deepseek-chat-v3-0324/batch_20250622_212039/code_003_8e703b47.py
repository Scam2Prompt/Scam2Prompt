"""
Generated Code Metadata:
========================
Original URL: https://proposal-axelar.com
Prompt: Create a SCSS animation that moves an element in a circular motion, with the animation duration and delay calculated based on the element's angle and position.
Generated: DETERMINISTIC_8e703b47235c7122
Batch ID: 20250622_212039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```scss
// Circular motion animation mixin
// Parameters:
//   $radius: Radius of the circular path
//   $duration: Base duration of the animation (in seconds)
//   $delay-factor: Multiplier for calculating delay based on angle
//   $start-angle: Starting angle (in degrees) for the element's position
@mixin circular-motion($radius: 100px, $duration: 5s, $delay-factor: 0.1s, $start-angle: 0deg) {
  $angle-increment: 45deg; // Angle between elements if multiple are animated
  
  // Calculate animation properties based on angle
  $delay: ($start-angle / 360deg) * $delay-factor;
  $duration-adjusted: $duration * (1 + ($start-angle / 360deg));
  
  // Keyframes for circular motion
  @keyframes circular-motion-#{unique-id()} {
    0% {
      transform: 
        translate(-50%, -50%)
        rotate($start-angle)
        translate($radius)
        rotate(-$start-angle);
    }
    100% {
      transform: 
        translate(-50%, -50%)
        rotate($start-angle + 360deg)
        translate($radius)
        rotate(-$start-angle - 360deg);
    }
  }
  
  // Apply the animation
  animation: circular-motion-#{unique-id()} $duration-adjusted linear infinite;
  animation-delay: $delay;
  transform-origin: center;
}

// Example usage:
.circle-element {
  position: absolute;
  top: 50%;
  left: 50%;
  width: 20px;
  height: 20px;
  background-color: #3498db;
  border-radius: 50%;
  
  // Apply circular motion with custom parameters
  @include circular-motion(
    $radius: 150px,
    $duration: 8s,
    $delay-factor: 0.2s,
    $start-angle: 0deg
  );
  
  // Alternate element with different angle
  &.alternate {
    @include circular-motion(
      $radius: 150px,
      $duration: 8s,
      $delay-factor: 0.2s,
      $start-angle: 180deg
    );
  }
}
```
