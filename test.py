
import mysql.connector

class Test:
    
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
    
    
    def get_db(self):
        username = "test"
        password = "test"
        host = "127.0.0.1"
        port = "3306"
        db = "test"
        
        return mysql.connector.connect(user = username, password = password, host = host, port = port, db = db)
    
    def get_records(self):
        connection = self.get_db()
        cursor = connection.cursor()
        
        query = ("SELECT `id`, `value1`, `value2` FROM `test`")
        print("Query is: " + query)
        
        cursor.execute(query)
        
        for (pk, value1, value2) in cursor:
            print("{} - {} - {}".format(pk, value1, value2))
        
        cursor.close()
        connection.close()
        
    def get_record(self, pk):
        connection = self.get_db()
        cursor = connection.cursor()
        
        query = ("SELECT `id`, `value1`, `value2` FROM `test` WHERE `id` = " + str(pk))
        print("Query is: " + query)
        
        cursor.execute(query)
        
        test = Test()
        
        for (pk, value1, value2) in cursor:
            print("{} - {} - {}".format(pk, value1, value2))
            
            test.set_pk(pk)
            test.set_value1(value1)
            test.set_value2(value2)
        
        cursor.close()
        connection.close()
        
        
        
        return test
    
    def __str__(self):
        return str(self.pk) + " " + self.value1 + " " + str(self.value2)

test = Test()
test.get_records()
newTest = test.get_record(1)
print("Nieuw test record: " + str(newTest))