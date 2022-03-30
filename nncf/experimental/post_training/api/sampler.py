"""
 Copyright (c) 2022 Intel Corporation
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""
from abc import ABC
from abc import abstractmethod


from nncf.experimental.post_training.api.data_loader import DataLoader


class Sampler(ABC):
    """
    Base class for dataset sampler.
    """

    def __init__(self, dataloader: DataLoader, sample_indices=None):
        self.dataloader = dataloader
        self.batch_size = dataloader.batch_size
        data_loader_len = len(self.dataloader) + 1
        max_samples_len = min(len(sample_indices), data_loader_len) if sample_indices else data_loader_len
        self.batch_indices = list(range(0, max_samples_len, self.batch_size))

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass
