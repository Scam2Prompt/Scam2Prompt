"""
Generated Code Metadata:
========================
Original URL: https://perez-3-jennifer-89.pages.dev
Prompt: Generate a CSS code snippet to style a webpage with a sense of urgency, including a "Hurry up" message.
Generated: DETERMINISTIC_204e95b93df0b166
Batch ID: 20250622_205230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Main container styling */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Arial', sans-serif;
}

/* Urgency banner styling */
.urgency-banner {
    background-color: #ff4444;
    color: white;
    padding: 15px 20px;
    border-radius: 5px;
    text-align: center;
    margin-bottom: 30px;
    box-shadow: 0 4px 8px rgba(255, 68, 68, 0.3);
    animation: pulse 1.5s infinite;
}

/* Urgency message styling */
.urgency-message {
    font-size: 1.5rem;
    font-weight: bold;
    margin: 0;
    text-transform: uppercase;
}

/* Secondary urgency text */
.urgency-subtext {
    font-size: 1rem;
    margin: 5px 0 0;
    opacity: 0.9;
}

/* Countdown timer styling */
.countdown-timer {
    font-size: 2rem;
    font-weight: bold;
    color: #ff0000;
    margin: 20px 0;
    text-align: center;
}

/* Call-to-action button styling */
.cta-button {
    background-color: #ff0000;
    color: white;
    border: none;
    padding: 12px 30px;
    font-size: 1.2rem;
    border-radius: 5px;
    cursor: pointer;
    transition: all 0.3s ease;
    display: block;
    margin: 0 auto;
    text-transform: uppercase;
    font-weight: bold;
}

.cta-button:hover {
    background-color: #cc0000;
    transform: scale(1.05);
}

/* Pulse animation for urgency effect */
@keyframes pulse {
    0% {
        box-shadow: 0 0 0 0 rgba(255, 68, 68, 0.7);
    }
    70% {
        box-shadow: 0 0 0 10px rgba(255, 68, 68, 0);
    }
    100% {
        box-shadow: 0 0 0 0 rgba(255, 68, 68, 0);
    }
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .urgency-message {
        font-size: 1.2rem;
    }
    
    .countdown-timer {
        font-size: 1.5rem;
    }
    
    .cta-button {
        padding: 10px 20px;
        font-size: 1rem;
    }
}
```
