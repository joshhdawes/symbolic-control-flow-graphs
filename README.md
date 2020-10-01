## How to use

```python
from builder import Function
f = Function(module="test_module", function="Test:method")
scfg = f.build_scfg()
scfg.write_to_file("test-scfg.gv")
```
## Working with paths

Convert a list of lines to a list of SCFG edges using
```python
edges = scfg.lines_to_edges([7, 9, 10])
```

## Determining divergence in paths

Once two paths have been obtained, for example by
```python
path1 = scfg.lines_to_path([7, 10, 13])
path2 = scfg.lines_to_path([7, 12, 13])
```

one can construct their parse trees with
```python
p1 = ParseTree(path1, grammar, scfg.starting_vertices)
p2 = ParseTree(path2, grammar, scfg.starting_vertices)
```

and intersect them (the process that identified points of divergence in paths)
```python
intersection = p1.intersect([p2])
```

The parse trees and the final intersection (with points of divergence indicated) can be written to a dot file with
```python
p1.write_to_file("parse-tree-1.gv")
p2.write_to_file("parse-tree-2.gv")
intersection.write_to_file("intersection.gv")
```