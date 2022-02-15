# -*- coding: utf-8 -*-
__author__ = ["Ayushmann Seth", "mloning"]

import numpy as np
import pytest

from sktime.datatypes import convert
from sktime.transformations.panel.tsfresh import TSFreshFeatureExtractor
from sktime.utils._testing.panel import make_classification_problem


@pytest.mark.parametrize("default_fc_parameters", ["minimal"])
def test_tsfresh_extractor(default_fc_parameters):
    X, _ = make_classification_problem()

    transformer = TSFreshFeatureExtractor(
        default_fc_parameters=default_fc_parameters, disable_progressbar=True
    )

    Xt = transformer.fit_transform(X)
    actual = Xt.filter(like="__mean", axis=1).values.ravel()
    converted = convert(X, from_type="nested_univ", to_type="pd-wide")
    expected = converted.mean(axis=1).values
    assert expected[0] == X.iloc[0, 0].mean()
    np.testing.assert_allclose(actual, expected)
