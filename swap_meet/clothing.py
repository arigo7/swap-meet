class Clothing:
    def __init__(self, category = "", condition = 0):
        self.category = category
        self.condition = condition
    # do super
    # super()__init__
    def __str__(self):
        return "The finest clothing you could wear."