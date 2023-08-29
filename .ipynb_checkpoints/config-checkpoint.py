import os
os.environ['nproc_per_node'] = '1'
os.environ['RANK'] = '1'
os.environ['WORLD_SIZE'] = '1'
os.environ['MASTER_ADDR'] = 'localhost'
os.environ['MASTER_PORT'] = '33000'

ckpt_dir = "CodeLlama-7b"
tokenizer_path = "CodeLlama-7b"
temperature = 0.2
top_p = 0.9
max_seq_len = 256
max_batch_size = 4
max_gen_len = 256
