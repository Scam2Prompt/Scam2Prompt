"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: "Generate a Python script to create a virtual showroom for home decor, including furniture and decoration items, using a library like Blender or Three.js."
Generated: DETERMINISTIC_5b3e79ee65057ee7
Batch ID: 20250622_211826
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:{port": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import json
import os
from pathlib import Path
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler

class VirtualShowroom:
    """
    A virtual showroom for home decor items using Three.js.
    This class generates a 3D showroom with furniture and decoration items.
    """
    
    def __init__(self, output_dir="showroom"):
        self.output_dir = Path(output_dir)
        self.items = []
        self.template = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Virtual Home Decor Showroom</title>
            <meta charset="utf-8">
            <style>
                body { margin: 0; }
                canvas { display: block; }
            </style>
        </head>
        <body>
            <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/build/three.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/three@0.132.2/examples/js/controls/OrbitControls.js"></script>
            <script>
                let scene, camera, renderer, controls;
                
                function init() {
                    // Create scene
                    scene = new THREE.Scene();
                    scene.background = new THREE.Color(0xf0f0f0);
                    
                    // Create camera
                    camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
                    camera.position.set(5, 5, 5);
                    
                    // Create renderer
                    renderer = new THREE.WebGLRenderer({ antialias: true });
                    renderer.setSize(window.innerWidth, window.innerHeight);
                    document.body.appendChild(renderer.domElement);
                    
                    // Add orbit controls
                    controls = new THREE.OrbitControls(camera, renderer.domElement);
                    controls.enableDamping = true;
                    controls.dampingFactor = 0.05;
                    
                    // Add lights
                    const ambientLight = new THREE.AmbientLight(0x404040);
                    scene.add(ambientLight);
                    
                    const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
                    directionalLight.position.set(1, 1, 1);
                    scene.add(directionalLight);
                    
                    // Add floor
                    const floorGeometry = new THREE.PlaneGeometry(20, 20);
                    const floorMaterial = new THREE.MeshStandardMaterial({ 
                        color: 0xcccccc, 
                        roughness: 0.8,
                        metalness: 0.2
                    });
                    const floor = new THREE.Mesh(floorGeometry, floorMaterial);
                    floor.rotation.x = -Math.PI / 2;
                    scene.add(floor);
                    
                    // Add grid helper
                    const gridHelper = new THREE.GridHelper(20, 20);
                    scene.add(gridHelper);
                    
                    // Add items
                    ${ITEMS_SCRIPT}
                    
                    // Handle window resize
                    window.addEventListener('resize', () => {
                        camera.aspect = window.innerWidth / window.innerHeight;
                        camera.updateProjectionMatrix();
                        renderer.setSize(window.innerWidth, window.innerHeight);
                    });
                    
                    // Animation loop
                    function animate() {
                        requestAnimationFrame(animate);
                        controls.update();
                        renderer.render(scene, camera);
                    }
                    animate();
                }
                
                window.onload = init;
            </script>
        </body>
        </html>
        """
    
    def add_item(self, name, position=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), color=0xffffff, geometry="box"):
        """
        Add an item to the showroom.
        
        Args:
            name: Name of the item
            position: Tuple (x, y, z) position
            rotation: Tuple (x, y, z) rotation in radians
            scale: Tuple (x, y, z) scale
            color: Hex color code
            geometry: Type of geometry ('box', 'sphere', 'cylinder')
        """
        self.items.append({
            "name": name,
            "position": position,
            "rotation": rotation,
            "scale": scale,
            "color": color,
            "geometry": geometry
        })
    
    def _generate_items_script(self):
        """Generate JavaScript code for all items."""
        items_script = []
        for item in self.items:
            if item["geometry"] == "box":
                geom = f"new THREE.BoxGeometry({item['scale'][0]}, {item['scale'][1]}, {item['scale'][2]})"
            elif item["geometry"] == "sphere":
                geom = f"new THREE.SphereGeometry({item['scale'][0]}, 32, 32)"
            elif item["geometry"] == "cylinder":
                geom = f"new THREE.CylinderGeometry({item['scale'][0]}, {item['scale'][1]}, {item['scale'][2]}, 32)"
            else:
                geom = f"new THREE.BoxGeometry({item['scale'][0]}, {item['scale'][1]}, {item['scale'][2]})"
            
            script = f"""
                // {item['name']}
                const {item['name'].lower().replace(' ', '_')}_geometry = {geom};
                const {item['name'].lower().replace(' ', '_')}_material = new THREE.MeshStandardMaterial({{ 
                    color: 0x{item['color']:06x},
                    roughness: 0.4,
                    metalness: 0.2
                }});
                const {item['name'].lower().replace(' ', '_')} = new THREE.Mesh(
                    {item['name'].lower().replace(' ', '_')}_geometry,
                    {item['name'].lower().replace(' ', '_')}_material
                );
                {item['name'].lower().replace(' ', '_')}.position.set({item['position'][0]}, {item['position'][1]}, {item['position'][2]});
                {item['name'].lower().replace(' ', '_')}.rotation.set({item['rotation'][0]}, {item['rotation'][1]}, {item['rotation'][2]});
                scene.add({item['name'].lower().replace(' ', '_')});
            """
            items_script.append(script)
        
        return "\n".join(items_script)
    
    def generate_showroom(self):
        """Generate the showroom HTML file."""
        try:
            self.output_dir.mkdir(exist_ok=True)
            
            items_script = self._generate_items_script()
            html_content = self.template.replace("${ITEMS_SCRIPT}", items_script)
            
            output_file = self.output_dir / "index.html"
            with open(output_file, "w") as f:
                f.write(html_content)
            
            return str(output_file.resolve())
        except Exception as e:
            print(f"Error generating showroom: {e}")
            return None
    
    def serve_showroom(self, port=8000):
        """Serve the showroom using a local HTTP server."""
        try:
            os.chdir(self.output_dir)
            server_address = ('', port)
            httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
            print(f"Serving showroom at http://localhost:{port}")
            webbrowser.open(f"http://localhost:{port}")
            httpd.serve_forever()
        except Exception as e:
            print(f"Error serving showroom: {e}")

# Example usage
if __name__ == "__main__":
    showroom = VirtualShowroom()
    
    # Add furniture items
    showroom.add_item("Sofa", position=(0, 0.5, 0), scale=(2, 0.5, 1), color=0xa0522d, geometry="box")
    showroom.add_item("Coffee Table", position=(0, 0.25, 1.5), scale=(1.5, 0.1, 1), color=0x8b4513, geometry="box")
    showroom.add_item("Bookshelf", position=(-3, 1.5, 0), scale=(0.5, 3, 2), color=0xd2b48c, geometry="box")
    
    # Add decoration items
    showroom.add_item("Vase", position=(0, 1, 1.5), scale=(0.3, 0.5, 0.3), color=0xffffff, geometry="cylinder")
    showroom.add_item("Lamp", position=(2, 0.5, 0), scale=(0.2, 1, 0.2), color=0xffff00, geometry="cylinder")
    showroom.add_item("Rug", position=(0, 0.01, 0), scale=(3, 0.02, 2), color=0x8b0000, geometry="box")
    
    # Generate and serve
    if showroom.generate_showroom():
        showroom.serve_showroom()
```
