
def pizzaMenuVeg() :
    print("Choose your pizza :");
    print();
    print("PIZZA             SMALL      MEDIUM       LARGE");
    print();
    print();
    print("1: %s         %s         %s         %s" %(menu[0][0], menu[0][1], menu[0][2], menu[0][3]));
    print();
    print("2: %s         %s         %s         %s" %(menu[1][0], menu[1][1], menu[1][2], menu[1][3]));
    print();
    print("3: %s      %s         %s         %s" %(menu[2][0], menu[2][1], menu[2][2], menu[2][3]));
    print();
    print("4: %s       %s         %s         %s" %(menu[3][0], menu[3][1], menu[3][2], menu[3][3]));
    print();
    print("5: %s    %s         %s         %s" %(menu[4][0], menu[4][1], menu[4][2], menu[4][3]));
    print();
    print("6: %s       %s         %s         %s" %(menu[5][0], menu[5][1], menu[5][2], menu[5][3]));
    print();
    print("7: %s     %s         %s         %s" %(menu[6][0], menu[6][1], menu[6][2], menu[6][3]));
    print();
    print("8: %s           %s         %s         %s" %(menu[7][0], menu[7][1], menu[7][2], menu[7][3]));
    print();
    print("9: %s   %s         %s         %s" %(menu[8][0], menu[8][1], menu[8][2], menu[8][3]));
    print();
    print();


def pizzaMenuNonVeg() :
    print("Choose you pizza :");
    print();
    print("PIZZA                 SMALL       MEDIUM      LARGE");
    print();
    print();
    print("10: %s          %s         %s         %s" %(menu[9][0], menu[9][1], menu[9][2], menu[9][3]));
    print();
    print("11: %s      %s         %s         %s" %(menu[10][0], menu[10][1], menu[10][2], menu[10][3]));
    print();
    print("12: %s          %s         %s         %s" %(menu[11][0], menu[11][1], menu[11][2], menu[11][3]));
    print();
    print("13: %s        %s         %s         %s" %(menu[12][0], menu[12][1], menu[12][2], menu[12][3]));
    print();
    print("14: %s          %s         %s         %s" %(menu[13][0], menu[13][1], menu[13][2], menu[13][3]));
    print();
    print("15 :%s        %s         %s         %s" %(menu[14][0], menu[14][1], menu[14][2], menu[14][3]));
    print();
    print("16: %s         %s         %s         %s" %(menu[15][0], menu[15][1], menu[15][2], menu[15][3]));
    print();
    print("17: %s        %s         %s         %s" %(menu[16][0], menu[16][1], menu[16][2], menu[16][3]));
    print();
    print("18: %s      %s         %s         %s" %(menu[17][0], menu[17][1], menu[17][2], menu[17][3]));
    print();
    print();


def pizzaMenuDrink() :
    print("Choose your drink :");
    print();
    print("DRINK                 SMALL       MEDIUM      LARGE");
    print();
    print();
    print("1: %s              %s           %s          %s" %(drink[0][0], drink[0][1], drink[0][2], drink[0][3]));
    print();
    print("2: %s     %s           %s         %s" %(drink[1][0], drink[1][1], drink[1][2], drink[1][3]));
    print();
    print("3: %s         %s           %s         %s" %(drink[2][0], drink[2][1], drink[2][2], drink[2][3]));
    print();
    print("4: %s                  %s           %s          %s" %(drink[3][0], drink[3][1], drink[3][2], drink[3][3]));
    print();
    print("5: %s                 %s           %s          %s" %(drink[4][0], drink[4][1], drink[4][2], drink[4][3]));
    print();
    print();
       
def getPizzaVeg() :
    pizza=input("Which pizza you want to have ?\n");
    pizza=int(pizza);
    print();
    pizzasize=input("small, medium or large ?\t(S:small  M:medium  L:large)\n");
    pizzasize=pizzasize.lower();
    print();
    for i in range(0,9) :
        if i==pizza-1 :    
            if pizzasize=="s" :
                print("You have selected SMALL size %s and the price is Rs: %s/-" %(menu[i][0],menu[i][1]));
                return [pizzasize,menu[i][0],menu[i][1]];
                print();
            elif pizzasize=="m" :
                print("You have selected MEDIUM size %s and the price is Rs: %s/-" %(menu[i][0],menu[i][2]));
                return [pizzasize,menu[i][0],menu[i][2]];
                print();
            elif pizzasize=="l" :
                print("You have selected LARGE size %s and the price is Rs: %s/-" %(menu[i][0],menu[i][3]));
                return [pizzasize,menu[i][0],menu[i][3]];
                print();
        
def getPizzaNonVeg() :
    pizza=input("Which pizza you want to have ?\n");
    pizza=int(pizza);
    print();
    pizzasize=input("small, medium or large ?\t(S:small  M:medium  L:large)\n");
    pizzasize=pizzasize.lower();
    print();
    for i in range(9,18) :
        if i==pizza-1 :   
            if pizzasize=="s" :
                print("You have selected SMALL size %s and the price is Rs: %s/-" %(menu[i][0],menu[i][1]));
                return [pizzasize,menu[i][0],menu[i][1]];
                print();
            elif pizzasize=="m" :
                print("You have selected MEDIUM size %s and the price is Rs: %s/-" %(menu[i][0],menu[i][2]));
                return [pizzasize,menu[i][0],menu[i][2]];
                print();
            elif pizzasize=="l" :
                print("You have selected LARGE size %s and the price is Rs: %s/-" %(menu[i][0],menu[i][3]));
                return [pizzasize,menu[i][0],menu[i][3]];
                print();

def getPizzaDrink() :
    drnk=input("Which drink you want to have ?\n");
    drnk=int(drnk);
    print();
    drnksize=input("small, medium or large ?\t(S:small  M:medium  L:large)\n");
    drnksize=drnksize.lower();
    for i in range(5) :
        if i==drnk-1 :
            if drnksize=="s" :
                print("You have selected SMALL size %s and the price is Rs: %s/-" %(drink[i][0],drink[i][1]));
                return [drnksize,drink[i][0],drink[i][1]];
                print();
            elif drnksize=="m" :
                print("You have selected MEDIUM size %s and the price is Rs: %s/-" %(drink[i][0],drink[i][2]));
                return [drnksize,drink[i][0],drink[i][2]];
                print();
            elif drnksize=="l" :
                print("You have selected LARGE size %s and the price is Rs: %s/-" %(drink[i][0],drink[i][3]));
                return [drnksize,drink[i][0],drink[i][3]];
                print();


def pizzaBill(bill) :
    #print("Your pizza :\t\t%s %s" %(nonvegpz[1],(nonvegpz[0])));
    #print("Price :\t\t\t\t%s" %(nonvegpz[2]));
    pzBill=0; vatTotal=0; cgst=0; sgst=0;
    size=len(bill);
    for i in range(size):
        pzBill+=bill[i];
   
    vatTotal=(pzBill*12)/100;
    cgst=(pzBill*6)/100;
    sgst=(pzBill*6)/100;
    print("VAT 12 percent : \t\t%s" %vatTotal);
    print("CGST 6 percent : \t\t%s" %cgst);
    print("SGST 6 percent : \t\t%s" %sgst);
    total=pzBill+vatTotal+cgst+sgst;
    print("Total bill :\t\t\t%s" %total);

  
  
menu=[["MARGHERITA", 100, 150, 200],["FARM HOUSE", 120, 170, 220],
      ["DOUBLE CHEESE", 150, 200, 250],["PEPPY PANEER", 170, 230, 270],
      ["VEGGIE PARADISE", 170, 240, 290],["FRESH VEGGIE", 190, 270, 330],
      ["PANEER MAKHANI", 220, 270, 340],["5 PEPPER", 220, 270, 350],
      ["VEG EXTRAVAGANZA", 170, 210, 290],["CHEESE N CORN", 220, 290, 360],
      ["MEXICAN GREENWAVE", 220, 260, 310],["DELUXE VEGGIE", 240, 300, 370],
      ["PEPPER BARBECUE", 260, 320, 380],["CHICKEN TIKKA", 320, 400, 430],
      ["CHICKEN SAUSAGE", 330, 430, 480],["GOLDEN DELIGHT", 330, 390, 440],
      ["NON-VEG SUPREME", 340, 430, 510],["CHICKEN DOMINATOR", 320, 480, 540],
      ["PERI-PERI CHICKEN", 340, 390, 440],["BARBECUE & ONION", 360, 410, 460],
      ["CHICKEN FIESTA", 350, 410, 450]];
            
drink=[["COCA-COLA", 30, 50, 70], ["COCA-COLA NO-SUGER", 50, 70, 100],
       ["DIET COCA-COLA", 70, 90, 120],["FANTA", 40, 60, 80],["SPRITE", 40, 60, 90]];


print("\t....................WELCOME TO DOMINO'S....................");
print();
print();
from datetime import datetime;
ref=datetime.now();
print("Day : %s-%s-%s\t\t\t\t\t\t\tTime : %s:%s %s"%(ref.day,ref.month,ref.year,ref.strftime("%I"),ref.strftime("%M"),ref.strftime("%p")));
print();
print();
print("\t\t\tWelcome to %s dhamaka"%ref.strftime("%A"));
print();
print();
flag=True; i=True; bill=[];
while flag :
    pz=input("Which type of pizza you want ?\t(1:Veg  2:Non-veg)\n");
    print();

    if pz=="1" :
        pizzaMenuVeg();
        vegpz=getPizzaVeg();
        print();
        pizzaMenuDrink();
        ask=input("Do you want some drink ? (1:yes  2:no)\n");
        print();
        if ask=="1" :
            drnkpz=getPizzaDrink();
        elif ask=="2" :
            drnkpz=0;
        ask=input("Do you want anything else ? (1:yes 2:no)\n");
        print();
        if ask=="1" :
            i=True;
        elif ask=="2" :
            i=False;
    
        bill.append(vegpz[2]);
        
        if type(drnkpz)==list :
            drnkpz1=drnkpz[2];
        else :
            drnkpz1=0;
        
        bill.append(drnkpz1);    
        
        if i==False :    
            print();
            print("Your bill : ");
            print();    
            pizzaBill(bill);
            
    if i==False :
        break;
        
    elif pz=="2" :
        pizzaMenuNonVeg();
        nonvegpz=getPizzaNonVeg();
        print();
        pizzaMenuDrink();
        ask=input("Do you want some drink ? (1:yes  2:no)\n");
        print();
        if ask=="1" :
            drnkpz=getPizzaDrink();
        elif ask=="2" :
            drnkpz=0;
        ask=input("Do you want anything else ? (1:yes  2:no)\n");
        print();
        if ask=="1" :
            i=True;
        elif ask=="2" :
            i=False;
        
        bill.append(nonvegpz[2]);
        
        if type(drnkpz)==list :
            drnkpz2=drnkpz[2];
        else :
            drnkpz2=0;

        bill.append(drnkpz2);
        
        if i==False :    
            print();
            print("Your bill : ");
            print();    
            pizzaBill(bill);
            
    if i==False :
        break;
    
    
    