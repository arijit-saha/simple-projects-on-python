#make-my-trip
def displayFlightFair() :
    print("Choose your destination :");
    print();
    print(" PLACE             FLIGHT FAIR");
    print();
    print();
    print("1: %s         %s" %(flight[0][0], flight[0][1]));
    print();
    print("2: %s             %s" %(flight[1][0], flight[1][1]));
    print();
    print("3: %s              %s" %(flight[2][0], flight[2][1]));
    print();
    print("4: %s            %s" %(flight[3][0], flight[3][1]));
    print();
    print();

def displayHotelFair() :
    print("Suggested hotels for your stay :");
    print();
    print("HOTEL                 FAIR (per day)");
    print();
    print();
    if flightfair[0]==flight[0][0] :
        print("1: %s                   %s" %(chandigarh_hotel[0][0], chandigarh_hotel[0][1]));
        print();
        print("2: %s                %s" %(chandigarh_hotel[1][0], chandigarh_hotel[1][1]));
        print();
        print("3: %s          %s" %(chandigarh_hotel[2][0], chandigarh_hotel[2][1]));
        print();
        print("4: %s       %s" %(chandigarh_hotel[3][0], chandigarh_hotel[3][1]));
        print();
    elif flightfair[0]==flight[1][0] :
        print("1: %s                %s" %(mumbai_hotel[0][0], mumbai_hotel[0][1]));
        print();
        print("2: %s                 %s" %(mumbai_hotel[1][0], mumbai_hotel[1][1]));
        print();
        print("3: %s         %s" %(mumbai_hotel[2][0], mumbai_hotel[2][1]));
        print();
    elif flightfair[0]==flight[2][0] :
        print("1: %s      %s" %(delhi_hotel[0][0], delhi_hotel[0][1]));
        print();
        print("2: %s              %s" %(delhi_hotel[1][0], delhi_hotel[1][1]));
        print();
        print("3: %s             %s" %(delhi_hotel[2][0], delhi_hotel[2][1]));
        print();
    elif flightfair[0]==flight[3][0] :
        print("1: %s               %s" %(ladakh_hotel[0][0], ladakh_hotel[0][1]));
        print();
        print("2: %s            %s" %(ladakh_hotel[1][0], ladakh_hotel[1][1]));
        print();
        print("3: %s             %s" %(ladakh_hotel[2][0], ladakh_hotel[2][1]));
        print();
        print();

def getFlightFair() :
    place=input("Which place you want to visit ?\n");
    place=int(place);
    print();
    i=True;
    while i :
        for i in range(4) :  
            if i==place-1 :
                print("You have selected %s and the fair is Rs: %s/-" %(flight[i][0],flight[i][1]));
                return [flight[i][0],flight[i][1]];
                print();
        i=False;
        print("Wrong input"); break;
        
def getHotelFair() :
    hotel=input("Choose your hotel : \n");
    hotel=int(hotel);
    print(); 
    if flightfair[0]==flight[0][0] :
        i=True;
        while i :
            for i in range(4) :    
                if i==hotel-1 :
                    print("You have selected %s and the fair is Rs: %s/-" %(chandigarh_hotel[i][0],chandigarh_hotel[i][1]));
                    return [chandigarh_hotel[i][0],chandigarh_hotel[i][1]];
                    print();
            i=False;
            print("Wrong input"); break;
    elif flightfair[0]==flight[1][0] :
        i=True;
        while i :
            for i in range(3) :
                if i==hotel-1 :
                    print("You have selected %s and the fair is Rs: %s/-" %(mumbai_hotel[i][0],mumbai_hotel[i][1]));
                    return [mumbai_hotel[i][0],mumbai_hotel[i][1]];
                    print();
            i=False;
            print("Wrong input"); break;
    elif flightfair[0]==flight[2][0] :
        i=True;
        while i :
            for i in range(3) :
                if i==hotel-1 :
                    print("You have selected %s and the fair is Rs: %s/-" %(delhi_hotel[i][0],delhi_hotel[i][1]));
                    return [delhi_hotel[i][0],delhi_hotel[i][1]];
                    print();
            i=False;
            print("Wrong input"); break;
    elif flightfair[0]==flight[3][0] :
        i=True;
        while i :
            for i in range(3) :
                if i==hotel-1 :
                    print("You have selected %s and the fair is Rs: %s/-" %(ladakh_hotel[i][0],ladakh_hotel[i][1]));
                    return [ladakh_hotel[i][0],ladakh_hotel[i][1]];
                    print();
            i=False;
            print("Wrong input"); break;
    

def tripBill(billflight,billhotel) :
    a=0; b=0;
    for i in range(len(tripplace)) :
        print("Travel from :\t\t'Bengaluru' to '%s'" %tripplace[i]);
        print("Flight fair :\t\t\t%s/-"%billflight[i]);
    
    if len(triphotel)>0 :    
        for j in range(len(triphotel)) :
            print("Hotel booked :\t\t\t%s" %triphotel[j]);
            print("Hotel charges :\t\t\t%s/-" %billhotel[j]);
            
    
    tbill=0; vatTotal=0; cgst=0; sgst=0;
    for (i,j) in zip(range(len(billflight)),range(len(billhotel))) :
        tbill+=(billflight[i]+billhotel[j]);
   
    cgst=(tbill*9)/100;
    sgst=(tbill*9)/100;
    
    print("CGST 9 percent : \t\t%s" %cgst);
    print("SGST 9 percent : \t\t%s" %sgst);
    totalbill=tbill+cgst+sgst;
    print("Total bill :\t\t\t%s" %totalbill);

  
chandigarh_hotel=[["Taj", 18000],["Oberoi", 20000],["Leela Palace", 25000],["ChotuKamal Hotel", 1500]];
mumbai_hotel=[["Vivanta", 15000],["Oberoi", 16000],["Panvillas Hotel", 1100]];
delhi_hotel=[["SasteMeinRaho Hotel", 1200],["Leela Palace", 1700, 2100, 2900],["Pearl Grand", 10000]];   
ladakh_hotel=[["Ginger", 15000],["West Views", 3000],["Marriotte", 8000]];
            
flight=[["Chandigarh", 5000], ["Mumbai", 2000],["Delhi", 6000],["Ladakh", 11000]];


print("\t....................WELCOME TO MAKE MY TRIP....................");
print();
print();
from datetime import datetime;
ref=datetime.now();
print("Date : %s-%s-%s  (%s)\t\t\t\t\tTime : %s:%s %s"%(ref.day,ref.month,ref.year,ref.strftime("%A"),ref.strftime("%I"),ref.strftime("%M"),ref.strftime("%p")));
print();
print();
flag=True; i=True; billflight=[];billhotel=[]; tripplace=[]; triphotel=[];
while flag :
    flt=input("Which type of flight you want ?\t(1:One Way 2:Round Trip)\n");
    flt=flt;
    print();

    if flt=='1' :
        displayFlightFair();
        flightfair=getFlightFair();
        if flightfair==None : break;
        print();
        displayHotelFair();
        ask=input("Do you want to book a hotel now ? (1:yes 2:no)\n");
        ask=int(ask);
        print();
        if ask==1 : hotelfair=getHotelFair();
        elif ask==2 : hotelfair=0;
        else : print("Wrong input"); break;
        
        ask=input("Do you want to book another trip ? (1:yes 2:no)\n");
        ask=int(ask);
        print();
        if ask==1 : i=True;
        elif ask==2 : i=False;
        else : print("Wrong input"); break;
        
        if type(hotelfair)==list :
            tripplace.append(flightfair[0]);
            triphotel.append(hotelfair[0]);
            hotelfair1=hotelfair[1];
        else :
            tripplace.append(flightfair[0]);
            hotelfair1=0;
                        
        billflight.append(flightfair[1]);
        billhotel.append(hotelfair1); 
        
        if i==False :
            print("Your bill : ");
            print();    
            tripBill(billflight,billhotel);
            
    if i==False : break;
        
    elif flt=='2' :
        displayFlightFair();
        flightfair=getFlightFair();
        if flightfair==None : break;
        print();
        displayHotelFair();
        ask=input("Do you want to book a hotel now ? (1:yes 2:no)\n");
        ask=int(ask);
        print();
        if ask==1 : hotelfair=getHotelFair();
        elif ask==2 : hotelfair=0;
        else : print("Wrong input"); break;
        
        ask=input("Do you want to book another trip ? (1:yes 2:no)\n");
        ask=int(ask);
        print();
        if ask==1 : i=True;
        elif ask==2 : i=False;
        else : print("Wrong input"); break;
        
        if type(hotelfair)==list :
            tripplace.append(flightfair[0]);
            triphotel.append(hotelfair[0]);
            hotelfair1=hotelfair[1];
        else :
            tripplace.append(flightfair[0]);
            hotelfair1=0;
                        
        billflight.append(flightfair[1]*2);
        billhotel.append(hotelfair1); 
        
        if i==False :
            print("Your bill : ");
            print();    
            tripBill(billflight,billhotel);
    
    else : print("Wrong input"); break;
            
    if i==False : break;
    
    
    