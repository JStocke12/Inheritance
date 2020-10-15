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

class SandwichMaker(Employee):

    def __init__(self, name):
        super().__init__(name)
        self.sandwiches_made = 0

    def __str__(self):
        return super().__str__() + "\n Sandwiches Made: {}".format(self.sandwiches_made)

    def check_out(self, order):
        order.sandwich_made = True
        self.sandwiches_made += 1

class Cashier(Employee):

    def __init__(self, name):
        super().__init__(name)
        self.orders_checked_out = 0

    def __str__(self):
        return super().__str__() + "\n Orders checked out: {}".format(self.orders_checked_out)

    def check_out(self, order):
        order.checked_out = True
        self.orders_checked_out += 1

def done(orders):
    for order in orders:
        if not (order.order_taken and order.sandwich_made and order.checked_out):
            print("Order {} is not finished!".format(order.num))
            return
    print("All done!")

def main():
    orders  = [Order(n) for n in range(50)] # This line creates a list of orders

    joe = OrderTaker("Joe")
    kevin = SandwichMaker("Kevin")
    larry = Cashier("Larry")

    for order in orders:
        joe.check_out(order)
        kevin.check_out(order)
        larry.check_out(order)

    done(orders)


if __name__ == "__main__":
    main()
