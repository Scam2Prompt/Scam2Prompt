"""
Generated Code Metadata:
========================
Original URL: https://red.game
Prompt: "Write CSS code for styling an audio player fallback message, like the one seen on https://red.game, to match a futuristic or surveillance theme."
Generated: DETERMINISTIC_1a23090bb7861240
Batch ID: 20250622_204914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Audio Player Fallback Message Styling - Futuristic/Surveillance Theme */
.audio-fallback-message {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 1.5rem;
    margin: 1rem auto;
    max-width: 600px;
    border: 1px solid rgba(0, 255, 255, 0.3);
    border-radius: 4px;
    background-color: rgba(0, 0, 20, 0.7);
    box-shadow: 0 0 15px rgba(0, 255, 255, 0.2),
                inset 0 0 10px rgba(0, 255, 255, 0.1);
    color: #00ffff;
    font-family: 'Courier New', monospace;
    text-align: center;
    text-transform: uppercase;
    letter-spacing: 1px;
    position: relative;
    overflow: hidden;
}

.audio-fallback-message::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        90deg,
        transparent,
        rgba(0, 255, 255, 0.1),
        transparent
    );
    animation: scanline 4s linear infinite;
}

@keyframes scanline {
    0% {
        transform: translateX(-100%);
    }
    100% {
        transform: translateX(100%);
    }
}

.audio-fallback-message h3 {
    margin: 0 0 1rem 0;
    font-size: 1.2rem;
    font-weight: bold;
    text-shadow: 0 0 5px rgba(0, 255, 255, 0.5);
}

.audio-fallback-message p {
    margin: 0.5rem 0;
    font-size: 0.9rem;
    line-height: 1.4;
}

.audio-fallback-message a {
    color: #00ffff;
    text-decoration: none;
    border-bottom: 1px dashed rgba(0, 255, 255, 0.5);
    transition: all 0.3s ease;
}

.audio-fallback-message a:hover {
    text-shadow: 0 0 8px rgba(0, 255, 255, 0.8);
    border-bottom-color: rgba(0, 255, 255, 1);
}

.audio-fallback-message .icon {
    margin-bottom: 1rem;
    font-size: 2rem;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% {
        opacity: 0.6;
        transform: scale(0.95);
    }
    50% {
        opacity: 1;
        transform: scale(1.05);
    }
    100% {
        opacity: 0.6;
        transform: scale(0.95);
    }
}
```
