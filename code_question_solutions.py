'''
    :author: Jonathan Ben Avraham
    :date: 09/09/2024
    This is a file to demonstrate solutions for the coding questions from Black Cow Tech
'''

# Constant variable OBJ
OBJ = {
    'age': '21',
    'year': '2001',
    'month': '06',
    'day': '20'
}

# This class is to illustrate a class based implementation of the logic shown in Question 1.
class SampleObjectWithConfig():
    def __init__(self, dictionary, keys_allowed) -> None:
        '''
        obj: any dictionary passed to the object on init, to be used in place of self.request.GET.items() example in question.
        '''
        self.request_GET = dictionary
        self.keys_allowed = keys_allowed
        self.ret_list = []

    # sample method named config which returns a list of the integer values from the dictionary passed to the function.
    def config(self, **kwargs:dict) -> list:
        '''
            **kwargs allows for variable length keyword arguments to be passed to a method and either used or ignored.
        '''
        for v in kwargs.values():
            self.ret_list.append(v)
        return self.ret_list
    
    # a sample method for returning the values of a, *_, and b as shown in the question.
    def return_a_and_b(self) -> None:
        a, *_, b = self.config(**{k:int(v) for (k,v) in self.request_GET.items() if k in self.keys_allowed})
        print(a)
        print(_)
        print(b)

# defining a list of allowed keys
keys_allowed = ['age','year','month']
# creating an instance of the SampleObjectWithConfig class and calling the return_a_and_b method.
# sample_obj = SampleObjectWithConfig(dictionary=OBJ, keys_allowed=keys_allowed)
# sample_obj.return_a_and_b()

# This class is to illustrate my answer for question 2.
class MyObject():
    def __init__(self, v:int) -> None:
        # uncomment lines 51 - 53 to add type enforcement for self.__v
        # if not isinstance(v, (int, float)):
        #     raise ValueError("v must be an integer or floating point variable.")
        # else:
            self.__v = v

    def __lt__(self, o: int | float) -> bool:
        if not isinstance(self.__v, (int, float)) or not isinstance(o.__v, (int, float)):
            raise TypeError("self.__v and o.__v must both be integer or floating point variables.")
        else:
            return self.__v < o.__v

    def __eq__(self, o: int | float) -> bool:
        if not isinstance(self.__v, (int, float)) or not isinstance(o.__v, (int, float)):
            raise TypeError("self.__v and o.__v must both be integer or floating point variables.")
        else:
            return self.__v == o.__v
    
    def __repr__(self) -> str:
        return f"MyObject({self.__v})"
    
    def __str__(self) -> str:
        return str(self.__v)
    
obj_a = MyObject(12)
obj_b = MyObject(42)
obj_c = MyObject('hello')

outcome_a = obj_a < obj_b
print(outcome_a)
outcome_b = obj_a == obj_b
print(outcome_b)
print(repr(obj_a))
print(obj_a)

# uncomment line 86 and run the file again from the cli to see the custom TypeError message.
# outcome_c = obj_a == obj_c

# Sample SQL Transaction to handle the epected behaviour from Question 3.
# This is a pseudocode query and will not work without replacing :order_id and :order_value with dynamic string values
# SQL strings should also not be run directly from python scripts and should be handled in a separate package,
# especially in relation to production databases.
SQL_TRANSACTION_QUERY = """
TRANSACTION

-- removes orderId from 
DELETE FROM pending_orders WHERE order_id= :order_id;

-- simply just adding the data into the completed_orders table.
INSERT INTO completed_orders (order_id, order_date, order_value) 
VALUES (:order_id, :order_date, :order_value);

-- implements row-level locking to prevent the same row being updated from different sources at the same time causing inconsistency
UPDATE daily_totals
SET orders_count = orders_count + 1,
    total_value = total_value + :order_value
    version = version + 1
WHERE date = :order_date AND version = :current_version;

COMMIT;
"""

print(SQL_TRANSACTION_QUERY)