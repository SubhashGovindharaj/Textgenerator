import streamlit as st
import openai

import streamlit as st
import openai

# Set up OpenAI API key
openai.api_key = 'your_openai_api_key'  # Replace with your actual API key

def generate_text(prompt, max_tokens=50):
    try:
        # Call the OpenAI API to generate text
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7  # Adjust temperature for creativity vs. coherence
        )
        # Extract the generated text from the response
        return response.choices[0].message['content'].strip()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

# Streamlit app interface
def main():
    st.title("GPT-4 Text Generator")

    # Input prompt from the user
    prompt = st.text_area("Enter your prompt:", "Once upon a time in a land far away")

    # Button to generate text
    if st.button("Generate Text"):
        if prompt:
            generated_text = generate_text(prompt)
            if generated_text:
                st.subheader("Generated Text:")
                st.write(generated_text)
        else:
            st.error("Please enter a prompt.")

if __name__ == "__main__":
    main()