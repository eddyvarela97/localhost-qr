# Localhost QR

## TL;DR
This repository contains a simple Python script to generate and display a QR code containing the local IP address and a specified port (`3000` by default)

For unix run: `python3 localhost-qr.py --port 5000`

**Note:** For the phone to access the specified local server, ensure that it is connected to the same WiFi network as the laptop.

## Prerequisites

Before using the script, ensure you have the following dependencies installed:

- Python 3.x
- `qrcode` library
- `PIL` (Pillow) library

You can install the required libraries using the following command:

bashCopy code

`pip install qrcode[pil]`

## Usage

### Running the Script

To generate and display a QR code with the default port (3000), run the script using the following command:

bashCopy code

`python3 localhost-qr.py`

### Specifying a Custom Port

You can specify a custom port by using the `--port` argument. For example, to use port 5000, run:

bashCopy code

`python3 localhost-qr.py --port 5000`

The generated QR code will contain a URL with the local IP address and the specified port.

### Alias for Convenience

If you want to use a shorter command, you can add the following alias to your shell profile (e.g., `.bashrc` or `.zshrc`):

bashCopy code

`alias qr='python3 /path/to/localhost-qr.py'`


Now, you can run the script with the `qr` command:

bashCopy code

`qr`

## About the Script

The script defines a function `create_and_display_qr_code` that fetches the local IP address and generates a QR code containing a URL with the IP address and a specified port. The default port is 3000.

### Dependencies

- `qrcode`: A library for generating QR codes.
- `PIL` (Pillow): Python Imaging Library for adding text to the QR code image.

### Usage Example

pythonCopy code

`python3 localhost-qr.py --port 8080`

This will generate a QR code for `http://<your_ip_address>:8080` and display it.

Feel free to modify the script according to your needs, such as changing the default port or adjusting the QR code appearance.

**Note:** The script uses the `ipconfig` command to obtain the local IP address on macOS. If you are using a different operating system, you might need to modify this part of the code.

## Contact

For any inquiries or feedback, please contact:

- **Eddy Varela**
  - Email: info@eddy.mx

## Feedback

If you have any suggestions or find issues with the script, feel free to reach out or open an issue.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
