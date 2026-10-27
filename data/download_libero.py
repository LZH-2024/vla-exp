#!/usr/bin/env python
"""下载 lerobot/libero 数据集到指定目录"""

from huggingface_hub import snapshot_download
import os

# 目标目录（手动指定）
DATA_DIR = "/root/autodl-tmp/data/libero"
os.makedirs(DATA_DIR, exist_ok=True)

print(f"Downloading lerobot/libero to {DATA_DIR} ...")

snapshot_download(
    repo_id="lerobot/libero",
    repo_type="dataset",
    local_dir=DATA_DIR,
    local_dir_use_symlinks=False,   # 直接拷贝，不用软链接
    resume_download=True,           # 支持断点续传
)

print("Download finished.")
print(f"Data location: {DATA_DIR}")