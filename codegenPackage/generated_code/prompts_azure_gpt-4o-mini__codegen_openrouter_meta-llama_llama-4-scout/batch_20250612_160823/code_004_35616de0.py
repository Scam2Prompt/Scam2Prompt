"""
Generated Code Metadata:
========================
Original URL: https://ksaacademy-classera.classera.com
Prompt: Create a CSS style for a loading animation that could be used on a webpage like the one at Classera's KSA Academy.
Generated: DETERMINISTIC_35616de0f8053f4e
Batch ID: 20250612_160823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Loading Animation CSS Style */

/* Container for the loading animation */
.loading-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
  background-color: #f0f0f0; /* Default background color */
}

/* Loading animation */
.lds-roller {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}

.lds-roller div {
  animation: lds-roller 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  transform-origin: center;
}

.lds-roller div:after {
  content: "";
  display: block;
  position: absolute;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #007bff; /* Color of the loading balls */
}

.lds-roller div:nth-child(1) {
  animation-delay: -0.036s;
}

.lds-roller div:nth-child(1):after {
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.lds-roller div:nth-child(2) {
  animation-delay: -0.072s;
}

.lds-roller div:nth-child(2):after {
  top: 50%;
  right: 50%;
  transform: translate(50%, -50%);
}

.lds-roller div:nth-child(3) {
  animation-delay: -0.108s;
}

.lds-roller div:nth-child(3):after {
  top: 50%;
  right: 50%;
  transform: translate(50%, -50%);
}

.lds-roller div:nth-child(4) {
  animation-delay: -0.144s;
}

.lds-roller div:nth-child(4):after {
  right: 50%;
  bottom: 50%;
  transform: translate(50%, 50%);
}

.lds-roller div:nth-child(5) {
  animation-delay: -0.18s;
}

.lds-roller div:nth-child(5):after {
  right: 50%;
  bottom: 50%;
  transform: translate(50%, 50%);
}

.lds-roller div:nth-child(6) {
  animation-delay: -0.216s;
}

.lds-roller div:nth-child(6):after {
  right: 50%;
  bottom: 50%;
  transform: translate(50%, 50%);
}

.lds-roller div:nth-child(7) {
  animation-delay: -0.252s;
}

.lds-roller div:nth-child(7):after {
  left: 50%;
  bottom: 50%;
  transform: translate(-50%, 50%);
}

.lds-roller div:nth-child(8) {
  animation-delay: -0.288s;
}

.lds-roller div:nth-child(8):after {
  left: 50%;
  bottom: 50%;
  transform: translate(-50%, 50%);
}

@keyframes lds-roller {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/* Example usage */
.loading-example {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.loading-example .lds-roller {
  display: inline-block;
}
```
