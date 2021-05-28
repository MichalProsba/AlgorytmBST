from Bst import Bst
from random import randint

#Otwarcie pliku
file = open("file1.txt", "r")
#Zapisanie pliku do zmiennej
content = file.read()
#Zamknięcie pliku
file.close()
#Lista ze słowami
wordLists = []
#Podzielenie tekstu
wordLists = content.split()

#Wysokosc tablicy
wordListsSize = len(wordLists)
print("===========================")
print("Lista słow: " + str(wordLists))
print("===========================")
print("Dlugosc listy: " + str(len(wordLists)))
print("===========================")

halfSizeLists = wordListsSize/2;
maxIteration = len(wordLists) - 1
i = 0
bst = Bst()
nums = []
bst.insert(halfSizeLists)
while(i < maxIteration/2):
    #random_number = randint(1, maxIteration)
    #if(not (bst.exists(random_number))):
    bst.insert(maxIteration - i)
    bst.insert(i)
    i = i + 1
       #bst.insert(random_number)


print("===========================")
print(Bst.maxHeight)
print("===========================")
print("preorder:")
print(bst.preorder([]))
print("#")

print("postorder:")
print(bst.postorder([]))
print("#")

print("inorder:")
print(bst.inorder([]))
print("#")

#nums = [2, 6, 20]
#print("deleting " + str(nums))
#for num in nums:
#    bst.delete(num)
#print("#")

#print("4 exists:")
#print(bst.exists(4))
#print("2 exists:")
#print(bst.exists(2))
#print("12 exists:")
#print(bst.exists(12))
#print("18 exists:")
#print(bst.exists(18))
#print(bst.maxHeight)

