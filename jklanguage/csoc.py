import sys
class EV:
    def ev(self,s):
        self.vars = {}
        lines = [x for x in s.split("\n") if x != ""]
        pc = 0

        while pc < len(lines):
            line = lines[pc]
            match line.split(maxsplit=1)[0]:
                case "while":
                    condition = line.split(maxsplit=1)[1]
                    if self.ev_expr(condition) == 1:
                        pc += 1
                    else:
                        depth = 1
                        pc += 1
                        while pc < len(lines):
                            head = lines[pc].split(maxsplit=1)[0]
                            if head == "while":
                                depth += 1
                            elif head == "end":
                                depth -= 1
                                if depth == 0:
                                    pc += 1
                                    break
                            pc += 1

                case "end":
                    depth = 1
                    pc -= 1
                    while pc >= 0:
                        head = lines[pc].split(maxsplit=1)[0]
                        if head == "end":
                            depth += 1
                        elif head == "while":
                            depth -= 1
                            if depth == 0:
                                break
                        pc -= 1

                
                case "if":
                    if self.ev_expr(lines[pc].split(maxsplit=1)[1]) == 1:
                        pc += 1
                    else:
                        depth = 1
                        pc += 1
                        while pc < len(lines):
                            head = lines[pc].split(maxsplit=1)[0]
                            if head == "if":
                                depth += 1
                            elif head == "endif":
                                depth -= 1
                                if depth == 0:
                                    pc += 1
                                    break
                            elif head == "else" and depth == 1:
                                pc += 1
                                break
                            pc += 1

                case "else":
                    depth = 1
                    pc += 1
                    while pc < len(lines):
                        head = lines[pc].split(maxsplit=1)[0]
                        if head == "if":
                            depth += 1
                        elif head == "endif":
                            depth -= 1
                            if depth == 0:
                                pc += 1
                                break
                        pc += 1

                case "endif":
                    pc += 1


                case "for":
                    parts = line.split()
                    if len(parts) != 6 or parts[2] != "=" or parts[4] != "to":
                        print(f"Invalid for syntax at line: {line}")
                        pc += 1
                        break

                    varname = parts[1]
                    start = int(parts[3])
                    end = int(parts[5])

                    self.vars[varname] = start
                    self.for_loop = {
                        "var": varname,
                        "end": end,
                        "start_pc": pc
                    }
                    pc += 1


                case "endfor":
                    varname = self.for_loop["var"]
                    end = self.for_loop["end"]
                    start_pc = self.for_loop["start_pc"]

                    self.vars[varname] += 1
                    if self.vars[varname] <= end:
                        pc = start_pc + 1
                    else:
                        del self.for_loop
                        pc += 1

                case "print":
                    print(lines[pc].split(maxsplit=1)[1])
                    pc +=1
                
                case _:
                    parts = line.split(maxsplit=2)
                    if len(parts) == 3 and parts[1] == "=":
                        name, _, expr = parts
                        self.vars[name] = self.ev_expr(expr)
                        pc += 1
                    else:
                        print(f"Invalid syntax at line: {line}")
                        pc += 1

        print(self.vars)

    def ev_expr(self, s):
        toks = s.split()    
        stack = []
        for tok in toks:
            if tok.isdigit():
                stack.append(int(tok))
            elif tok in self.vars:
                stack.append(self.vars[tok])
            elif tok == "+":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs + rhs)
            elif tok == "-":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs - rhs)
            elif tok == "*":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs * rhs)
            elif tok == "/":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(lhs // rhs)
            elif tok == ">=":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(1 if lhs >= rhs else 0)
            elif tok == "<=":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(1 if lhs <= rhs else 0)
            elif tok == ">":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(1 if lhs > rhs else 0)
            elif tok == "<":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(1 if lhs < rhs else 0)
            elif tok == "!=":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(1 if lhs != rhs else 0)
            elif tok == "==":
                rhs = stack.pop()
                lhs = stack.pop()
                stack.append(1 if lhs == rhs else 0)
        return stack[0]


EV().ev(open(sys.argv[1]).read())