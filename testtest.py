
class TestTest:
    
    def __init__(self):
        pass
    
    def set_pk(self, pk):
        self.pk = pk
    
    def get_pk(self):
        return self.pk
    
    def set_value1(self, value1):
        self.value1 = value1;
    
    def get_value1(self):
        return self.value1
    
    def set_value2(self, value2):
        self.value2 = value2
    
    def get_value2(self):
        return self.value2
    
    def __str__(self):
        return str(self.pk) + " " + self.value1 + " " + str(self.value2)

test = TestTest()

test.set_value1("iets")

print(test)

testtest = Test()

