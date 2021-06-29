from typing import List, Tuple
import numpy as np
from io import BytesIO


class Chunk:
    """A Chunk should only be provided data to store in bytes form, alongside the meta information (like shape/num_samples). The
    byte ranges are to be generated by this chunk, and it can also spawn new chunks as needed."""

    def __init__(self, max_data_bytes: int):
        self.index_shape_encoder = None
        self.index_byte_range_encoder = None
        self.max_data_bytes = max_data_bytes

        self.data = bytearray()

        self.next_chunk = None

    def tobytes(self) -> bytes:
        out = BytesIO()
        np.savez(
            out,
            index_shape_encoder=self.index_shape_encoder,
            index_byte_range_encoder=self.index_byte_range_encoder,
            data=self.data,
        )
        out.seek(0)
        return out.read()

    @property
    def num_samples(self):
        raise NotImplementedError

    @property
    def has_space(self):
        raise NotImplementedError

    def extend(
        self, buffer: bytes, num_samples: int, sample_shape: Tuple[int]
    ) -> Tuple:
        raise NotImplementedError

    def numpy(self):
        raise NotImplementedError

    def __getitem__(self, sample_index: int):
        raise NotImplementedError

    def __eq__(self, o: object) -> bool:
        raise NotImplementedError


def chunk_from_buffer(buffer: bytes) -> Chunk:
    raise NotImplementedError
