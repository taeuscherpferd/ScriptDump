import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.colors import to_rgba

# TODO: Modify this to properly set the columns and rows

# Load the user's CSV file to inspect its structure
file_path = './1000_korean_words.csv'
vocab_data = pd.read_csv(file_path)

# Display the first few rows to understand its format
print(vocab_data.head())

# Define parameters for the image
background_color = to_rgba("black")
text_color = "black"
font_size = 14
font = fm.FontProperties(fname='./fonts/NotoSerifKR-Regular.ttf')
dpi = 100  # Higher DPI for clarity

# Extract and format the data for visualization
data_flat = vocab_data.fillna("").values.flatten()
data_text = "\n".join(data_flat)  # Combine all rows into a single text block

# Calculate figure size for a 2560x1440 image
fig_width, fig_height = 2560 / dpi, 1440 / dpi

# Create the image
plt.figure(figsize=(fig_width, fig_height), dpi=dpi)
plt.text(0.5, 0.5, data_text, fontsize=font_size, color=text_color, ha="center", va="center", wrap=True, fontproperties=font)

# Style adjustments
plt.gca().set_facecolor(background_color)
plt.axis("off")

# Save the image
output_path = "./out/korean_vocab_background.png"
plt.savefig(output_path, bbox_inches="tight", dpi=dpi)
plt.close()


