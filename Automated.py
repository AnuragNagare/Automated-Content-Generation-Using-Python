import streamlit as st
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def generate_content(prompt, max_length=300, temperature=0.7, model_name="gpt2"):
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=max_length,
        temperature=temperature,
        num_return_sequences=1,
        no_repeat_ngram_size=2
    )
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

# Streamlit app
st.title("Automated Content Generation")
st.write("Generate blog posts, articles, or reports based on specific topics or keywords.")

prompt = st.text_input("Enter a prompt:", "Write a blog post about Generative AI.")
tone = st.selectbox("Select tone:", ["formal", "casual", "technical"])

if st.button("Generate"):
    temperature = 0.7 if tone == "formal" else 0.9 if tone == "casual" else 0.5
    generated_text = generate_content(prompt, temperature=temperature)
    st.subheader("Generated Content:")
    st.write(generated_text)
