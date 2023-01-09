from test import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)


def encrypt(citext, shifts, deriction):
    finish_text = ""
    if deriction == 'decrypt':
        shifts *= -1
    for texti in citext:
        if texti in alphabet:
            position = alphabet.index(texti)
            new_position = position + shifts
            finish_text += alphabet[new_position]
        else:
            finish_text += texti

    print(finish_text)


main_ques = 'yes'
while main_ques.lower() != 'no':
    ques = input("What do you want encrypt or decrypt your text? : ")
    text = str(input("Write your text   : "))
    shift = int(input("How many shifts should be? : "))
    shift = shift % 26
    encrypt(text, shift, ques)
    main_ques = str(input("Do you want continue? : "))

print("Goodbye")