
from datetime import datetime, timedelta

class Beer:
    def __init__(self, style, ebc, abv):
        self.style = style
        self.ebc = ebc
        self.abv = abv
                
    def get_style(self):
        return f"This style of beer is: {self.style}"
    
    def get_ebc(self):
        if self.ebc <= 20:
            return "This is a light beer"
        return "This is a dark beer"
    
    def get_abv(self):
        if self.abv > 6:
            return "Be careful, you can get drunk!"
    
    
class Ipa(Beer):
    def __init__(self, style, ebc, abv, bitterness):
        self.bitterness = bitterness
        
        super().__init__(style, ebc, abv)
        
    def get_bitterness(self):
        if self.bitterness > 100:
            return "This beer is very bitter"
        
        if 40 < self.bitterness < 100:
            return "This beer is not very bitter"
        
ipa = Ipa('Ipa', 15, 7, 1000)
print(ipa.get_style()) 
print(ipa.get_ebc())
print(ipa.get_bitterness())
print(ipa.get_abv())


        
class Brew:
    def __init__(self, mash, boil):
        self.mash = mash
        self.boil = boil
        
    def mashing_and_boiling(self):
        message = f"The first step of brewing is mash, its time is {self.mash} hour(s), "
        
        start = datetime.now().strftime('%H:%M:%S')

        message += f"and started at {start}. "
        
        start_boil = (datetime.now() + timedelta(hours=self.mash)).strftime('%H:%M:%S')
        
        message += f"The second step is boil, its time is {self.boil} hour(s), and will start at {start_boil}. "
        
        end_brew = (datetime.now() + timedelta(hours=self.mash + self.boil)).strftime('%H:%M:%S')
        
        return message + f"The end of brew will be at {end_brew}."
    
brewing = Brew(2,5)
print(brewing.mashing_and_boiling())
        
        


