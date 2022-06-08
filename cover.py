class Cover:
   array_iphone = []
   def  __init__(self, name, color, serial_number):
       self.name = name
       self.color = color
       self.serial_number = serial_number
       self.array_iphone.append({self.serial_number, self.name, self.color})
   
   def show_color(self):
       print("the cover name is: ", self.name)
       print("the cover color is: ", self.color)
      
   def all_phones(self):
       print("The all phones are: ", self.array_iphone)



cover = Cover("iphone cover", "red", "AB12")
print(cover.show_color())
cover = Cover("iphone cover", "blue", "AB14")
print(cover.show_color())
cover = Cover("iphone cover", "black", "AB15")
print(cover.show_color())
cover = Cover("samsung cover", "black", "AB18")
print(cover.show_color())

print(cover.all_phones())



