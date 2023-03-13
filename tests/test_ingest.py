from src.ingest import create_synthetic_basket
import pandas as pd
import pytest

class TestCreateSyntheticBasket:
    def test_correct_input(self, synthetic_item_list, synthetic_init_freq):
        # Notice: n_basket need to be large enough to convert to init_freq (actual distribution)
        baskets_dict = create_synthetic_basket(synthetic_item_list, synthetic_init_freq, 1000)
        baskets_series = pd.Series(baskets_dict)
        items_freq = baskets_series.value_counts(normalize=True)
        assert len(baskets_series) == 1000
        assert baskets_series.isin(synthetic_item_list).all()
        for i in items_freq.index:
            assert pytest.approx(items_freq[i], abs=0.02) == synthetic_init_freq[synthetic_item_list.index(i)]
        