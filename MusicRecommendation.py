import math
from operator import itemgetter

# define class similarity
class similarity:
    
    # class instantiation 
    def __init__ (self, ratingX, ratingY):
        self.ratings1 = ratingX
        self.ratings2 = ratingY

    # minkowski distance between two vectors
    def minkowksi(self, r):
    
        # calculate minkowski distance
        distance = 0       
        for k in (set(self.ratings1.keys()) & set(self.ratings2.keys())):
            x = self.ratings1[k]
            y = self.ratings2[k]
            distance += pow(abs(x - y), r)
    
        # return value of minkowski distance
        return pow(distance,1/r)

    # pearson correlation between two vectors
    def pearson(self):
        
        sumXY = 0
        sumX = 0
        sumY = 0
        sumX2 = 0
        sumY2 = 0
        n = 0

        # calculate pearson correlation
        for k in (set(self.ratings1.keys()) & set(self.ratings2.keys())):
            n += 1
            x = self.ratings1[k]
            y = self.ratings2[k]
            sumXY += x * y
            sumX += x
            sumY += Y
            sumX2 += pow(z, 2)
            sumY2 += pow(y, 2)
    
        # error check for n==0 condition
        if n == 0:
            print (">>> pearson debug: n=0; returning -2 correlation!")
            return -2    

        # calculate nr and dr for pearson correlation
        nr = (sumXY - (sumX * sumY) / n)
        dr = (math.sqrt(sumX2 - pow(sumY, 2) / n) * math.sqrt(sumX2 - pow(sumY, 2) / n))
        
        # error check for dr==0 condition
        if dr == 0:
            print (">>> pearson debug: denominator=0; returning -2 correlation!")
            return -2

        # return value of pearson correlation coefficient        
        return nr / dr

# user ratings
songData = {"David": {"Post Malone": 3.5, "Taylor Swift": 2.0, "Ellie Goulding": 4.5, "The Cure": 5.0, "Calvin Harris": 1.5, "The Beatles": 2.5, "Migos": 2.0},
         "Ashley":{"Post Malone": 4.0, "Taylor Swift": 5.0, "The Cure": 3.0, "Calvin Harris": 3.5},
         "Ryan": {"Post Malone": 5.0, "Taylor Swift": 1.0, "AC/DC": 1.0, "Ellie Goulding": 3.0, "The Cure": 5, "Calvin Harris": 1.0},
         "John": {"Post Malone": 3.0, "Taylor Swift": 4.0, "AC/DC": 4.5, "The Cure": 3.0, "Calvin Harris": 4.5, "The Beatles": 4.0, "Migos": 2.0},
         "Victoria": {"Taylor Swift": 4.0, "AC/DC": 1.0, "Ellie Goulding": 4.0, "The Beatles": 4.0, "Migos": 1.0},
         "Stephanie":  {"Taylor Swift": 4.5, "AC/DC": 4.0, "Ellie Goulding": 5.0, "The Cure": 5.0, "Calvin Harris": 4.5, "The Beatles": 4.0, "Migos": 4.0},
         "Charlie": {"Post Malone": 5.0, "Taylor Swift": 2.0, "Ellie Goulding": 3.0, "The Cure": 5.0, "Calvin Harris": 4.0, "The Beatles": 5.0},
         "Katie": {"Post Malone": 3.0, "Ellie Goulding": 5.0, "The Cure": 4.0, "Calvin Harris": 2.5, "The Beatles": 3.0}
        }

# Ashley’s recommendations
userX = "Ashley"
userXRatings = songData[userX]

# calculate euclidean distance
userDistances = []
for userY, userYRatings in songData.items():
    if (userX != userY):
        simobj = similarity (userXRatings, userYRatings)
        userDistances.append((userY, round(simobj.minkowksi(2),2)))

# sort userDistances by lowest distance to highest distance and assign sorted list to variable userSortedDistances.
userSortedDistances = sorted(userDistances, key=itemgetter(1), reverse=False)

# userX's NN is the user at the 0th position of the sorted list.
userXNN = userSortedDistances[0][0]
# recommendations for userX will include albums rated by userXNN, not already rated by userX.
userXRecos = []
for album in songData[userXNN].keys():
    if (album not in songData[userX].keys()):
        userXRecos.append((album, songData[userXNN][album]))

# sort list of tuples by highest rating to lowest rating and assign sorted list to varaible userXSortedRecos.
# example: [('Ellie Goulding', 4.0), ('The Beatles', 4.0), ('AC/DC', 1.0), ('Migos', 1.0)]

userXSortedRecos = sorted(userXRecos, key=itemgetter(1), reverse=True)

print ("Recommendations for", userX)
print ("--------------------------")
print ()
print (userXSortedRecos)
