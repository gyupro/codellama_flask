from flask import Flask, request, jsonify
from llama import Llama
from typing import Optional
import fire
import os

app = Flask(__name__)
generator = None  # Placeholder for the generator

def get_completions(
    prompts,
    temperature: float = 0.2,
    top_p: float = 0.9,
    max_gen_len: Optional[int] = None,
):
    results = generator.text_completion(
        prompts,
        max_gen_len=max_gen_len,
        temperature=temperature,
        top_p=top_p,
    )
    return results

@app.route('/complete', methods=['POST'])
def complete_code():
    data = request.json
    prompts = data.get('prompts', [])
    print(prompts)
    results = get_completions(prompts)
    return jsonify(results)

def start_server(
    ckpt_dir: str,
    tokenizer_path: str,
    temperature: float = 0.2,
    top_p: float = 0.9,
    max_seq_len: int = 256,
    max_batch_size: int = 4,
    port: int = 5000
):
    global generator  # Declare as global to modify the global instance
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )
    print(get_completions(
                ["""\
import socket

def ping_exponential_backoff(host: str):""",
        """\
import argparse

def main(string: str):
    print(string)
    print(string[::-1])

if __name__ == "__main__":"""]
    ))
    app.run(debug=False, port=port, host='0.0.0.0')

if __name__ == '__main__':
    if 'LOCAL_RANK' not in os.environ or int(os.environ['LOCAL_RANK']) == 0:  # Only run on main process
        fire.Fire(start_server)
