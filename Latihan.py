listGPA = [3, 2.7, 2.5, 4]
def hadiah(GPA):
    bonus = 500000
    hadiah = GPA * bonus
    return hadiah


for GPA in listGPA :
    if GPA >= 3 :
        print ("Selamat anda dapat hadiah : Rp ", hadiah(GPA))
    else :
        print("Anda kurang beruntung")