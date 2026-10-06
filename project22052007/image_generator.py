import requests
from io import BytesIO
from urllib.parse import quote
# GENERATE ONE IMAGE


def generate_image(prompt):

    url = (
        "https://image.pollinations.ai/prompt/"
        + quote(prompt)
    )

    response = requests.get(
        url,
        timeout=120
    )

    if response.status_code == 200:

        return BytesIO(
            response.content
        )

    raise Exception(
        f"Image generation failed. "
        f"Status code: {response.status_code}"
    )

# GENERATE HOUSE IMAGES


def generate_house_images(details):
    # OUTSIDE HOUSE PROMPT
    outside_prompt = f"""
Photorealistic Indian residential house exterior.

Total floors: {details['total_floors']}.
Design ONLY: {details['floor_to_design']}.

The selected floor must be the main focus.
Do not design another floor.
Keep lower floors as existing structural context.

Style: {details['style']}.
Plot size: {details['plot_size']}.
Bedrooms: {details['bedrooms']}.
Bathrooms: {details['bathrooms']}.
Parking: {details['parking']}.
Location: {details['location']}.
Exterior colors: {details['colors']}.

Front elevation, realistic windows, doors and balcony,
Indian architecture, realistic daylight,
professional architectural visualization.

No people. No text. No watermark.
"""


    # INSIDE HOUSE PROMPT
    inside_prompt = f"""
Photorealistic interior of an Indian residential house.

Total floors: {details['total_floors']}.
Design interior ONLY for: {details['floor_to_design']}.

Do not design another floor.

Style: {details['style']}.
Bedrooms: {details['bedrooms']}.
Bathrooms: {details['bathrooms']}.
Location: {details['location']}.
Interior colors: {details['colors']}.

Modern living room, comfortable sofa, television,
coffee table, ceiling lights, windows, curtains,
modern flooring, wall decorations and indoor plants.

Realistic furniture, Indian home interior,
professional interior photography,
realistic daylight, high quality.

No people. No text. No watermark.
"""
        # GENERATE IMAGES
    outside_image = generate_image(
        outside_prompt
    )
    inside_image = generate_image(
        inside_prompt
    )
    # RETURN BOTH IMAGES
    return inside_image, outside_image 