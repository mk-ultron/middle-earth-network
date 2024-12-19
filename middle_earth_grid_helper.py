import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def show_coordinate_grid():
    # Create figure with map background
    plt.figure(figsize=(20, 15))
    
    # Load and display the map
    map_img = mpimg.imread('middle_earth_map_optimized.png')
    plt.imshow(map_img, extent=[0, 100, 0, 75], aspect='auto', alpha=0.7)
    
    # Add grid
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Add major grid lines every 10 units with labels
    for i in range(0, 101, 10):
        plt.axvline(x=i, color='r', linestyle='--', alpha=0.3)
        plt.text(i, -2, str(i), ha='center', va='top')
    
    for i in range(0, 76, 10):
        plt.axhline(y=i, color='r', linestyle='--', alpha=0.3)
        plt.text(-2, i, str(i), ha='right', va='center')
    
    # Enable mouse hover coordinate display
    def format_coord(x, y):
        return f'x={x:.1f}, y={y:.1f}'
    
    plt.gca().format_coord = format_coord
    
    # Add title and adjust layout
    plt.title("Middle Earth Coordinate Grid")
    plt.margins(0.1)
    
    # Show plot with grid numbers visible
    plt.show()

# Run this first to get coordinates
show_coordinate_grid()