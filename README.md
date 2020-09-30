## How to use

```
from builder import Function
f = Function(module="test_module", function="Test:method")
scfg = f.build_scfg()
scfg.write_to_file("test-scfg.gv")
```
## Working with paths

Convert a list of lines to a list of SCFG edges using
```
edges = scfg.lines_to_edges([7, 9, 10])
```