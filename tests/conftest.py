import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def synthetic_item_list():
    return ['beer', 'egg', 'cheese', 'bread', 'wine', 'apple', 'orange']


@pytest.fixture
def synthetic_init_freq():
    return [0.2, 0.05, 0.1, 0.3, 0.05, 0.2, 0.1]