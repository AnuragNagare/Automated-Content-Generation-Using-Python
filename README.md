# Automated-Content-Generation-Using-Python

This code creates a simple web app using **Streamlit** that generates text content based on a prompt provided by the user. It uses the **GPT-2 language model** from the **Hugging Face Transformers library** for content generation. Here's how the app works, step-by-step:

### 1. **Streamlit Setup**
- `import streamlit as st`: Streamlit is a framework used to build web applications, especially for data science projects.
- The app's title is set using `st.title("Automated Content Generation")`, and a brief description of the app is shown with `st.write()`.

### 2. **User Inputs**
- The app provides an input field for the user to enter a **prompt** (a text string) using `st.text_input()`. It defaults to the prompt "Write a blog post about Generative AI."
- It also provides a **dropdown menu** to select the tone of the generated text (formal, casual, or technical) using `st.selectbox()`.

### 3. **Generate Button**
- A button labeled **"Generate"** is created using `st.button()`. When the user clicks this button, the app triggers the content generation process.

### 4. **Content Generation with GPT-2**
- When the button is clicked, the app calls the `generate_content()` function, which is responsible for generating the text. Inside this function:
  - **GPT-2** model (`GPT2LMHeadModel`) and tokenizer (`GPT2Tokenizer`) are loaded using the Hugging Face library.
  - The user’s input (prompt) is tokenized into a format suitable for the GPT-2 model.
  - The model then generates text based on the prompt. Several parameters control the generation:
    - `max_length`: Limits the length of the generated content to 300 tokens.
    - `temperature`: Controls the creativity or randomness of the output (lower values like 0.5 make it more deterministic; higher values like 0.9 make it more creative).
    - `num_return_sequences`: Specifies how many versions of the text are generated (only 1 is generated here).
    - `no_repeat_ngram_size`: Prevents the model from repeating the same sequence of words (ngram) within the output.
  - The generated text is then decoded back into a readable string using the tokenizer.

### 5. **Tone Adjustment**
- The selected **tone** (formal, casual, or technical) influences the **temperature** of the text generation. Different temperatures make the output more structured or creative, depending on the selected tone:
  - **Formal tone** uses a temperature of 0.7.
  - **Casual tone** uses a higher temperature of 0.9 (more creative).
  - **Technical tone** uses a lower temperature of 0.5 (more precise).

### 6. **Displaying the Generated Content**
- Once the content is generated, it is displayed back to the user with `st.write()` under a subheading labeled **"Generated Content"**.

### Summary:
- **Input prompt and tone** from the user.
- **Generate button** triggers text generation.
- **GPT-2 model** generates content based on the prompt and tone.
- **Output** is displayed in the app.

This process allows the app to generate blog posts, articles, or other text-based content automatically based on the provided user input.

https://github.com/user-attachments/assets/3ae2a831-5f99-4e2a-ae7f-b4f39652dc93

