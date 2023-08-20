#Cleaning Text
import string 


text = open("./read.txt","r",encoding="utf-8").read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans("","",string.punctuation))
print(cleaned_text)

