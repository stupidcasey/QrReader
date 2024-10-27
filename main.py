import qrcode
import qrcode.image.svg


def generate_svg_qr(url, filename):
    # Use the SvgPathImage factory for generating SVG QR codes
    factory = qrcode.image.svg.SvgPathImage

    # Create a QRCode instance and add the URL data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    # Generate the SVG image
    img = qr.make_image(image_factory=factory)

    # Save the SVG image to a file
    with open(filename, 'w') as f:
        f.write(img.to_string(encoding='unicode'))


# Example usage
if __name__ == "__main__":
    url = input("Enter the URL to generate QR code: ")
    filename = input("Enter the filename to save the SVG (e.g., qr_code.svg): ")
    generate_svg_qr(url, filename)
    print(f"QR code for {url} saved as {filename}.")
