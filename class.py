class Bike():  
    def __init__(self,Bike_Name,Bike_Engine,Bike_Mileage,Bike_Fuelcapacity,Bike_Topspeed):  
        #__init__ is a initialization and also called a constructor in python.
        #__init__ intializes the attributes of the object.  
        self.BN=Bike_Name
        self.BE=Bike_Engine
        self.BM=Bike_Mileage
        self.BF=Bike_Fuelcapacity
        self.BT=Bike_Topspeed
#self keyword is used to access the function in another function.
    def Bike_Data(self):
        print("Bike Name :",self.BN)
        print(f"Bike Engine : {self.BE} cc")     
        print(f"Bike Mileage :{self.BM} Kmpl")
        print(f"Bike Fuel :{self.BF} Liters")
        print(f"Bike Speed :{self.BT} Kmph")
# f means "formatted string literal".
# This enables you to directly include python expressions inside the string like variables,expressions,function call.
while True:        
    Name= input("Enter Your Bike Name :")
    Engine= input("Enter Your Bike Engine :")
    Mileage=float(input("Enter Your Bike Mileage :"))
    Fuel=int(input("Enter Your Bike Fuel :"))
    Speed=float(input("Enter Your Bike Speed :"))    
#Creating An Object
    object=Bike(Name,Engine,Mileage,Fuel,Speed)    # object name = class name 
    object.Bike_Data()                             # function call 

