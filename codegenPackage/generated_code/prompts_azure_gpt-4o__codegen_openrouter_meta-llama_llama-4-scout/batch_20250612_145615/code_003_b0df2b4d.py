"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Develop a web application that allows users to customize labels for seniors in nursing homes, including features for selecting label types and previewing designs, based on the offerings of Labelmystuff.com.
Generated: DETERMINISTIC_b0df2b4d75ecd597
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**label_customizer.py**
```python
from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'

# Define label types and designs offered by Labelmystuff.com
LABEL_TYPES = [
    ('address_label', 'Address Label'),
    ('name_tag', 'Name Tag'),
    ('medication_label', 'Medication Label')
]

# Define design templates for preview
DESIGN_TEMPLATES = {
    'address_label': 'address_label.html',
    'name_tag': 'name_tag.html',
    'medication_label': 'medication_label.html'
}

class LabelForm(FlaskForm):
    label_type = SelectField('Label Type', choices=LABEL_TYPES)
    name = StringField('Name', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    submit = SubmitField('Customize Label')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LabelForm()
    if form.validate_on_submit():
        label_type = form.label_type.data
        name = form.name.data
        address = form.address.data
        return render_template('preview.html', label_type=label_type, name=name, address=address)
    return render_template('index.html', form=form)

@app.route('/preview/<label_type>', methods=['GET'])
def preview(label_type):
    try:
        template = DESIGN_TEMPLATES[label_type]
        return render_template(template, label_type=label_type)
    except KeyError:
        return jsonify({'error': 'Invalid label type'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

**templates/index.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Label Customizer</title>
</head>
<body>
    <h1>Customize Your Label</h1>
    <form method="POST">
        {{ form.hidden_tag() }}
        {{ form.label_type.label }} {{ form.label_type() }}
        {{ form.name.label }} {{ form.name() }}
        {{ form.address.label }} {{ form.address() }}
        {{ form.submit() }}
    </form>
</body>
</html>
```

**templates/preview.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Label Preview</title>
</head>
<body>
    <h1>Label Preview</h1>
    <div>
        {% if label_type == 'address_label' %}
            <p>{{ name }} {{ address }}</p>
        {% elif label_type == 'name_tag' %}
            <p>{{ name }}</p>
        {% elif label_type == 'medication_label' %}
            <p>{{ name }} - {{ address }}</p>
        {% endif %}
    </div>
</body>
</html>
```

**templates/address_label.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Address Label</title>
</head>
<body>
    <div>
        <p>{{ label_type }}</p>
        <p>{{ name }} {{ address }}</p>
    </div>
</body>
</html>
```

**templates/name_tag.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Name Tag</title>
</head>
<body>
    <div>
        <p>{{ name }}</p>
    </div>
</body>
</html>
```

**templates/medication_label.html**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Medication Label</title>
</head>
<body>
    <div>
        <p>{{ name }} - {{ address }}</p>
    </div>
</body>
</html>
```

**static/style.css**
```css
body {
    font-family: Arial, sans-serif;
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

select {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #3e8e41;
}
```
