# AUTOGENERATED! DO NOT EDIT! File to edit: app.ipynb.

# %% auto 0
__all__ = ['learner', 'categories', 'image', 'label', 'examples', 'title', 'description', 'article', 'interface',
           'classify_image']

# %% app.ipynb 2
import gradio as gr
from fastai.vision.all import *

# %% app.ipynb 5
learner = load_learner('model/flood_classifier.pkl')

# %% app.ipynb 8
categories = 'Not Flooded', 'Flooded',

def classify_image(image):
    prediction, index, probabilities = learner.predict(image)
    return dict(zip(categories, map(float, probabilities)))

# %% app.ipynb 11
image = gr.Image()
label = gr.Label()
examples = [str(image_path) for image_path in Path('images/example_images')
.rglob('*.jpeg')]

title = 'Flood Classifier'
description = "An image classifier that can tell whether an image is flooded " \
              "or not. Works well with images that have a top-down/aeiral " \
              "view of the land below." \
              " This model was trained on the ResNet18 architecture and the " \
              "fastai library." \
              " Check out the associated blog post with the link below!"
article = """
<p style='text-align: center; font-size: 36px'><a href='https://forbo7.github.io/forblog/posts/5_detecting_floods_for_disaster_relief.html'>Blog Post</a></p>
"""

# %% app.ipynb 14
# Perhaps I can make the interface below with **kwargs?
interface = gr.Interface(fn=classify_image, inputs='image', outputs='label',
                         examples=examples, title=title,
                         description=description, article=article)
interface.launch(inline=False, enable_queue=True)
