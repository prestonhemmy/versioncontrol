# COP3502C: Lab 6: Version Control
# Preston Hemmy

import decode

def encode_password(password):
    encoded_data = ''
    for i in password:
        encoded_data += str(int(i) + 3)
    return encoded_data


# def decode_password(encoded_password):
#     decoded_data = ''
#     for i in encoded_password:
#         decoded_data += str(int(i) - 3)
#     return decoded_datagit

if __name__ == '__main__':
    user_encoded = ''
    while True:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')
        option_select = input('Please enter an option: ')
        if option_select != '3':
            if option_select == '1':
                user_password = input('Please enter your password to encode: ')
                user_encoded = encode_password(user_password)
                print('Your password has been encoded and stored!')
            elif option_select == '2':

                decode.decode(user_encoded)
                pass
        else:
            exit()