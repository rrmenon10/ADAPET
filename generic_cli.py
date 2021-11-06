import argparse
import os
import json

from src.utils.Config import Config
from src.train import train


parser = argparse.ArgumentParser()
parser.add_argument('-d', "--data_dir", required=True, help="Data directory storing train/val/test jsonl files ")
parser.add_argument('-p', "--pattern", required=True, help="Pattern")
parser.add_argument('-v', "--dict_verbalizer", required=True, help="Dictionary mapping label name (in dataset) to the verbalizer to use ", type=json.loads)
args = parser.parse_args()

update_config = {"data_dir": args.data_dir, "pattern": args.pattern, "dict_verbalizer": args.dict_verbalizer}
config = Config(os.path.join("config", "Generic.json"), update_config, mkdir=True)
train(config)
