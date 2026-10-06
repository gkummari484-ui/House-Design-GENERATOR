import streamlit as st
from pathlib import Path

from image_generator import generate_house_images
# PAGE CONFIGURATION


st.set_page_config(
    page_title="House Design Generator",
    page_icon="🏠",
    layout="wide"
)
# LOAD CSS


css_file = Path("style.css")

if css_file.exists():
    css = css_file.read_text(encoding="utf-8")
    st.markdown(
        f"<style>{css}</style>",
        unsafe_allow_html=True
    )
# TITLE


st.markdown(
    '<div class="title">🏠 HOUSE DESIGN GENERATOR</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Create your dream house using Artificial Intelligence'
    '</div>',
    unsafe_allow_html=True
)
# HOUSE DETAILS


st.markdown(
    '<div class="form-title">🏡 Enter House Details</div>',
    unsafe_allow_html=True
)

plot_size = st.text_input(
    "📐 Plot Size",
    "50 × 50 ft"
)

total_floors = st.selectbox(
    "🏢 Total Number of Floors",
    ["1", "2", "3", "4", "5"]
)

floor_to_design = st.selectbox(
    "🏗️ Floor to Design",
    [
        "Ground Floor",
        "1st Floor",
        "2nd Floor",
        "3rd Floor",
        "4th Floor",
        "5th Floor"
    ]
)

bedrooms = st.selectbox(
    "🛏️ Number of Bedrooms",
    ["1", "2", "3", "4", "5",
     "6", "7", "8", "9", "10"]
)

bathrooms = st.selectbox(
    "🚿 Number of Bathrooms",
    ["1", "2", "3", "4", "5",
     "6", "7", "8", "9", "10"]
)

parking = st.selectbox(
    "🚗 Parking",
    ["Yes", "No"]
)

style = st.selectbox(
    "🏠 House Style",
    [
        "Modern",
        "Luxury",
        "Traditional",
        "Minimalist"
    ]
)

location = st.text_input(
    "📍 Location",
    "Nizamabad"
)

colors = st.text_input(
    "🎨 Exterior Colors",
    "White + Brown + Gray"
)



# GENERATE BUTTON


st.write("")

generate = st.button(
    "🚀 GENERATE HOUSE DESIGN",
    use_container_width=True
)



# GENERATE IMAGES


if generate:

    if not location.strip():
        st.warning("⚠️ Please enter the house location.")
        st.stop()

    if not colors.strip():
        st.warning("⚠️ Please enter the exterior colors.")
        st.stop()

    details = {
        "plot_size": plot_size,
        "total_floors": total_floors,
        "floor_to_design":floor_to_design,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "parking": parking,
        "style": style,
        "location": location,
        "colors": colors
    }

    with st.spinner(
        "🤖 AI is designing your house..."
    ):

        try:
            inside_image, outside_image = (
                generate_house_images(details)
            )

        except Exception as e:
            st.error(
                f"❌ Image generation failed: {e}"
            )
            st.stop()

    # INSIDE IMAGE


    if inside_image is not None:

        st.markdown(
            '<div class="section-title">'
            '🏠 INSIDE THE HOUSE'
            '</div>',
            unsafe_allow_html=True
        )

        st.image(
            inside_image,
            caption="AI Generated Interior",
            use_container_width=True
        )

        st.download_button(
            "⬇️ Download Inside Image",
            data=inside_image,
            file_name="house_inside.png",
            mime="image/png",
            use_container_width=True
        )

    # ======================================
    # OUTSIDE IMAGE
    # ======================================

    if outside_image is not None:

        st.markdown(
            '<div class="section-title">'
            '🏡 OUTSIDE THE HOUSE'
            '</div>',
            unsafe_allow_html=True
        )

        st.image(
            outside_image,
            caption="AI Generated Exterior",
            use_container_width=True
        )

        st.download_button(
            "⬇️ Download Outside Image",
            data=outside_image,
            file_name="house_outside.png",
            mime="image/png",
            use_container_width=True
        )