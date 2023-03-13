"""Functions to create synthetic data for basket analysis."""
from typing import Dict
from numpy.random import choice

def create_synthetic_basket(list_item: list, init_freq: list, n_basket: int) -> Dict:
    """Create a basket of items.
    Args:
        list_item (list): list of items ['beer', 'egg', 'cheese', 'bread']
        init_freq (list): initial frequency of items [0.2, 0.3, 0.1, 0.4]
    Returns:
    """
    baskets = {}
    for basket_id in range(n_basket):
        baskets[basket_id] = choice(list_item, p=init_freq)
    return baskets

# TODO: Read online_retails.csv data