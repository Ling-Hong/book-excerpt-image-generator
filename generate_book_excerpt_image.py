from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def generate_book_excerpt_image(full_text, output_path='book_snippet.png'):
    # Image settings
    img_width, img_height = 1080, 1080
    background_color = (255, 255, 240)  # Light cream background
    text_color = (0, 0, 0)              # Black text

    # Create an image
    img = Image.new('RGB', (img_width, img_height), color=background_color)
    draw = ImageDraw.Draw(img)

    # Load a font
    font_path = os.path.expanduser("~/Library/Fonts/Arial Unicode.ttf")
    font_size = 40
    font_main = ImageFont.truetype(font_path, size=font_size)

    # Split the main text from the metadata
    main_text, *meta = full_text.split("Excerpt From")
    meta_text = "Excerpt From" + ''.join(meta).strip()

    # Remove everything after the URL (including the URL)
    url_start_index = meta_text.find("https://")
    if url_start_index != -1:
        meta_text = meta_text[:url_start_index].strip()

    # Wrap the main text to fit within the image width
    max_text_width = img_width - 200
    lines = textwrap.wrap(main_text.strip(), width=40)  # Adjust width based on font size and image width
    y_offset = 100

    for line in lines:
        line_width, line_height = font_main.getbbox(line)[2:4]
        draw.text(((img_width - line_width) / 2, y_offset), line, fill=text_color, font=font_main)
        y_offset += line_height + 10

    # Add the metadata
    font_meta = ImageFont.truetype(font_path, size=30)
    meta_lines = textwrap.wrap(meta_text, width=50)
    y_offset += 50
    for line in meta_lines:
        line_width, line_height = font_meta.getbbox(line)[2:4]
        draw.text(((img_width - line_width) / 2, y_offset), line, fill=text_color, font=font_meta)
        y_offset += line_height + 10

    # Save the image
    img.save(output_path)
    print(f"Instagram post created: {output_path}")

# Input details
full_text = """“The criminalization of the presumed idleness and unemployment of Black people as “vagrancy” was a critical weapon to coerce Black people to sign exploitative labor contracts.”

Excerpt From
Undoing Border Imperialism
Harsha Walia
https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewBook?id=0
This material may be protected by copyright."""

# Generate the Instagram post
generate_book_excerpt_image(full_text)
