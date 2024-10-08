import Interpreter

global_symbol_table = Interpreter.SymbolTable()
global_symbol_table.set("null", Interpreter.null)
global_symbol_table.set("true", Interpreter.true)
global_symbol_table.set("false", Interpreter.false)

global_symbol_table.set("println", Interpreter.println)
global_symbol_table.set("readline", Interpreter.readline)

global_symbol_table.set("int", Interpreter.int_)
global_symbol_table.set("float", Interpreter.float_)
global_symbol_table.set("string", Interpreter.str_)
global_symbol_table.set("boolean", Interpreter.bool_)
global_symbol_table.set("array", Interpreter.array)

global_symbol_table.set("length", Interpreter.len_)
global_symbol_table.set("run", Interpreter.run)


if __name__ == "__main__":
    while True:
        syntax = str(input("Toy > "))
        if syntax.strip():
            res = Interpreter.execute("<shell>", str(syntax))
            if res is not None:
                try:
                    if isinstance(res.elements[0], Interpreter.Null):
                        continue
                    if len(res.elements) == 1:
                        print(repr(res.elements[0]))
                    else:
                        print(repr(res))
                except AttributeError:
                    print(res)
