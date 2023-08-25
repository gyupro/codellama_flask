# codellama_flask
RESTful API flask server

This repository provides a simple Flask server for hosting [codellama](https://github.com/facebookresearch/codellama).


Setup & Installation

1. git clone https://github.com/facebookresearch/codellama
2. pip install flask
3. torchrun --nproc_per_node 1 app.py     --ckpt_dir ckpt_dir     --tokenizer_path tokenizer_path     --max_seq_len 128 --max_batch_size 4
Run example  
```bash
torchrun --nproc_per_node 1 app.py     --ckpt_dir CodeLlama-7b/     --tokenizer_path CodeLlama-7b/tokenizer.model     --max_seq_len 128 --max_batch_size 4
```


# Request example

## Curl example
```bash
curl -X POST http://localhost:5000/complete -H "Content-Type: application/json" -d '{"prompts": ["import socket\n\ndef ping_exponential_backoff(host: str):", "import argparse\n\ndef main(string: str):"]}'
```
## Python example
```python
import requests

url = "http://localhost:5000/complete"
data = {
    "prompts": [
        "import socket\n\ndef ping_exponential_backoff(host: str):",
        "import argparse\n\ndef main(string: str):"
    ]
}

response = requests.post(url, json=data)
print(response.json())
```


![image](https://github.com/gyupro/codellama_flask/assets/79894531/89521d10-3e15-4e90-b437-0c9b547ada6d)
