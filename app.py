import streamlit as st
import base64
from pathlib import Path
import google.generativeai as genai
from api_key import api_key
api_key="AIzaSyDASMvPCMLzf5pONCTeO4UyimdnGgx_O2E"
genai.configure(api_key=api_key)
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
#   "response_mime_type": "text/plain",
}
# safety_settings = [
#     {
#         "category": "HARM_CATEGORY_HARASSMENT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     },
#     # {
#     #     "category": "HARM_CATEGORY_VIOLENCE",
#     #     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     # },
#     {
#         "category": "HARM_CATEGORY_ILLEGAL",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_MEDICAL",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_DRUGS",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_WEAPONS",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_CHILD_ENDANGERMENT",
#         "threshold": "BLOCK_MEDIUM_AND_ABOVE"
#     },
#     {
#         "category": "HARM_CATEGORY_TERRORISM",
#         "thresold":"BLOCK_MEDIUM_AND_ABOVE"
#     }

# ]

system_prompt="""
As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a renowned hospital. Your expertise is crucial in identifying any anomalies, diseases, or health issues that may be present in the images.

Your Responsibilities INCLUDES:

1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.
2.Findings Report: pocument all observed anomalies or signs of disease. Clearly articulate these findings in structured formats.
3.Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable.
4.Treatment Suggestions: If appropriate, recommend possible treatment options or interventions.
Important Notes:

1. Scope of Response: Only respond if the image pertains to human health issues.
2.Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are "Unable to be provided based on the provided image quality."
3.Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before makinmg any medical decisions. This analysis is based on the image provided and may not be accurate.
4. Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis, ashering to structured and detailed documentation above.
Please provide me an output response with these 4 headings Detailed Analysis,Finding Report,Recommendations and Next Steps,Treatment Suggestions
"""

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
#   safety_settings=safety_settings
)


# Configure page title and icon
st.set_page_config(page_title="Vital Image Analytics", page_icon="🤖")
st.image("images.jpg", width=50)
st.title("Vital Image Analytics")
st.subheader("An application for analyzing medical images using deep learning.")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file:
  st.image(uploaded_file,width=300,caption="Uploaded Medical Image")
submit_button = st.button("Analyze Image")
if submit_button:
    image_data=uploaded_file.getvalue()
    image_parts=[
        {
            "mime_type":"image/jpg",
            "data":Path("images.jpg").read_bytes()
        },

    ]
    prompt_parts=[
      image_parts[0],
      system_prompt,
    ]
    
    response = model.generate_content(prompt_parts)
    if response:
      st.title("Here is the analysis based on your image :")
      st.write(response.text)
   

    



