def descending_order(num):
    max_number = sorted(str(num), reverse=True)
    return int(''.join(max_number))

def square_every_digit(num):
    digits = str(num)
    square_num = ''
    for i in digits:
        square_num += str(pow(int(i), 2))
    return square_num

def find_the_odd_int(num_arr):
    for i in num_arr:
        if num_arr.count(i) % 2 != 0:
            return i

def persistence(num):
    count = 0
    digits = num
    if len(str(num)) != 1:
        while True:
            new_num = 1
            for i in str(digits):
                new_num *= int(i)
            count += 1
            if len(str(new_num)) != 1:
                digits = new_num
            else:
                break
    return count

def counting_duplicates(text):
    letter = []
    text = text.lower()
    for el in text:
        if text.count(el) > 1:
            letter.append(el) 
    return len(set(letter))

def who_likes_it(people):
    l = len(people)
    if l == 0:
        return("no one likes this")
    elif l == 1:
        return(f"{people[0]} likes this")
    elif l == 2:
        return(f"{people[0]} and {people[1]} like this")
    elif l == 3:
        return(f"{people[0]}, {people[1]} and {people[2]} like this")
    else:
        return(f"{people[0]}, {people[1]} and {l - 2} others like this")

# def snail(array):
#     lst = []
#     i, j, dim  = 0, 0, 0
#     n = len(array)
#     while i < n - dim:
#         while j < n - dim:
#             #lst.append(array[i][j])
#             j+=1
#         i += 1
#     print(lst)

def validate_pin(pin):
    if len(pin) == (4 or 6) and pin.isdigit():
        return True
    else:
        return False


def disemvowel_trolls(text):
    vowels = "euioaEUIOA"
    for char in vowels:
        text = text.replace(char, '')
    return(text)

def convert_to_camel_case(text):
    delimiters = '-_'
    flag = text.istitle()
    for char in delimiters:
        text = text.replace(char, ' ')
    text = text.title()
    text = text.replace(' ', '')
    if flag == False:
        text = text[0].lower() + text[1:]
    return text

#print(validate_pin("1234"))
print(convert_to_camel_case('The_Stealth-Warrior'))        
#snail([[1,2,3], [4,5,6], [7,8,9]])

