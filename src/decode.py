from PIL import Image

# Open the image file
image = Image.open("../my-image.png")

# Get the width and height of the image
width, height = image.size

# Convert the image to a list of pixels
pixels = list(image.getdata())

# Convert each pixel to a hex code and group the hex codes by row
hex_codes = []
for y in range(height):
    # Create a new array for the row of hex codes
    row = []
    for x in range(width):
        # Get the pixel at the current position
        pixel = pixels[x + y * width]
        r, g, b, a = pixel
        # Check if the image has an alpha channel
        if a is not None:
            # Image has an alpha channel, include the alpha value in the hex code
            hex_code = "#{:02x}{:02x}{:02x}{:02x}".format(r, g, b, a)
        else:
            # Image does not have an alpha channel, only include RGB values in the hex code
            hex_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
        # Add the hex code to the row
        row.append(hex_code)
    # Add the row of hex codes to the array
    hex_codes.append(row)

# Open the file for writing
with open("pixels.dat", "w") as f:
    # Create the string to be written to the file by concatenating "hex_codes = " with the hex_codes array
    hex_codes_str = "hex_codes = " + str(hex_codes)
    # Write the string to the file
    f.write(hex_codes_str)
