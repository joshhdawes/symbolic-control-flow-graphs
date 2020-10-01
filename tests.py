"""
Small module to test SCFG construction of the module test_module.
"""

from builder import Function
from comparison import ParseTree
import pprint

if __name__ == "__main__":
  f = Function(module="test_module", function="Test:method")
  scfg = f.build_scfg()

  grammar = scfg.derive_grammar()

  pprint.pprint(grammar)

  path1 = scfg.lines_to_path([7, 10, 13])

  path2 = scfg.lines_to_path([7, 12, 13])

  print("Comparing path \n %s with \n %s" % (path1, path2))

  p1 = ParseTree(path1, grammar, scfg.starting_vertices)
  p2 = ParseTree(path2, grammar, scfg.starting_vertices)

  p1.write_to_file("parse-tree-1.gv")
  p2.write_to_file("parse-tree-2.gv")

  intersection = p1.intersect([p2])

  intersection.write_to_file("intersection.gv")