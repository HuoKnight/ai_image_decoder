from PIL import Image

# Open the file containing the hex codes
with open("pixels.dat", "r") as f:
    # Read the text from the file and execute it to create the array of arrays
    exec(f.read())
    

# Create a new image with the same dimensions as the original
width = len(hex_codes[0])
height = len(hex_codes)
image = Image.new("RGBA", (width, height))

# Convert each hex code to a pixel and set the pixel in the image
pixels = []
for row in hex_codes:
    for hex_code in row:
        # Parse the hex code to get the RGB and alpha values
        r, g, b, a = int(hex_code[1:3], 16), int(hex_code[3:5], 16), int(hex_code[5:7], 16), int(hex_code[7:9], 16)
        # Create a new pixel using the RGB and alpha values
        pixel = (r, g, b, a)
        # Add the pixel to the array of pixels
        pixels.append(pixel)

# Set the pixels in the image
image.putdata(pixels)

# Save the image to a file
image.save("../reconstructed-image.png")