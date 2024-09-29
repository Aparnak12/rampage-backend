from openai import OpenAI
import image_store

YOUR_API_KEY = "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"


# image_url = "image:https://www.adasigndepot.com/cdn/shop/products/ADA-1007-Blue-ISA-Accessible-Sign-6x8_580x.gif?v=1530907133"


def prompt_feature_detection(detected_features, selected_features):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant and you need to "
                "engage in a helpful, detailed, polite conversation with a user. Just "
                "return the list of extracted features."
            ),
        },
        {
            "role": "user",
            "content": (
                    "accessibility_features = [elevator, wheelchair ramp, reserved parking for "
                    "disabled people, handrails, wide doorways for wheelchair access, braille text]. "
                    "Return the ones that match the ones in the accessibility_features list." 
                    "These were Detected Features: " + str(detected_features) + ", Check if it matches with"
                    "accessibility_features. Just respond with feature name else respond with None"
            )
        },

    ]

    client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")

    # Chat completion without streaming
    response = client.chat.completions.create(
        model="llama-3.1-sonar-small-128k-chat",
        messages=messages,
    )
    print(response)

# def analyze_image(img_base64):
#     uploaded_image_url = image_store.upload(img_base64)
#     print("uploaded_image_url: ", uploaded_image_url)
#     # img_str = f"data:image/jpeg;base64,{img_base64}"
#     messages = [
#         {
#             "role": "system",
#             "content": (
#                 "You are an artificial intelligence assistant and you need to "
#                 "engage in a helpful, detailed, polite conversation with a user. Just "
#                 "return the list of extracted features."
#             ),
#         },
#         {
#             "role": "user",
#             "content": {
#                     "accessibility_features = [elevator, wheelchair ramp, reserved parking for "
#                     "disabled people, handrails, wide doorways for wheelchair access, braille text]. "
#                     "Analyse the attached image and identify the objects/features within it. "
#                     "Return the ones that match the ones in the accessibility_features list."
#             }
#         },
#
#     ]
#
#     client = OpenAI(api_key=YOUR_API_KEY, base_url="https://api.perplexity.ai")
#
#     # Chat completion without streaming
#     response = client.chat.completions.create(
#         model="llama-3.1-sonar-small-128k-chat",
#         messages=messages,
#     )
#     print(response)
