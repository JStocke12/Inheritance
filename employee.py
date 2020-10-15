class Order:
    def __init__(self, num):
        self.num = num
        self.order_taken = False
        self.sandwich_made = False
        self.checked_out = False

    def __str__(self):
        return "Status of order {}:\n Taken: {}\n Made: {}\n Checked Out: {}".format(self.num,
                                                                                     self.order_taken,
                                                                                     self.sandwich_made,
                                                                                     self.checked_out)

class Employee:
    
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "Employee: {}".format(self.name)

    
class OrderTaker(Employee):

    def __init__(self, name):
        super().__init__(name)
        self.orders_taken = 0

    def __str__(self):
        return super().__str__() + "\n Orders taken: {}".format(self.orders_taken)

    def check_out(self, order):
        order.order_taken = True
        self.orders_taken += 1

# Create SandwichMaker and CheckOutClerk classes which inherit from Employee.

def main():
    orders  = [Order(n) for n in range(50)] # This line creates a list of orders

    joe = OrderTaker("Joe")

    # Using an OrderTaker, a SandwichMaker, and a CheckOutClerk, complete all the orders. 

    

if __name__ == "__main__":
    main()