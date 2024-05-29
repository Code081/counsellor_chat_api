from huggingface_hub import snapshot_download

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v0.1"
snapshot_download(repo_id=model_id,
                  local_dir="tinyllama_converted",
                  local_dir_use_symlinks=False,
                  revision="main")