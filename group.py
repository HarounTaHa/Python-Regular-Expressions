import re

# Groups

phone = '415-555-1325'

search = re.search(r"(\d{3})-(\d{3})-(\d{4})", phone)

print(search.group())
print(search.group(1))
print(search.group(2))

print('-' * 10)

date = "27-05-2020"
search = re.search(r"(\d{2})-(\d{2})-(\d{4})", date)
day = search.group(1)
month = search.group(2)
year = search.group(3)
print(f'The days is :{day}, the month is :{month}, the year is {year}')

day, month, year = search.groups()
print(f'The days is :{day}, the month is :{month}, the year is {year}')
