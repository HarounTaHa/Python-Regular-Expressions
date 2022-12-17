import re

# search
txt = 'My name is Haroun'
# search from capital character
search = re.search("[A-Z]", txt)

print(search)  # return object if find None if not
print(search.group())  # result

# format phone numbers must be => XXX-XXX-XXXX ✅
test = 'Call me at 791-808-8102 tomorrow, 428-562-2152 is my office'
# use r before str chain because use \b
search = re.search(r"\d{3}-\d{3}-\d{4}", test)
print(search)
print(search.group())  # result
print(search.string)  # print test variable
# ------------------------------------------------
# findall return list
test = 'Call me at 791-808-8102 tomorrow, 428-562-2152 is my office'
search = re.findall(r'\d{3}-\d{3}-\d{4}', test)
print(search)
test_search = re.findall(r'A', test)
print(test_search)

# practice
phone_number = input('Please enter your phone number: ')
search_phone = re.findall(r'\d{3}-\d{3}-\d{4}', phone_number)
phones = []
if search_phone is []:
    print('This phone number is not valid')
else:
    list.append(search_phone)
    print(list)
    print('This phone number is added')
