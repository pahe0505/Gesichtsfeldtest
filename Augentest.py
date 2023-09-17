import matplotlib.pyplot as plt
import random
from pynput import keyboard

# Create a new figure and axis with a black background
fig, ax = plt.subplots(facecolor='black')

# Set labels for the axes
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Set the title of the graph
ax.set_title('Sequential Points on Coordinate System')

# Set fixed axis limits
ax.set_xlim(0, 10)  # X-axis limits
ax.set_ylim(0, 10)  # Y-axis limits

# Set the background color of the entire plot to black
ax.set_facecolor('black')

# Create a list to store the points
points = []
pressed = []

# Define a function to handle spacebar presses
def on_press(key):
    if key == keyboard.Key.space:
        print(i,"Spacebar tapped")
        pressed.append(i)

# Set up keyboard event listeners
listener = keyboard.Listener(on_press=on_press)
listener.start()

# Open a text file for writing
with open('coordinates1709.txt', 'w') as file:
    # Plot and show 5 points sequentially
    plt.pause(5)
    for i in range(100):
        # Generate random coordinates for the point
        x = random.uniform(0, 10)  # Random x-coordinate between 0 and 10
        y = random.uniform(0,10)  # Random y-coordinate between 0 and 10
        print(i, x, y)

        # Check if the point was pressed

        # Clear the previous points
        for point in points:
            point.remove()
        points.clear()

        # Plot the new point as a red dot
        point = ax.plot(x, y, 'yo')  # 'yo' stands for yellow circle marker

        points.append(point[0])

        # Add a fixed blue point in the middle
        middle_point = ax.plot(5, 5, 'bo')  # 'bo' stands for blue circle marker

        # Display the updated graph
        plt.draw()

        # Pause for 3 seconds to show the point
        plt.pause(2)
        if i in pressed:
            file.write(f'Point {i + 1}: ({x:.2f}, {y:.2f}) - Pressed\n')
        else:
            file.write(f'Point {i + 1}: ({x:.2f}, {y:.2f}) - Not Pressed\n')

# Keep the plot window open until the user closes it
plt.show()
