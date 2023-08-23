class house:
  def __init__(self, price, size, num_bedrooms):
    self.price = price
    self.size = size
    self.num_bedrooms = num_bedrooms


  def price_per_sqft(self):
      price_per_sqft = self.price / self.size
      return price_per_sqft      

houseSearch = house(125000, 900, 3) 
houseSearch.price_per_sqft()
