from unittest import TestCase

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError


class ToolingTest(TestCase):

    def test_notebook(self):
        with open("tooling.ipynb") as f:
            nb = nbformat.read(f, as_version=4)
            ep = ExecutePreprocessor()
            try:
                ep.preprocess(nb, {'metadata': {'path': '.'}})
            except CellExecutionError as error:
                self.fail("Error executing notebook " + error.__str__())
