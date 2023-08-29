def ToHex(decimalNum):
    if 10 <= decimalNum <= 15:
        return HexMap[decimalNum]
    else:
        return str(decimalNum)    
    
HexMap = {15: "F", 14: "E", 13: "D", 12: "C", 11: "B", 10: "A"}

RGB = [255, 2, 69] [::-1]
base = 16
base_format = ""    


for color in RGB:
    devisor = color    
    
    while devisor > base:
        remainder = color % base
        base_format = base_format + ToHex(remainder) 
        
        devisor = int(devisor/base) 

    base_format = base_format + ToHex(devisor)

    if(color < base):
        base_format = base_format + "0"

    
print(base_format [::-1])   
    
    
