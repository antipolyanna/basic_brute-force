import itertools

password ="1881"

for i in range(1,5):
    for guess in itertools.product("0123456789", repeat=i):
        if "".join(guess) == password:
            print("Şifreyi Başarı ile kırdınız. ;)","".join(guess) , ",Şifren iyiymiş ponçikkk :)")
            break

