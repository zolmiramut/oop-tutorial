import pandas as pd
import numpy as np


IMAGE_HEIGHT = 48
IMAGE_WIDTH = 48
DATASET_PATH = '../../data/raw/fer2013.csv'
PROCESSED_DATA_PATH_EMOTIONS = '../../data/processed/emotion.pkl'
PROCESSED_DATA_PATH_PIXELS = '../../data/processed/pixels.pkl'
chunk_list = []
for chunk in pd.read_csv(DATASET_PATH, chunksize=5000):
    chunk_list.append(chunk)
df = pd.concat(chunk_list, axis=0)


def str_to_image(row):
    return np.reshape(np.array([int(i) for i in row.split(" ")], dtype=np.uint8), [IMAGE_HEIGHT, IMAGE_WIDTH])


df['pixels'] = df['pixels'].apply(lambda x: str_to_image(x))
# import cv2
# cv2.imshow('test', df['pixels'][99])
# cv2.waitKey(0)
pd.DataFrame(df['pixels'].to_pickle(PROCESSED_DATA_PATH_PIXELS))
pd.DataFrame(df['emotion'].to_pickle(PROCESSED_DATA_PATH_EMOTIONS))
