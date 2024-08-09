import json
import os
from pathlib import Path


def get_current_folder(global_variables):
    # if calling from a file
    if "__file__" in global_variables:
        current_file = Path(global_variables["__file__"])
        current_folder = current_file.parent.resolve()
    # if calling from a notebook
    else:
        current_folder = Path(os.getcwd())
    return current_folder

current_folder = get_current_folder(globals())

SOLUTION_PREFIX = "sagemaker-soln-documents-"

TAG_KEY = "sagemaker-soln"
TRAINING_INSTANCE_TYPE = "ml.c4.2xlarge"
INFERENCE_INSTANCE_TYPE = "ml.c4.2xlarge"
HOSTING_INSTANCE_TYPE = "ml.c4.2xlarge"
MY_AWS_ROLE = ""
BUCKET_NAME = ""
MODEL_ID = "tensorflow-tc-bert-en-uncased-L-12-H-768-A-12-2"