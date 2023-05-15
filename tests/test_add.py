import pytest
import sys, os
from src import add
myPath = os.path.dirname(os.path.abspath("E:\RAJA-PYTHON\python-github-actions\src"))
sys.path.insert(0, myPath + '/../')

def test_display():
  assert add.my_function("ALAGURAJA") == "ALAGURAJA"