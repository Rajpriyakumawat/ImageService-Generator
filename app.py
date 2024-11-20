from flask import Flask, request, send_file, render_template_string
from PIL import Image, ImageDraw
import io
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <h1>Welcome to the Image Service API</h1>
        <p>Use the following endpoints to generate images:</p>
        <ul>
            <li><a href="{{ url_for('generate_random_image', format='PNG', resolution=200, position_x=10, position_y=20) }}">Generate Random Image</a></li>
            <li><a href="{{ url_for('generate_specific_image', album='Sample Album', format='PNG', resolution=200, position_x=10, position_y=20) }}">Generate Specific Image</a></li>
            <li><a href="{{ url_for('adjust_image_center', format='PNG', resolution=200, position_x=50, position_y=50) }}">Adjust Image Center</a></li>
        </ul>
        <p>Click the links above to generate images directly.</p>
    ''')

# Helper function to create an image in memory
def create_image(text="Image", resolution=(100, 100), position=(0, 0)):
    image = Image.new("RGB", resolution, "white")
    draw = ImageDraw.Draw(image)
    draw.text(position, text, fill="black")
    return image

@app.route('/generate_random_image', methods=['GET'])
def generate_random_image():
    # Retrieve parameters
    image_format = request.args.get('format', 'PNG')
    resolution = (int(request.args.get('resolution', '100')), int(request.args.get('resolution', '100')))
    position_x = int(request.args.get('position_x', '0'))
    position_y = int(request.args.get('position_y', '0'))
    
    # Generate random image
    text = f"Random {random.randint(1, 100)}"
    image = create_image(text=text, resolution=resolution, position=(position_x, position_y))
    
    # Prepare image to send as response
    img_io = io.BytesIO()
    image.save(img_io, format=image_format)
    img_io.seek(0)
    
    return send_file(img_io, mimetype=f'image/{image_format.lower()}')

@app.route('/generate_specific_image', methods=['GET'])
def generate_specific_image():
    # Retrieve parameters
    album = request.args.get('album', 'Default Album')
    image_format = request.args.get('format', 'PNG')
    resolution = (int(request.args.get('resolution', '100')), int(request.args.get('resolution', '100')))
    position_x = int(request.args.get('position_x', '0'))
    position_y = int(request.args.get('position_y', '0'))

    # Generate specific image based on album name
    text = f"Album: {album}"
    image = create_image(text=text, resolution=resolution, position=(position_x, position_y))
    
    # Prepare image to send as response
    img_io = io.BytesIO()
    image.save(img_io, format=image_format)
    img_io.seek(0)
    
    return send_file(img_io, mimetype=f'image/{image_format.lower()}')

@app.route('/adjust_image_center', methods=['GET'])
def adjust_image_center():
    # Retrieve parameters
    image_format = request.args.get('format', 'PNG')
    resolution = (int(request.args.get('resolution', '100')), int(request.args.get('resolution', '100')))
    position_x = int(request.args.get('position_x', '50'))
    position_y = int(request.args.get('position_y', '50'))

    # Generate centered image
    text = "Centered Image"
    image = create_image(text=text, resolution=resolution, position=(position_x, position_y))
    
    # Prepare image to send as response
    img_io = io.BytesIO()
    image.save(img_io, format=image_format)
    img_io.seek(0)
    
    return send_file(img_io, mimetype=f'image/{image_format.lower()}')

if __name__ == '__main__':
    app.run(debug=True)
