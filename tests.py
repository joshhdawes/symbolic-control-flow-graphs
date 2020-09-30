"""
Small module to test SCFG construction of the module test_module.
"""

from builder import Function

if __name__ == "__main__":
  f = Function(module="test_module", function="Test:method")
  scfg = f.build_scfg()
  scfg.write_to_file("test-scfg.gv")
  print(scfg.get_vertices())
  print(scfg.get_edges())