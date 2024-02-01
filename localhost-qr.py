import qrcode
import os
import argparse
from PIL import ImageDraw, ImageFont

# Function to get the IP address
def get_ip_address():
    return os.popen('ipconfig getifaddr en0').read().strip()

# Function to create and display the QR code
def create_and_display_qr_code(port):
    ip_address = get_ip_address()
    data = f'http://{ip_address}:{port}'

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    print(data)
    
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    # Use Pillow to add text to the image
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()  # You can choose a different font if needed
    label_position = (10, img.size[1] - 20)  # Adjust the position as needed
    draw.text(label_position, data, font=font, fill="black")

    img.show()

if __name__ == "__main__":
    # Create ArgumentParser object
    parser = argparse.ArgumentParser(description="Generate and display a QR code with a specified port (default is 3000).")

    # Add argument for the port
    parser.add_argument('--port', type=int, default=3000, help='Port number for the URL (default is 3000).')

    # Parse the command line arguments
    args = parser.parse_args()

    # Call the function with the provided port or the default value
    create_and_display_qr_code(args.port)
