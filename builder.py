"""
Module with classes for reading in the relevant source code and constructing an SCFG.
"""

import ast

from scfg import CFG

def get_function_asts_in_module(module_ast):
    """
    Given a Module AST object, traverse it and find all the functions.
    :param module_ast:
    :return: List of function names.
    """
    all_function_names = []
    # map elements of ast to pairs - left hand side is module path, right hand side is ast object
    stack = list(map(lambda item : ("", item), module_ast.body))
    while len(stack) > 0:
        top = stack.pop()
        module_path = top[0]
        ast_obj = top[1]
        if type(ast_obj) is ast.FunctionDef:
            all_function_names.append(("%s%s" % (top[0], top[1].name), top[1]))
        elif hasattr(ast_obj, "body"):
            if type(ast_obj) is ast.If:
                stack += map(
                    lambda item : (module_path, item),
                    ast_obj.body
                )
            elif type(ast_obj) is ast.ClassDef:
                stack += map(
                    lambda item: ("%s%s%s:" %
                                  (module_path, "." if (module_path != "" and module_path[-1] != ":") else "",
                                   ast_obj.name), item),
                    ast_obj.body
                )
    return all_function_names


class Function(object):

  def __init__(self, module, function):
      try:
        # traverse the AST structure
        filename = "%s.py" % module.replace(".", "/")
        self.code = open(filename, "r").read()
        self.module = module
        self.function = function
      except:
      	print("Couldn't read in file '%s'" % module)

  def build_scfg(self):
    module_asts = ast.parse(self.code)
    function_asts = get_function_asts_in_module(module_asts)
    # process each function
    for (function_name, function_ast) in function_asts:
      if function_name == self.function:
        # construct the SCFG
        scfg = CFG()
        scfg.process_block(function_ast.body)
        return scfg
    return None