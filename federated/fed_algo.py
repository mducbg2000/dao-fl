from functools import reduce
from typing import List, Tuple
import numpy as np
from numpy.typing import NDArray

Layers = List[NDArray]
ClientParam = Tuple[Layers, int]


def fed_avg(clients: List[ClientParam]) -> Layers:
    num_examples_total = sum([num_examples for _, num_examples in clients])

    weighted_weights = [
        [layer * num_examples for layer in layers] for layers, num_examples in clients
    ]

    weights_prime: Layers = [
        reduce(np.add, layer_updates) / num_examples_total
        for layer_updates in zip(*weighted_weights)
    ]
    return weights_prime
