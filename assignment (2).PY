#all car prices
Jeep=10000
Corolla=20000 
Avalon=30000
Cadillac=40000
Volkswagen=50000
Nissan=60000
Hyundai=70000
Tesla=80000
Mercedes=90000
Lexus= 100000
BMWGroup=140000
Volvo=530000
Honda=61000
Audi=12000
Kia=38000
Ford=39000
Chevy99=48000
Chevy0=5600
Chevy23=90000
Chevy91=50000
Chevy21=78000
Chevy08=560000
Chevy13=730000
Chevy02=639000
Chevy22=530000
Chevy19=56800
Bent94=790000
ContinentalGT=890000
Muslanne=350000
BentleyArnage=740000
Bent22=60000000

from tabulate import tabulate

print('Car brands available')
print('(1)Cars \
       (2) Chevrolet \
      (3) Bentley')
    
    
brand=int(input('Specify car Brand using interger attached: '))   


if brand=='Cars':
    print('These are the Cars Available in showroom 1')
    data = [[1,"Jeep", 1998], 
        [2,"Corolla", 2022], 
        [3,"Avalon", 2019],
        [4,"Cadillac",2013],
        [5,"Volkswagen",2018],
        [6,"Nissan", 1999],
        [7,"Hyundai", 2020],
        [8,"Tesla", 2019],
        [9,"Lexus", 1989],
        [10,"BMWGroup",1980],
        [11,"Volvo",2000],
        [12,"Honda",2004],
        [13,"Audi",2015],
        [14,"Kia",2022],
        [15,"Ford",2008]],
    col_names = ["Number","Cars", "Models"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
    cartype=str(input('Specify car using : '))
    if cartype=='1':
     print('this car costs GHS {}'.format(Jeep))
    elif cartype=='Corolla':
      print('this car costs GHS {}'.format(Corolla))
    elif cartype=='Avalon':
        print('this car costs GHS {}'.format(Avalon))
    elif cartype=='Cadillac':
      print('this car costs GHS {}'.format(Cadillac))
    elif cartype=='Volkswagen':
      print('this car costs GHS {}'.format(Volkswagen))
    elif cartype=='Nissan':
        print('this car costs GHS {}'.format(Nissan))
    elif cartype=='Hyundai':
        print('this car costs GHS {}'.format(Hyundai))
    elif cartype=='Tesla':
        print('this car costs GHS {}'.format(Tesla))
    elif cartype=='Mercedes':
        print('this car costs GHS {}'.format(Mercedes))
    elif cartype=='Lexus':
         print('this car costs GHS {}'.format(Lexus))
    elif cartype=='BMWGroup':
         print('this car costs GHS {}'.format(BMWGroup))
    elif cartype=='Volvo':
         print('this car costs GHS {}'.format(Volvo))
    elif cartype=='Honda':
         print('this car costs GHS {}'.format(Honda))
    elif cartype=='Audi':
         print('this car costs GHS {}'.format(Audi))
    elif cartype=='Kia':
         print('this car costs GHS {}'.format(Kia))
    else:
         print('this car cost GHS {}'.format(Ford))
        
        
elif brand=='Chevroletj':
    print('These are the CHEVROLET Cars Available')
    data = [[1,"Chevy99", 1999], 
        [2,"Chevy91", 1991], 
        [3,"Chevy0", 2000], 
        [4,"Chevy08", 2008],
        [5,"Chevy21", 2021],
        [6,"Chevy19", 2019],
        [7,"Chevy13", 2013],
        [8,"Chevy02", 2002],
        [9,"Chevy22", 2022],
        [10,"Chevy23", 2023]]
    
    col_names = ["Number","Cars", "Models"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
    catype=str(input('Specify Chevy using : '))
    if cartype=='Chevy99': 
        print('this car costs GHS{}'.format(Chevy99))
    elif cartype=='Chevy91':
        print('this car cost GHS{}'.format(Chevy91))
    elif cartype=='3':
         print('this car cost GHS{}'.format(Chevy0))
    elif cartype=='4':
         print('this car cost GHS{}'.format(Chevy08))
    elif cartype=='5':
        print('this car cost GHS{}'.format(Chevy21))
    elif cartype=='6':
      print('this car cost GHS{}'.format(Chevy19))
    elif cartype=='7':
       print('this car cost GHS{}'.format(Chevy13))
    elif cartype=='8':
        print('this car cost GHS{}'.format(Chevy02))
    elif cartype=='9':
         print('this car cost GHS{}'.format(Chevy22))
    else:
        print('this car cost GHS{}'.format(Chevy23))
       
       

elif brand=='3':
    print('These are the BENTLEY Cars Available')
    data = [[1,"ContinentalGT",1899], 
        [2,"BentleyArnage", 2000], 
        [3,"Bent94", 1994], 
        [4,"Muslanne", 2009],
        [5,"Bent22", 2022],]
    col_names = ["Number","Cars", "Models"]
    print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
    cartype=str(input('Specify Car using number attached '))
    if cartype=='1':
     print('this car costs GHS{}'.format(ContinentalGT))
    elif cartype=='2':
     print('this car cost GHS{}'.format(BentleyArnage))
    elif cartype=='3':
      print('this car cost GHS{}'.format(Bent94))
    elif cartype=='4':
      print('this car cost GHS{}'.format(Muslanne))
    else:
     print('this car cost GHS{}'.format(Bent22))
    
    print('Thank You')