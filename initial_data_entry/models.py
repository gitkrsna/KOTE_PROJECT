from django.db import models

RANK_CHOICES = ( 
    ("L/Nk", "L/Nk"), 
    ("Sep", "Sep"), 
    ("Nk", "Nk"), 
    ("Hav", "Hav"), 
    ("Nb Sub", "Nb Sub"), 
    ("Sub", "Sub"), 
    ("SM", "SM"), 
    ("H/Lt", "H/Lt"), 
    ("Lt", "Lt"), 
    ("Capt", "Capt"), 
    ("Maj", "Maj"), 
    ("Lt Col", "Lt Col"), 
    ("Col", "Col"), 
    ("Brig", "Brig"), 
    ("Maj Gen", "Maj Gen"),
     ("Lt Gen", "Lt Gen"), 
) 

WEAPON_CHOICES =  ( 
    ("LMG 7.76mm", "LMG 7.76mm"), 
    ("INSAAS 5.56mm", "INSAAS 5.56mm"), 
    ("CMG 9mm", "CMG 9mm"), 
)  

TRADE_CHOICES=( 
    ("MT", "MT"), 
    ("SKT", "SKT"), 
    ("SHT", "SHT"), 
    ("H/Keeper", "H/Keeper"),  
    ("Washerman", "Washerman"),
    ("Cook Chef", "Cook Chef"),
    ("Carpenter", "Carpenter"),
    ("Clk SD", "Clk SD"),
 
)  


ISSUE_CHOICES =  ( 
    ("OD", "OD"), 
    ("TD", "TD"), 
    ("Attachment", "Attachment"), 
)  


COY_CHOICES= (
    ("HQ Coy", "HQ Coy"),
    ("A Coy", "A Coy"),
    ("B Coy", "B Coy"),
    ("C Coy", "C Coy"),
    ("D Coy", "D Coy"),
    ("LRW", "LRW"),
)

class InitialDataEntry(models.Model):
    army_no = models.CharField(max_length=20, verbose_name='Army Number',null=True, blank=True)
    name = models.CharField(max_length=25,null=True, blank=True)
    rank = models.CharField(choices=RANK_CHOICES,max_length=20,null=True, blank=True)
    i_card_no = models.CharField(max_length=20, verbose_name='I-Card Number',null=True, blank=True)   #I Card No
    trade = models.CharField(max_length=15, choices=TRADE_CHOICES,default="trade",null=True, blank=True)
    company = models.CharField(max_length=15, choices=COY_CHOICES,default="trade",null=True, blank=True)
    pic=models.ImageField(upload_to='profile_image', null=True, blank=True)
    wpn_type = models.CharField(max_length=15, choices = WEAPON_CHOICES, verbose_name='Wpn Type',null=True, blank=True)
    regd_no = models.CharField(max_length=20, verbose_name='Regd. Number',null=True, blank=True)    
    butt_no = models.CharField(max_length=20, verbose_name='Butt Number',null=True, blank=True)
    issue_type =   models.CharField(max_length=20, choices = ISSUE_CHOICES,null=True, blank=True)
    class Meta:
        verbose_name="Initial Data Entry"

class Attendance(models.Model):
    person = models.ForeignKey(InitialDataEntry,on_delete=models.CASCADE)
    weapon_out = models.CharField(max_length=6)
    weapon_in =  models.CharField(max_length=6, blank=True, null=True)
    date = models.DateField()

    def __str__(self):
        return self.person.name
    class Meta:
        verbose_name="IN-OUT"