import matplotlib.pyplot as plt

# Data for sections
section_labels = ['Section 1', 'Section 2', 'Section 3']
section_colors = ['#FFB3BA', '#FFEBA1', '#AED6F1']  # Pastel colors: Red-Orange, Yellow, Semi-Dark Blue

# Data for subsections within each section
subsection_labels = [
    ['Subsection 1-1', 'Subsection 1-2', 'Subsection 1-3'],
    ['Subsection 2-1', 'Subsection 2-2'],
    ['Subsection 3-1', 'Subsection 3-2', 'Subsection 3-3', 'Subsection 3-4']
]
subsection_percentages = [
    [30, 40, 30],  # Percentages for Subsection 1-1, Subsection 1-2, Subsection 1-3 (should add up to 100)
    [60, 40],     # Percentages for Subsection 2-1, Subsection 2-2
    [10, 20, 30, 40]  # Percentages for Subsection 3-1, Subsection 3-2, Subsection 3-3, Subsection 3-4
]

# Create the figure and axis
fig, ax = plt.subplots()

# Draw the sections
ax.pie([1, 1, 1], colors=section_colors, radius=1, startangle=90, counterclock=False, wedgeprops={'linewidth': 0})

# Draw the subsections within each section
start_angle = 90
for section_index, (subsection_labels_section, subsection_percentages_section) in enumerate(zip(subsection_labels, subsection_percentages)):
    section_color = section_colors[section_index]
    total_percentage = sum(subsection_percentages_section)
    for subsection_index, (label, percentage) in enumerate(zip(subsection_labels_section, subsection_percentages_section)):
        angle = 360 * percentage / total_percentage
        ax.annotate(
            label,
            xy=(0, 0),
            xytext=(0.7, 0),
            textcoords='data',
            ha='center',
            va='center',
            color=section_color,
            fontsize=8,
            rotation_mode='anchor',
            rotation=start_angle - angle / 2
        )
        start_angle -= angle

# Set the aspect ratio to be equal
ax.set_aspect('equal')

# Remove the axis labels and ticks
ax.axis('off')

# Set the title
ax.set_title('Interests Orbit Graph')

# Save the plot as a PNG file
plt.savefig('orbit_graph.png', dpi=300)

# Show the plot (optional)
plt.show()
