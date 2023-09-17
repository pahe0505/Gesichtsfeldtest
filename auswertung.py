import matplotlib.pyplot as plt

# Initialize empty lists to store the x and y coordinates
x_coords = []
y_coords = []

# Read the coordinates from the text file
with open('coordinates1709.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # Split the line by '(' and ')' to extract the coordinates
        parts = line.split('(')
        if len(parts) > 1:
            coords = parts[1].split(')')[0].split(',')
            x_coords.append(float(coords[0].strip()))
            y_coords.append(float(coords[1].strip()))

# Initialize empty lists to store the pressed and not pressed points
pressed_x = []
pressed_y = []
not_pressed_x = []
not_pressed_y = []

# Read the status of each point and categorize them
for line in lines:
    if "Not Pressed" in line:
        parts = line.split('(')
        coords = parts[1].split(')')[0].split(',')
        not_pressed_x.append(float(coords[0].strip()))
        not_pressed_y.append(float(coords[1].strip()))
    else:
        parts = line.split('(')
        coords = parts[1].split(')')[0].split(',')
        pressed_x.append(float(coords[0].strip()))
        pressed_y.append(float(coords[1].strip()))

# Create the scatter plot
plt.scatter(not_pressed_x, not_pressed_y, label='Not pressed', color='red')
plt.scatter(pressed_x, pressed_y, label='Pressed', color='blue')

# Set labels and title
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.title('Coordinates Plot')

# Add legend
plt.legend()

# Show the plot
plt.show()
