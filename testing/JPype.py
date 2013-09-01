from  import *

gateway = JavaGateway()
stack = gateway.entry_point.getStack()
stack.push("First %s" % ('item'))
stack.push("Second item")
stack.pop()