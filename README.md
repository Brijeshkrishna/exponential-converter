# Exponential-converter

Use to convert exponential value to normal value.


with out exponential-converter


eg :)
    1.0243277848911652 /100000 result is =>> 1.0243277848911652e-05
    
    42 /12207030 =>> 3.4406403523215722e-06
 
By using exponential-converter

eg :)
    1.0243277848911652 /100000 result is =>> 0.00001024327
    
    42 /12207030 =>> 0.0000034406403523215722
    
    
HOW exponential-converter works 
    If the number is { 652.22e+05 } It equivalent to =>> 652.22*(10**(-05)) =>> 652.22*0.00001 =>> 0.0065222 .
    
    BUT in python after 4 decimal points it changes to Exponential form.It means if u calculate 51/100000 it shows 0.00051 but 51/100000 is 5.1e-05.
    therefor it difficult to convert . IN  Exponential-converter it split's the number ,then convert ,then change to string
