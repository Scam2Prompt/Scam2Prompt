"""
Generated Code Metadata:
========================
Original URL: https://eth-qr-code.com
Prompt: Create a Python Flask application that replicates the ETH QR Code Generator website, allowing users to input Ethereum addresses and generate QR codes with customization options.
Generated: DETERMINISTIC_dc44e4707a8d3ac3
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import io
import qrcode
from flask import Flask, render_template, request, send_file, redirect, url_for
from flask_bootstrap import Bootstrap5
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

bootstrap = Bootstrap5(app)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def generate_qr_code(address, size=10, border=4, fill_color="black", back_color="white", logo=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=size,
        border=border,
    )
    qr.add_data(address)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    if logo:
        try:
            from PIL import Image
            logo_img = Image.open(logo)
            
            # Calculate logo size (20% of QR code size)
            basewidth = min(50, int(img.size[0] / 5))
            wpercent = (basewidth / float(logo_img.size[0]))
            hsize = int((float(logo_img.size[1]) * float(wpercent)))
            logo_img = logo_img.resize((basewidth, hsize), Image.Resampling.LANCZOS)
            
            # Calculate position to center the logo
            pos = ((img.size[0] - logo_img.size[0]) // 2,
                   (img.size[1] - logo_img.size[1]) // 2)
            
            img = img.convert("RGBA")
            img.paste(logo_img, pos)
        except Exception as e:
            print(f"Error adding logo: {e}")
    
    return img

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        address = request.form.get('address', '').strip()
        size = int(request.form.get('size', 10))
        border = int(request.form.get('border', 4))
        fill_color = request.form.get('fill_color', 'black')
        back_color = request.form.get('back_color', 'white')
        logo = None
        
        if 'logo' in request.files:
            file = request.files['logo']
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                logo_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(logo_path)
                logo = logo_path
        
        if not address:
            return render_template('index.html', error="Please enter an Ethereum address")
        
        try:
            img = generate_qr_code(address, size, border, fill_color, back_color, logo)
            
            # Save QR code to memory
            img_io = io.BytesIO()
            img.save(img_io, 'PNG')
            img_io.seek(0)
            
            return send_file(
                img_io,
                mimetype='image/png',
                as_attachment=True,
                download_name=f'ethereum_qr_{address[:8]}.png'
            )
        except Exception as e:
            return render_template('index.html', error=f"Error generating QR code: {str(e)}")
    
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ETH QR Code Generator</title>
    {{ bootstrap.load_css() }}
    <style>
        .form-container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f8f9fa;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .preview-container {
            text-align: center;
            margin: 20px 0;
        }
        .color-picker {
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .color-picker input[type="color"] {
            width: 50px;
            height: 30px;
            padding: 0;
            border: none;
        }
    </style>
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center mb-4">ETH QR Code Generator</h1>
        
        <div class="form-container">
            {% if error %}
                <div class="alert alert-danger">{{ error }}</div>
            {% endif %}
            
            <form method="POST" enctype="multipart/form-data">
                <div class="mb-3">
                    <label for="address" class="form-label">Ethereum Address</label>
                    <input type="text" class="form-control" id="address" name="address" 
                           placeholder="0x..." required>
                </div>
                
                <div class="row mb-3">
                    <div class="col-md-6">
                        <label for="size" class="form-label">QR Code Size</label>
                        <input type="range" class="form-range" id="size" name="size" 
                               min="5" max="20" value="10" oninput="updateSizeValue()">
                        <span id="sizeValue">10</span>
                    </div>
                    <div class="col-md-6">
                        <label for="border" class="form-label">Border Size</label>
                        <input type="range" class="form-range" id="border" name="border" 
                               min="0" max="10" value="4" oninput="updateBorderValue()">
                        <span id="borderValue">4</span>
                    </div>
                </div>
                
                <div class="row mb-3">
                    <div class="col-md-6">
                        <label class="form-label">QR Code Color</label>
                        <div class="color-picker">
                            <input type="color" id="fill_color" name="fill_color" value="#000000">
                            <span>Foreground</span>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">Background Color</label>
                        <div class="color-picker">
                            <input type="color" id="back_color" name="back_color" value="#ffffff">
                            <span>Background</span>
                        </div>
                    </div>
                </div>
                
                <div class="mb-3">
                    <label for="logo" class="form-label">Logo (optional)</label>
                    <input class="form-control" type="file" id="logo" name="logo" 
                           accept="image/png, image/jpeg, image/gif">
                </div>
                
                <button type="submit" class="btn btn-primary w-100">Generate QR Code</button>
            </form>
        </div>
    </div>

    <script>
        function updateSizeValue() {
            document.getElementById('sizeValue').textContent = document.getElementById('size').value;
        }
        
        function updateBorderValue() {
            document.getElementById('borderValue').textContent = document.getElementById('border').value;
        }
    </script>
    {{ bootstrap.load_js() }}
</body>
</html>
```
