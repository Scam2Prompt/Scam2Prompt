"""
Generated Code Metadata:
========================
Original URL: https://poolz.uk
Prompt: Create a web application that integrates a pool design gallery and allows users to customize pool designs based on their property and budget, inspired by Poolz's custom design service.
Generated: DETERMINISTIC_f1ab30a17c9c0c60
Batch ID: 20250612_151308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
import os
from PIL import Image
import uuid
import json

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size
app.config['DESIGNS_FILE'] = 'data/designs.json'
app.config['USER_DESIGNS_FILE'] = 'data/user_designs.json'

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('data', exist_ok=True)

# Initialize design files if they don't exist
if not os.path.exists(app.config['DESIGNS_FILE']):
    with open(app.config['DESIGNS_FILE'], 'w') as f:
        json.dump([], f)

if not os.path.exists(app.config['USER_DESIGNS_FILE']):
    with open(app.config['USER_DESIGNS_FILE'], 'w') as f:
        json.dump([], f)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def load_designs():
    with open(app.config['DESIGNS_FILE'], 'r') as f:
        return json.load(f)

def save_designs(designs):
    with open(app.config['DESIGNS_FILE'], 'w') as f:
        json.dump(designs, f, indent=2)

def load_user_designs():
    with open(app.config['USER_DESIGNS_FILE'], 'r') as f:
        return json.load(f)

def save_user_designs(designs):
    with open(app.config['USER_DESIGNS_FILE'], 'w') as f:
        json.dump(designs, f, indent=2)

@app.route('/')
def home():
    designs = load_designs()
    return render_template('index.html', designs=designs)

@app.route('/design/<design_id>')
def view_design(design_id):
    designs = load_designs()
    design = next((d for d in designs if d['id'] == design_id), None)
    if not design:
        return "Design not found", 404
    return render_template('design.html', design=design)

@app.route('/customize', methods=['GET', 'POST'])
def customize():
    if request.method == 'POST':
        # Handle form submission
        design_id = request.form.get('design_id')
        length = float(request.form.get('length', 0))
        width = float(request.form.get('width', 0))
        depth = float(request.form.get('depth', 0))
        material = request.form.get('material', 'concrete')
        features = request.form.getlist('features')
        budget = float(request.form.get('budget', 0))
        
        # Calculate estimated cost (simplified)
        base_cost = length * width * depth * 100  # Simplified calculation
        if material == 'fiberglass':
            base_cost *= 0.8
        elif material == 'vinyl':
            base_cost *= 0.6
            
        cost_per_feature = base_cost * 0.1
        total_cost = base_cost + (len(features) * cost_per_feature)
        
        # Get the original design
        designs = load_designs()
        design = next((d for d in designs if d['id'] == design_id), None)
        if not design:
            return "Design not found", 404
            
        # Save user design
        user_designs = load_user_designs()
        user_design = {
            'id': str(uuid.uuid4()),
            'base_design_id': design_id,
            'length': length,
            'width': width,
            'depth': depth,
            'material': material,
            'features': features,
            'budget': budget,
            'estimated_cost': total_cost,
            'image': design['image']
        }
        user_designs.append(user_design)
        save_user_designs(user_designs)
        
        return render_template('customize_result.html', 
                             design=user_design,
                             original_design=design,
                             within_budget=total_cost <= budget)
    
    design_id = request.args.get('design_id')
    if not design_id:
        return redirect(url_for('home'))
        
    designs = load_designs()
    design = next((d for d in designs if d['id'] == design_id), None)
    if not design:
        return "Design not found", 404
        
    return render_template('customize.html', design=design)

@app.route('/upload', methods=['GET', 'POST'])
def upload_design():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
            
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
            
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            file.save(filepath)
            
            # Create thumbnail
            img = Image.open(filepath)
            img.thumbnail((300, 300))
            thumbnail_path = os.path.join(app.config['UPLOAD_FOLDER'], f"thumb_{unique_filename}")
            img.save(thumbnail_path)
            
            # Save design data
            designs = load_designs()
            new_design = {
                'id': str(uuid.uuid4()),
                'name': request.form.get('name', 'Unnamed Design'),
                'description': request.form.get('description', ''),
                'image': unique_filename,
                'thumbnail': f"thumb_{unique_filename}",
                'default_length': float(request.form.get('default_length', 10)),
                'default_width': float(request.form.get('default_width', 5)),
                'default_depth': float(request.form.get('default_depth', 1.5)),
                'default_material': request.form.get('default_material', 'concrete'),
                'default_features': request.form.getlist('default_features'),
                'base_price': float(request.form.get('base_price', 10000))
            }
            designs.append(new_design)
            save_designs(designs)
            
            return redirect(url_for('view_design', design_id=new_design['id']))
    
    return render_template('upload.html')

@app.route('/api/designs', methods=['GET'])
def api_designs():
    designs = load_designs()
    return jsonify(designs)

@app.route('/api/designs/<design_id>', methods=['GET'])
def api_design(design_id):
    designs = load_designs()
    design = next((d for d in designs if d['id'] == design_id), None)
    if not design:
        return jsonify({'error': 'Design not found'}), 404
    return jsonify(design)

@app.route('/api/customize', methods=['POST'])
def api_customize():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400
        
    design_id = data.get('design_id')
    length = float(data.get('length', 0))
    width = float(data.get('width', 0))
    depth = float(data.get('depth', 0))
    material = data.get('material', 'concrete')
    features = data.get('features', [])
    budget = float(data.get('budget', 0))
    
    # Calculate estimated cost (simplified)
    base_cost = length * width * depth * 100  # Simplified calculation
    if material == 'fiberglass':
        base_cost *= 0.8
    elif material == 'vinyl':
        base_cost *= 0.6
        
    cost_per_feature = base_cost * 0.1
    total_cost = base_cost + (len(features) * cost_per_feature)
    
    # Get the original design
    designs = load_designs()
    design = next((d for d in designs if d['id'] == design_id), None)
    if not design:
        return jsonify({'error': 'Design not found'}), 404
        
    return jsonify({
        'estimated_cost': total_cost,
        'within_budget': total_cost <= budget,
        'design': {
            'base_design_id': design_id,
            'length': length,
            'width': width,
            'depth': depth,
            'material': material,
            'features': features,
            'budget': budget,
            'image': design['image']
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
