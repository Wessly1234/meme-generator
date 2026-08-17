from PIL import Image, ImageDraw, ImageFont
import textwrap


def draw_text_with_outline(draw, position, text, font):
    x, y = position
    outline_range = 2

    # Black outline
    for dx in range(-outline_range, outline_range + 1):
        for dy in range(-outline_range, outline_range + 1):
            draw.multiline_text((x + dx, y + dy), text, font=font, fill="black", align="center")

    # White main text
    draw.multiline_text((x, y), text, font=font, fill="white", align="center")


def get_text_size(draw, text, font):
    # New Pillow method
    bbox = draw.multiline_textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]
    height = bbox[3] - bbox[1]
    return width, height


def overlay_text(image_path, top_text, bottom_text, output_path):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    width, height = img.size

    try:
        font = ImageFont.truetype("arial.ttf", int(height / 12))
    except:
        font = ImageFont.load_default()

    # Wrap long text
    top_text = "\n".join(textwrap.wrap(top_text, width=20))
    bottom_text = "\n".join(textwrap.wrap(bottom_text, width=20))

    # ---- TOP TEXT ----
    w, h = get_text_size(draw, top_text, font)
    draw_text_with_outline(draw, ((width - w) / 2, 20), top_text, font)

    # ---- BOTTOM TEXT ----
    w, h = get_text_size(draw, bottom_text, font)
    draw_text_with_outline(draw, ((width - w) / 2, height - h - 20), bottom_text, font)

    img.save(output_path)
