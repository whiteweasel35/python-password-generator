import string, secrets
chrs = string.ascii_letters
numbers = string.digits

#author white weasel

lenght = input("şifre uzunluğunuzu girin: ")

password_in_chrs  = ''.join(secrets.choice(chrs)for i in range(int(lenght)))
password_in_numbers  = ''.join(secrets.choice(numbers)for i in range(int(lenght)))

choose = input("Text or Number: ")
print("************PYTHON PASSWORD GENERATOR************")
if choose == "text" :
    print(password_in_chrs)
if choose == "number":
    print(password_in_numbers)
