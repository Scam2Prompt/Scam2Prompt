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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3D Interior Design Transformation</title>
    <style>
        body { margin: 0; overflow: hidden; }
        canvas { display: block; }
        #slider { position: absolute; top: 20px; left: 50%; transform: translateX(-50%); z-index: 10; }
    </style>
</head>
<body>
    <input type="range" id="slider" min="0" max="100" value="50">
    <canvas id="webglCanvas"></canvas>
    
    <script>
        // Initialize WebGL context
        const canvas = document.getElementById('webglCanvas');
        const gl = canvas.getContext('webgl');

        // Handle possible context loss
        if (!gl) {
            console.error("Unable to initialize WebGL. Your browser may not support it.");
        }

        // Set canvas size
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        // Vertex shader source code
        const vertexShaderSource = `
            attribute vec3 aPosition;
            attribute vec2 aTexCoord;
            varying vec2 vTexCoord;
            void main() {
                gl_Position = vec4(aPosition, 1.0);
                vTexCoord = aTexCoord;
            }
        `;

        // Fragment shader source code
        const fragmentShaderSource = `
            precision mediump float;
            varying vec2 vTexCoord;
            uniform sampler2D uTextureBefore;
            uniform sampler2D uTextureAfter;
            uniform float uMixRatio;

            void main() {
                vec4 colorBefore = texture2D(uTextureBefore, vTexCoord);
                vec4 colorAfter = texture2D(uTextureAfter, vTexCoord);
                gl_FragColor = mix(colorBefore, colorAfter, uMixRatio);
            }
        `;

        // Compile shader
        function compileShader(source, type) {
            const shader = gl.createShader(type);
            gl.shaderSource(shader, source);
            gl.compileShader(shader);
            if (gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
                return shader;
            }
            console.error('An error occurred compiling the shaders: ' + gl.getShaderInfoLog(shader));
            gl.deleteShader(shader);
        }

        // Create and link shaders program
        const vertexShader = compileShader(vertexShaderSource, gl.VERTEX_SHADER);
        const fragmentShader = compileShader(fragmentShaderSource, gl.FRAGMENT_SHADER);
        const shaderProgram = gl.createProgram();
        gl.attachShader(shaderProgram, vertexShader);
        gl.attachShader(shaderProgram, fragmentShader);
        gl.linkProgram(shaderProgram);
        
        if (!gl.getProgramParameter(shaderProgram, gl.LINK_STATUS)) {
            console.error('Unable to initialize the shader program: ' + gl.getProgramInfoLog(shaderProgram));
        }

        // Define geometry for a full-screen quad
        const positions = new Float32Array([
            -1.0, -1.0,
             1.0, -1.0,
            -1.0,  1.0,
             1.0,  1.0,
        ]);

        const texCoords = new Float32Array([
            0.0, 1.0,
            1.0, 1.0,
            0.0, 0.0,
            1.0, 0.0,
        ]);

        const positionBuffer = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, positions, gl.STATIC_DRAW);

        const texCoordBuffer = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, texCoordBuffer);
        gl.bufferData(gl.ARRAY_BUFFER, texCoords, gl.STATIC_DRAW);

        // Load textures
        function loadTexture(url) {
            const texture = gl.createTexture();
            const image = new Image();
            image.onload = () => {
                gl.bindTexture(gl.TEXTURE_2D, texture);
                gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
                gl.generateMipmap(gl.TEXTURE_2D);
            };
            image.src = url;
            return texture;
        }

        const textureBefore = loadTexture('path/to/your/before-image.jpg');
        const textureAfter = loadTexture('path/to/your/after-image.jpg');

        // Main rendering function
        function render(mixRatio) {
            gl.clear(gl.COLOR_BUFFER_BIT);

            gl.useProgram(shaderProgram);
            gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
            const positionLocation = gl.getAttribLocation(shaderProgram, 'aPosition');
            gl.enableVertexAttribArray(positionLocation);
            gl.vertexAttribPointer(positionLocation, 2, gl.FLOAT, false, 0, 0);

            gl.bindBuffer(gl.ARRAY_BUFFER, texCoordBuffer);
            const texCoordLocation = gl.getAttribLocation(shaderProgram, 'aTexCoord');
            gl.enableVertexAttribArray(texCoordLocation);
            gl.vertexAttribPointer(texCoordLocation, 2, gl.FLOAT, false, 0, 0);

            gl.activeTexture(gl.TEXTURE0);
            gl.bindTexture(gl.TEXTURE_2D, textureBefore);
            const uTextureBeforeLocation = gl.getUniformLocation(shaderProgram, 'uTextureBefore');
            gl.uniform1i(uTextureBeforeLocation, 0);

            gl.activeTexture(gl.TEXTURE1);
            gl.bindTexture(gl.TEXTURE_2D, textureAfter);
            const uTextureAfterLocation = gl.getUniformLocation(shaderProgram, 'uTextureAfter');
            gl.uniform1i(uTextureAfterLocation, 1);

            const uMixRatioLocation = gl.getUniformLocation(shaderProgram, 'uMixRatio');
            gl.uniform1f(uMixRatioLocation, mixRatio);

            gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
        }

        // Slider event listener
        const slider = document.getElementById('slider');
        slider.addEventListener('input', (event) => {
            const mixRatio = event.target.value / 100;
            render(mixRatio);
        });

        // Initial render
        render(slider.value / 100);
    </script>
</body>
</html>
```
