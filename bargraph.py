import matplotlib.pyplot as plt

# Define the data for the bar graph
labels = ['Red', 'Blue', 'Green']
values = [45, 42, 28]
colors = ['red', 'blue', 'green']  # Add colors for each bar

# Create a bar graph using Matplotlib
fig, ax = plt.subplots()
ax.bar(labels, values, color=colors)  # Use the colors for each bar

# Save the bar graph as a static file
import os
if not os.path.exists('static'):
    os.makedirs('static')
plt.savefig('static/bar_graph.png', dpi=300, bbox_inches='tight')

# Render the HTML template with the bar graph
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
