
![Samples](https://github.com/user-attachments/assets/a77722c3-e638-4312-bc16-291fe7ae0fb1)

18/11/2024

# RandomPromptGenerator
Picture Random Prompt Generator to generate pictures with any chatbot like Co-Pilot, Grok, etc.

This is a project to explore generative IA capabilities through random prompting.

See article: [https://medium.com/@nicolas-martin/random-generative-ai-art-for-endless-creativity-d544e6cbe615](https://pub.towardsai.net/random-generative-ai-art-for-endless-creativity-d544e6cbe615)

# Prompt examples:
- Generate a picture of takeover, jealous, gamy, ritzy, filthy, care, during a heatwave, eye level, medium shot, f/2.8, in a moody cartoon style.
- Generate a picture of nudge, foamy, helpless, garrulous, multiply, moody, extreme wide shot, in a serene ultra realistic style.
- Generate a picture of interviewer, longing, resonant, dynamic, sweat, minimalist, moody, in a mysterious manga style.

# Guide:
Prerequisites: Python 3.8 or superior.
Install the wonderwords library:
```
pip install wonderwords
```

Download and run the RandomGenerator.ipynb notebook.

Use the generate_multiple_prompts function as you want:

```python
generate_multiple_prompts(
    color=True,                       # Use of camera color functions (black and white, sepia, etc.).
    count=5,                          # 1-5: controls number of elements.
    complexity=4,                     # 1-10: controls the prompt complexity (with different features)
    #semantic_field='prehistoric',    # Optional theme filter.
    randomness=0.8                    # 0-1: controls how experimental combinations can be
    
)
```



Google Collab link: https://colab.research.google.com/drive/1O-kzSiTGA-TstcujqKmL5WJ7Lco_eHWb?usp=sharing 

Author: Nicolas MARTIN.
