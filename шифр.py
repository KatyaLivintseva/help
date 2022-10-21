alfavit='абвгдеёжзийклмнопрстуфхцчшщъыьэюя' #задаем алфавит
print('\nЭто "Шифр Цезаря". Он поможет зашифровать или расшифровать послание')
def shifr():
    print('\nНапишите текст (на русском языке), который нужно зашифровать или расшифровать')
    try:
        A=0
        text=input()
        print('Сдвиг шифровки')

        try:
            sdvig=int(input())
            text_z=text.lower() 
            text_new=''
            
            if sdvig==0:
                print("Ваш текст не изменился:", text)
            
            if sdvig>=1: #зашифровка
                while sdvig > 33: #если сдвиг больше букв в алфавите
                    sdvig -= 33
                k = sdvig
                
                for ic in text_z:
                    position=alfavit.find(ic)
                    new_position=position+k 
                    if ic in alfavit:
                        text_new=text_new + alfavit[new_position]
                    else:
                        text_new=text_new+ic
                        
                if text==text_new:
                    A=1
                    print('Вы ввели или символ, или текст не на русском языке')
                else:
                    print ('Зашифрованный текст:', text_new)
                    
            if sdvig<0: #расшифровка
                while sdvig <(-33):
                    sdvig += 33
                k = sdvig
                
                for ic in text_z:
                    position=alfavit.find(ic)
                    new_position=position+k
                    if ic in alfavit:
                        text_new=text_new + alfavit[new_position]
                    else:
                        text_new=text_new+ic
                        
                if text==text_new:
                    A=1
                    print('Вы ввели или символ, или текст не на русском языке')
                else:
                    print ('Расшифрованный текст:', text_new)    
            
        except IndexError:
            A=1
            print('Шаг сдвига слишком большой.  ')

        except ValueError:
            A=1
            print('Шаг должен быть обозначен цифрой.')

    except TypeError:
        A=1
        print('Введите текст.')
        
while A==1:
    shifr()
