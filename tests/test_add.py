import pytest
import sys, os
from src import add
myPath = os.path.dirname(os.path.abspath("../src"))
sys.path.insert(0, myPath + '/../')

def test_display():
  assert add.my_function("ALAGURAJA") == "ALAGURAJA"
