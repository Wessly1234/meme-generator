import os
from image_overlay import overlay_text

def generate_ai_meme(topic, caption_text):

    top_text, bottom_text = caption_text.split("\n")

    template_path = "static/templates/drake.jpg"
    output_path = "static/output/meme.jpg"

    overlay_text(template_path, top_text, bottom_text, output_path)

    return output_path
