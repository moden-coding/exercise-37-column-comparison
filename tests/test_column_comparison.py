#!/usr/bin/env python3
"""Tests for the Column Comparison assignment."""

import unittest

import numpy as np

from src.column_comparison import column_comparison


class TestColumnComparison(unittest.TestCase):
    """column_comparison(a) -> rows of a where column 1 > second-to-last column."""

    def test_greater(self):
        n = 10
        for m in range(2, 10):
            a = np.random.randn(n, m)
            result = column_comparison(a)
            for row in result:
                self.assertGreater(
                    row[1],
                    row[-2],
                    msg="Row %s should not be in the result: its column 1 "
                    "value is not greater than its second-to-last column "
                    "value." % row,
                )

    def test_shape(self):
        n = 10
        for m in range(2, 10):
            a = np.random.randn(n, m)
            result = column_comparison(a)
            self.assertEqual(
                result.shape[1],
                m,
                msg="The result should have as many columns as the input "
                "(%d), got %d." % (m, result.shape[1]),
            )
            self.assertLessEqual(
                result.shape[0],
                n,
                msg="The result should have no more rows (%d) than the "
                "input (%d)." % (result.shape[0], n),
            )

    def test_content(self):
        n = 10
        for m in range(2, 10):
            a = np.random.randn(n, m)
            result = column_comparison(a)
            ri = 0
            for row in a:
                if row[1] > row[-2]:
                    np.testing.assert_allclose(
                        row,
                        result[ri],
                        err_msg="Incorrect result for array\n%s" % a,
                    )
                    ri += 1
            self.assertEqual(
                ri,
                result.shape[0],
                msg="Wrong number of rows for array\n%s: expected %d rows "
                "matching the filter, got %d." % (a, ri, result.shape[0]),
            )


if __name__ == "__main__":
    unittest.main()
