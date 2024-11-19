import tkinter as tk
from tkinter import ttk, Toplevel, Label, Button
import webbrowser
import pyperclip

from wonderwords import RandomWord

import random
from typing import List, Dict


randomword = RandomWord()


def get_words(category, quantity):
    global randomword
    new_word = ''
    if quantity == 0 or quantity == 1:
      new_word = randomword.word(include_parts_of_speech=[category])
      return new_word

    words_list= []
    for i in range(quantity):
        new_word = randomword.word(include_parts_of_speech=[category])

        words_list.append(new_word)

    #print(words_list)

    return words_list

class PromptGenerator:
    def __init__(self):
        # Camera settings from the previous table
        self.camera_features = {
            'focal_length': ['14mm', '35mm', '50mm', '85mm', '200mm'],
            'aperture': ['f/1.4', 'f/2.8', 'f/8', 'f/16'],
            'angle': ['low angle', 'eye level', 'high angle', "bird's eye view"],
            'shot_type': ['close-up', 'medium shot', 'wide shot', 'extreme wide shot','extreme close-up'],
            'lighting': ['natural lighting', 'studio lighting', 'dramatic lighting', 'soft lighting'],
            'style': ['cinematic', 'documentary', 'artistic', 'minimalist','cartoon','manga','ultra realistic'],
            'mood': [
                    'moody', 'cheerful', 'mysterious', 'serene',
                    'melancholic', 'nostalgic', 'whimsical', 'surreal',
                    'gothic', 'futuristic', 'ethereal', 'ominous',
                    'playful', 'romantic', 'dark', 'idyllic',
                    'bleak', 'vibrant', 'tranquil', 'turbulent',
                    'sophisticated', 'apocalyptic', 'dreamy', 'anxious',
                    'peaceful', 'chaotic', 'elegant', 'rustic',
                    'intense', 'meditative'
                    ]
        }



        # Main subjects and themes
        self.subjects = [
            'landscape', 'portrait', 'still life', 'architecture',
            'wildlife', 'street scene', 'abstract', 'macro'
        ]

        # Common adjectives for visual description
        self.adjectives = [
            'vibrant', 'ethereal', 'rustic', 'futuristic', 'vintage',
            'minimalist', 'elaborate', 'surreal', 'geometric', 'organic',
            'weathered', 'pristine', 'chaotic', 'harmonious', 'textured'
        ]

        # Time and weather conditions
        self.conditions = [
            'at sunset', 'during golden hour', 'at midnight',
            'in fog', 'during a storm', 'on a clear day',
            'under starlight', 'at dawn', 'in rainfall',
            'during a blizzard', 'underwater', 'in a desert',
            'in a forest', 'in a bustling city', 'on a snowy mountain',
            'in a lush meadow', 'during twilight', 'in autumn leaves',
            'in a futuristic setting', 'in ancient ruins', 'under a rainbow',
            'during a heatwave', 'at high noon', 'in a haunted house',
            'in a time warp', 'in a cyberpunk city', 'during an eclipse',
            'in deep space', 'in a post-apocalyptic world', 'in a serene garden',
            'in a dark alley', 'on a volcanic landscape', 'in a misty swamp',
            'on a frozen lake', 'in a cave lit by crystals', 'on a distant planet',
            'during a sandstorm', 'in a busy marketplace', 'on a pirate ship',
            'in a magical forest', 'in a medieval castle', 'at a carnival',
            'in a labyrinth', 'on a tropical island', 'in an underwater cave',
            'in a parallel universe', 'at an ancient battlefield', 'on a snowy beach',
            'in a neon-lit alley', 'in a spacecraft', 'in a robot factory',
            'in a wasteland', 'on a mountain peak', 'in an alien jungle',
            'in a sunken city', 'in a grand ballroom', 'in a crowded stadium',
            'during a meteor shower', 'in a dark, moonlit forest', 'on a floating island',
            'during a full moon', 'in zero gravity', 'under northern lights',
            'in an ice palace', 'on a wind-swept plain', 'in a virtual reality',
            'during a solar flare', 'in a steampunk city', 'in dense fog with fireflies',
            'on a haunted ship', 'in a glass dome', 'in a field of poppies',
            'during an earthquake', 'in a ghost town', 'in a high-tech lab',
            'in the eye of a hurricane', 'at the edge of a cliff', 'in a silent library',
            'in a bustling port', 'underwater at night', 'inside a giant tree',
            'in a surrealist dreamscape', 'during a festival', 'in a hidden valley',
            'in a bioluminescent sea', 'on a bridge at night', 'in an old mill',
            'during a time loop', 'in a skydiving session', 'in a world of mirrors',
            'in a bustling subway', 'in an art gallery', 'in a vineyard at harvest',
            'on a derelict spaceship', 'during a musical parade', 'in an ice cave',
            'in an abandoned amusement park', 'during a celestial alignment', 'in a sky city',
            'in a dimension of shadows', 'in a room of holograms', 'on a road trip through the desert',
            'in a castle garden at night', 'during a blackout', 'in a cloud forest',
            'on a gondola in Venice', 'in a battlefield of flowers', 'in a futuristic farm',
            'in a maze of mirrors', 'during a drone show', 'in an ethereal grove',
            'in an ancient library', 'at a masquerade ball', 'in a neon-lit cityscape',
            'under a meteor shower', 'in the ruins of civilization', 'during a lunar eclipse',
            'on a tranquil farm', 'in a bustling bazaar', 'in an enchanted forest',
            'during a festive parade', 'in a transparent underwater hotel', 'on a windswept cliff',
            'in a bustling fish market', 'during a solar eclipse', 'in a mystical temple',
            'in a peaceful monastery', 'on an active volcano', 'in a vintage diner',
            'during a vintage car show', 'in a quiet village', 'on an ancient battlefield',
            'in a futuristic subway', 'under the Aurora Australis', 'in a vibrant coral reef',
            'during a cultural festival', 'in a bustling food market', 'on top of a skyscraper',
            'in a secret garden', 'under a canopy of stars', 'on a deserted island',
            'in a bustling train station', 'during a thunderstorm', 'in a historic theater',
            'in a futuristic museum', 'under a double rainbow', 'in a zero-gravity environment',
            'in an art deco city', 'during cherry blossom season', 'in a bustling airport',
            'on a steam train', 'in an old-world tavern', 'during a fireworks display',
            'in an underwater city', 'during a pagan festival', 'on a historic battlefield',
            'in a holographic performance hall', 'under a blood moon', 'in a haunted forest',
            'in an alien bazaar', 'during a cosmic storm', 'on a space station',
            'in an interdimensional portal', 'in a vintage carnival', 'during a comet sighting',
            'in a high-tech greenhouse', 'on a floating market', 'in a mystical cave',
            'during a quantum leap', 'in a Victorian-era mansion', 'under a meteor shower',
            'in an echo chamber', 'during an interstellar ballet', 'in a dream within a dream',
            'in a time-frozen moment', 'on an eternal staircase', 'in an infinite library',
            'during a telepathic symposium', 'in a gravity well', 'on an artificial island',
            'in a virtual art gallery', 'under a canopy of bioluminescent mushrooms', 'in a cybernetic jungle',
        ]



        # Action verbs for dynamic scenes
        self.actions = [
            'floating', 'dancing', 'emerging', 'dissolving',
            'transforming', 'reflecting', 'growing', 'flowing',
            'spinning', 'glowing', 'hovering', 'melting'
        ]


    def generate_prompt(self,
                       category: str = "picture",
                       subject: str = "",
                       plural: bool = False,
                       color: bool = False,           # Use of camera color functions (black and white, sepia, etc.).
                       complexity: int = 3,           # 1-10: controls the prompt complexity (with different features)
                       randomness: float = 0.5,       # 0-1: controls how experimental combinations can be
                       theme: str = None     # Optional theme filter
                       ) -> str:
        """
        Generate a random image prompt with specified parameters.
        """
        global randomword

        color_list = [
            'monochrome', 'black and white', 'sepia', 'vibrant', 'pastel', 'high contrast', 'muted', 'cool tones', 'warm tones', 'desaturated',
            'neon', 'fluorescent', 'retro', 'vintage', 'grunge', 'cyberpunk', 'futuristic', 'metallic', 'gold', 'silver',
            'bronze', 'pastel goth', 'candy', 'rainbow', 'earth tones', 'natural', 'forest', 'oceanic', 'sky', 'sunset',
            'sunrise', 'autumn', 'winter', 'spring', 'summer', 'golden hour', 'twilight', 'midnight', 'rustic', 'industrial',
            'minimalist', 'abstract', 'pop art', 'watercolor', 'oil painting', 'impressionist', 'expressionist', 'cubist', 'surreal', 'steampunk',
            'gothic', 'noir', 'acid', 'technicolor', 'pastel metallic', 'vivid', 'dramatic'
        ]

        elements = []

        # Start with base prompt
        prompt = "Generate a " + category

        # Add main subject
        if subject=="":
          if plural:
            subject = subject + "s"
          subject = " of " + randomword.word(include_parts_of_speech=["nouns"]) #random.choice(self.subjects)
        else:
          subject = " of " + subject

        action = random.choice(self.actions) #get_words('verb',1)

        subject = subject + " " + action


        if theme:
            subject = subject + ", around " + theme + " theme"

        # Add adjectives based on complexity
        adj_count = max(3, int(complexity * random.random() + 1))

        adjectives = get_words('adjective',adj_count) #random.sample(self.adjectives, adj_count)

        # Build the basic scene
        elements.append(f"{subject}, " + ", ".join(adjectives))


            #elements.append(random.choice(self.actions))

        # Add conditions based on complexity
        if complexity >= 3 and random.random() < randomness:
            elements.append(random.choice(self.conditions))

        # Add camera features based on complexity and randomness
        if complexity >= 4 and category!="story":
            camera_elements = []
            feature_count = min(3, int(complexity * random.random()))
            selected_features = random.sample(list(self.camera_features.keys()), feature_count)

            for feature in selected_features:
                value = random.choice(self.camera_features[feature])
                camera_elements.append(f"{value}")

            elements.extend(camera_elements)

        # Combine all elements
        prompt += ", ".join(elements)

        # Add style modifier based on complexity and randomness
        if complexity >= 5 and random.random() < randomness:
            style = random.choice(self.camera_features['style'])
            mood = random.choice(self.camera_features['mood'])
            prompt += f", in a {mood} {style} style"

        if color:
          color_select = random.choice(color_list)
          prompt += f", " + color_select + " colors"

        return prompt + "."



def on_generate():
    category = category_var.get()
    subject = subject_entry.get()
    plural = plural_var.get()

    color = color_var.get()

    complexity = int(complexity_entry.get())
    randomness = float(randomness_entry.get())
    theme = theme_entry.get() if theme_entry.get() else None

    generator = PromptGenerator()

    output = generator.generate_prompt(category, subject, plural, color, complexity, randomness, theme)
    output_text.delete(1.0, tk.END)  # Clear previous text
    output_text.insert(tk.END, output)


def on_copy():
    try:
        text = output_text.get("1.0", tk.END)
        pyperclip.copy(text)
        #messagebox.showinfo("Copy", "Text copied to clipboard!")
    except Exception as e:
        messagebox.showerror("Error", f"Could not copy text: {e}")


def show_about():
    about_window = Toplevel(root)
    about_window.title("About")
    about_window.minsize(350, 250) # Set a size for the window

    about_window.iconbitmap('logo.ico')  # Set the icon for the about window

    # Text content
    about_text = (
        "This is a tool to generate random prompts and explore creative ways to generate stories, "
        "pictures, or videos. It is in beta version.\n\n"
        "Author: Nicolas Martin\nCompany: Fractal-Apps Pvt Ltd\nYear: 2024\n"
    )

    # GitHub link
    github_url = "https://github.com/aicollectivecommunity/RandomPromptGenerator/tree/main"

    # Create a frame to hold the text
    text_frame = tk.Frame(about_window, width=330, height=150)
    text_frame.pack_propagate(0)
    text_frame.pack(pady=5)

    # Create Text widget inside the frame for better control over text display
    text_widget = tk.Text(text_frame, wrap="word", font=("Arial", 10))
    text_widget.pack(fill=tk.BOTH, expand=True)

    # Insert the text into the Text widget
    text_widget.insert(tk.INSERT, about_text)
    text_widget.config(state="disabled")  # Disable editing of the text

    # Add a vertical scrollbar
    scrollbar = tk.Scrollbar(text_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Attach the scrollbar to the Text widget
    text_widget.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_widget.yview)

    # Function to open link
    def open_link(event):
        webbrowser.open_new(github_url)

    # Create a clickable label with "GitHub link"
    github_label = Label(about_window, text="GitHub link", fg="blue", cursor="hand2")
    github_label.pack(pady=5)
    github_label.bind("<Button-1>", open_link)

    # Okay button to close the window
    ok_button = Button(about_window, text="OK", command=about_window.destroy)
    ok_button.pack(pady=10)


root = tk.Tk()
root.title("Random Prompt Generator")

root.iconbitmap('logo.ico')


root.minsize(360, 550)
# Create a menu bar
menubar = tk.Menu(root)

# Create the file menu
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)

# Add an "About" item to the File menu
file_menu.add_command(label="About", command=show_about)

# Add an exit option for completeness
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Display the menu
root.config(menu=menubar)

# Main variable definitions
category_var = tk.StringVar(value="picture")
plural_var = tk.BooleanVar()
color_var = tk.BooleanVar()

# Radio buttons for category selection
tk.Label(root, text="Choose Category:").pack()
category_frame = tk.Frame(root)
category_frame.pack()
ttk.Radiobutton(category_frame, text="Story", variable=category_var, value="story").pack(side=tk.LEFT)
ttk.Radiobutton(category_frame, text="Picture", variable=category_var, value="picture").pack(side=tk.LEFT)
ttk.Radiobutton(category_frame, text="Video", variable=category_var, value="video").pack(side=tk.LEFT)

# Subject entry
tk.Label(root, text="Subject (optional):").pack()
subject_entry = ttk.Entry(root)
subject_entry.pack()

# Plural checkbox
plural_check = tk.Checkbutton(root, text="Use subject in plural?", variable=plural_var)
plural_check.pack()

# Color checkbox
color_check = tk.Checkbutton(root, text="Use a color style", variable=color_var)
color_check.pack()

# Complexity entry
tk.Label(root, text="Complexity (1-10):").pack()
complexity_entry = ttk.Entry(root)
complexity_entry.insert(0, "5")  # Default value
complexity_entry.pack()


# Randomness entry
tk.Label(root, text="Randomness (0-1):").pack()
randomness_entry = ttk.Entry(root)
randomness_entry.insert(0, "0.8")  # Default value
randomness_entry.pack()

# Semantic Field entry
tk.Label(root, text="Theme (optional):").pack()
theme_entry = ttk.Entry(root)
theme_entry.pack()

# Generate Button
generate_btn = ttk.Button(root, text="Generate", command=on_generate)
generate_btn.pack(pady=10)  # Add some padding for better visual separation

# Output Text Area
output_text = tk.Text(root, height=12, width=40)
output_text.pack()

# Copy Button
copy_btn = ttk.Button(root, text="Copy Output", command=on_copy)
copy_btn.pack()

root.mainloop()