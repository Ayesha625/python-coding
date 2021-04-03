import phonenumbers
#geocoder: to know specific location
#carrier: to know the sim name

from phonenumbers import geocoder
from phonenumbers import carrier

input_phone=input("Enter the phone number: ")
phno=phonenumbers.parse(input_phone)

print(geocoder.description_for_number(phno,'en'))
print(carrier.name_for_number(phno,'en'))
      
