"""
Generated Code Metadata:
========================
Original URL: https://genopets.eu
Prompt: "How would you implement a 3D pet avatar rendering system using WebGL and JavaScript, suitable for a web-based pet simulation game?"
Generated: DETERMINISTIC_f1463dbfd2207c72
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// 3D Pet Avatar Rendering System using WebGL and JavaScript

// Ensure the script runs after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    // Initialize WebGL context
    const canvas = document.getElementById("petCanvas");
    const gl = canvas.getContext("webgl");

    if (!gl) {
        console.error("WebGL is not supported by your browser.");
        return;
    }

    // Vertex shader source code
    const vertexShaderSource = `
        attribute vec3 aPosition;
        attribute vec3 aColor;
        uniform mat4 uModelViewMatrix;
        uniform mat4 uProjectionMatrix;
        varying vec3 vColor;
        void main() {
            gl_Position = uProjectionMatrix * uModelViewMatrix * vec4(aPosition, 1.0);
            vColor = aColor;
        }
    `;

    // Fragment shader source code
    const fragmentShaderSource = `
        precision mediump float;
        varying vec3 vColor;
        void main() {
            gl_FragColor = vec4(vColor, 1.0);
        }
    `;

    // Compile shader function
    function compileShader(gl, source, type) {
        const shader = gl.createShader(type);
        gl.shaderSource(shader, source);
        gl.compileShader(shader);

        if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
            console.error("Error compiling shader:", gl.getShaderInfoLog(shader));
            gl.deleteShader(shader);
            return null;
        }

        return shader;
    }

    // Create and link shader program
    const vertexShader = compileShader(gl, vertexShaderSource, gl.VERTEX_SHADER);
    const fragmentShader = compileShader(gl, fragmentShaderSource, gl.FRAGMENT_SHADER);

    const shaderProgram = gl.createProgram();
    gl.attachShader(shaderProgram, vertexShader);
    gl.attachShader(shaderProgram, fragmentShader);
    gl.linkProgram(shaderProgram);

    if (!gl.getProgramParameter(shaderProgram, gl.LINK_STATUS)) {
        console.error("Error linking shader program:", gl.getProgramInfoLog(shaderProgram));
        return;
    }

    gl.useProgram(shaderProgram);

    // Define pet avatar geometry (a simple cube for demonstration)
    const vertices = new Float32Array([
        // Positions       // Colors
        -0.5, -0.5, -0.5,  1.0, 0.0, 0.0, // Red
         0.5, -0.5, -0.5,  0.0, 1.0, 0.0, // Green
         0.5,  0.5, -0.5,  0.0, 0.0, 1.0, // Blue
        -0.5,  0.5, -0.5,  1.0, 1.0, 0.0, // Yellow
        -0.5, -0.5,  0.5,  1.0, 0.0, 1.0, // Magenta
         0.5, -0.5,  0.5,  0.0, 1.0, 1.0, // Cyan
         0.5,  0.5,  0.5,  1.0, 1.0, 1.0, // White
        -0.5,  0.5,  0.5,  0.0, 0.0, 0.0  // Black
    ]);

    const indices = new Uint16Array([
        0, 1, 2,  0, 2, 3, // Front face
        4, 5, 6,  4, 6, 7, // Back face
        0, 4, 7,  0, 7, 3, // Left face
        1, 5, 6,  1, 6, 2, // Right face
        3, 2, 6,  3, 6, 7, // Top face
        0, 1, 5,  0, 5, 4  // Bottom face
    ]);

    // Create and bind vertex buffer
    const vertexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertexBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

    // Create and bind index buffer
    const indexBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indexBuffer);
    gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, indices, gl.STATIC_DRAW);

    // Get attribute locations
    const aPosition = gl.getAttribLocation(shaderProgram, "aPosition");
    const aColor = gl.getAttribLocation(shaderProgram, "aColor");

    // Enable attributes and set pointers
    gl.vertexAttribPointer(aPosition, 3, gl.FLOAT, false, 6 * Float32Array.BYTES_PER_ELEMENT, 0);
    gl.enableVertexAttribArray(aPosition);

    gl.vertexAttribPointer(aColor, 3, gl.FLOAT, false, 6 * Float32Array.BYTES_PER_ELEMENT, 3 * Float32Array.BYTES_PER_ELEMENT);
    gl.enableVertexAttribArray(aColor);

    // Get uniform locations
    const uModelViewMatrix = gl.getUniformLocation(shaderProgram, "uModelViewMatrix");
    const uProjectionMatrix = gl.getUniformLocation(shaderProgram, "uProjectionMatrix");

    // Define matrices
    const modelViewMatrix = mat4.create();
    const projectionMatrix = mat4.create();

    mat4.perspective(projectionMatrix, Math.PI / 4, canvas.width / canvas.height, 0.1, 100.0);
    mat4.translate(modelViewMatrix, modelViewMatrix, [0, 0, -3]);

    // Set uniform values
    gl.uniformMatrix4fv(uModelViewMatrix, false, modelViewMatrix);
    gl.uniformMatrix4fv(uProjectionMatrix, false, projectionMatrix);

    // Render loop
    function render() {
        gl.clearColor(0.1, 0.1, 0.1, 1.0); // Set background color
        gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT); // Clear buffers

        gl.enable(gl.DEPTH_TEST); // Enable depth testing

        gl.drawElements(gl.TRIANGLES, indices.length, gl.UNSIGNED_SHORT, 0); // Draw the cube

        requestAnimationFrame(render); // Loop the render function
    }

    render(); // Start rendering
});

// HTML Canvas Element
// <canvas id="petCanvas" width="800" height="600"></canvas>
```
