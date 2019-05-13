import numpy as np
import os
import pickle

from torch.utils import data


class Synthetic4Dataset(data.Dataset):
    def __init__(self, data_dir):
        data_path = os.path.join(data_dir, 'synthetic_4.p')
        with open(data_path, 'rb') as file:
            synthetic_data = pickle.load(file)

        self._synthetic_data = np.array(synthetic_data).astype(np.float32)

        self._n = len(self._synthetic_data)

    def __getitem__(self, item):
        return self._synthetic_data[item]

    def __len__(self):
        return self._n

