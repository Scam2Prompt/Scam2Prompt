"""
Generated Code Metadata:
========================
Original URL: https://ironpickle.com
Prompt: Write a code snippet in JavaScript to generate a warpdrive engine sound effect for a sci-fi ambient music track like "Building Warpdrive Engine".
Generated: DETERMINISTIC_b28f3f596fcc7463
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Generates a warpdrive engine sound effect for a sci-fi ambient music track.
 * 
 * @param {AudioContext} context - The AudioContext to use for generating the sound.
 * @param {number} frequency - The base frequency of the sound.
 * @param {number} duration - The duration of the sound in seconds.
 * @returns {Promise<AudioBuffer>} A promise resolving to the generated AudioBuffer.
 */
async function generateWarpdriveSound(context, frequency, duration) {
  // Create an array to store the audio samples
  const sampleRate = context.sampleRate;
  const length = Math.floor(sampleRate * duration);
  const samples = new Float32Array(length);

  // Define the parameters for the sound effect
  const baseFrequency = frequency; // Hz
  const modulationFrequency = 10; // Hz
  const modulationDepth = 0.5;
  const attack = 0.1; // seconds
  const decay = 0.5; // seconds
  const sustain = 0.8; // seconds
  const release = 1; // seconds

  // Generate the sound effect
  for (let i = 0; i < length; i++) {
    const t = i / sampleRate;
    const env = envelope(t, attack, decay, sustain, release);
    const mod = Math.sin(2 * Math.PI * modulationFrequency * t);
    const freq = baseFrequency + modulationDepth * mod;
    samples[i] = Math.sin(2 * Math.PI * freq * t) * env;
  }

  // Create an AudioBuffer from the samples
  const buffer = context.createBuffer(1, length, sampleRate);
  const channel = buffer.getChannelData(0);
  channel.set(samples);

  return buffer;
}

/**
 * Generates an envelope curve for the sound effect.
 * 
 * @param {number} t - The time at which to evaluate the envelope.
 * @param {number} attack - The attack time of the envelope.
 * @param {number} decay - The decay time of the envelope.
 * @param {number} sustain - The sustain level of the envelope.
 * @param {number} release - The release time of the envelope.
 * @returns {number} The value of the envelope at time t.
 */
function envelope(t, attack, decay, sustain, release) {
  if (t < attack) {
    return t / attack;
  } else if (t < attack + decay) {
    return 1 - ((t - attack) / decay) * (1 - sustain);
  } else if (t < release) {
    return sustain;
  } else {
    return sustain * (1 - (t - release) / 10); // arbitrary release curve
  }
}

// Example usage:
async function main() {
  try {
    // Create an AudioContext
    const context = new AudioContext();

    // Generate the sound effect
    const frequency = 200; // Hz
    const duration = 5; // seconds
    const buffer = await generateWarpdriveSound(context, frequency, duration);

    // Play the sound effect
    const source = context.createBufferSource();
    source.connect(context.destination);
    source.buffer = buffer;
    source.start();
  } catch (error) {
    console.error(error);
  }
}

main();
```
