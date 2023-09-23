import torch
import os
from transformers import AutoModelForCausalLM, AutoTokenizer, GPTQConfig

print(f"GPU is available: {torch.cuda.is_available()}")

model_name_or_path = "TheBloke/Wizard-Vicuna-13B-Uncensored-GPTQ"
model_dir = os.path.join(os.path.dirname(__file__), "model")

# Check if the model is already downloaded, and if not, download and save it
try:
    model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="cuda")
except OSError:
    # If the model is not found locally, download and save it
    print("Downloading and saving the model...")
    model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
                                                device_map="auto",
                                                revision="main",
                                                trust_remote_code=False)
    model.save_pretrained(model_dir)

tokenizer_name_or_path = "TheBloke/Wizard-Vicuna-13B-Uncensored-GPTQ"
tokenizer = AutoTokenizer.from_pretrained(tokenizer_name_or_path, use_fast=True)


def run_model():
    while True:
        prompt = input("Enter a message: ")
        prompt_template = \
            f'''
            You are an AI that generates C# code for Unity. You will only respond with code that solves the prompt the user presents you. User's prompt: {prompt}
        '''

        print("\n\n*** Generate:")

        # Move the input data to CPU
        input_ids_cpu = tokenizer(prompt_template, return_tensors='pt').input_ids.cpu()

        # Split the generation process into chunks
        chunk_size = 128  # Adjust the chunk size as needed
        chunks = [input_ids_cpu[:, i:i+chunk_size] for i in range(0, input_ids_cpu.shape[1], chunk_size)]

        # Generate text in chunks and concatenate the results
        generated_text = []
        for chunk in chunks:
            chunk_output = model.generate(inputs=chunk.cuda(), temperature=0.0001, do_sample=True, top_p=0.05, top_k=5, max_new_tokens=128)
            generated_text.append(tokenizer.decode(chunk_output[0]))

        print("".join(generated_text))


if __name__ == "__main__":
    run_model()


# import torch
# import os
# from transformers import AutoModelForCausalLM, AutoTokenizer, GPTQConfig
#
# print(f"GPU is available: {torch.cuda.is_available()}")
#
# model_name_or_path = "TheBloke/Wizard-Vicuna-13B-Uncensored-GPTQ"
# model_dir = os.path.join(os.path.dirname(__file__), "model")
#
# # Check if the model is already downloaded, and if not, download and save it
# try:
#     model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="cuda")
# except OSError:
#     # If the model is not found locally, download and save it
#     print("Downloading and saving the model...")
#     model = AutoModelForCausalLM.from_pretrained(model_name_or_path,
#                                                 device_map="auto",
#                                                 revision="main",
#                                                 trust_remote_code=False)
#     model.save_pretrained(model_dir)
#
# tokenizer_name_or_path = "TheBloke/Wizard-Vicuna-13B-Uncensored-GPTQ"
# tokenizer = AutoTokenizer.from_pretrained(tokenizer_name_or_path, use_fast=True)
#
#
# def run_model():
#     while True:
#         prompt = input("Enter a message: ")
#         prompt_template = \
#             f'''
#             You are a AI that only generates C# code for Unity. You will only respond with code that solves the prompt
#             the user presents you. User's prompt: {prompt}
#         '''
#
#         print("\n\n*** Generate:")
#
#         input_ids = tokenizer(prompt_template, return_tensors='pt').input_ids.cuda()
#         output = model.generate(inputs=input_ids, temperature=0.0001, do_sample=True, top_p=0.95, top_k=40, max_new_tokens=512)
#         print(tokenizer.decode(output[0]))
#
#
# if __name__ == "__main__":
#     run_model()
