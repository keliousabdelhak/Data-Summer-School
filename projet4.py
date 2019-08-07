import csv

my_list=[]
my_list_1=[]

#open csv file
with open('old.csv') as f:

    f = csv.reader(f)
    number_of_word=0
    number_of_element=0

    #count number of words in list
    #count number of elements in list 
    for row in f:
        nbr=len(row[0].split())

        for ele in row[0].split():
        	my_list_1.append(ele)

        number_of_word+=nbr
        number_of_element+=1

        my_list.append(row[0])

print("\nThe list in order from A to Z (you can find it in the new csv file --generated automatically) :")
print("-----------------------------------------------------------------------------------------------")
#order the list from A to Z
my_list.sort(key=lambda v: v.upper())
print(my_list)

print("\n-----------------------------------------------------------------------------------------------\n")
print("- Number of words in list is : ",number_of_word)
print("- Number of elements in list is : ",number_of_element)

#the average word length for the list
nbr_char=0
for elem in my_list_1:
	nbr_char+=len(elem)

print("\n----------------------------------------------------------------------------------------------\n")
average_word=nbr_char/number_of_word
print("-the average [word length] for the list is : ",round(average_word))

#the average element length for the list (without space)
nbr_char_1=0
for elemn in my_list:
	nbr_char_1+=len(elemn)-elemn.count(' ')

average_element=nbr_char_1/number_of_element
print("-the average [element length] for the list is : ",round(average_element))


#generate new csv file and save list

new_file = open("new.csv",'w')
for line in my_list:
    new_file.write(line + "\n")

print("\n------------------------------------ list saved in new.csv -----------------------------------\n") 
