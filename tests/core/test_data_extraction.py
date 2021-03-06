from __future__ import print_function
from __future__ import division
import pytest
from os import path
import vtk
import turbulucid
from turbulucid.core.data_extraction import *
from numpy.testing import assert_allclose


def test_dist_orthogonal():
    casePath = path.join(turbulucid.__path__[0], "..", "tests", "datasets",
                         "test_case_block", "averaged.vtm")
    case = turbulucid.Case(casePath)

    distance = dist(case, "bottomWall")
    assert_allclose(distance, 0.25)

    distance = dist(case, "topWall")
    assert_allclose(distance, 0.25)

    distance = dist(case, "inlet")
    assert_allclose(distance, 1/6, rtol=1e-5)

    distance = dist(case, "outlet")
    assert_allclose(distance, 1/6, rtol=1e-5)
