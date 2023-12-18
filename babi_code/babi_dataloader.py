import pandas as pd 
import numpy as np 
from keras.utils import get_file
import tarfile
import os

path = get_file('babi-tasks-v1-2.tar.gz', origin='https://s3.amazonaws.com/text-datasets/babi_tasks_1-20_v1-2.tar.gz')
tar = tarfile.open(path)
tar.extractall(path=os.getcwd())
tar.close()
