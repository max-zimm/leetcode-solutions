class MinStack:

    def __init__(self):
        self.stack = []
        self.currentIndex = 0
        self.minValues = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minValues:
            if self.minValues[-1] > val:
                self.minValues.append(val)
            else:
                self.minValues.append(self.minValues[-1])
        else:
            self.minValues.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.minValues.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minValues[-1]

        
