"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greystoneinfra.in
Prompt: Generate a script using JavaScript and WebGL to create an interactive "before-and-after" view of a 3D interior design transformation, similar to the virtual reality services provided by Greystone Infra.
Generated: DETERMINISTIC_18c09b5bb2438c0c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Interactive "before-and-after" 3D interior design viewer.
 * This script uses WebGL to render two scenes and allows users to interactively toggle
 * between the "before" and "after" views via a slider.
 */

// Ensure modern browsers support WebGL
if (!window.WebGLRenderingContext) {
  alert("WebGL is not supported by your browser. Please upgrade to a modern browser.");
  throw new Error("WebGL not supported");
}

// HTML setup for slider and canvas
document.body.innerHTML = `
  <div style="position: relative; width: 100%; height: 100%;">
    <canvas id="webglCanvas" style="width: 100%; height: 100%;"></canvas>
    <input type="range" id="slider" min="0" max="100" value="50" 
           style="position: absolute; bottom: 10px; left: 10px; width: 90%; z-index: 10;">
  </div>
`;

// JavaScript/WebGL code starts here
const canvas = document.getElementById('webglCanvas');
const slider = document.getElementById('slider');
const gl = canvas.getContext('webgl');

// Resize canvas to fit the window
function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  gl.viewport(0, 0, canvas.width, canvas.height);
}

resizeCanvas();
window.addEventListener('resize', resizeCanvas);

// Vertex shader source code
const vertexShaderSource = `
  attribute vec3 aPosition;
  attribute vec2 aTexCoord;
  varying vec2 vTexCoord;
  void main(void) {
    gl_Position = vec4(aPosition, 1.0);
    vTexCoord = aTexCoord;
  }
`;

// Fragment shader source code
const fragmentShaderSource = `
  precision mediump float;
  uniform sampler2D uBeforeTexture;
  uniform sampler2D uAfterTexture;
  uniform float uMixFactor;
  varying vec2 vTexCoord;

  void main(void) {
    vec4 beforeColor = texture2D(uBeforeTexture, vTexCoord);
    vec4 afterColor = texture2D(uAfterTexture, vTexCoord);
    gl_FragColor = mix(beforeColor, afterColor, uMixFactor);
  }
`;

// Create and compile shader
function createShader(gl, type, source) {
  const shader = gl.createShader(type);
  gl.shaderSource(shader, source);
  gl.compileShader(shader);
  if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
    console.error('Shader compilation error:', gl.getShaderInfoLog(shader));
    gl.deleteShader(shader);
    throw new Error('Shader compilation failed');
  }
  return shader;
}

// Link shaders to create program
function createProgram(gl, vertexShader, fragmentShader) {
  const program = gl.createProgram();
  gl.attachShader(program, vertexShader);
  gl.attachShader(program, fragmentShader);
  gl.linkProgram(program);
  if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
    console.error('Program linking error:', gl.getProgramInfoLog(program));
    gl.deleteProgram(program);
    throw new Error('Program linking failed');
  }
  return program;
}

// Load textures
function loadTexture(gl, url) {
  const texture = gl.createTexture();
  const image = new Image();
  image.onload = () => {
    gl.bindTexture(gl.TEXTURE_2D, texture);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
    gl.generateMipmap(gl.TEXTURE_2D);
    gl.bindTexture(gl.TEXTURE_2D, null);
  };
  image.src = url;
  return texture;
}

// Prepare shaders and program
const vertexShader = createShader(gl, gl.VERTEX_SHADER, vertexShaderSource);
const fragmentShader = createShader(gl, gl.FRAGMENT_SHADER, fragmentShaderSource);
const program = createProgram(gl, vertexShader, fragmentShader);

// Load "before" and "after" textures
const beforeTexture = loadTexture(gl, 'path/to/before.jpg'); // Replace with actual image path
const afterTexture = loadTexture(gl, 'path/to/after.jpg'); // Replace with actual image path

// Define vertices and texture coordinates for a full-screen quad
const vertices = new Float32Array([
  -1, -1, 0, 0, 1,
   1, -1, 0, 1, 1,
  -1,  1, 0, 0, 0,
   1,  1, 0, 1, 0,
]);
const indices = new Uint16Array([0, 1, 2, 2, 1, 3]);

// Create and bind buffer
const vertexBuffer = gl.createBuffer();
gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

const indexBuffer = gl.createBuffer();
gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, gl.STATIC_DRAW);

// Configure attributes
const aPosition = gl.getAttribLocation(program, 'aPosition');
const aTexCoord = gl.getAttribLocation(program, 'aTexCoord');

gl.vertexAttribPointer(aPosition, 3, gl.FLOAT, false, 20, 0);
gl.vertexAttribPointer(aTexCoord, 2, gl.FLOAT, false, 20, 12);

gl.enableVertexAttribArray(aPosition);
gl.enableVertexAttribArray(aTexCoord);

// Activate the program
gl.useProgram(program);

// Bind textures
const uBeforeTexture = gl.getUniformLocation(program, 'uBeforeTexture');
const uAfterTexture = gl.getUniformLocation(program, 'uAfterTexture');
const uMixFactor = gl.getUniformLocation(program, 'uMixFactor');

gl.activeTexture(gl.TEXTURE0);
gl.bindTexture(gl.TEXTURE_2D, beforeTexture);
gl.uniform1i(uBeforeTexture, 0);

gl.activeTexture(gl.TEXTURE1);
gl.bindTexture(gl.TEXTURE_2D, afterTexture);
gl.uniform1i(uAfterTexture, 1);

// Slider interaction
slider.addEventListener('input', () => {
  const mixFactor = slider.value / 100;
  gl.uniform1f(uMixFactor, mixFactor);
  renderScene();
});

// Render scene
function renderScene() {
  gl.clearColor(0, 0, 0, 1);
  gl.clear(gl.COLOR_BUFFER_BIT);
  gl.drawElements(gl.TRIANGLES, indices.length, gl.UNSIGNED_SHORT, 0);
}

// Initial render
gl.uniform1f(uMixFactor, 0.5); // Default mix factor
renderScene();
```
