from PIL import Image

import gamerruner

user_img_name = "pic.jpg"
desired_size = (40,40) # a recommeded size


trails = 12500 # this determines how many pieces the program tries to place onto the board. Another parameter to change 

# takes in a set of coordinates from the 2D board
# and outputs averages all RGB values
def average_rgb(image, coordinates):
    total_r, total_g, total_b = 0, 0, 0
    count = len(coordinates)
    
    for x, y in coordinates:
        # Get the pixel value at (x, y)
        r, g, b = image.getpixel((x, y))
        total_r += r
        total_g += g
        total_b += b
    
    # Calculate average
    if count > 0:
        average_r = total_r // count
        average_g = total_g // count
        average_b = total_b // count
    else:
        average_r = average_g = average_b = 0  # Default to 0 if no pixels

    return (average_r, average_g, average_b)

# takes in a set of coordinates from the 2D board
# and outputs a copy of the image with those coordinates chaged to a color
def change_pixel_color(image, coordinates, new_color):
    # Create a copy of the image to modify
    modified_image = image.copy()
    for x, y in coordinates:
        modified_image.putpixel((x, y), new_color)
    
    return modified_image


# Open the image
image = Image.open(user_img_name).convert('RGB') # converted to RGB to limit compression
new_image = image.resize(desired_size)

gamerruner.gen_empty_board(desired_size)
board = gamerruner.main_run(trails)

pixelLocs = {} 

# loop over the board. save all the numbers in locations. then loop and find average colors
for row in range(len(board)):
    for col in range(len(board[row])):
        val = board[row][col].item()
        if val not in pixelLocs:
            pixelLocs[val] = []
        pixelLocs[val].append((row,col))

for piece in pixelLocs:
    new_color = (average_rgb(new_image,pixelLocs[piece]))
    new_image = change_pixel_color(new_image, pixelLocs[piece], new_color)
    
new_image.resize(desired_size)
new_image.save("output_"+ user_img_name.split(".")[0] + ".bmp") # saves at bmp to minimize compression
