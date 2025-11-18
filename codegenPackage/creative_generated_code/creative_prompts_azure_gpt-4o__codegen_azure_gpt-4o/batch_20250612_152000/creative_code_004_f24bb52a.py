"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refikanadol.pages.dev
Prompt: Suggest tools and frameworks for visualizing AI-generated art in immersive environments, such as the Sphere in Las Vegas, and provide code snippets for integrating 3D visualization.
Generated: DETERMINISTIC_f24bb52ae1952819
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for 3D visualization and immersive environments
import moderngl
import numpy as np
import glfw
from PIL import Image

# Initialize GLFW for window management
if not glfw.init():
    raise Exception("GLFW initialization failed")

# Create a window for rendering immersive environments
window = glfw.create_window(1920, 1080, "AI Art in Immersive 3D Environment", None, None)
if not window:
    glfw.terminate()
    raise Exception("Failed to create GLFW window")

# Set the current OpenGL context
glfw.make_context_current(window)

# Define the shader programs for rendering
vertex_shader = """
#version 330
in vec3 in_position;
in vec2 in_texcoord;
out vec2 frag_texcoord;
uniform mat4 model;
uniform mat4 projection;

void main() {
    frag_texcoord = in_texcoord;
    gl_Position = projection * model * vec4(in_position, 1.0);
}
"""

fragment_shader = """
#version 330
in vec2 frag_texcoord;
out vec4 out_color;
uniform sampler2D texture_sampler;

void main() {
    out_color = texture(texture_sampler, frag_texcoord);
}
"""

# Compile and link the shaders
ctx = moderngl.create_context()
prog = ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)

# Define geometry data (a basic sphere for immersive visualization)
def generate_sphere(radius, segments):
    vertices = []
    indices = []

    for i in range(segments):
        theta1 = i * np.pi / segments
        theta2 = (i + 1) * np.pi / segments

        for j in range(segments * 2):
            phi1 = j * np.pi / segments
            phi2 = (j + 1) * np.pi / segments
            
            # Generate sphere vertices
            vertices.append([
                radius * np.sin(theta1) * np.cos(phi1),
                radius * np.cos(theta1),
                radius * np.sin(theta1) * np.sin(phi1),
            ])
    
    return np.array(vertices, dtype=np.float32)

sphere_vertices = generate_sphere(1, 32)

# Load AI-generated texture/art
def load_texture(filepath):
    img = Image.open(filepath).transpose(Image.FLIP_TOP_BOTTOM)
    texture_data = np.array(img).astype(np.uint8)
    texture = ctx.texture(img.size, 3, texture_data.tobytes())
    texture.use()
    return texture

ai_texture = load_texture('ai_generated_art.jpg')  # Replace with a path to your AI-generated image.

# Create a buffer for sphere geometry
vbo = ctx.buffer(sphere_vertices.tobytes())

vao = ctx.simple_vertex_array(prog, vbo, 'in_position', 'in_texcoord')

# Main rendering loop
while not glfw.window_should_close(window):
    # Set background color (black)
    ctx.clear(0.0, 0.0, 0.0)

    # Render geometry
    vao.render(moderngl.TRIANGLE_STRIP)

    # Swap the front and back buffers
    glfw.swap_buffers(window)

    # Poll for events (keyboard, mouse, etc.)
    glfw.poll_events()

# Proper cleanup
glfw.terminate()
```
